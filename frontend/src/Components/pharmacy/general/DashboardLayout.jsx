import React from "react";
import { Outlet } from "react-router-dom";
export default function DashboardLayout({ sidebar, header }) {
  return (
    <div className="min-h-[100vh] flex">
      {sidebar}
      <main className="w-full">
        {header}
        <Outlet />
      </main>
    </div>
  );
}
