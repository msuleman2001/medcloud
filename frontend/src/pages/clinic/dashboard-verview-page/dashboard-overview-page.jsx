import { Button, Select } from "antd";
import React from "react";
import RoundedSelect from "../../../Components/clinic/general/RoundedSelect/RoundedSelect";
import RoundedButton from "../../../Components/clinic/general/RoundedButton/RoundedButton";
import PatientsList from "../../../Components/clinic/dashboard-overview/patients-list/PatientsList";
import PatientDetailsForm from "../../../Components/clinic/dashboard-overview/patient-details-form/PatientDetailsForm";

export default function DashboardOverviewPage() {
  return (
    <div className="w-full bg-gray-50 py-10">
      <div className="w-[1050px]  min-h-[100vh] mx-auto">
        <div className="flex gap-6">
          <RoundedSelect placeholder={"Select a doctor"} />
          <RoundedSelect placeholder={"Select a patient"} />
          <div className="w-fit">
            <RoundedButton>Add new patient</RoundedButton>
          </div>
        </div>
        <PatientsList />
        <PatientDetailsForm />
      </div>
    </div>
  );
}
