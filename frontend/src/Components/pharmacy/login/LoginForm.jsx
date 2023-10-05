import FormButton from "../General/FormButon";
import {
  getRequrieRules,
  getValidateEmailRules,
} from "../../../lib/FormValidation";
import { Input, Form } from "antd";

export default function LoginForm() {
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
        <FormButton htmlType={"submit"}>login</FormButton>
      </Form>
    </div>
  );
}
