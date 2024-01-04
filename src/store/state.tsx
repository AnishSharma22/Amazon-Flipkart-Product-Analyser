import { atom } from "recoil";

export const textState = atom({
  key: "textState",
  default: ''
});

export const inputBoxState = atom({
  key: "inputBoxState",
  default: "",
});

export const amazonState = atom({
  key: "amazonState",
  default: true,
});
export const flipkartState = atom({
  key: "flipkartState",
  default: false,
});

export const loadingState = atom({
  key: "loadingState",
  default: false,
});

export const notFoundState = atom({
  key: "notFoundState",
  default: false,
});
