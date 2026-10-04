import json
import os
from dotenv import load_dotenv

from smolagents import CodeAgent, OpenAIModel
from security_tools import get_mitre_information


# Load environment variables
load_dotenv()

# Load alerts
with open("alerts.json", "r") as file:
    alerts = json.load(file)


# Create the AI model
model = OpenAIModel(
    model_id="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)


# Create the cybersecurity agent
agent = CodeAgent(
    tools=[get_mitre_information],
    model=model,
    additional_authorized_imports=["json"]
)


# Analyze each security alert
for alert in alerts:

    print("\n" + "=" * 60)
    print("AI CYBERSECURITY ALERT ANALYZER")
    print("=" * 60)

    prompt = f"""
You are a cybersecurity SOC analyst.

Analyze the following security alert:

{json.dumps(alert, indent=2)}

Perform the following tasks:

1. Explain what happened.
2. Determine the likely attack type.
3. Assign a severity: Low, Medium, High, or Critical.
4. Identify the relevant MITRE ATT&CK technique.
5. Explain the evidence supporting your conclusion.
6. Provide recommended investigation steps.
7. Provide a confidence level.
8. State whether human analyst review is required.

Use the cybersecurity knowledge tool when appropriate.

Do not take any destructive or automatic response actions.
This is an AI-assisted analysis system and all recommendations
must be validated by a human security analyst.

Return the result in a clear structured format.
"""

    result = agent.run(prompt)

    print(result)
