import React from "react";
import { DatePicker, Form, Input, Select, Typography } from "antd";
import styles from "./PatientDetailsForm.module.css";
import RoundedButton from "../../general/RoundedButton/RoundedButton";
const { Title } = Typography;
export default function PatientDetailsForm() {
  return (
    <div className="mt-10 patient-form">
      <Title level={3}>Patients details form</Title>
      <div className="p-6 bg-white rounded-lg">
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
