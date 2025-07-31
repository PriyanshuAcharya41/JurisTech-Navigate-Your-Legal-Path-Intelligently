# # legal_drafter_agent.py

# from crewai import Agent, LLM

# llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.4)

# legal_drafter_agent = Agent(
#     role="Legal Document Drafting Agent",
#     goal="Draft legally sound documents based on the user's case summary, applicable IPC sections, and relevant precedents.",
#     backstory=(
#         "You are a seasoned legal document expert trained in Indian law. "
#         "You specialize in drafting formal legal documents such as FIRs, legal notices, and complaints, tailored to specific case scenarios. "
#         "Your drafts are precise, compliant with Indian legal standards, and written in plain yet formal legal language."
#     ),
#     tools=[],  # No tools needed; all inputs are from upstream agents
#     llm=llm,
#     verbose=True,
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
from crewai import Agent
from langchain_openai import ChatOpenAI

# Replace with your chosen LLM (e.g., ChatOpenAI, ChatGroq, Ollama)
llm = ChatOpenAI(model="gpt-4o-mini") 

legal_drafter_agent = Agent(
    role="Legal Document Drafting & Consolidation Agent",
    goal="Draft legally sound documents and consolidate all provided information from other agents into a final structured JSON output.",
    backstory=(
        "You are a meticulous legal expert and document specialist. Your primary role is to take all the structured data, research, and legal sections provided by other agents and assemble them into a final, clean JSON object that includes a professionally drafted legal document."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)