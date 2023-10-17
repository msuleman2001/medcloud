import { Table, Typography } from "antd";
import React from "react";
import { useGetDoctorsQuery } from "../../../../store/clinic/clinic-api";
const { Title } = Typography;

export default function DoctorsTable() {
  const { data, error } = useGetDoctorsQuery();
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
  console.log(error);

  return (
    <div className="shadow-lg bg-white rounded-lg overflow-hidden border border-red-600">
      <Title level={2}>Doctors</Title>
      <Table pagination={false} dataSource={dataSource} columns={columns} />
    </div>
  );
}
