# legal_drafter_task.py

# from crewai import Task

# from agents.legal_drafter_agent import legal_drafter_agent
# from tasks.case_intake_task import case_intake_task
# from tasks.ipc_section_task import ipc_section_task
# from tasks.legal_precedent_task import legal_precedent_task

# legal_drafter_task = Task(
#     agent=legal_drafter_agent,
#     description=(
#         "Based on the legal case summary, IPC sections, and precedents retrieved form the previous tasks, draft a formal legal document (e.g., FIR or legal notice) "
#         "that the user can submit to the authorities or use for legal action.\n\n"
#         "Draft a clear and properly formatted legal notice or complaint that is appropriate to this situation. "
#         "The document should include a subject line, date, involved parties, factual background, applicable legal sections, and a formal request for action."
#     ),
#     expected_output=(
#         "A formal legal document such as:\n"
#         "- Title (e.g., LEGAL COMPLAINT)\n"
#         "- Parties involved\n"
#         "- Factual summary\n"
#         "- Applicable legal sections\n"
#         "- Demand or request\n"
#         "- Date and sender details"
#     ),
#     context=[case_intake_task, ipc_section_task, legal_precedent_task]
# )
# from crewai import Task
# from agents.legal_drafter_agent import legal_drafter_agent

# legal_drafter_task = Task(
#     agent=legal_drafter_agent,
#     description=(
#         "Consolidate all the information from the previous tasks into a single, structured JSON object. "
#         "You will receive the structured case analysis, a list of applicable IPC sections, and a summary of legal precedents. "
#         "Your final job is to draft the legal document based on all this context AND structure the entire output."
#         "\n\nTHE FINAL OUTPUT MUST BE A SINGLE, VALID JSON OBJECT containing these top-level keys:"
#         "\n- 'case_analysis': The JSON output from the Case Intake Agent."
#         "\n- 'applicable_ipc_sections': The JSON array from the IPC Section Agent."
#         "\n- 'legal_precedents': A JSON object containing a single key 'summary' with the text from the Legal Precedent Agent."
#         "\n- 'drafted_document': A JSON object containing the drafted legal document with keys like 'title', 'parties_involved', etc."
#     ),
#     expected_output=(
#         "A single, complete JSON object containing all the structured information and the fully drafted legal document."
#     ),
#     # The context will be passed automatically by the crew definition
#     # The output_json=True parameter tells CrewAI to expect and validate a JSON output from this task.
#     output_json=True
# )
# tasks/legal_drafter_task.py

from crewai import Task
from agents.legal_drafter_agent import legal_drafter_agent
from pydantic import BaseModel, Field
from typing import List, Dict, Any

# Define the Pydantic models for structured output
class CaseAnalysis(BaseModel):
    case_type: str = Field(description="The type of legal case.")
    legal_domain: str = Field(description="The domain of law (e.g., Criminal, Civil).")
    summary: str = Field(description="A concise summary of the case.")
    relevant_entities: List[str] = Field(description="List of involved parties.")
    jurisdiction: str = Field(description="The jurisdiction of the case.")

class IPCSection(BaseModel):
    section: str = Field(description="The IPC section number.")
    section_title: str = Field(description="The title of the IPC section.")
    content: str = Field(description="The description of the IPC section.")

class LegalPrecedents(BaseModel):
    summary: str = Field(description="A summary of relevant legal precedents.")

class DraftedDocument(BaseModel):
    title: str = Field(description="The title of the legal document.")
    parties_involved: str = Field(description="Details of the parties involved.")
    factual_summary: str = Field(description="A summary of the facts of the case for the document.")
    applicable_sections: str = Field(description="The text describing the applicable legal sections.")
    demand_or_request: str = Field(description="The specific demand or request being made.")
    sender_details: str = Field(description="Details of the sender/complainant.")

# Define the final, top-level output model
class FinalOutputModel(BaseModel):
    case_analysis: CaseAnalysis
    applicable_ipc_sections: List[IPCSection]
    legal_precedents: LegalPrecedents
    drafted_document: DraftedDocument

# This is the updated Task definition
legal_drafter_task = Task(
    agent=legal_drafter_agent,
    description=(
        "Consolidate all information into a single, structured JSON object. "
        "Your final job is to draft the legal document and structure the entire output according to the provided JSON schema."
    ),
    expected_output=(
        "A single, complete, and valid JSON object that strictly adheres to the 'FinalOutputModel' Pydantic schema."
    ),
    # The context will be passed automatically by the crew definition
    # Pass the Pydantic model to the 'output_json' parameter
    output_json=FinalOutputModel
)