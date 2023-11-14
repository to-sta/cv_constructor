<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";

	let numbers: number = 1;
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Work Experience</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			{#each Array(numbers) as _}
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label for="company" class="font-oswald">Company:</label>
						<input
							id="company"
							name="company"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Company Inc."
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="location" class="font-oswald">Location:</label>
						<input
							id="location"
							name="location"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Berlin, Germany"
							type="text"
						/>
					</fieldset>
				</div>
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label for="job_titel" class="font-oswald">Job Title:</label>
						<input
							id="job_titel"
							name="job_titel"
							class="py-1 pl-2 pr-1 bg-white rounded-lg opacity-75"
							placeholder="Software Engineer"
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="start_date" class="font-oswald">Start Date:</label>
						<input
							id="start_date"
							name="start_date"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							type="date"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label for="end_date" class="font-oswald">End Date:</label>
						<input
							id="end_date"
							name="end_date"
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
							name="summary"
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
