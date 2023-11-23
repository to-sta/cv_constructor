<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";
	import user from "../../../../../stores/user";
	import { variables } from "$lib/dotenv/dotenv";
	import Cookies from "js-cookie";

	let skill: string[] = [];
	let rating: string[] = [];

	async function handleForm() {
		let objects: { skill: string; rating: string }[] = [];
		for (let i = 0; i < skill.length; i++) {
			objects.push({ skill: skill[i], rating: rating[i] });
		}

		let csrftoken = Cookies.get("csrftoken");
		const response = await fetch(`${variables.API_ROOT}/api/skill/`, {
			method: "POST",
			mode: "cors",
			credentials: "include",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": csrftoken
			},
			// User as pk must be sent back to the API, this might need to be changed in the backend
			// rating value is not bind
			body: JSON.stringify(objects)
		});
		let data = await response.json();

		if (response.status === 200) {
			user.update(() => ({ ...data }));
		}
	}

	let numbers: number = 1;
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Skills</h1>
</div>
<div>
	<form on:submit|preventDefault={handleForm}>
		<div class="space-y-4">
			{#each Array(numbers) as _, id}
				<div class="relative flex gap-3">
					<!-- Trashcan button -->
					{#if id > 0}
						<div class="absolute right-0">
							<div
								class="flex items-center justify-center w-8 h-8 bg-black rounded-full fill-primary-300"
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									width="0.75em"
									height="1em"
									viewBox="0 0 12 16"
									><path
										fill-rule="evenodd"
										d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"
										fill="current"
									/></svg
								>
							</div>
						</div>
					{/if}
					<fieldset class="flex flex-col gap-2">
						<label for="skill" class="font-oswald">Skill</label>
						<input
							id="skill"
							name="skill_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Javascript"
							type="text"
							bind:value={skill[id]}
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
							bind:value={rating[id]}
						/>
					</fieldset>
				</div>
			{/each}

			<div class="flex items-center justify-center">
				<button on:click|preventDefault={() => numbers++}>
					<AddButton />
				</button>
			</div>

			<Button text="submit" />
		</div>
	</form>
</div>
