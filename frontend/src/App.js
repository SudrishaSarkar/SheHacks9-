
import React from 'react';
import './App.css';
//import { IoDownloadOutline } from "react-icons/io5";
//import { SlMicrophone } from "react-icons/sl";

function App() {
  return (
    <div className="homepage">
      <header className="header">
      <div
  style={{
    color: '#35522B',
    textAlign: 'center',
    fontFeatureSettings: "'liga' off, 'clig' off",
    fontFamily: 'Nerko One' ,
    fontSize: '60px',
    fontStyle: 'normal',
    fontWeight: 400,
    lineHeight: '120%',
    letterSpacing: '-1.5px',
  }}
>
  MoodMate
</div>

<div
  style={{
    width: '868px',
    height: '83px',
    flexShrink: '0',
    color: '#35522B',
    textAlign: 'center',
    fontFeatureSettings: "'liga' off, 'clig' off",  // Corrected camelCase for fontFeatureSettings
    fontFamily: 'Neucha',
    fontSize: '30px',
    fontStyle: 'normal',
    fontWeight: 400,
    lineHeight: '120%',  // line-height can remain a percentage
    letterSpacing: '-0.96px',
  }}
>
  Vent, rant, talk — it's your space, your pace.
</div>

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
