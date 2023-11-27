import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vite";
import dotenv from 'dotenv';

dotenv.config({ path: '../.env' });

export default defineConfig({
	plugins: [sveltekit()],

});
