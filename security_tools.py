from smolagents import tool


@tool
def get_mitre_information(technique_id: str) -> str:
    """
    Provides basic MITRE ATT&CK information for common
    cybersecurity techniques.

    Args:
        technique_id: MITRE ATT&CK technique ID such as T1110.

    Returns:
        Information about the technique.
    """

    mitre_database = {

        "T1110": {
            "name": "Brute Force",
            "description": "Adversaries may use repeated authentication attempts to gain access to an account.",
            "examples": "Password guessing, password spraying and credential stuffing."
        },

        "T1059.001": {
            "name": "PowerShell",
            "description": "Adversaries may abuse PowerShell to execute commands and scripts.",
            "examples": "Malicious PowerShell commands and scripts."
        },

        "T1071.004": {
            "name": "DNS",
            "description": "Adversaries may use DNS to communicate with command and control infrastructure.",
            "examples": "DNS-based command and control and DNS tunneling."
        },

        "T1566": {
            "name": "Phishing",
            "description": "Adversaries may use phishing techniques to obtain access or execute malicious content.",
            "examples": "Malicious emails, links and attachments."
        },

        "T1003": {
            "name": "OS Credential Dumping",
            "description": "Adversaries may attempt to obtain credentials from operating system components.",
            "examples": "Credential extraction from memory or credential stores."
        }
    }

    if technique_id in mitre_database:

        technique = mitre_database[technique_id]

        return f"""
MITRE ATT&CK Technique: {technique_id}

Name:
{technique['name']}

Description:
{technique['description']}

Examples:
{technique['examples']}
"""

    return f"No local information is available for {technique_id}."
