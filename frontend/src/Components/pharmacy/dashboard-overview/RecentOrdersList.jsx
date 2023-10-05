import React from "react";
import { Table, Typography } from "antd";
import { AiOutlineRight } from "react-icons/ai";
import { Link } from "react-router-dom";

const { Title, Paragraph } = Typography;
export default function RecentOrdersList() {
  const dataSource = [
    {
      key: "1",
      orderNumber: 202094094,
      name: "Mark zkb",
      amount: 4000,
      phoneNumber: "03139120432",
    },
    {
      key: "2",
      orderNumber: 202094094,
      name: "Mark zkb",
      amount: 4000,
      phoneNumber: "03139120432",
    },
  ];

  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Order Number",
      dataIndex: "orderNumber",
      key: "orderNumber",
    },
    {
      title: "Phone Number",
      dataIndex: "phoneNumber",
      key: "phoneNumber",
    },
    {
      title: "Amount",
      dataIndex: "amount",
      key: "amount",
    },
  ];
  return (
    <div className="custom-shadow general-reset-table rounded-lg bg-white px-5  py-4  ">
      <div className="flex justify-between px-4 mb-3">
        <div>
          <Title level={4}>Recent Order's </Title>
        </div>

        <Link className="text-blue-500 font-semibold flex gap-2 text-sm items-center ">
          <p>See All</p>
          <div className="w-[24px] flex justify-center items-center rounded-lg h-[24px] bg-gray-100">
            <AiOutlineRight size={14} />
          </div>
        </Link>
      </div>
      <div>
        <Table
          footer={false}
          pagination={false}
          dataSource={dataSource}
          columns={columns}
        />
      </div>
    </div>
  );
}
