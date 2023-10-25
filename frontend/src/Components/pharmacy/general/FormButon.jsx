import { Button } from "antd";

function FormButton({ children, loading, disable, htmlType }) {
  return (
    <div className="form-button mt-10 w-fit">
      <Button
        htmlType={htmlType}
        disabled={disable}
        className=" px-8 uppercase"
        loading={loading}
      >
        {children}
      </Button>
    </div>
  );
}

export default FormButton;
