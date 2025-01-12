// import Header from './Header.js'

// function App() {

//   return(
//   <homepage></homepage>
//   );
// }

// export default App



import React from 'react';
import './App.css';

function App() {
  return (
    <div className="homepage">
      <header className="header">
        <h1>MoodMate</h1>
        <p>Vent, rant, talk—it's your space, your pace.</p>
      </header>

      <div className="robot-section">
        <img src="/robot.png" alt="MoodMate Robot" className="robot-image" />
        <div className="speech-bubble">
          Got no one to talk to? <br /> I am here for you when no one is.
        </div>
      </div>

      <div className="input-section">
        <input
          type="text"
          placeholder="Type your feelings away or record..."
          className="input-box"
        />
        <button className="send-button">➤</button>
      </div>
    </div>
  );
}

export default App;
