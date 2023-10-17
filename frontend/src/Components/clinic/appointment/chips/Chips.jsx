import React, { useState } from "react";
import { AiOutlineCheck } from "react-icons/ai";
const Chips = ({ label, id, onSelect }) => {
  const [select, setSelect] = useState(false);
  const handleClick = () => {
    if (!select) onSelect(id);
    setSelect((preState) => !preState);
  };
  return (
    <div
      onClick={handleClick}
      className={`py-2 px-6 flex gap-2 items-center duration-150 rounded-full cursor-pointer ${
        select ? "bg-pink-700 shadow-lg text-white" : "bg-gray-100 "
      }`}
    >
      {select && <AiOutlineCheck size={16} />}
      <span className="text-sm font-semibold">{label}</span>
    </div>
  );
};

export default Chips;
