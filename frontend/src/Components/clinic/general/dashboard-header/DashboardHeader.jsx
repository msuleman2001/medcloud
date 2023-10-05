import { Avatar, Typography } from "antd";
import React from "react";
const { Paragraph, Title } = Typography;
import styles from "./DashboardHeader.module.css";
export default function DashboardHeader() {
  return (
    <header
      className={`flex h-[60px] ${styles["dashboard-header"]} border-b-[1px] custom-shadow border-b-gray-200 items-center  w-full px-6 justify-between`}
    >
      <div>
        <Title level={3}>9000</Title>
      </div>
      <div
        className={`flex items-center gap-4 ${styles["dashboard-header-child"]}`}
      >
        <Avatar style={{ verticalAlign: "middle" }} size="large" />
        <Paragraph>Ali Hamza</Paragraph>
      </div>
    </header>
  );
}
