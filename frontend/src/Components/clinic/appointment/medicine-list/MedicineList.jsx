import { Table, Typography } from "antd";
import React, { useState } from "react";
import { GrAdd } from "react-icons/gr";

import { AiTwotoneEdit, AiTwotoneDelete } from "react-icons/ai";
import styles from "./MedicineList.module.css";
import RoundedSelect from "../../general/rounded-select/RoundedSelect";
import RoundedInput from "../../general/rounded-input/RoundedInput";
import NewMedicineForm from "../new-medicine-form/NewMedicineForm";
const { Title } = Typography;
export default function MedicineList({
  onMedicineAdd,
  prescribedMedicine,
  onMedicineRemove,
  onMedicineEdit,
  toBeUpdatedMedicine,
}) {
  const columns = [
    {
      title: "Medicine Name",
      dataIndex: "medicineName",
      key: "medicineName",
      render: (data) => {
        return <div>{data}</div>;
      },
    },
    {
      title: "Medicine Potency",
      dataIndex: "medicinePotency",
      key: "medicinePotency",
      render: (data) => {
        console.log(data);
        return <div>{data}</div>;
      },
    },
    {
      title: "Medicine Type",
      dataIndex: "medicineType",
      key: "medicineType",
      render: (medicineType) => {
        return <div>{medicineType}</div>;
      },
    },
    {
      title: "Medicine Dose",
      dataIndex: "medicineDose",
      key: "medicineDose",
      render: (dose) => {
        return <div>{dose}</div>;
      },
    },
    {
      title: "Actions",
      dataIndex: "medicineDose",
      key: Math.random(),
      render: (_, rowData, index) => {
        return (
          <div className="flex gap-4 items-center">
            <div
              onClick={onMedicineEdit.bind(null, rowData)}
              className={`${styles["edit-icon"]} px-2 py-1 cursor-pointer`}
            >
              <AiTwotoneEdit />
            </div>
            <div
              onClick={onMedicineRemove.bind(null, index)}
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
      <NewMedicineForm
        defaultValues={toBeUpdatedMedicine}
        onMedicineAdd={onMedicineAdd}
      />
      <Table
        rowKey={"id"}
        pagination={false}
        dataSource={prescribedMedicine}
        columns={columns}
      />
    </div>
  );
}
