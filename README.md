# AI Cybersecurity Alert Analyzer

An AI-assisted cybersecurity alert analysis prototype built using Python, smolagents, OpenAI, and MITRE ATT&CK concepts.

## Overview

Security Operations Center (SOC) analysts receive large numbers of security alerts that require initial triage and investigation.

This project explores how agentic AI can assist with the initial analysis of cybersecurity alerts.

The system accepts structured security alerts and uses an AI agent to:

- Analyze the alert
- Identify the likely attack type
- Assess severity
- Map activity to MITRE ATT&CK techniques
- Explain supporting evidence
- Recommend investigation steps
- Provide a confidence level
- Indicate whether human review is required

The system is designed as an AI-assisted security analysis prototype and does not automatically perform destructive response actions.

---

## Project Objective

The objective of this project is to explore the application of agentic AI to cybersecurity operations, particularly security alert triage and investigation.

The project demonstrates how an AI agent can use cybersecurity-specific tools and knowledge to assist a security analyst.

---

## Architecture

```text
                Security Alert
                      |
                      v
              Python Application
                      |
                      v
               AI Agent
              (smolagents)
                      |
                      v
          Cybersecurity Knowledge Tool
                      |
                      v
              MITRE ATT&CK
                      |
                      v
             Security Analysis
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Severity   Attack Type   Evidence
          |
          v
   Investigation Steps
          |
          v
      Human Analyst
