import React, { useState } from "react";
import { DatePicker, Form, Input, Select, Typography } from "antd";
import styles from "./PatientDetailsForm.module.css";
import { IoIosArrowDown, IoIosArrowUp } from "react-icons/io";
import RoundedButton from "../../general/rounded-button/RoundedButton";
const { Title } = Typography;
export default function PatientDetailsForm() {
  const [showForm, setShowForm] = useState(false);
  return (
    <div
      className={`mt-10 patient-form bg-white shadow-lg border border-gray-100 rounded-md overflow-hidden duration-150 ${
        !showForm ? "max-h-[50px] " : "max-h-[700px] "
      }`}
    >
      <div className="flex cursor-pointer justify-between px-5 py-3 rounded-lg ">
        <Title className={styles["title"]} level={4}>
          Personal details
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
            <Form.Item style={{ width: "100%" }} name={"name"} label="Name">
              <Input size="large" />
            </Form.Item>
            <Form.Item style={{ width: "100%" }} name={"age"} label="Age">
              <Input size="large" />
            </Form.Item>
          </div>

          <div className="flex gap-6">
            <Form.Item style={{ width: "100%" }} name={"gender"} label="Gender">
              <Select
                size="large"
                style={{ width: "100%" }}
                options={[
                  {
                    value: "male",
                    label: "male",
                  },
                  {
                    value: "female",
                    label: "Female",
                  },
                  {
                    value: "other",
                    label: "Other",
                  },
                ]}
              />
            </Form.Item>
            <Form.Item style={{ width: "100%" }} name={"date"} label="Date">
              <DatePicker size="large" style={{ width: "100%" }} />
            </Form.Item>
          </div>
          <Form.Item style={{ width: "100%" }} name={"address"} label="Address">
            <Input size="large" />
          </Form.Item>
          <Form.Item style={{ width: "100%" }} name={"remarks"} label="Remarks">
            <Input.TextArea rows={5} size="large" />
          </Form.Item>
          <div className="flex w-full justify-end">
            <div className="w-fit">
              <RoundedButton>Add now</RoundedButton>
            </div>
          </div>
        </Form>
      </div>
    </div>
  );
}
