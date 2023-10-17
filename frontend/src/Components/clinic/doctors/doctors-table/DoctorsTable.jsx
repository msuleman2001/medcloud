import { Table, Typography } from "antd";
import React, { useEffect } from "react";
import {
  useGetDoctorsQuery,
  useGetTestProductQuery,
} from "../../../../store/clinic/clinic-api";
const { Title } = Typography;

export default function DoctorsTable() {
  const { data, error, isLoading } = useGetTestProductQuery();
  const dataSource = [
    {
      key: "1",
      name: "Mike",
      phone: "03144832432",
      email: "abuzain432432@gmail.com",
    },
    {
      key: "2",
      name: "John",
      phone: "03144832432",
      email: "abuzain432432@gmail.com",
    },
  ];
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Phone",
      dataIndex: "phone",
      key: "phone",
    },
    {
      title: "Email",
      dataIndex: "email",
      key: "email",
    },
  ];
  console.log(data);
  // console.log(error);

  return (
    <div className="shadow-lg p-4 bg-white rounded-lg overflow-hidden border">
      <Title level={3} className="px-4">
        Doctors in database
      </Title>
      <Table
        loading={isLoading}
        pagination={false}
        dataSource={dataSource}
        columns={columns}
      />
    </div>
  );
}
