import { Typography } from "antd";
import { BsFillCartDashFill } from "react-icons/bs";
import { Link } from "react-router-dom";
const { Title } = Typography;
export default function TotalMedicineSold() {
  return (
    <div>
      <div className="flex gap-x-3">
        <div className="w-[40px] h-[40px] bg-[#02b8f2] flex justify-center items-center rounded-full">
          <BsFillCartDashFill color="white" />
        </div>
        <div>
          <div className="text-gray-700">
            <Title className="general-title" level={5}>
              Total Medicine Sold
            </Title>
          </div>
          <Title className="mt-0" level={4}>
            455
          </Title>
        </div>
      </div>
      <div className="mt-3">
        <Link className="text-[#02b8f2] text-sm">Show details</Link>
      </div>
    </div>
  );
}
