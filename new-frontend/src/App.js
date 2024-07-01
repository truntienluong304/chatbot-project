import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:3000/api/ask', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error('Error fetching the answer:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Health Chatbot</h1>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Enter your question"
          />
          <button type="submit">Ask</button>
        </form>
        {answer && (
          <div>
            <h2>Answer:</h2>
            <p>{answer}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
