import { Typography } from "antd";
// import Form from 'antd';
const { Paragraph, Title } = Typography;

import LoginForm from "../../../Components/clinic/login/login-form/LoginForm";
import styles from "./LoginPage.module.css";
function LoginPage() {
  return (
    <div className={styles["login-page"]}>
      <div className="flex flex-1 flex-column  min-h-[100vh] w-[90%] max-w-[1300px] mx-auto">
        <div className={`flex items-center justify-between flex-1 gap-5`}>
          <div className="flex flex-col justify-between flex-1">
            <div className="text-center mb-5">
              {/* <img src={logo} alt='logo' /> */}
              LOGO
            </div>
            <div className={`text-center`}>
              <Title level={2}>
                <span className={`${styles["login-title"]}`}>
                  Welcome to the MedCloud Family
                </span>
              </Title>
              <Paragraph className={"login-paragh"}>
                <span className={styles["login-paragraph"]}>
                  Simplify your finance, Boost your credit score
                </span>
              </Paragraph>
            </div>
          </div>
          <LoginForm />
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
