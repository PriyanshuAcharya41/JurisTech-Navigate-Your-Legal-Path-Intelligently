from crewai import Task
from agents.legal_drafter_agent import legal_drafter_agent

legal_drafter_task_simple = Task(
    agent=legal_drafter_agent,
    description=(
        "Based on the legal case summary, IPC sections, and precedents, draft a formal legal document "
        "(e.g., FIR or legal notice) that the user can submit to the authorities. "
        "The document should include a subject line, date, involved parties, factual background, "
        "applicable legal sections, and a formal request for action. The final output must be a single, formatted string."
    ),
    expected_output=(
        "A formal legal document as a single block of text."
    ),
)