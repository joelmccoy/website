/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./core/templates/core/*.html"],
  theme: {
    extend: {},
  },
  plugins: [
    require("@catppuccin/tailwindcss")({
      prefix: "ctp",
      defaultFlavour: "mocha",
    }),
  ],
  safelist: [
    "outline-ctp-rosewater",
    "outline-ctp-lavender",
    "outline-ctp-pink",
    "outline-ctp-sapphire",
    "outline-ctp-red",
    "outline-ctp-teal",
    "outline-ctp-peach",
    "outline-ctp-green",
  ],
};
