// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true;

import { browser } from "$app/environment";
import user from "../stores/user";
import { get } from "svelte/store";
import { goto } from "$app/navigation";

if (browser) {
	goto(get(user) == null ? "/auth" : "/dashboard")
}
