import { Table, Typography } from "antd";
import React, { useState } from "react";
import { GrAdd } from "react-icons/gr";

import { AiTwotoneEdit, AiTwotoneDelete } from "react-icons/ai";
import styles from "./MedicineList.module.css";
import RoundedSelect from "../../general/rounded-select/RoundedSelect";
import RoundedInput from "../../general/rounded-input/RoundedInput";
import NewMedicineForm from "../new-medicine-form/NewMedicineForm";
const { Title } = Typography;
export default function MedicineList({ onMedicineAdd, rows }) {
  const columns = [
    {
      title: "Medicine Name",
      dataIndex: "medicineName",
      key: "medicineName",
      render: (data) => {
        return (
          <RoundedSelect
            size="middle"
            options={[{ value: data, label: data }]}
            defaultValue={data}
            disabled={true}
          />
        );
      },
    },
    {
      title: "Medicine Potency",
      dataIndex: "medicinePotency",
      key: "medicinePotency",
      render: (data) => {
        console.log(data);
        return (
          <RoundedSelect
            size="middle"
            options={[{ value: data, label: data }]}
            defaultValue={data}
            disabled={true}
          />
        );
      },
    },
    {
      title: "Medicine Type",
      dataIndex: "medicineType",
      key: "medicineType",
      render: (medicineType) => {
        return (
          <RoundedSelect
            size="middle"
            options={[{ value: medicineType, label: medicineType }]}
            defaultValue={medicineType}
            disabled={true}
          />
        );
      },
    },
    {
      title: "Medicine Dose",
      dataIndex: "medicineDose",
      key: "medicineDose",
      render: (dose) => {
        return <RoundedInput size={"large"} value={dose} disabled={true} />;
      },
    },
    {
      title: "Actions",
      dataIndex: "medicineDose",
      key: Math.random(),
      render: () => {
        return (
          <div className="flex gap-4 items-center">
            <div className={`${styles["edit-icon"]} px-2 py-1 cursor-pointer`}>
              <AiTwotoneEdit />
            </div>
            <div
              className={`${styles["delete-icon"]} px-2 py-1 cursor-pointer`}
            >
              <AiTwotoneDelete />
            </div>
          </div>
        );
      },
    },
  ];
  return (
    <div className="my-4">
      <div className="flex justify-between">
        <Title className={styles["title"]} level={4}>
          Prescriptions
        </Title>
      </div>
      <NewMedicineForm onMedicineAdd={onMedicineAdd} />
      <Table
        rowKey={"id"}
        pagination={false}
        dataSource={rows}
        columns={columns}
      />
    </div>
  );
}
