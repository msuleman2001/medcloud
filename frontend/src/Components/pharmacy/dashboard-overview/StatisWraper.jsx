import React from "react";

export default function StatisWraper({ children }) {
  return (
    <div className="custom-shadow statis-wraper bg-white rounded-lg px-8 flex-1 py-4">
      {children}
    </div>
  );
}
