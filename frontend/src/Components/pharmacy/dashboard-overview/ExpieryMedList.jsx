import React from "react";
import { Table, Typography } from "antd";
import { Link } from "react-router-dom";
import { AiOutlineRight } from "react-icons/ai";
const { Title, Paragraph } = Typography;
export default function ExpieryMedList() {
  const dataSource = [
    {
      key: "1",
      medicineName: "Fluciux",
      expireDate: "2022-12-13",
      quantity: 1,
    },
    {
      key: "2",
      medicineName: "Fluciux",
      expireDate: "2022-12-13",
      quantity: 1,
    },
  ];

  const columns = [
    {
      title: "Medicine Name",
      dataIndex: "medicineName",
      key: "medicineName",
    },
    {
      title: "Expire Date",
      dataIndex: "expireDate",
      key: "expireDate",
    },
    {
      title: "Quantity",
      dataIndex: "quantity",
      key: "quantity",
    },
  ];

  return (
    <div className="custom-shadow rounded-lg general-reset-table bg-white px-5  py-4">
      <div className="flex justify-between px-4 mb-5">
        <div>
          <Title level={3}>Expiring List</Title>
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
