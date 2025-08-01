# import streamlit as st
# from dotenv import load_dotenv
# from crew import legal_assistant_crew
# import json

# load_dotenv()

# def format_legal_output(result):
#     """Format the crew output into a professional legal mail template"""
    
#     # Handle different types of result objects
#     if isinstance(result, str):
#         try:
#             data = json.loads(result)
#         except:
#             # If it's already formatted text, return as is
#             return result
#     elif hasattr(result, 'dict'):
#         # Handle Pydantic objects
#         data = result.dict()
#     elif hasattr(result, '__dict__'):
#         # Handle other objects with __dict__
#         data = result.__dict__
#     elif hasattr(result, 'to_dict'):
#         # Handle objects with to_dict method
#         data = result.to_dict()
#     else:
#         # Try to convert to string and parse, or use as dictionary
#         try:
#             if hasattr(result, 'get'):
#                 data = result
#             else:
#                 data = dict(result)
#         except:
#             # Last resort - convert to string
#             return f"<pre>{str(result)}</pre>"
    
#     # Extract data with fallbacks
#     case_analysis = data.get('case_analysis', {}) if hasattr(data, 'get') else {}
#     ipc_sections = data.get('applicable_ipc_sections', []) if hasattr(data, 'get') else []
#     precedents = data.get('legal_precedents', {}) if hasattr(data, 'get') else {}
#     document = data.get('drafted_document', {}) if hasattr(data, 'get') else {}
    
#     # Handle nested objects safely
#     if hasattr(case_analysis, 'get'):
#         case_type = case_analysis.get('case_type', 'Legal Matter')
#         summary = case_analysis.get('summary', 'Legal issue requires attention')
#         jurisdiction = case_analysis.get('jurisdiction', '[Your Location]')
#     else:
#         case_type = getattr(case_analysis, 'case_type', 'Legal Matter') if case_analysis else 'Legal Matter'
#         summary = getattr(case_analysis, 'summary', 'Legal issue requires attention') if case_analysis else 'Legal issue requires attention'
#         jurisdiction = getattr(case_analysis, 'jurisdiction', '[Your Location]') if case_analysis else '[Your Location]'
    
#     # Format IPC sections safely
#     ipc_text = ""
#     if ipc_sections:
#         for section in ipc_sections:
#             if hasattr(section, 'get'):
#                 section_num = section.get('section', 'Section')
#                 section_title = section.get('section_title', 'Title')
#                 content = section.get('content', 'Content')
#             else:
#                 section_num = getattr(section, 'section', 'Section')
#                 section_title = getattr(section, 'section_title', 'Title')
#                 content = getattr(section, 'content', 'Content')
            
#             ipc_text += f"""
#         **{section_num}**: {section_title}
        
#         _{content}_
        
#         """
    
#     # Create the professional mail template
#     template = f"""
#     <div style="background: white; padding: 2rem; border-radius: 12px; border: 1px solid #e1e5e9; font-family: 'Times New Roman', serif; line-height: 1.6;">
        
#         <div style="text-align: right; margin-bottom: 2rem; color: #666;">
#             <strong>Date:</strong> [Current Date]<br>
#             <strong>From:</strong> [Your Full Name]<br>
#             <strong>Address:</strong> [Your Complete Address]<br>
#             <strong>Phone:</strong> [Your Phone Number]<br>
#             <strong>Email:</strong> [Your Email Address]
#         </div>
        
#         <div style="margin-bottom: 2rem;">
#             <strong>To:</strong><br>
#             [Recipient Name]<br>
#             [Recipient Designation]<br>
#             [Office Address]<br>
#             {jurisdiction}
#         </div>
        
#         <div style="text-align: center; margin: 2rem 0; font-size: 1.2rem; font-weight: bold; text-decoration: underline;">
#             Subject: Legal Complaint/Consultation Regarding {case_type}
#         </div>
        
#         <div style="margin-bottom: 1.5rem;">
#             <strong>Respected Sir/Madam,</strong>
#         </div>
        
#         <div style="margin-bottom: 1.5rem; text-align: justify;">
#             I am writing to bring to your attention a serious legal matter that requires immediate intervention. 
#             {summary} I seek your legal guidance and assistance in this matter.
#         </div>
        
#         <div style="margin-bottom: 1.5rem;">
#             <strong>FACTUAL BACKGROUND:</strong>
#         </div>
        
#         <div style="margin-bottom: 1.5rem; text-align: justify; padding-left: 1rem;">
#             {getattr(document, 'factual_summary', '[Please provide detailed facts of your case here, including dates, times, locations, and parties involved.]') if hasattr(document, 'factual_summary') else document.get('factual_summary', '[Please provide detailed facts of your case here, including dates, times, locations, and parties involved.]') if hasattr(document, 'get') else '[Please provide detailed facts of your case here, including dates, times, locations, and parties involved.]'}
#         </div>
        
#         <div style="margin-bottom: 1.5rem;">
#             <strong>APPLICABLE LEGAL PROVISIONS:</strong>
#         </div>
        
#         <div style="margin-bottom: 1.5rem; padding-left: 1rem;">
#             Based on the facts of the case, the following sections of the Indian Penal Code appear to be applicable:
            
#             {ipc_text}
#         </div>
        
#         <div style="margin-bottom: 1.5rem;">
#             <strong>LEGAL PRECEDENTS:</strong>
#         </div>
        
#         <div style="margin-bottom: 1.5rem; text-align: justify; padding-left: 1rem;">
#             {getattr(precedents, 'summary', 'Relevant legal precedents support the application of the above-mentioned sections and provide guidance for appropriate legal remedies.') if hasattr(precedents, 'summary') else precedents.get('summary', 'Relevant legal precedents support the application of the above-mentioned sections and provide guidance for appropriate legal remedies.') if hasattr(precedents, 'get') else 'Relevant legal precedents support the application of the above-mentioned sections and provide guidance for appropriate legal remedies.'}
#         </div>
        
#         <div style="margin-bottom: 1.5rem;">
#             <strong>PRAYER/REQUEST:</strong>
#         </div>
        
#         <div style="margin-bottom: 1.5rem; text-align: justify; padding-left: 1rem;">
#             In light of the above facts and applicable legal provisions, I humbly request your office to:
#             <br><br>
#             1. Register the complaint under the appropriate sections of law<br>
#             2. Conduct a thorough investigation into the matter<br>
#             3. Take necessary legal action against the accused<br>
#             4. {getattr(document, 'demand_or_request', 'Ensure justice is served in accordance with the law') if hasattr(document, 'demand_or_request') else document.get('demand_or_request', 'Ensure justice is served in accordance with the law') if hasattr(document, 'get') else 'Ensure justice is served in accordance with the law'}
#         </div>
        
#         <div style="margin-bottom: 1.5rem; text-align: justify;">
#             I have attached all relevant documents and evidence supporting my case. I am available for any further 
#             clarification or additional information that may be required.
#         </div>
        
#         <div style="margin-bottom: 1.5rem;">
#             I look forward to your prompt action in this matter.
#         </div>
        
#         <div style="margin-top: 3rem;">
#             <div>Thanking you,</div>
#             <div style="margin-top: 2rem;">
#                 <div>Yours faithfully,</div>
#                 <div style="margin-top: 2rem; border-bottom: 1px solid #333; width: 200px;"></div>
#                 <div style="margin-top: 0.5rem;"><strong>[Your Full Name]</strong></div>
#                 <div><strong>[Your Signature]</strong></div>
#             </div>
#         </div>
        
#         <div style="margin-top: 2rem; border-top: 1px solid #ddd; padding-top: 1rem; font-size: 0.9rem; color: #666;">
#             <strong>Enclosures:</strong><br>
#             1. [List of documents attached, if any]<br>
#             2. [Evidence/Supporting materials]<br>
#             3. [Any other relevant documents]
#         </div>
        
#         <div style="margin-top: 2rem; padding: 1rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2a5298;">
#             <strong>📝 Instructions for Use:</strong><br>
#             <em style="color: #666; font-size: 0.9rem;">
#             • Replace all bracketed placeholders [ ] with your actual information<br>
#             • Add current date and your complete contact details<br>
#             • Customize the factual background with specific details of your case<br>
#             • Attach relevant documents as mentioned in enclosures<br>
#             • Print on letterhead if available for formal submission
#             </em>
#         </div>
#     </div>
#     """
    
#     return template

# # Page configuration
# st.set_page_config(
#     page_title="AI Legal Assistant", 
#     page_icon="⚖️", 
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS for enhanced styling
# st.markdown("""
# <style>
#     /* Main container styling */
#     .main-header {
#         background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
#         padding: 2rem;
#         border-radius: 15px;
#         margin-bottom: 2rem;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#     }
    
#     .main-header h1 {
#         color: white;
#         margin: 0;
#         font-size: 2.5rem;
#         font-weight: 700;
#         text-align: center;
#     }
    
#     .main-header p {
#         color: rgba(255,255,255,0.9);
#         margin: 1rem 0 0 0;
#         font-size: 1.1rem;
#         text-align: center;
#     }
    
#     /* Feature cards */
#     .feature-card {
#         background: white;
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 4px 16px rgba(0,0,0,0.08);
#         border-left: 4px solid #2a5298;
#         margin: 1rem 0;
#         transition: transform 0.2s ease;
#     }
    
#     .feature-card:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 24px rgba(0,0,0,0.12);
#     }
    
#     .feature-icon {
#         font-size: 1.5rem;
#         margin-right: 0.5rem;
#         color: #2a5298;
#     }
    
#     .feature-title {
#         font-weight: 600;
#         color: #1e3c72;
#         margin: 0;
#         font-size: 1.1rem;
#     }
    
#     .feature-desc {
#         margin: 0.5rem 0 0 0;
#         color: #666;
#         font-size: 0.95rem;
#     }
    
#     /* Form styling */
#     .stTextArea textarea {
#         border-radius: 12px !important;
#         border: 2px solid #e1e5e9 !important;
#         box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
#         transition: all 0.2s ease !important;
#     }
    
#     .stTextArea textarea:focus {
#         border-color: #2a5298 !important;
#         box-shadow: 0 4px 16px rgba(42,82,152,0.1) !important;
#     }
    
#     /* Button styling */
#     .stButton > button {
#         background: linear-gradient(135deg, #2a5298 0%, #1e3c72 100%) !important;
#         color: white !important;
#         border: none !important;
#         border-radius: 12px !important;
#         padding: 0.75rem 2rem !important;
#         font-weight: 600 !important;
#         font-size: 1.1rem !important;
#         transition: all 0.2s ease !important;
#         box-shadow: 0 4px 16px rgba(42,82,152,0.2) !important;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px) !important;
#         box-shadow: 0 6px 24px rgba(42,82,152,0.3) !important;
#     }
    
#     /* Results container */
#     .results-container {
#         background: white;
#         border-radius: 15px;
#         padding: 2rem;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#         border: 1px solid #e1e5e9;
#         margin-top: 2rem;
#     }
    
#     .results-header {
#         color: #1e3c72;
#         font-size: 1.5rem;
#         font-weight: 700;
#         margin-bottom: 1rem;
#         padding-bottom: 0.5rem;
#         border-bottom: 2px solid #2a5298;
#     }
    
#     /* Success message styling */
#     .success-banner {
#         background: linear-gradient(135deg, #10b981 0%, #059669 100%);
#         color: white;
#         padding: 1rem 1.5rem;
#         border-radius: 12px;
#         margin: 1rem 0;
#         font-weight: 600;
#         text-align: center;
#         box-shadow: 0 4px 16px rgba(16,185,129,0.2);
#     }
    
#     /* Spinner customization */
#     .stSpinner > div {
#         border-top-color: #2a5298 !important;
#     }
    
#     /* Warning styling */
#     .stAlert > div {
#         border-radius: 12px !important;
#     }
    
#     /* Hide streamlit branding */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
# </style>
# """, unsafe_allow_html=True)

# # Header section
# st.markdown("""
# <div class="main-header">
#     <h1>⚖️ Personal AI Legal Assistant</h1>
#     <p>Intelligent legal analysis powered by AI - Get instant insights for your legal matters</p>
# </div>
# """, unsafe_allow_html=True)

# # Features section
# st.markdown("### 🌟 What This Assistant Can Do")

# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">🔍</div>
#         <div class="feature-title">Legal Issue Analysis</div>
#         <div class="feature-desc">Understand complex legal problems in simple terms</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">📚</div>
#         <div class="feature-title">IPC Section Identification</div>
#         <div class="feature-desc">Find applicable Indian Penal Code sections</div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">⚖️</div>
#         <div class="feature-title">Precedent Case Research</div>
#         <div class="feature-desc">Retrieve relevant legal precedents and case law</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     st.markdown("""
#     <div class="feature-card">
#         <div class="feature-icon">📄</div>
#         <div class="feature-title">Legal Document Generation</div>
#         <div class="feature-desc">Create formal legal documents and reports</div>
#     </div>
#     """, unsafe_allow_html=True)

# # Main form section
# st.markdown("### 📝 Describe Your Legal Issue")
# st.markdown("*Provide a detailed description of your legal situation in plain English. The more specific you are, the better the analysis will be.*")

# with st.form("legal_form", clear_on_submit=False):
#     user_input = st.text_area(
#         "Legal Issue Description:",
#         height=200,
#         placeholder="Example: I am facing a property dispute with my neighbor who has built a wall on my land without permission. The wall blocks access to my garden and I believe this violates my property rights. What legal action can I take?",
#         help="Describe your situation in detail including relevant facts, parties involved, and what outcome you're seeking."
#     )
    
#     # Submit button with custom styling
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         submitted = st.form_submit_button("🔍 Analyze Legal Issue", use_container_width=True)

# # Processing and results
# if submitted:
#     if not user_input.strip():
#         st.warning("⚠️ Please enter a legal issue to analyze.")
#     else:
#         # Show processing state
#         with st.spinner("🔎 Analyzing your case and preparing comprehensive legal output..."):
#             st.info("🤖 AI Legal Assistant is working on your case. This may take a moment...")
#             result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

#         # Success message
#         st.markdown("""
#         <div class="success-banner">
#             ✅ Legal Analysis Complete! Your comprehensive legal report is ready.
#         </div>
#         """, unsafe_allow_html=True)

#         # Results section
#         st.markdown("""
#         <div class="results-container">
#             <div class="results-header">📄 Comprehensive Legal Analysis</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Format the result as a professional legal mail template
#         formatted_output = format_legal_output(result)
        
#         # Display formatted result
#         st.markdown(formatted_output, unsafe_allow_html=True)
        
#         # Additional action buttons
#         st.markdown("---")
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             if st.button("💾 Save Analysis", help="Save this analysis for future reference"):
#                 st.success("Analysis saved to your session!")
        
#         with col2:
#             if st.button("📧 Email Report", help="Send this report to your email"):
#                 st.info("Email functionality coming soon!")
        
#         with col3:
#             if st.button("🔄 New Analysis", help="Start a new legal analysis"):
#                 st.rerun()

# # Footer section
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; color: #666; padding: 2rem 0;">
#     <p><strong>⚖️ AI Legal Assistant</strong></p>
#     <p style="font-size: 0.9rem;">This tool provides legal information and guidance. For complex legal matters, please consult with a qualified attorney.</p>
#     <p style="font-size: 0.8rem; margin-top: 1rem;">Powered by Advanced AI • Secure & Confidential</p>
# </div>
# """, unsafe_allow_html=True)

# import streamlit as st
# from dotenv import load_dotenv
# # --- CHANGE 1: Import the simple crew instead of the main one ---
# from crew_simple import legal_assistant_crew_simple

# load_dotenv()

# # --- CHANGE 2: The complex HTML formatting function is no longer needed ---
# # We have removed the entire 'format_legal_output' function.

# # Page configuration
# st.set_page_config(
#     page_title="AI Legal Assistant", 
#     page_icon="⚖️", 
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS for enhanced styling (Your beautiful CSS is kept)
# st.markdown("""
# <style>
#     /* ... Your entire CSS from the previous version goes here ... */
#     /* Main container styling */
#     .main-header {
#         background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
#         padding: 2rem;
#         border-radius: 15px;
#         margin-bottom: 2rem;
#         box-shadow: 0 8px 32px rgba(0,0,0,0.1);
#     }
#     .main-header h1 { color: white; margin: 0; font-size: 2.5rem; text-align: center; }
#     .main-header p { color: rgba(255,255,255,0.9); margin: 1rem 0 0 0; font-size: 1.1rem; text-align: center; }
#     /* ... etc. ... */
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
# </style>
# """, unsafe_allow_html=True)

# # Header section
# st.markdown("""
# <div class="main-header">
#     <h1>⚖️ Personal AI Legal Assistant</h1>
#     <p>Intelligent legal analysis powered by AI - Get instant insights for your legal matters</p>
# </div>
# """, unsafe_allow_html=True)

# # Features section
# st.markdown("### 🌟 What This Assistant Can Do")
# col1, col2 = st.columns(2)
# # ... (Your feature cards are kept)

# # Main form section
# st.markdown("### 📝 Describe Your Legal Issue")
# st.markdown("*Provide a detailed description of your legal situation in plain English. The more specific you are, the better the analysis will be.*")

# with st.form("legal_form", clear_on_submit=False):
#     user_input = st.text_area(
#         "Legal Issue Description:",
#         height=200,
#         placeholder="Example: I am facing a property dispute with my neighbor...",
#         help="Describe your situation in detail..."
#     )
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         submitted = st.form_submit_button("🔍 Analyze Legal Issue", use_container_width=True)

# # Processing and results
# if submitted:
#     if not user_input.strip():
#         st.warning("⚠️ Please enter a legal issue to analyze.")
#     else:
#         with st.spinner("🔎 Analyzing your case and preparing legal output..."):
            
#             # --- CHANGE 3: Call the simple crew to get a plain text string ---
#             result_text = legal_assistant_crew_simple.kickoff(inputs={"user_input": user_input})

#         st.markdown("""
#         <div class="success-banner">
#             ✅ Legal Draft Complete! Your document is ready below.
#         </div>
#         """, unsafe_allow_html=True)

#         # --- CHANGE 4: Display the result in a simple, copy-friendly text area ---
#         st.markdown("""
#         <div class="results-container">
#             <div class="results-header">📄 Generated Legal Document</div>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Using st.text_area to display the plain text result
#         st.text_area("Your Legal Draft:", result_text, height=500)
        
#         st.markdown("---")
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("💾 Save Analysis"):
#                 st.success("Analysis saved to your session!")
#         with col2:
#             if st.button("📧 Email Report"):
#                 st.info("Email functionality coming soon!")
#         with col3:
#             if st.button("🔄 New Analysis"):
#                 st.rerun()

# # Footer section
# st.markdown("---")
# st.markdown("""
# <div style="text-align: center; color: #666; padding: 2rem 0;">
#     <p><strong>⚖️ AI Legal Assistant</strong></p>
#     <p style="font-size: 0.9rem;">This tool provides legal information and guidance. For complex legal matters, please consult with a qualified attorney.</p>
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
from dotenv import load_dotenv
# --- CHANGE 1: Import the simple crew instead of the main one ---
from crew_simple import legal_assistant_crew_simple

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Legal Assistant", 
    page_icon="⚖️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Custom CSS for modern styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Main header with gradient and glassmorphism */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        font-family: 'Inter', sans-serif;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.95);
        margin: 1.5rem 0 0 0;
        font-size: 1.3rem;
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        position: relative;
        z-index: 1;
    }
    
    /* Feature cards with hover animations */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        margin: 1.5rem 0;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        border-color: #667eea;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 1rem;
        display: block;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .feature-title {
        font-weight: 600;
        color: #2d3748;
        margin: 0 0 0.5rem 0;
        font-size: 1.3rem;
        font-family: 'Inter', sans-serif;
    }
    
    .feature-desc {
        color: #718096;
        font-size: 1rem;
        line-height: 1.6;
        font-family: 'Inter', sans-serif;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2d3748;
        margin: 3rem 0 1.5rem 0;
        font-family: 'Inter', sans-serif;
        position: relative;
        padding-left: 1rem;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 2px;
    }
    
    /* Enhanced form styling */
    .stTextArea textarea {
        border-radius: 16px !important;
        border: 2px solid #e2e8f0 !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
        padding: 1rem !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea !important;
        box-shadow: 0 8px 40px rgba(102, 126, 234, 0.2) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Glowing button effect */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 1rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 16px 48px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) !important;
    }
    
    /* Results container with glassmorphism */
    .results-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2.5rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        margin-top: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .results-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    .results-header {
        color: #2d3748;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        font-family: 'Inter', sans-serif;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Enhanced success banner */
    .success-banner {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 16px;
        margin: 2rem 0;
        font-weight: 600;
        text-align: center;
        font-size: 1.1rem;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 8px 32px rgba(72, 187, 120, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .success-banner::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: rgba(255,255,255,0.1);
        animation: shimmer 2s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Text area for results */
    .stTextArea div[data-testid="stTextArea"] > div > div {
        background: #f7fafc !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 16px !important;
        font-family: 'Courier New', monospace !important;
    }
    
    /* Action buttons row */
    .action-buttons {
        display: flex;
        gap: 1rem;
        margin-top: 2rem;
        justify-content: center;
    }
    
    /* Footer enhancement */
    .footer-container {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border-radius: 16px;
        padding: 2rem;
        margin-top: 3rem;
        text-align: center;
        border: 1px solid #e2e8f0;
    }
    
    .footer-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 0.5rem;
        font-family: 'Inter', sans-serif;
    }
    
    .footer-subtitle {
        color: #718096;
        font-size: 1rem;
        margin-bottom: 1rem;
        font-family: 'Inter', sans-serif;
    }
    
    .footer-note {
        color: #a0aec0;
        font-size: 0.9rem;
        font-family: 'Inter', sans-serif;
    }
    
    /* Spinner customization */
    .stSpinner > div {
        border-top-color: #667eea !important;
        border-right-color: #764ba2 !important;
    }
    
    /* Warning and info alerts */
    .stAlert > div {
        border-radius: 12px !important;
        border: none !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Hide streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        .main-header p {
            font-size: 1rem;
        }
        .feature-card {
            margin: 1rem 0;
            padding: 1.5rem;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a67d8, #6b46c1);
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Header section with floating elements
st.markdown("""
<div class="main-header">
    <h1>⚖️ JurisTech: Navigate Your Legal Path</h1>
    <p>Intelligent legal analysis powered by AI • Get instant insights for your legal matters</p>
</div>
""", unsafe_allow_html=True)

# Enhanced Features section
st.markdown('<div class="section-header">🌟 What This Assistant Can Do</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Legal Issue Analysis</div>
        <div class="feature-desc">Understand complex legal problems broken down into clear, actionable insights</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">IPC Section Identification</div>
        <div class="feature-desc">Find applicable Indian Penal Code sections with detailed explanations</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚖️</div>
        <div class="feature-title">Precedent Case Research</div>
        <div class="feature-desc">Retrieve relevant legal precedents and landmark case law references</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Legal Document Generation</div>
        <div class="feature-desc">Create formal legal documents, complaints, and professional reports</div>
    </div>
    """, unsafe_allow_html=True)

# Enhanced Main form section
st.markdown('<div class="section-header">📝 Describe Your Legal Issue</div>', unsafe_allow_html=True)
st.markdown("""
<div style="background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%); 
           padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; 
           border-left: 4px solid #667eea;">
    <em style="color: #4a5568; font-size: 1rem; font-family: 'Inter', sans-serif;">
        💡 <strong>Pro Tip:</strong> Provide a detailed description of your legal situation in plain English. 
        Include relevant dates, parties involved, and what outcome you're seeking for the most accurate analysis.
    </em>
</div>
""", unsafe_allow_html=True)

with st.form("legal_form", clear_on_submit=False):
    user_input = st.text_area(
        "Legal Issue Description:",
        height=220,
        placeholder="Example: I am facing a property dispute with my neighbor who has built a wall on my land without permission. The wall blocks access to my garden and I believe this violates my property rights. What legal action can I take? Please include specific dates, documents you have, and any communication with the other party...",
        help="📋 Describe your situation in detail including relevant facts, parties involved, timeline, and what outcome you're seeking."
    )
    
    # Enhanced Submit button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        submitted = st.form_submit_button("🔍 Analyze Legal Issue", use_container_width=True)

# Enhanced Processing and results
if submitted:
    if not user_input.strip():
        st.warning("⚠️ Please enter a legal issue to analyze for comprehensive assistance.")
    else:
        # Enhanced loading state
        with st.spinner("🔎 Our AI Legal Expert is analyzing your case and preparing comprehensive legal documentation..."):
            st.info("🤖 **Processing Steps:** Analyzing legal context → Identifying applicable laws → Researching precedents → Drafting document...")
            
            # --- CHANGE 3: Call the simple crew to get a plain text string ---
            result_text = legal_assistant_crew_simple.kickoff(inputs={"user_input": user_input})

        # Enhanced success message
        st.markdown("""
        <div class="success-banner">
            ✅ Legal Analysis Complete! Your comprehensive legal document is ready below.
        </div>
        """, unsafe_allow_html=True)

        # --- CHANGE 4: Display the result in a simple, copy-friendly text area ---
        st.markdown("""
        <div class="results-container">
            <div class="results-header">📄 Generated Legal Document</div>
            <div style="color: #718096; margin-bottom: 1rem; font-family: 'Inter', sans-serif;">
                Your personalized legal document is ready. You can copy, edit, or save this content for your use.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced text area for results
        st.text_area(
            "Your Legal Draft:", 
            result_text, 
            height=500,
            help="💾 You can select all (Ctrl+A) and copy (Ctrl+C) this text to save or share your legal document."
        )
        
        # Enhanced action buttons
        st.markdown("---")
        st.markdown("### Quick Actions")
        col1, col2, col3 = st.columns(3, gap="large")
        
        with col1:
            if st.button("💾 Save Analysis", help="Save this analysis to your session history"):
                st.success("✅ Analysis saved to your session!")
        
        with col2:
            if st.button("📧 Email Report", help="Send this report to your email address"):
                st.info("📬 Email functionality coming soon!")
        
        with col3:
            if st.button("🔄 New Analysis", help="Start fresh with a new legal analysis"):
                st.rerun()

# Enhanced Footer section
st.markdown("---")
st.markdown("""
<div class="footer-container">
    <div class="footer-title">⚖️ AI Legal Assistant</div>
    <div class="footer-subtitle">
        This tool provides legal information and guidance based on Indian law. 
        For complex legal matters, please consult with a qualified attorney.
    </div>
    <div class="footer-note">
        🔒 Secure & Confidential • 🤖 Powered by Advanced AI • 🇮🇳 Indian Legal Framework
    </div>
</div>
""", unsafe_allow_html=True)