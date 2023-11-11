import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";

export default defineConfig({
	plugins: [sveltekit()],
	// envDir causes a restart in the docker setup and needs to be fixed
	envDir: "../",
	server: {
		host: "0.0.0.0"
	}
});
