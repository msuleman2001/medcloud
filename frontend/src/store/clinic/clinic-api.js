import { baseApi } from "../baseApi";

const clinicApi = baseApi.injectEndpoints({
  endpoints: (build) => ({
    getDoctors: build.query({
      // query: () => "",
      query: () => "doctor/doctors",
    }),
    getTestProduct: build.query({
      query: () => "test/product",
    }),
  }),
  overrideExisting: false,
});

const { useGetDoctorsQuery, useGetTestProductQuery } = clinicApi;
export { clinicApi, useGetDoctorsQuery, useGetTestProductQuery };
