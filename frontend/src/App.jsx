// import React, { useState, useRef, useEffect } from 'react';
// import { Send, FileText, Scale, Search, BookOpen, User, Gavel, Shield, Zap, Loader2, CheckCircle, Clock, AlertCircle } from 'lucide-react';
// import './App.css';

// function App() {
//   const [userInput, setUserInput] = useState('');
//   const [isProcessing, setIsProcessing] = useState(false);
//   const [currentStep, setCurrentStep] = useState(0);
//   const [results, setResults] = useState(null);
//   const [error, setError] = useState(null);
//   const textareaRef = useRef(null);

//   const agents = [
//     { id: 'intake', name: 'Case Intake Agent', description: 'Structuring case information' },
//     { id: 'ipc', name: 'IPC Section Agent', description: 'Finding relevant laws' },
//     { id: 'precedent', name: 'Legal Precedent Agent', description: 'Researching past cases' },
//     { id: 'drafting', name: 'Document Drafting Agent', description: 'Preparing your document' }
//   ];

//   const handleSubmit = async () => {
//     if (!userInput.trim()) return;

//     setIsProcessing(true);
//     setCurrentStep(0);
//     setResults(null);
//     setError(null);

//     try {
//       // Simulate agent workflow for UI effect
//       for (let i = 0; i < agents.length; i++) {
//         setCurrentStep(i);
//         await new Promise(resolve => setTimeout(resolve, 1500));
//       }
      
//       const response = await fetch('http://localhost:8000/analyze', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ user_input: userInput }),
//       });

//       const data = await response.json();

//       // **THIS IS THE KEY FIX:** Check for both network errors and application errors
//       if (!response.ok || data.error) {
//         throw new Error(data.error || 'Failed to analyze the issue.');
//       }

//       setResults(data.response);
//       console.log(data.response);
//       console.log(results.case_analysis);
//       setCurrentStep(agents.length);

//     } catch (err) {
//       console.error('API call failed:', err);
//       setError(err.message);
//     } finally {
//       setIsProcessing(false);
//     }
//   };

//   useEffect(() => {
//     if (textareaRef.current) {
//       textareaRef.current.style.height = 'auto';
//       textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
//     }
//   }, [userInput]);

//   return (
//     <div className="app-container">
//       <div className="background-overlay">
//         <div className="floating-element floating-1"></div>
//         <div className="floating-element floating-2"></div>
//         <div className="floating-element floating-3"></div>
//       </div>

//       <div className="main-container">
//         <header className="hero-section">
//           <div className="hero-icon"><Scale size={40} /></div>
//           <h1 className="hero-title">AI Legal Assistant</h1>
//           <p className="hero-subtitle">
//             Get comprehensive legal analysis powered by advanced AI agents. 
//             <span className="highlight-text"> Streamline your legal research</span> with intelligent automation.
//           </p>
//           <div className="features-grid">
//             <FeatureCard icon={<Zap size={24} />} title="Lightning Fast" description="Get instant legal analysis" color="emerald" />
//             <FeatureCard icon={<Shield size={24} />} title="Comprehensive" description="Multi-agent legal research" color="purple" />
//             <FeatureCard icon={<Gavel size={24} />} title="Accurate" description="Precise case analysis" color="orange" />
//           </div>
//         </header>

//         <div className="input-form-container">
//           <div className="input-wrapper">
//             <textarea
//               ref={textareaRef}
//               value={userInput}
//               onChange={(e) => setUserInput(e.target.value)}
//               placeholder="Describe your legal situation in detail..."
//               className="input-textarea"
//               rows={6}
//               disabled={isProcessing}
//             />
//             <div className="character-count">{userInput.length} characters</div>
//           </div>
//           <button onClick={handleSubmit} disabled={!userInput.trim() || isProcessing} className={`submit-button ${isProcessing ? 'processing' : ''}`}>
//             {isProcessing ? <><Loader2 className="button-icon spinning" size={20} />Analyzing...</> : <><Send className="button-icon" size={20} />Analyze Legal Issue</>}
//           </button>
//         </div>

//         {(isProcessing || results || error) && (
//           <div className="results-section">
//             <div className="workflow-container">
//               <h2 className="section-title"><BookOpen className="section-icon" size={24} />AI Agent Workflow</h2>
//               <div className="agents-list">
//                 {agents.map((agent, index) => {
//                   const isCompleted = (!isProcessing && results) || (isProcessing && index < currentStep);
//                   const isActive = isProcessing && index === currentStep;
//                   return (
//                     <div key={agent.id} className={`agent-card ${isCompleted ? 'agent-completed' : isActive ? 'agent-active' : 'agent-pending'}`}>
//                       <div className="agent-status-icon">
//                         {isCompleted ? <div className="status-icon status-success"><CheckCircle size={20} /></div> : isActive ? <div className="status-icon status-processing"><Loader2 className="spinning" size={20} /></div> : <div className="status-icon status-waiting"><Clock size={20} /></div>}
//                       </div>
//                       <div className="agent-info"><p className="agent-name">{agent.name}</p><p className="agent-description">{agent.description}</p></div>
//                       {isActive && <div className="active-indicator"></div>}
//                     </div>
//                   );
//                 })}
//               </div>
//             </div>

//             {error && <div className="error-container"><div className="error-header"><AlertCircle size={20} /><p className="error-title">Analysis Error</p></div><p className="error-message">{error}</p></div>}

//             {results && (
//               <div className="results-container">
//                 <h2 className="results-title"><Scale size={24} />Legal Analysis Results</h2>
//                 <div className="results-grid">
                    
//                   <ResultCard icon={<FileText size={20} />} title="Case Analysis" data={results.case_analysis} color="blue" />
//                   <ResultCard icon={<Scale size={20} />} title="Applicable IPC Sections" data={results.applicable_ipc_sections} color="purple" />
//                   <ResultCard icon={<Search size={20} />} title="Legal Precedents" data={results.legal_precedents} color="emerald" isSummary={true} />
//                   <ResultCard icon={<Gavel size={20} />} title="Drafted Document" data={results.drafted_document} color="orange" />
//                 </div>
//               </div>
//             )}
//           </div>
//         )}
//       </div>
//     </div>
//   );
// };

// const FeatureCard = ({ icon, title, description, color }) => (
//   <div className="feature-card">
//     <div className={`feature-icon feature-icon-${color}`}>{icon}</div>
//     <h3 className="feature-title">{title}</h3>
//     <p className="feature-description">{description}</p>
//   </div>
// );

// const ResultCard = ({ icon, title, data, color, isSummary }) => (
//   <div className={`result-card result-card-${color}`}>
//     <h3 className="result-card-title">{icon}{title}</h3>
//     <div className="result-content"><pre className="result-text">{isSummary ? data?.summary : JSON.stringify(data, null, 2)}</pre></div>
//   </div>
// );

// export default App;

import React, { useState, useRef, useEffect } from 'react';
import { Send, FileText, Scale, Search, BookOpen, User, Gavel, Shield, Zap, Loader2, CheckCircle, Clock, AlertCircle } from 'lucide-react';
import './App.css';

function App() {
  const [userInput, setUserInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const textareaRef = useRef(null);

  const agents = [
    { id: 'intake', name: 'Case Intake Agent', description: 'Structuring case information' },
    { id: 'ipc', name: 'IPC Section Agent', description: 'Finding relevant laws' },
    { id: 'precedent', name: 'Legal Precedent Agent', description: 'Researching past cases' },
    { id: 'drafting', name: 'Document Drafting Agent', description: 'Preparing your document' }
  ];

  const handleSubmit = async () => {
    if (!userInput.trim()) return;
    setIsProcessing(true);
    setCurrentStep(0);
    setResults(null);
    setError(null);
    try {
      for (let i = 0; i < agents.length; i++) {
        setCurrentStep(i);
        await new Promise(resolve => setTimeout(resolve, 1500));
      }
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_input: userInput }),
      });
      const data = await response.json();
      if (!response.ok || data.error) {
        throw new Error(data.error || 'Failed to analyze the issue.');
      }
      setResults(data.response);
      setCurrentStep(agents.length);
    } catch (err) {
      console.error('API call failed:', err);
      setError(err.message);
    } finally {
      setIsProcessing(false);
    }
  };

  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
    }
  }, [userInput]);

  return (
    <div className="app-container">
      <div className="background-overlay">
        <div className="floating-element floating-1"></div>
        <div className="floating-element floating-2"></div>
        <div className="floating-element floating-3"></div>
      </div>
      <div className="main-container">
        <header className="hero-section">
          <div className="hero-icon"><Scale size={30} /></div>
          <h1 className="hero-title">JurisTech: Navigate Your Legal Path</h1>
          <p className="hero-subtitle">
            Get comprehensive legal analysis powered by advanced AI agents. 
            <span className="highlight-text"> Streamline your legal research</span> with intelligent automation.
          </p>
          <div className="features-grid">
            <FeatureCard icon={<Zap size={24} />} title="Lightning Fast" description="Get instant legal analysis" color="emerald" />
            <FeatureCard icon={<Shield size={24} />} title="Comprehensive" description="Multi-agent legal research" color="purple" />
            <FeatureCard icon={<Gavel size={24} />} title="Accurate" description="Precise case analysis" color="orange" />
          </div>
        </header>
        <div className="input-form-container">
          <div className="input-wrapper">
            <textarea
              ref={textareaRef}
              value={userInput}
              onChange={(e) => setUserInput(e.target.value)}
              placeholder="Describe your legal situation in detail..."
              className="input-textarea"
              rows={6}
              disabled={isProcessing}
            />
            <div className="character-count">{userInput.length} characters</div>
          </div>
          <button onClick={handleSubmit} disabled={!userInput.trim() || isProcessing} className={`submit-button ${isProcessing ? 'processing' : ''}`}>
            {isProcessing ? <><Loader2 className="button-icon spinning" size={20} />Analyzing...</> : <><Send className="button-icon" size={20} />Analyze Legal Issue</>}
          </button>
        </div>
        {(isProcessing || results || error) && (
          <div className="results-section">
            <div className="workflow-container">
              <h2 className="section-title"><BookOpen className="section-icon" size={24} />AI Agent Workflow</h2>
              <div className="agents-list">
                {agents.map((agent, index) => {
                  const isCompleted = (!isProcessing && results) || (isProcessing && index < currentStep);
                  const isActive = isProcessing && index === currentStep;
                  return (
                    <div key={agent.id} className={`agent-card ${isCompleted ? 'agent-completed' : isActive ? 'agent-active' : 'agent-pending'}`}>
                      <div className="agent-status-icon">{isCompleted ? <div className="status-icon status-success"><CheckCircle size={20} /></div> : isActive ? <div className="status-icon status-processing"><Loader2 className="spinning" size={20} /></div> : <div className="status-icon status-waiting"><Clock size={20} /></div>}</div>
                      <div className="agent-info"><p className="agent-name">{agent.name}</p><p className="agent-description">{agent.description}</p></div>
                      {isActive && <div className="active-indicator"></div>}
                    </div>
                  );
                })}
              </div>
            </div>
            {error && <div className="error-container"><div className="error-header"><AlertCircle size={20} /><p className="error-title">Analysis Error</p></div><p className="error-message">{error}</p></div>}
            
            {/* --- START OF CHANGES --- */}
            {results && (
              <div className="results-container">
                <h2 className="results-title"><Scale size={24} />Legal Analysis Results</h2>
                <div className="results-grid">

                  <ResultCard icon={<FileText size={20} />} title="Case Analysis" color="blue">
                    <p className="result-text">{results.case_analysis?.summary}</p>
                  </ResultCard>

                  <ResultCard icon={<Scale size={20} />} title="Applicable IPC Sections" color="purple">
                    {results.applicable_ipc_sections?.map((section, index) => (
                      <div key={index} className="ipc-section">
                        <strong>Section {section.section}: {section.section_title}</strong>
                        <p>{section.content}</p>
                      </div>
                    ))}
                  </ResultCard>

                  <ResultCard icon={<Search size={20} />} title="Legal Precedents" color="emerald">
                    <p className="result-text">{results.legal_precedents?.summary}</p>
                  </ResultCard>
                  
                  <ResultCard icon={<Gavel size={20} />} title="Drafted Document Demand" color="orange">
                    <p className="result-text">{results.drafted_document?.demand_or_request}</p>
                  </ResultCard>

                </div>
              </div>
            )}
            {/* --- END OF CHANGES --- */}

          </div>
        )}
      </div>
    </div>
  );
};

const FeatureCard = ({ icon, title, description, color }) => (
  <div className="feature-card">
    <div className={`feature-icon feature-icon-${color}`}>{icon}</div>
    <h3 className="feature-title">{title}</h3>
    <p className="feature-description">{description}</p>
  </div>
);

// This component is now a simple wrapper
const ResultCard = ({ icon, title, color, children }) => (
  <div className={`result-card result-card-${color}`}>
    <h3 className="result-card-title">{icon}{title}</h3>
    <div className="result-content">{children}</div>
  </div>
);

export default App;