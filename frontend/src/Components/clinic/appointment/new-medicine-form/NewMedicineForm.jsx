import { Button, Form, Input } from "antd";
import React, { useEffect, useReducer, useState } from "react";
import RoundedSelect from "../../general/rounded-select/RoundedSelect";
import RoundedButton from "../../general/rounded-button/RoundedButton";
import RoundedInput from "../../general/rounded-input/RoundedInput";
const initialState = {
  medicineName: "",
  medicinePotency: "",
  medicineType: "",
  medicineDose: "",
  medicineNameError: false,
  medicinePotencyError: false,
  medicineTypeError: false,
  medicineDoseError: false,
};
function formReducer(state, action) {
  switch (action.type) {
    case "SET_FIELD":
      return {
        ...state,
        [action.fieldName]: action.fieldValue,
        [`${action.fieldName}Error`]: false,
      };
    case "SET_DEFAULT_VALUES":
      const { medicineName, medicinePotency, medicineType, medicineDose } =
        action.defaultValues;
      console.log(action.defaultValues);
      return {
        ...initialState,
        medicineDose,
        medicineName,
        medicinePotency,
        medicineType,
      };
    case "RESET":
      return { ...initialState };
    case "CLICK":
      return {
        ...state,
        medicineNameError: !!!state.medicineName,
        medicinePotencyError: !!!state.medicinePotency,
        medicineTypeError: !!!state.medicineType,
        medicineDoseError: !!!state.medicineDose,
      };
    default:
      return state;
  }
}

export default function NewMedicineForm({ onMedicineAdd, defaultValues }) {
  const [
    {
      medicineName,
      medicineNameError,
      medicinePotency,
      medicinePotencyError,
      medicineTypeError,
      medicineType,
      medicineDose,
      medicineDoseError,
    },
    dispatch,
  ] = useReducer(formReducer, initialState);

  useEffect(() => {
    if (defaultValues)
      dispatch({ type: "SET_DEFAULT_VALUES", defaultValues: defaultValues });
  }, [defaultValues]);

  const handleMedicineNameSelect = (value) => {
    dispatch({
      type: "SET_FIELD",
      fieldName: "medicineName",
      fieldValue: value,
    });
  };
  const handleMedicinePotancySelect = (value) => {
    dispatch({
      type: "SET_FIELD",
      fieldName: "medicinePotency",
      fieldValue: value,
    });
  };
  const handleMedicineTypeSelect = (value) => {
    dispatch({
      type: "SET_FIELD",
      fieldName: "medicineType",
      fieldValue: value,
    });
  };
  const handleNewMedicineClick = () => {
    dispatch({
      type: "CLICK",
    });
    if (
      !!!medicineName ||
      !!!medicineType ||
      !!!medicinePotency ||
      !!!medicineDose
    ) {
      return;
    } else {
      onMedicineAdd({
        id: Math.random(),
        medicineName,
        medicinePotency,
        medicineType,
        medicineDose,
      });
      dispatch({ type: "RESET" });
    }
  };
  const handleMedicineDoseChange = (value) => {
    dispatch({
      type: "SET_FIELD",
      fieldName: "medicineDose",
      fieldValue: value.target.value,
    });
  };
  return (
    <div className="my-4" layout="vertical">
      <div className="flex items-start  w-full gap-4">
        <div className="w-full">
          <RoundedSelect
            allowClear={true}
            value={medicineName}
            onSelect={handleMedicineNameSelect}
            onClear={handleMedicineNameSelect.bind(null, "")}
            placeholder="Medicine name"
          />
          {medicineNameError && (
            <p className="text-red-500 pl-2">This field is required</p>
          )}
        </div>
        <div className="w-full">
          <RoundedSelect
            allowClear={true}
            value={medicinePotency}
            onSelect={handleMedicinePotancySelect}
            onClear={handleMedicinePotancySelect.bind(null, "")}
            placeholder="Medicine potancy"
          />
          {medicinePotencyError && (
            <p className="text-red-500 pl-2">This field is required</p>
          )}
        </div>
        <div className="w-full">
          <RoundedSelect
            allowClear={true}
            value={medicineType}
            onSelect={handleMedicineTypeSelect}
            onClear={handleMedicineTypeSelect.bind(null, "")}
            placeholder="Medicine type"
          />
          {medicineTypeError && (
            <p className="text-red-500 pl-2">This field is required</p>
          )}
        </div>
        <div className="w-full">
          <RoundedInput
            value={medicineDose}
            onChange={handleMedicineDoseChange}
            styles={{ width: "100%" }}
            placeholder="Medicine dose"
            size={"large"}
          />
          {medicineDoseError && (
            <p className="text-red-500 pl-2 mt-2">This field is required</p>
          )}
        </div>
        <div className="w-fit">
          <RoundedButton
            disabled={
              medicineDoseError ||
              medicineNameError ||
              medicinePotencyError ||
              medicineTypeError
            }
            onClick={handleNewMedicineClick}
            htmlType={"button"}
          >
            Add
          </RoundedButton>
        </div>
      </div>
    </div>
  );
}
