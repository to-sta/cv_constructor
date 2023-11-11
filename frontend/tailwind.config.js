/** @type {import('tailwindcss').Config} */
export default {
	content: ["./src/**/*.{html,js,svelte,ts}"],
	theme: {
		extend: {
			colors: {
				primary: {
					100: "#F7E480",
					200: "#F3D640",
					300: "#EEC800",
					400: "#B39600",
					500: "#776400"
				},
				secondary: {
					100: "#080808",
					200: "#040404",
					300: "#000000"
				},
				"main-transparent": {
					100: "rgba(0, 0, 0, 0.35)",
					200: "rgba(0, 0, 0, 0.55)"
				},
				error: {
					100: "#D14D58",
					200: "#CC2828",
					300: "#991E1E"
				}
			},
			fontFamily: {
				oswald: ["Oswald", "sans-serif"]
			}
		}
	},
	plugins: []
};
