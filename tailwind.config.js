/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
