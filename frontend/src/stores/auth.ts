import { writable } from "svelte/store";

// Is used to switch from signup to login after signing up
// By default, we assume the user has already signed up

const auth = writable<boolean>(false);

export default auth;
