import { Button } from "antd";
import React from "react";
import styles from "./RoundedButton.module.css";
export default function RoundedButton({
  children,
  htmlType,
  onClick,
  loading,
}) {
  return (
    <Button
      htmlType={htmlType}
      onClick={onClick}
      loading={loading}
      className={styles["rounded-button"]}
      style={{ width: "100%" }}
      shape="round"
      size="large"
    >
      {children}
    </Button>
  );
}
