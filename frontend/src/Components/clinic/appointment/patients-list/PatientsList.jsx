import React, { useRef } from "react";
import PatientCard from "../patient-card/PatientCard";
import { MdArrowBackIosNew, MdOutlineArrowForwardIos } from "react-icons/md";
import { Carousel, Typography } from "antd";
import IconButton from "../../general/icon-button/IconButton";
import styles from "./PatientsList.module.css";
const { Title } = Typography;
export default function PatientsList() {
  const carouselRef = useRef();
  const leftIconClcik = () => {
    carouselRef.current.prev();
  };
  const rightIconClcik = () => {
    carouselRef.current.next();
  };
  return (
    <div className="mt-10">
      <Title level={3}>Patients regestered on number</Title>
      <div className="relative">
        <Carousel
          ref={carouselRef}
          dots={false}
          className="overflow-x-hidden w-[90%] mx-auto  rounded-lg"
        >
          <div className=" overflow-x-hidden rounded-lg">
            <div className="grid-cols-3 grid gap-6 mt-4 ">
              <PatientCard />
              <PatientCard />
              <PatientCard />
            </div>
          </div>
          <div>
            <div className="grid-cols-3 grid gap-6 mt-4">
              <PatientCard />
              <PatientCard />
              <PatientCard />
            </div>
          </div>
        </Carousel>
        <IconButton
          onClick={leftIconClcik}
          className={`absolute top-[55%] translate-y-[-50%] left-0 ${styles["icon-btn"]} `}
        >
          <MdArrowBackIosNew size={18} color="white" />
        </IconButton>
        <IconButton
          onClick={rightIconClcik}
          className={`absolute top-[55%] translate-y-[-50%] right-0 ${styles["icon-btn"]} `}
        >
          <MdOutlineArrowForwardIos color="white" size={18} />
        </IconButton>
      </div>
    </div>
  );
}
