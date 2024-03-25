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
};

