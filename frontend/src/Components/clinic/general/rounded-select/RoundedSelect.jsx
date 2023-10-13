import { Select } from "antd";
import React, { useState } from "react";
import styels from "./RoundedSelect.module.css";
export default function RoundedSelect({
  placeholder = "",
  size = "large",
  defaultValue,
  disabled,
  onSelect,
  value,
  allowClear,
  onClear,
  options = [
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
  ],
}) {
  // const onChange = (value) => {
  //   console.log(`selected ${value}`);
  // };

  const onSearch = (value) => {
    console.log("search:", value);
  };
  const filterOption = (input, option) =>
    (option?.label ?? "").toLowerCase().includes(input.toLowerCase());

  return (
    <Select
      allowClear={allowClear}
      onSelect={onSelect}
      className={`overflow-hidden rounded-select duration-150 `}
      showSearch
      value={value ? value : undefined}
      onClear={onClear}
      defaultValue={defaultValue}
      optionFilterProp="children"
      // onChange={onChange}
      onSearch={onSearch}
      filterOption={filterOption}
      placeholder={placeholder}
      options={options}
      size={size}
      disabled={disabled}
      style={{ width: "100%" }}
    />
  );
}
