<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";
	import { variables } from "$lib/dotenv/dotenv";
	import Cookies from "js-cookie";
	import Icon from "../../../../icons/icon.svelte";
	import { writable } from "svelte/store";
	import { preFetchData } from "$lib/util/create/prefetch";
	import { onMount } from "svelte";
	import { deleteEntry } from "$lib/util/create/deleteEntry";
	import type { cvTypes } from "$lib/types/cvTypes";

	let skill = writable<cvTypes[]>([{ skill: "", rating: "" }]);

	function addElement() {
		$skill.push({ skill: "", rating: "" });
		skill.update(() => $skill);
	}

	onMount(async () => {
		const initialData = await preFetchData("/api/skill/");
		skill.update(() => Object.values(initialData));
	});

	async function handleForm() {
		if ($skill.length === 0) {
			return;
		}

		let newSkills = $skill.filter((skill) => !skill.id && skill.skill !== "");
		let existingSkills = $skill.filter((skill) => skill.id);

		let csrftoken: string | undefined = Cookies.get("csrftoken") || "";

		if (newSkills.length > 0) {
			const response = await fetch(`${variables.API_ROOT}/api/skill/`, {
				method: "POST",
				mode: "cors",
				credentials: "include",
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": csrftoken
				},
				body: JSON.stringify(newSkills)
			});

			if (!response.ok) {
				// Handle error...
			}
		}

		if (existingSkills.length > 0) {
			for (let i = 0; i < existingSkills.length; i++) {
				const response = await fetch(`${variables.API_ROOT}/api/skill/${$skill[i].id}/`, {
					method: "PUT",
					mode: "cors",
					credentials: "include",
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": csrftoken
					},
					body: JSON.stringify(existingSkills[i])
				});

				if (!response.ok) {
					// Handle error...
				}
			}
		}
	}

	async function handleDelete(id: number) {
		const updatedSkill = await deleteEntry($skill, id);
		skill.update(() => updatedSkill);
	}

	// async function deleteEntry(id: number) {
	// 	if (!$skill[id].id) {
	// 		$skill.splice(id, 1);
	// 		skill.update(() => $skill);
	// 		return;
	// 	}

	// 	const payload = $skill[id];

	// 	let csrftoken: string | undefined = Cookies.get("csrftoken") || "";

	// 	const response = await fetch(`${variables.API_ROOT}/api/skill/${$skill[id].id}/`, {
	// 		method: "DELETE",
	// 		mode: "cors",
	// 		credentials: "include",
	// 		headers: {
	// 			"Content-Type": "application/json",
	// 			"X-CSRFToken": csrftoken
	// 		},
	// 		body: JSON.stringify(payload)
	// 	});

	// 	if (response.ok) {
	// 		$skill.splice(id, 1);
	// 		console.log("request was successful");
	// 	}
	// }
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Skills</h1>
</div>
<div>
	<form on:submit|preventDefault={handleForm}>
		<div class="pt-4 space-y-4">
			{#each Array($skill.length) as _, id}
				<div class="relative flex gap-3">
					<!-- Trashcan button -->

					<div class="absolute right-0">
						<div
							class="flex items-center justify-center w-8 h-8 bg-black rounded-full text-primary-300 fill-primary-300 hover:bg-secondary-100"
						>
							<button on:click|preventDefault={() => handleDelete(id)}>
								<Icon icon="Delete" height="1em" width="1em" />
							</button>
						</div>
					</div>

					<fieldset class="flex flex-col gap-2">
						<label for="skill" class="font-oswald">Skill</label>
						<input
							id="skillFields.name"
							name="skillFields.name"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Javascript"
							type="text"
							bind:value={$skill[id].skill}
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="rating" class="font-oswald">Rating:</label>
						<input
							id="rating"
							min="1"
							max="5"
							name="rating_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							type="range"
							bind:value={$skill[id].rating}
						/>
					</fieldset>
				</div>
			{/each}
			<div class="flex items-center justify-center">
				<button on:click|preventDefault={addElement}>
					<AddButton />
				</button>
			</div>
			<Button text="submit" />
		</div>
	</form>
</div>
