import Cookies from "js-cookie";
import { variables } from "$lib/dotenv/dotenv";


export async function preFetchData(endpoint: string) {
    const csrftoken: string | undefined = Cookies.get("csrftoken") || "";

    const response = await fetch(`${variables.API_ROOT}${endpoint}`, {
        method: "GET",
        mode: "cors",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        }
    });
    const data = response.json();
    return data;
}
