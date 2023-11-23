import { writable } from "svelte/store";
import { browser } from "$app/environment";

const initialValue:string|null = browser ? localStorage.getItem("user") : null;

const user = writable(initialValue);

export default user;
