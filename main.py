import json

# This string simulates the content of an AGENTS.md file.
# AGENTS.md aims to standardize how AI agents are defined,
# enabling machine readability and interoperability across systems.
# Here, we use a JSON structure to represent an agent's properties.
agents_md_content = """
{
    "agentName": "SimpleChatbot",
    "version": "1.0.0",
    "description": "A basic chatbot capable of answering simple questions and greeting users.",
    "capabilities": [
        {
            "name": "greetUser",
            "description": "Greets the user with a friendly message.",
            "inputs": [],
            "outputs": [
                {"type": "string", "description": "A greeting message"}
            ]
        },
        {
            "name": "answerQuestion",
            "description": "Provides a predefined answer to specific questions.",
            "inputs": [
                {"name": "question", "type": "string", "description": "The user's question"}
            ],
            "outputs": [
                {"type": "string", "description": "The answer to the question"}
            ]
        }
    ],
    "interactionMethods": [
        {
            "type": "http",
            "endpoint": "https://api.example.com/chatbot/v1",
            "methods": ["POST"]
        }
    ],
    "licensing": "MIT",
    "contact": {
        "name": "AI Agent Team",
        "email": "agent.team@example.com"
    }
}
"""

def parse_agents_md(content: str):
    """
    Parses the AGENTS.md-like content (JSON string) and returns a dictionary.
    This demonstrates how a system could read and understand an agent's definition
    from a standardized format.
    """
    try:
        agent_definition = json.loads(content)
        return agent_definition
    except json.JSONDecodeError as e:
        print(f"Error parsing AGENTS.md content: {e}")
        return None

def display_agent_info(agent_data: dict):
    """
    Displays key information about the AI agent from its parsed definition.
    This simulates how a system might interpret and utilize the defined properties.
    """
    if not agent_data:
        print("No agent data to display.")
        return

    print("--- AI Agent Definition (Parsed) ---")
    print(f"Agent Name: {agent_data.get('agentName', 'N/A')}")
    print(f"Version: {agent_data.get('version', 'N/A')}")
    print(f"Description: {agent_data.get('description', 'N/A')}")

    print("\nCapabilities:")
    for capability in agent_data.get('capabilities', []):
        print(f"  - Name: {capability.get('name', 'N/A')}")
        print(f"    Description: {capability.get('description', 'N/A')}")
        if capability.get('inputs'):
            print("    Inputs:")
            for inp in capability['inputs']:
                print(f"      - {inp.get('name', 'N/A')} ({inp.get('type', 'N/A')}): {inp.get('description', 'N/A')}")
        if capability.get('outputs'):
            print("    Outputs:")
            for out in capability['outputs']:
                print(f"      - {out.get('type', 'N/A')}: {out.get('description', 'N/A')}")

    print("\nInteraction Methods:")
    for method in agent_data.get('interactionMethods', []):
        print(f"  - Type: {method.get('type', 'N/A')}")
        print(f"    Endpoint: {method.get('endpoint', 'N/A')}")
        print(f"    HTTP Methods: {', '.join(method.get('methods', []))}")

    print(f"\nLicensing: {agent_data.get('licensing', 'N/A')}")
    contact = agent_data.get('contact', {})
    print(f"Contact: {contact.get('name', 'N/A')} <{contact.get('email', 'N/A')}>")
    print("------------------------------------")

if __name__ == "__main__":
    print("Simulating AGENTS.md parsing for an AI agent definition.")
    print("This demonstrates how a standardized format can enable machine readability and interoperability.")

    # Parse the simulated AGENTS.md content
    parsed_agent = parse_agents_md(agents_md_content)

    # Display the parsed information
    if parsed_agent:
        display_agent_info(parsed_agent)
    else:
        print("Failed to parse agent definition.")
