import { Chart as ChartJS } from "chart.js/auto";
import { Chart } from "react-chartjs-2";

import { Pie, Bar } from "react-chartjs-2";
import { Doughnut } from "react-chartjs-2";
import React from "react";
import { background, color } from "@chakra-ui/react";

const data = {
  labels: ["red", "Blue", "Green"],
  datasets: [
    {
      data: [23, 4, 45],
    },
  ],
};

function CHRT() {
  return (
    <div className="App">
      <h1>Gantt chart</h1>
      <div style={{ maxWidth: "650px" }}>
        <Bar
          data={{
            // Name of the variables on x-axies for each bar
            labels: ["-"],
            datasets: [
              {
                data: [12, 33, 56],
                backgroundColor: ["violet"],
              },
            ],
            options: {
              scales: {
                yAxes: [
                  {
                    stacked: true,
                  },
                ],
              },
            },
          }}
          // Height of graph
          height = {2000}
          width = {900}
          options={{
            responsive:true,
            indexAxis: "y",
            // scales: {
            //   yAxes: [
            //     {
            //       ticks: {
            //         beginAtZero: true,
            //       },
            //     },
            //   ],
            // },
          }}
        />
      </div>
    </div>
  );
}

export default CHRT;
