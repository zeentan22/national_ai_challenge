import React, { useState, useRef, useEffect} from "react";
import './App.css';
import { ThreeCircles } from 'react-loader-spinner';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title } from 'chart.js';
import { Pie, Bar } from 'react-chartjs-2';

function App() {

  const [toggle, setToggle] = useState(false); //toggling analyse button
  const [status, setStatus] = useState(false); //status of get request 
  const [outputt, setOutputt] = useState({
    'school': {'count': 4, 'positive': 3, 'neutral': 0, 'negative': 1}, 
    'students': {'count': 4, 'positive': 2, 'neutral': 1, 'negative': 1}, 
    'meeting': {'count': 1, 'positive': 1, 'neutral': 0, 'negative': 0},
    'scripts': {'count': 5, 'positive': 0, 'neutral': 1, 'negative': 4},
    'exams': {'count': 6, 'positive': 1, 'neutral': 1, 'negative': 4},
    'colleagues': {'count': 1, 'positive': 0, 'neutral': 0, 'negative': 1}
    }); //to store output of get request
  

  let loading = 
    <div style={{display:'flex', flexDirection:'column', alignItems:'center', }}>
      <ThreeCircles height="100" width="100" color="#4fa94d" visible={true} ariaLabel="three-circles-rotating" />
      <p>Running our model through your inputs</p>
    </div>

  
  //data preparations for the chart + creation of charts

  //the analysis div is empty until the data is ready to display
  let analysis = <div style={{marginTop:40}}></div>
  if (status) {
    ChartJS.register(ArcElement, Tooltip, Legend);
    ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
    
    //aspect bar graph
    const options_color_aspects = {
      responsive: true,
      plugins: {
        title: {display: true, text: 'Summary of Aspects detected',}
      }
    };
    const color_aspects = Object.keys(outputt).map(x => `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 1)`);
    const aspectCount = {
      labels: Object.keys(outputt),
      datasets: [{
          label: 'Aspects',
          data: Object.keys(outputt).map(x => outputt[x]['count']),
          backgroundColor: color_aspects,
          borderColor: color_aspects,
          borderWidth: 1,
        },
      ],}

    //emotions pie chart
    const options_emotionsChart = {
      responsive: true,
      plugins: {
        title: {display: true,text: 'Breakdown of the different emotions',}
      }};
    let emotions = [0, 0, 0];
    for (const aspect in outputt) {
        emotions[0] = emotions[0] + outputt[aspect]['positive'];
        emotions[1] = emotions[1] + outputt[aspect]['neutral'];
        emotions[2] = emotions[2] + outputt[aspect]['negative'];
    }
    const color_emotions = emotions.map(x => `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 1)`);
    const emotionsChart = {
      labels: ["Positive", "Neutral", "Negative"],
      datasets: [{
          label: 'Count',
          data: emotions, 
          backgroundColor: color_emotions,
          borderColor: color_emotions,
          borderWidth: 1,
        },
      ],}

    //aspect pie chart
    const options_aspectsChart = {responsive: true,
      plugins: {
        title: {display: true, text: 'Summary of Aspects detected',
        }
      }};
    let negativeAspects = Object.keys(outputt).sort(function(a, b) {
        return outputt[b]['negative'] - outputt[a]['negative'];
    }).splice(0,3)

    const color_analysis = negativeAspects.map(x => `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 1)`);
    const aspectsChart = {labels: negativeAspects,
    datasets: [{
        label: 'Count',
        data: [outputt[negativeAspects[0]]['negative'], outputt[negativeAspects[1]]['negative'], outputt[negativeAspects[2]]['negative'] ],
        backgroundColor: color_analysis,
        borderColor: color_analysis,
        borderWidth: 1,
      },
    ],
  }

  //this is the component that will be loaded after data is processed successfully
  analysis = 
    <div id="analysis" style={{marginTop:40, display:'flex', flexDirection:'column', alignItems:'center'}}>
      <div style={{height:'60vh', width:'40%'}}>
        <Bar data={aspectCount} options={options_color_aspects}/>
      </div>

      <div style={{display:'flex', height:'60vh', width:'100%', justifyContent:'space-around',}}>
        <div style={{width:"28%"}}><Pie data={emotionsChart} options={options_emotionsChart}/></div>
        <div style={{width:"28%"}}><Pie data={aspectsChart} options={options_aspectsChart}/></div>
      </div>
    </div>
  }
    

  const handleAnalysis = () => {
    //toggling to true starts the loading animation, setting toggling to false stops the animation
    setToggle(true);
    //timeout function is to simulate retrieving of data, setting status to true renders the analysis component
    setTimeout(() => {setToggle(false); setStatus(true);}, 2000);
  }

  return (
    <div style={{display:'flex', flexDirection:'column', height:600}}>
      <div style={{height:'60%', display:'flex', flexDirection:'column', alignItems:'center', justifyContent:'flex-end'}}>
        <p style={{fontSize:80, fontWeight:'bold', marginBottom:5}}>AI Challenge 2023 
        {<p style={{fontSize:20, marginLeft:30}}>We provide meaning to your sentences</p>}
        </p>
      </div>

      {/*user interface*/}
      <div style={{display:'flex', marginTop:10, marginLeft:30 ,justifyContent:'center', width:'95%'}}>
        <div>
          <div style={{display:'flex', alignItems:'center', height:'100%'}}>
            <button onClick={()=>{handleAnalysis();document.getElementById("analysis").scrollIntoView({behavior: "smooth"});}}>Analyse</button>
          </div>
        </div>
      </div>
      
      {/*loading animation / transition to actual analysis*/}
      <div style={{display:'flex', height: '30%', justifyContent:'center', alignItems:'center', marginTop:20}}>
        {toggle ?  loading : <div></div>}
      </div>

      {analysis}

    </div>
  );
}

export default App;
