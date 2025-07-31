# # api.py

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from crew import legal_assistant_crew

# # Initialize the FastAPI app
# app = FastAPI(
#     title="AI Legal Assistant API",
#     description="An API to get legal analysis using a CrewAI team."
# )

# # This is the code that connects the backend to the frontend.
# # It allows your React app (running on a different port) to make requests.
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins for simplicity.
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Define the structure of the incoming request data
# class LegalQuery(BaseModel):
#     user_input: str

# @app.get("/")
# def read_root():
#     return {"status": "AI Legal Assistant API is running."}


# @app.post("/analyze")
# def analyze_legal_issue(query: LegalQuery):
#     """
#     Takes a user's legal issue and returns the AI-generated analysis.
#     """
#     try:
#         inputs = {"user_input": query.user_input}
#         result = legal_assistant_crew.kickoff(inputs=inputs)
#         return {"response": result}
#     except Exception as e:
#         # It's good practice to handle potential errors
#         return {"error": str(e)}
# api.py

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from dotenv import load_dotenv  # <-- ADD THIS LINE
# from crew import legal_assistant_crew
# import logging

# # Load environment variables from .env file
# load_dotenv()  # <-- ADD THIS LINE

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# app = FastAPI(
#     title="AI Legal Assistant API",
#     description="An API to get legal analysis using a CrewAI team."
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class LegalQuery(BaseModel):
#     user_input: str

# @app.post("/analyze")
# def analyze_legal_issue(query: LegalQuery):
#     logger.info(f"Received request for analysis: {query.user_input[:50]}...")
#     try:
#         inputs = {"user_input": query.user_input}
#         result = legal_assistant_crew.kickoff(inputs=inputs)
#         logger.info("Crew kickoff successful, returning result.")
#         return {"response": result}
#     except Exception as e:
#         logger.error(f"An error occurred during crew execution: {e}", exc_info=True)
#         return {"error": str(e)}

# @app.get("/")
# def read_root():
#     return {"status": "AI Legal Assistant API is running."}

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from dotenv import load_dotenv
# from crew import legal_assistant_crew
# import logging
# import json # <-- ADD THIS IMPORT

# # Load environment variables from .env file
# load_dotenv()

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# app = FastAPI(
#     title="AI Legal Assistant API",
#     description="An API to get legal analysis using a CrewAI team."
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class LegalQuery(BaseModel):
#     user_input: str

# @app.post("/analyze")
# def analyze_legal_issue(query: LegalQuery):
#     logger.info(f"Received request for analysis: {query.user_input[:50]}...")
#     try:
#         inputs = {"user_input": query.user_input}
#         result = legal_assistant_crew.kickoff(inputs=inputs)
        
#         # --- START OF THE FIX ---
#         # CrewAI might return a JSON string, so we ensure it's a Python dict
#         if isinstance(result, str):
#             try:
#                 # Attempt to parse the string into a dictionary
#                 result = json.loads(result)
#             except json.JSONDecodeError:
#                 logger.error("Failed to parse AI output as JSON.")
#                 # If parsing fails, wrap it in a simple structure or return an error
#                 return {"error": "The AI returned a malformed response."}
#         # --- END OF THE FIX ---

#         logger.info("Crew kickoff successful, returning result.")
#         return {"response": result}
#     except Exception as e:
#         logger.error(f"An error occurred during crew execution: {e}", exc_info=True)
#         return {"error": str(e)}

# @app.get("/")
# def read_root():
#     return {"status": "AI Legal Assistant API is running."}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from crew import legal_assistant_crew
import logging
import json

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Legal Assistant API",
    description="An API to get legal analysis using a CrewAI team."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LegalQuery(BaseModel):
    user_input: str

@app.post("/analyze")
def analyze_legal_issue(query: LegalQuery):
    logger.info(f"Received request for analysis: {query.user_input[:50]}...")
    try:
        inputs = {"user_input": query.user_input}
        crew_result = legal_assistant_crew.kickoff(inputs=inputs)
        
        # --- START OF THE FIX ---
        # The result from kickoff() might be a dictionary with a key like 'Final Output'
        # or it could be a JSON string. We handle both cases to get the core data.
        
        final_data = crew_result
        
        # If the result is a dictionary and contains a single key, we extract the value.
        # This handles the case where the output is {'Final Output': {...}}
        if isinstance(final_data, dict) and len(final_data) == 1:
            final_data = list(final_data.values())[0]

        # If the result is a string, we parse it as JSON.
        if isinstance(final_data, str):
            try:
                final_data = json.loads(final_data)
            except json.JSONDecodeError:
                logger.error("Failed to parse AI output string as JSON.")
                return {"error": "The AI returned a malformed response."}
        # --- END OF THE FIX ---

        logger.info("Crew kickoff successful, returning result.")
        return {"response": final_data}
        
    except Exception as e:
        logger.error(f"An error occurred during crew execution: {e}", exc_info=True)
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"status": "AI Legal Assistant API is running."}