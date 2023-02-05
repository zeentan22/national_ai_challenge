import React, { useState, useRef, useEffect} from "react";
import './App.css';
import { ThreeCircles } from 'react-loader-spinner';
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title } from 'chart.js';
import { Pie, Bar } from 'react-chartjs-2';

//settle layout
//tryout input and uploading of files
//based on input, perform analysis

function App() {
  const scrollRef = useRef(null);
  const executeScroll = () => {scrollRef.current.scrollIntoView();} 
  //const useMountEffect = fun => useEffect(fun, []); // i think it rerenders the page and scrolls to that portion
  //useMountEffect(executeScroll);

  const [sentence, setSentence] = useState('');
  const [aspect, setAspect] = useState('');
  const [file, setFile] = useState(null);
  
  const [toggle, setToggle] = useState(false);
  const [status, setStatus] = useState(false);
  const [outputt, setOutputt] = useState({
    'school': {'count': 4, 'positive': 3, 'neutral': 0, 'negative': 1}, 
    'students': {'count': 4, 'positive': 2, 'neutral': 1, 'negative': 1}, 
    'meeting': {'count': 1, 'positive': 1, 'neutral': 0, 'negative': 0},
    'scripts': {'count': 5, 'positive': 0, 'neutral': 1, 'negative': 4},
    'exams': {'count': 6, 'positive': 1, 'neutral': 1, 'negative': 4},
    'colleagues': {'count': 1, 'positive': 0, 'neutral': 0, 'negative': 1}
    });

  let loading = 
  <div style={{display:'flex', flexDirection:'column', alignItems:'center', }}>
    <ThreeCircles
      height="100"
      width="100"
      color="#4fa94d"
      wrapperStyle={{}}
      wrapperClass=""
      visible={true}
      ariaLabel="three-circles-rotating"
      outerCircleColor=""
      innerCircleColor=""
      middleCircleColor=""
    />
    <p>Running our model through your inputs</p>
  </div>

let analysis = <div id="analysis" style={{marginTop:40}}></div>
if (status) {
  //formatting data for charts
  ChartJS.register(ArcElement, Tooltip, Legend);
  ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
  const data = {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
        label: 'Occurences',
        data: [12, 19, 3, 5, 2, 3],
      },
    ],
  };
  
  //data for aspect bar graph
  const aspectCount = {labels: Object.keys(outputt),
  datasets: [{
      label: 'Aspect',
      data: Object.keys(outputt).map(x => outputt[x]['count']),
    },
  ],}

  //data for emotions pie chart
  let emotions = [0, 0, 0];
  for (const aspect in outputt) {
      emotions[0] = emotions[0] + outputt[aspect]['positive'];
      emotions[1] = emotions[1] + outputt[aspect]['neutral'];
      emotions[2] = emotions[2] + outputt[aspect]['negative'];
  }
  const emotionsChart = {labels: ["Positive", "Neutral", "Negative"],
    datasets: [{
        label: 'Emotions',
        data: emotions
      },
    ],}

  //data for aspect pie chart
  let negativeAspects = Object.keys(outputt).sort(
    function(a, b) {
      return outputt[b]['negative'] - outputt[a]['negative'];
  }).splice(0,3)

  const aspectsChart = {labels: negativeAspects,
  datasets: [{
      label: 'Top 3 Most Negative Aspects',
      data: [outputt[negativeAspects[0]]['negative'], outputt[negativeAspects[1]]['negative'], outputt[negativeAspects[2]]['negative'] ]
    },
  ],}


  analysis = 
  <div id="analysis" style={{marginTop:40, display:'flex', flexDirection:'column', alignItems:'center'}}>
    <div style={{height:'60vh', width:'40%'}}>
      <Bar data={aspectCount}/>
    </div>

    <div style={{display:'flex', height:'60vh', width:'100%', justifyContent:'space-around',}}>
      <div style={{width:"28%"}}><Pie data={emotionsChart}/></div>
      <div style={{width:"28%"}}><Pie data={aspectsChart}/></div>
    </div>
  </div>
}
  


const handleAnalysis = () => {
  //check for file type, if file type is not correct, raise an alert
  let db;
  //toggling to true starts the loading animation
  setToggle(true);
  //timeout function is to simulate retrieving of data
  retrieveData(db);
}



const retrieveData = async(db) => {
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
