import { Typography } from "antd";
// import Form from 'antd';
const { Paragraph, Title } = Typography;

import LoginForm from "../../../Components/pharmacy/login/LoginForm";
function LoginPage() {
  return (
    <div className="bg-[#18132A] text-white ">
      <div className="flex flex-1 flex-column  min-h-[100vh] w-[90%] max-w-[1300px] mx-auto">
        <div className={`flex items-center justify-between flex-1 gap-5`}>
          <div className="flex flex-col justify-between flex-1">
            <div className="text-center mb-5">
              {/* <img src={logo} alt='logo' /> */}
              LOGO
            </div>
            <div className={`text-center `}>
              <Title className={`login-title`} level={2}>
                Welcome to the MedCloud Family
              </Title>
              <Paragraph className={"login-paragh"}>
                Simplify your finance, Boost your credit score
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
