import React from "react";
import {
  BarChart,
  Bar,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import { Typography } from "antd";
import DashboardChartFilter from "./DashboardChartFilter";
const { Title } = Typography;

export default function MonthlyProgressChart() {
  const data = [
    {
      name: "Jan",
      amount: 10000000,
    },
    {
      name: "Feb",
      amount: 3000,
    },
    {
      name: "Mar",
      amount: 2000,
    },
    {
      name: "Apr",
      amount: 2780,
    },
    {
      name: "May",
      amount: 1890,
    },
    {
      name: "Jun",
      amount: 2390,
    },
    {
      name: "Jul",
      amount: 3490,
    },
    {
      name: "Aug",
      amount: 3490,
    },
    {
      name: "Sep",
      amount: 3490,
    },
    {
      name: "Oct",
      amount: 3490,
    },
    {
      name: "Nov",
      amount: 3490,
    },
    {
      name: "Dec",
      amount: 3490,
    },
  ];

  //   {
  //     name: "Page A",
  //     uv: 4000,
  //     pv: 2400,
  //     amt: 2400,
  //   },
  //   {
  //     name: "Page B",
  //     uv: 3000,
  //     pv: 1398,
  //     amt: 2210,
  //   },
  //   {
  //     name: "Page C",
  //     uv: 2000,
  //     pv: 9800,
  //     amt: 2290,
  //   },
  //   {
  //     name: "Page D",
  //     uv: 2780,
  //     pv: 3908,
  //     amt: 2000,
  //   },
  //   {
  //     name: "Page E",
  //     uv: 1890,
  //     pv: 4800,
  //     amt: 2181,
  //   },
  //   {
  //     name: "Page F",
  //     uv: 2390,
  //     pv: 3800,
  //     amt: 2500,
  //   },
  //   {
  //     name: "Page G",
  //     uv: 3490,
  //     pv: 4300,
  //     amt: 2100,
  //   },
  // ];
  return (
    <div className=" w-[100%]  px-5 py-4 monthly-progress-chart">
      <div className="mb-7 pt-5 px-5 flex justify-between">
        <Title className="general-title" level={3}>
          Monthly Progress
        </Title>
        <DashboardChartFilter />
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart
          width={500}
          height={300}
          data={data}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          {/* <CartesianGrid strokeDasharray="3 3" /> */}
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          {/* <Legend /> */}
          <Bar dataKey="amount" fill="#02b8f2" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
