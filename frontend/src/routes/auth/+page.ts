import { browser } from "$app/environment";
import user from "../../stores/user";
import { get } from "svelte/store";
import { goto } from "$app/navigation";

if (browser) {
    if (get(user) !== null) {
        goto("/dashboard")
    }
}
