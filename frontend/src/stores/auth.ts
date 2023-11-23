import { writable } from "svelte/store";

const auth = writable<boolean>(false);

export default auth;
