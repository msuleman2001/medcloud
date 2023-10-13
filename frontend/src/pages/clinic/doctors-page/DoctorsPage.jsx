import React from "react";
import DoctorsTable from "../../../Components/clinic/doctors/doctors-table/DoctorsTable";

export default function DashboardDoctorsPage() {
  return (
    <div className="w-full bg-gray-50 py-10">
      <div className="w-[1050px]  min-h-[100vh] mx-auto">
        <DoctorsTable />
      </div>
    </div>
  );
}
