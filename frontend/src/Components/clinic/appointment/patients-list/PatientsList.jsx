import React from "react";
import PatientCard from "../patient-card/PatientCard";
import { Typography } from "antd";
const { Title } = Typography;
export default function PatientsList() {
  return (
    <div className="mt-10">
      <Title level={3}>Patients regestered on number</Title>
      <div className="grid-cols-3 grid gap-6 mt-3">
        <PatientCard />
        <PatientCard />
        <PatientCard />
      </div>
    </div>
  );
}
