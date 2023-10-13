import { Input } from "antd";
import React from "react";
import styles from "./RoundedInput.module.css";
export default function RoundedInput({
  value,
  onChange = () => {},
  size,
  disabled,
  styles,
  placeholder,
}) {
  return (
    <Input
      size={size}
      placeholder={placeholder}
      className="rounded-input"
      style={{ ...styles }}
      value={value ? value : null}
      onChange={onChange}
      disabled={disabled}
    ></Input>
  );
}
