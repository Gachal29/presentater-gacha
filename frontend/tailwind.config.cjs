module.exports = {
  variants: {
    extend: {
    },
  },
  content: [
    "./*.html",
    "../presentater_gacha/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
  daisyui: {
  }
}