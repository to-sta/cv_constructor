import Cookies from "js-cookie";
import { variables } from "$lib/dotenv/dotenv";
import type { cvTypes } from "$lib/types/cvTypes";

export async function deleteEntry(object: cvTypes[], id: number) {
	if (!object[id].id) {
		object.splice(id, 1);
		return object;
	}

	const payload = object[id];

	const csrftoken: string | undefined = Cookies.get("csrftoken") || "";

	const response = await fetch(`${variables.API_ROOT}/api/skill/${object[id].id}/`, {
		method: "DELETE",
		mode: "cors",
		credentials: "include",
		headers: {
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken
		},
		body: JSON.stringify(payload)
	});

	if (response.ok) {
		object.splice(id, 1);
	}
	return object;
}
