<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";

	let numbers: number = 1;
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Skills</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			{#each Array(numbers) as _}
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label for="first_name" class="font-oswald">Language</label>
						<input
							id="first_name"
							name="first_name"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Javascript"
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="last_name" class="font-oswald">Rating:</label>
						<input
							id="last_name"
							max="5"
							name="last_name"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Mustermann"
							type="range"
						/>
					</fieldset>
				</div>
			{/each}

			<div class="flex items-center justify-center">
				<button on:click={() => numbers++}>
					<AddButton />
				</button>
			</div>

			<Button text="submit" />
		</div>
	</form>
</div>
