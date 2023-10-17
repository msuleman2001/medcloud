import React, { useState } from "react";
import { Checkbox, List, Select, Typography } from "antd";
import Chips from "../chips/Chips";
const { Title } = Typography;
export default function NewLabTestForm() {
  const [selectedTest, setSelectedTest] = useState("");
  const [relatedTestToSelectTest, setRelatedTestToSelectedTest] = useState([]);
  const relatedTest = [
    {
      name: "Complete blood count",
      id: 1,
    },
    {
      name: "Urinalysis",
      id: 2,
    },
    {
      name: "Lipid panel",
      id: 3,
    },
  ];
  const handleSelect = (value) => {
    console.log(value);
  };
  const handleChipSelect = (id) => {
    console.log(id);
  };

  return (
    <div>
      <div className="mt-8">
        <Title level={4}>Pathology</Title>
        <div className="my-4">
          <Select
            size="large"
            style={{
              width: "100%",
            }}
            placeholder="select symptoms"
            onSelect={handleSelect}
            options={[
              {
                value: "jack",
                label: "Jack",
                id: 1,
              },
              {
                value: "lucy",
                label: "Lucy",
                id: 2,
              },
              {
                value: "tom",
                label: "Tom",
                id: 3,
              },
            ]}
          />
        </div>
        <div className="flex my-5 gap-4">
          {relatedTest.map((item) => (
            <Chips id={item.id} onSelect={handleChipSelect} label={item.name} />
          ))}
        </div>
      </div>
    </div>
  );
}
