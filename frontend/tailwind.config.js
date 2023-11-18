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
					100: "#424242",
					200: "#323232",
					300: "#212121",
					400: "#111111",
					500: "#000000"
				},
				info: {
					100: "#94BAE5",
					200: "#4A91DE",
					300: "#0068D6",
					400: "#005CBD",
					500: "#004FA3"
				},
				warning: {
					100: "#F0A150",
					200: "#F29138",
					300: "#F48020",
					400: "#E57315",
					500: "#D6660A"
				},
				success: {
					100: "#9ECBBE",
					200: "#7FBFAF",
					300: "#5FB2A0",
					400: "#3FA691",
					500: "#1F9981"
				},
				error: {
					100: "#D14D58",
					200: "#CF3B40",
					300: "#CC2828",
					400: "#B32323",
					500: "#991E1E"
				}
			},
			fontFamily: {
				oswald: ["Oswald", "sans-serif"]
			}
		}
	},
	plugins: []
};
