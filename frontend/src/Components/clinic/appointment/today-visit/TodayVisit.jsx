import React, { useState } from "react";
import { Form, Input, Select, Space, Typography } from "antd";
import styles from "./TodayVisit.module.css";
import { IoIosArrowDown, IoIosArrowUp } from "react-icons/io";
import RoundedButton from "../../general/rounded-button/RoundedButton";
import MedicineList from "../medicine-list/MedicineList";
const { Title } = Typography;
export default function TodayVisitForm() {
  const [showForm, setShowForm] = useState(true);
  const handleChange = (value) => {
    console.log(`selected ${value}`);
  };

  const [rows, setRows] = useState([]);
  const handleAddRow = (data) => {
    console.log(data);
    setRows([...rows, data]);
  };
  const handleRemoveRow = (index) => {
    const newRows = [...rows];
    newRows.splice(index, 1);
    setRows(newRows);
  };

  return (
    <div
      className={`mt-10 patient-form bg-white shadow-lg border border-gray-100 rounded-md overflow-hidden duration-150 ${
        !showForm ? "max-h-[50px] " : "max-h-[auto] "
      }`}
    >
      <div className="flex cursor-pointer justify-between px-5 py-3 rounded-lg ">
        <Title className={styles["title"]} level={4}>
          Patient visit details
        </Title>

        <span
          onClick={() => setShowForm((pState) => !pState)}
          className="flex cursor-pointer gap-1 items-center"
        >
          <span className="text-sm">Expand </span>
          {showForm ? <IoIosArrowUp /> : <IoIosArrowDown />}
        </span>
      </div>

      <div className={`p-6 rounded-lg duration-150 `}>
        <Form layout="vertical">
          <div className="flex gap-6">
            <Form.Item style={{ width: "100%" }} name={"name"} label="Symptom">
              <Select
                size="large"
                mode="multiple"
                style={{
                  width: "100%",
                }}
                placeholder="select symptoms"
                defaultValue={[]}
                onChange={handleChange}
                options={[
                  {
                    value: "jack",
                    label: "Jack",
                  },
                  {
                    value: "lucy",
                    label: "Lucy",
                  },
                  {
                    value: "tom",
                    label: "Tom",
                  },
                ]}
              />
            </Form.Item>
          </div>

          <Form.Item
            style={{ width: "100%" }}
            name={"primaryDiagnose"}
            label="Primary Diagnose"
          >
            <Input size="large" style={{ width: "100%" }} />
          </Form.Item>
          <div>
            <MedicineList
              rows={rows}
              handleRemoveRow={handleRemoveRow}
              onMedicineAdd={handleAddRow}
            />
          </div>
          <div className="flex w-full justify-end">
            <div className="w-fit">
              <RoundedButton uppercase={true}>Add patient visit</RoundedButton>
            </div>
          </div>
        </Form>
      </div>
    </div>
  );
}
