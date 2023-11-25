<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";
	import user from "../../../../../stores/user";
	import { variables } from "$lib/dotenv/dotenv";
	import Cookies from "js-cookie";
	import Icon from "../../../../icons/icon.svelte";

	let skill: string[] = [];
	let rating: string[] = [];
	let numbers: number = 1;

	const skillFields = {
		name: "skill",
		type: "text",
		placeholder: "Javascript"
	};

	async function handleForm() {
		if (skill.length === 0) {
			return;
		}

		let objects: { skill: string; rating: string }[] = [];
		for (let i = 0; i < skill.length; i++) {
			objects.push({ skill: skill[i], rating: rating[i] });
		}

		let csrftoken: string | undefined = Cookies.get("csrftoken");
		if (csrftoken == undefined) {
			return (csrftoken = "");
		}

		const response = await fetch(`${variables.API_ROOT}/api/skill/`, {
			method: "POST",
			mode: "cors",
			credentials: "include",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": csrftoken
			},
			body: JSON.stringify(objects)
		});
		let data = await response.json();

		if (response.status === 200) {
			user.update(() => ({ ...data }));
		}
	}

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
								class="flex items-center justify-center w-8 h-8 bg-black rounded-full text-primary-300 fill-primary-300 hover:bg-secondary-100"
							>
							<button>
								<Icon icon="Delete" height="1em" width="1em" />
							</button>
							</div>
						</div>
					{/if}
					<fieldset class="flex flex-col gap-2">
						<label for="skill" class="font-oswald">Skill</label>
						<input
							id=skillFields.name
							name="skillFields.name"
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
