
import React from 'react';
import './App.css';
import { IoDownloadOutline } from "react-icons/io5";
import { SlMicrophone } from "react-icons/sl";

function App() {
  return (
    <div className="homepage">
      <header className="header">
      <div
  style={{
    color: 'rgba(53, 82, 43, 0.87)',
    textAlign: 'center',
    fontFeatureSettings: "'liga' off, 'clig' off",
    fontFamily: '"Nerko One"',
    fontSize: '128px',
    fontStyle: 'normal',
    fontWeight: 400,
    lineHeight: '120%',
    letterSpacing: '-2.56px',
  }}
>
  MoodMate
</div>

        <p>Vent, rant, talk — it's your space, your pace.</p>
      </header>

      <div className="robot-section">
        <img src="/robot.png" alt="MoodMate Robot" className="robot-image" />
        <div className="speech-bubble">
          Got no one to talk to? <br /> I am here for you when no one is.
        </div>
      </div>

      <div className="input-section">
      <SlMicrophone className="mic" />
        <input
          type="text"
          placeholder="Type your feelings away or record..."
          className="input-box"
        />
        <IoDownloadOutline className="download"/>
        <button className="send-button">➤</button>
      </div>
    </div>











  );
}

export default App;
