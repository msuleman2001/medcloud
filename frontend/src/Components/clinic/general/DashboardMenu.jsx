import React, { useState } from "react";
import {
  AppstoreOutlined,
  DesktopOutlined,
  PieChartOutlined,
} from "@ant-design/icons";

import { Menu } from "antd";
function getItem(label, key, icon, children, type) {
  return {
    key,
    icon,
    children,
    label,
    type,
  };
}
const items = [
  getItem("Overview", "1", <PieChartOutlined />),
  getItem("Employee", "2", <DesktopOutlined />),
  getItem("Purchase", "3", <AppstoreOutlined />),
];
const DashboardMenu = () => {
  const [collapsed, setCollapsed] = useState(false);
  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };
  return (
    <sidebar className={"w-[256px] bg-[#18132A]  pt-5 "}>
      <Menu
        defaultSelectedKeys={["1"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
        // theme="dark"
        style={{ background: "#18132A", color: "white", height: "100%" }}
        inlineCollapsed={collapsed}
        items={items}
      />
    </sidebar>
  );
};
export default DashboardMenu;
