import React from "react";

export default function IconButton({ children, className, onClick }) {
  return (
    <button
      onClick={onClick}
      className={`rounded-full flex justify-center items-center w-[40px] h-[40px] ${className}`}
    >
      {children}
    </button>
  );
}
