import React from "react";
import { Outlet } from "react-router-dom";
export default function DashboardLayout({ sidebar, header }) {
  return (
    <div className="min-h-[100vh] flex">
      {sidebar}
      <main className="w-full bg-gray-50">
        {header}
        <div className="w-[95%] mx-auto">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
