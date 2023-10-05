import { Select } from "antd";
import React, { useState } from "react";
import styels from "./RoundedSelect.module.css";
export default function RoundedSelect({ placeholder }) {
  const onChange = (value) => {
    console.log(`selected ${value}`);
  };

  const onSearch = (value) => {
    console.log("search:", value);
  };
  const filterOption = (input, option) =>
    (option?.label ?? "").toLowerCase().includes(input.toLowerCase());

  return (
    <Select
      className={`overflow-hidden rounded-select duration-150 `}
      showSearch
      optionFilterProp="children"
      onChange={onChange}
      onSearch={onSearch}
      filterOption={filterOption}
      placeholder={placeholder}
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
      size="large"
      style={{ width: "100%" }}
    />
  );
}
