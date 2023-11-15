<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";

	let numbers: number = 1;
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Academic Experience:</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			{#each Array(numbers) as id}
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label for="institution" class="font-oswald">Institution:</label>
						<input
							id="institution"
							name="institution_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Univercity"
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="location" class="font-oswald">Location:</label>
						<input
							id="location"
							name="location_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Berlin"
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="location" class="font-oswald">State:</label>
						<input
							id="location"
							name="location{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Germany"
							type="text"
						/>
					</fieldset>
				</div>
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label for="degree" class="font-oswald">Degree:</label>
						<input
							id="degree"
							name="degree_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="B.Sc. Computer Science"
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="grade" class="font-oswald">Grade:</label>
						<input
							id="grade"
							name="grade_{id}"
							step=".1"
							class="py-1 pl-2 bg-white rounded-lg opacity-75 w-14"
							type="number"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="start_date" class="font-oswald">Start Date:</label>
						<input
							id="start_date"
							name="start_date_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							type="date"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="end_date" class="font-oswald">End Date:</label>
						<input
							id="end_date"
							name="end_date_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							type="date"
						/>
					</fieldset>
				</div>
				<div>
					<fieldset class="flex flex-col gap-2">
						<label for="summary" class="font-oswald">Summary:</label>
						<textarea
							id="summary"
							name="summary_{id}"
							placeholder="Type your summary here..."
							class="p-2 bg-white rounded-lg opacity-75"
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
