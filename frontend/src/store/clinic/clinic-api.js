import { baseApi } from "../baseApi";

const clinicApi = baseApi.injectEndpoints({
  endpoints: (build) => ({
    getDoctors: build.query({
      query: () => "doctor/doctors",
    }),
  }),
  overrideExisting: false,
});

const { useGetDoctorsQuery } = clinicApi;
export { clinicApi, useGetDoctorsQuery };
