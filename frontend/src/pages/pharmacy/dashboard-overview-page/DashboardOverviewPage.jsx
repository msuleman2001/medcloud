import TotalRevenue from "../../../Components/pharmacy/dashboard-overview/TotalRevenue";
import StatisWraper from "../../../Components/pharmacy/dashboard-overview/StatisWraper";
import ExpieryMedList from "../../../Components/pharmacy/dashboard-overview/ExpieryMedList";
import RecentOrdersList from "../../../Components/pharmacy/dashboard-overview/RecentOrdersList";
import MonthlyProgressChart from "../../../Components/pharmacy/dashboard-overview/MonthlyProgressChart";
import TotalMedicineSold from "../../../Components/pharmacy/dashboard-overview/TotalMedicineSold";
import TotalCustomers from "../../../Components/pharmacy/dashboard-overview/TotalCustomers";
// import CustomSelect from "../../../Components/clinic/dashboard-overview/CustomSelect";
import { Button } from "antd";
export default function DashboardOverviewPage() {
  return (
    <div className="w-full pharmacy-dashboard-overview p-8 bg-gray-50">
      <div className="flex-1 grid grid-cols-3 gap-4">
        <StatisWraper>
          <TotalRevenue />
        </StatisWraper>
        <StatisWraper>
          <TotalMedicineSold />
        </StatisWraper>
        <StatisWraper>
          <TotalCustomers />
        </StatisWraper>
      </div>
      <div className="grid grid-cols-2 mt-8 gap-5 ">
        <ExpieryMedList />
        <RecentOrdersList />
      </div>
      <div className="flex custom-shadow bg-white rounded-lg overflow-hidden mt-8">
        <MonthlyProgressChart />
      </div>
    </div>
  );
}
