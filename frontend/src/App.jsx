import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";

import LoginPage from "./pages/general-pages/login-page/LoginPage";
import ClinicLoginPage from "./pages/clinic/login-page/LoginPage";
import DashboardLayout from "./Components/pharmacy/general/DashboardLayout";
import DashboardPharmacyOverviewPage from "./pages/pharmacy/dashboard-overview-page/DashboardOverviewPage";
import DashboardPharmacyMenu from "./Components/pharmacy/general/DashboardMenu";
// clinic components
import DashboardDoctorsPage from "./pages/clinic/doctors-page/DoctorsPage";
import DashboardAppointmentPage from "./pages/clinic/appointment-page/AppointmentPage";
import DashboardClinicMenu from "./Components/clinic/general/dashboard-menu/DashboardMenu";
function App() {
  return (
    <>
      <BrowserRouter>
        {/* clinic routes */}
        <Routes>
          <Route>
            <Route index element={<Navigate replace to={"login"} />} />
            <Route path="login" element={<ClinicLoginPage />} />
            <Route
              path="dashboard"
              element={<DashboardLayout sidebar={<DashboardClinicMenu />} />}
            >
              <Route index element={<Navigate replace to={"appointments"} />} />
              <Route
                path="appointments"
                element={<DashboardAppointmentPage />}
              />
              <Route path="doctors" element={<DashboardDoctorsPage />} />
              <Route path="patients" element={<DashboardDoctorsPage />} />
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
