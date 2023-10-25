import { Table, Typography, Pagination } from "antd";
import React, { useEffect } from "react";
import {
  useGetDoctorsQuery,
  useGetTestProductQuery,
} from "../../../../store/clinic/clinic-api";
const { Title } = Typography;

export default function DoctorsTable() {
  const { data, error, isLoading } = useGetTestProductQuery();
  const dataSource = [
    // {
    //   key: "1",
    //   name: "Mike",
    //   phone: "03144832432",
    //   email: "abuzain432432@gmail.com",
    // },
    // {
    //   key: "2",
    //   name: "John",
    //   phone: "03144832432",
    //   email: "abuzain432432@gmail.com",
    // },
  ];
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Description",
      dataIndex: "description",
      key: "description",
    },
    {
      title: "price",
      dataIndex: "price",
      key: "price",
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
        dataSource={data}
        columns={columns}
      />
      <div className="flex justify-center mt-4">
        <Pagination hideOnSinglePage={true} total={1080} />
      </div>
    </div>
  );
}
