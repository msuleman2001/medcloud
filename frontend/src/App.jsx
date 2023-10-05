import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import LoginPage from "./pages/general-pages/login-page/LoginPage";
import DashboardLayout from "./Components/pharmacy/general/DashboardLayout";
import DashboardPharmacyOverviewPage from "./pages/pharmacy/dashboard-overview-page/DashboardOverviewPage";
import DashboardPharmacyMenu from "./Components/pharmacy/general/DashboardMenu";
import DashboardOverviewPage from "./pages/clinic/dashboard-verview-page/dashboard-overview-page";
import DashboardClinicMenu from "./Components/clinic/general/DashboardMenu";
import ClinicDashboardHeader from "./Components/clinic/general/dashboard-header/DashboardHeader";
function App() {
  return (
    <>
      <BrowserRouter>
        {/* clinic routes */}
        <Routes>
          <Route>
            <Route index element={<Navigate replace to={"login"} />} />
            <Route path="login" element={<LoginPage />} />
            <Route
              path="dashboard"
              element={
                <DashboardLayout
                  header={<ClinicDashboardHeader />}
                  sidebar={<DashboardClinicMenu />}
                />
              }
            >
              <Route index element={<Navigate replace to={"overview"} />} />
              <Route path="overview" element={<DashboardOverviewPage />} />
            </Route>
          </Route>
          {/* pharmacy routes */}

          <Route path="pharmacy">
            <Route index element={<Navigate replace to={"login"} />} />
            <Route path="login" element={<LoginPage />} />
            <Route
              path="dashboard"
              element={<DashboardLayout sidebar={<DashboardPharmacyMenu />} />}
            >
              <Route index element={<Navigate replace to={"overview"} />} />
              <Route
                path="overview"
                element={<DashboardPharmacyOverviewPage />}
              />
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
