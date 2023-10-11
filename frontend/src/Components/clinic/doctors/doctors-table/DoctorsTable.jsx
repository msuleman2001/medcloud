import { Table, Typography } from "antd";
import React from "react";
const { Title } = Typography;

// email = models.EmailField()
// name = models.CharField(max_length=255)
// phone = models.CharField(max_length=20)
// license_no = models.CharField(max_length=54)
// speciality = models.CharField(max_length=100)
// start_year = models.PositiveIntegerField()
// clinic_address = models.TextField()
// country = models.CharField(max_length=50)
// added_by_id = models.PositiveIntegerField()
// added_datetime = models.DateTimeField(auto_now_add=True)
// last_update_date_time = models.DateTimeField(auto_now=True)
// is_enabled= models.BooleanField(default=False)
// remarks = models.TextField()

export default function DoctorsTable() {
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
  return (
    <div className="shadow-lg bg-white rounded-lg overflow-hidden border border-red-600">
      <Title level={2}>Doctors</Title>
      <Table pagination={false} dataSource={dataSource} columns={columns} />
    </div>
  );
}
