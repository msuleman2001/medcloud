import { configureStore } from "@reduxjs/toolkit";
import { baseApi } from "./baseApi";
import { clinicApi } from "./clinic/clinic-api"; // Import specific API slice for users
// Import additional API slices if needed

const store = configureStore({
  reducer: {
    [baseApi.reducerPath]: baseApi.reducer,
    [clinicApi.reducerPath]: clinicApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(baseApi.middleware),
});

export default store;
