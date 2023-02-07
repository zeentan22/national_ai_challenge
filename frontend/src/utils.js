import React from "react";

let used_output = {
  school: { count: 4, positive: 3, neutral: 0, negative: 1 },
  students: { count: 4, positive: 2, neutral: 1, negative: 1 },
  meeting: { count: 1, positive: 1, neutral: 0, negative: 0 },
  scripts: { count: 5, positive: 0, neutral: 1, negative: 4 },
  exams: { count: 6, positive: 1, neutral: 1, negative: 4 },
  colleagues: { count: 1, positive: 0, neutral: 0, negative: 1 },
}; //to store output of get request

// example data from jerry api
// let output_from_api = [
//   {
//     time: "2019-08-24T14:15:22Z",
//     history_data: [
//       {
//         id: 0,
//         aspect: "school",
//         emotion: -1,
//         history: 0,
//       },
//       {
//         id: 1,
//         aspect: "student",
//         emotion: -1,
//         history: 0,
//       },
//     ],
//   },
//   {
//     time: "2019-09-24T14:15:22Z",
//     history_data: [
//       {
//         id: 0,
//         aspect: "meetings",
//         emotion: 1,
//         history: 0,
//       },
//       {
//         id: 1,
//         aspect: "scripts",
//         emotion: -1,
//         history: 0,
//       },
//       {
//         id: 2,
//         aspect: "student",
//         emotion: -1,
//         history: 0,
//       },
//     ],
//   },
// ];

// helper function
let update_aspect_result_label = (current_res, label) => {
  if (label == 1) {
    current_res["positive"] = current_res["positive"] + 1;
  } else if (label == 0) {
    current_res["neutral"] = current_res["neutral"] + 1;
  } else {
    current_res["negative"] = current_res["negative"] + 1;
  }
  return current_res;
};

// this is to help you convert data from jerry api into the format that you are currently using
export const convert_data = (input) => {
  let result = {};
  for (let index in input) {
    let historydata = input[index].history_data;
    // console.log(historydata);
    for (let j in historydata) {
      let aspect = historydata[j].aspect;
      let emotion = historydata[j].emotion;
      // console.log(emotion);
      // console.log(aspect);
      let temp_res = {};
      if (!(aspect in result)) {
        // console.log("here");
        temp_res = { count: 1, positive: 0, neutral: 0, negative: 0 };
        temp_res = update_aspect_result_label(temp_res, emotion);
      } else {
        let aspect_result = result[aspect];
        aspect_result["count"] = aspect_result["count"] + 1;
        temp_res = update_aspect_result_label(aspect_result, emotion);
      }
      result[aspect] = temp_res;
    }
  }
  return result;
};
// console.log(output_from_api);
// let result = convert_data(output_from_api);
// console.log(used_output["school"]);
// console.log(result["school"]);
// console.log(result);
// console.log(used_output);

export async function getAllData() {
  let response = await fetch("http://127.0.0.1:8000/api/sentiment/");
  // console.log(response);
  let data = response.json();
  // console.log(data);
  return data;
}

export async function sendSentence(obj) {
  fetch("http://127.0.0.1:8000/api/sentiment/", {
    method: "POST",
    body: obj, // The data
    headers: {
      "Content-type": "application/json", // The type of data you're sending
    },
  });
}
