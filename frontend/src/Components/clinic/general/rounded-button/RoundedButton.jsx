import { Button } from "antd";
import React from "react";
import styles from "./RoundedButton.module.css";
export default function RoundedButton({
  children,
  htmlType,
  onClick,
  disabled,
  loading,
  uppercase,
}) {
  return (
    <Button
      disabled={disabled || loading}
      htmlType={htmlType}
      onClick={onClick ? onClick : null}
      loading={loading}
      className={`${styles["rounded-button"]} ${uppercase && "uppercase"}`}
      style={{ width: "100%" }}
      shape="round"
      size="large"
    >
      {children}
    </Button>
  );
}
