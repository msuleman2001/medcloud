import React from "react";
import RoundedSelect from "../../../Components/clinic/general/rounded-select/RoundedSelect";
import RoundedButton from "../../../Components/clinic/general/rounded-button/RoundedButton";
import PatientsList from "../../../Components/clinic/appointment/patients-list/PatientsList";
import PatientDetailsForm from "../../../Components/clinic/appointment/patient-details-form/PatientDetailsForm";
import TodayVisit from "../../../Components/clinic/appointment/today-visit/TodayVisit";
import DashboardAppointmentHeader from "../../../Components/clinic/appointment/appointment-header/AppointmentsHeader";
export default function DashboardAppointmentPage() {
  return (
    <>
      <DashboardAppointmentHeader />
      <div className="w-full bg-gray-50 py-10">
        <div className="w-[1050px]  min-h-[100vh] mx-auto">
          <div className="flex gap-6">
            <RoundedSelect placeholder={"Select a doctor"} />
            <RoundedSelect placeholder={"Select a patient"} />
            <div className="w-fit">
              <RoundedButton uppercase={true}>Add new patient</RoundedButton>
            </div>
          </div>
          <PatientsList />
          <PatientDetailsForm />
          <TodayVisit />
        </div>
      </div>
    </>
  );
}
