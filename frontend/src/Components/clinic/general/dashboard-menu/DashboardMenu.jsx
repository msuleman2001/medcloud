import React, { useState } from "react";
import { FaUserAlt } from "react-icons/fa";
import { FaUserDoctor } from "react-icons/fa6";
import { IoTime } from "react-icons/io5";
import { Menu } from "antd";
import { Link } from "react-router-dom";

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
  // {
  {
    label: "Appointments",
    key: "/dashboard/appointments",
    icon: <IoTime size={22} />,
  },
  {
    label: "Doctors",
    key: "/dashboard/doctors",
    icon: <FaUserDoctor size={18} />,
  },
  {
    label: "Patients",
    key: "/dashboard/patients",
    icon: <FaUserAlt size={18} />,
  },
];

const DashboardMenu = () => {
  const [collapsed, setCollapsed] = useState(false);

  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };

  return (
    <sidebar className={"w-[300px] px-6 bg-[#18132A]  pt-5 "}>
      <Menu
        defaultSelectedKeys={["/dashboard/appointments"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
        // theme="dark"
        style={{
          background: "#18132A",
          color: "white",
          height: "100%",
          // width: 400,
        }}
        inlineCollapsed={collapsed}
      >
        {items.map((item) => (
          <Menu.Item key={item.key} icon={item.icon}>
            <Link to={item.key}>{item.label}</Link> {/* Use Link component */}
          </Menu.Item>
        ))}
      </Menu>
    </sidebar>
  );
};

export default DashboardMenu;
