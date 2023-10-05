import { Button, Select } from "antd";
import React from "react";
import { useState } from "react";

const getCurrentYear = () => {
  return new Date().getFullYear();
};
export default function DashboardChartFilter() {
  const currentYear = getCurrentYear();
  const [selectedYear, setSelectedYear] = useState(currentYear);

  const handleYearChange = (value) => {
    setSelectedYear(value);
  };
  return (
    <div className="flex dashboard-overview-chart-filter gap-4">
      <Select
        className="round"
        defaultValue={selectedYear}
        style={{ width: "100%" }}
        onChange={handleYearChange}
      >
        {Array.from({ length: 10 }, (_, index) => (
          <Option key={currentYear - index} value={currentYear - index}>
            {currentYear - index}
          </Option>
        ))}
      </Select>
      <Button className="round pr-9 pl-5 text-white duration-150 hover:opacity-90  bg-[#02b8f2]">
        Clear
      </Button>
    </div>
  );
}
