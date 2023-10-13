import React from "react";
import { Typography } from "antd";
const { Title } = Typography;
import styles from "./PatientCard.module.css";
export default function PatientCard() {
  return (
    <div
      className={`${styles["patient-card"]} duration-200 rounded-lg px-6 py-6`}
    >
      <Title level={4} className={`${styles["patient-card-title"]}`}>
        Patient details
      </Title>
      <div className="flex gap-2">
        <span className="font-bold text-sm text-white/90">Patient name: </span>
        <span className="text-sm text-white">Umari</span>
      </div>
      <div className="flex gap-2 ">
        <span className="font-bold text-sm text-white/90">Patient age: </span>
        <span className="text-sm text-white">Umari</span>
      </div>
    </div>
  );
}
