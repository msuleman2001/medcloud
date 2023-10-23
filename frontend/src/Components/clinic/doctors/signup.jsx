import {
  getRequrieRules,
  getValidateEmailRules,
} from "../../../lib/FormValidation";
import { Input, Form } from "antd";
import RoundedButton from "../general/rounded-button/RoundedButton";

export default function DoctorsSignUpForm() {
  return (
    <div className="w-[45%] flex flex-col rounded-lg  bg-white/95 px-10 py-10">
      <Form layout="vertical">
        <Form.Item
          required
          rules={[getValidateEmailRules(), getRequrieRules("email")]}
          label="Email Address"
          name={"emailAddress"}
        >
          <Input size={"large"} placeholder="Enter your email address" />
        </Form.Item>
        <Form.Item
          rules={[getRequrieRules("password")]}
          required
          label="Password"
          name={"password"}
        >
          <Input size={"large"} placeholder="Enter your password" />
        </Form.Item>
        <RoundedButton uppercase={true} htmlType={"submit"}>
          login
        </RoundedButton>
      </Form>
    </div>
  );
}
