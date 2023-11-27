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
			{#each Array(numbers) as id}
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label class="font-oswald" for="company">Company:</label>
						<input
							id="company"
							name="company_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Company Inc."
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label class="font-oswald" for="location">Location:</label>
						<input
							id="location"
							name="location_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Berlin, Germany"
							type="text"
						/>
					</fieldset>
				</div>
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label class="font-oswald" for="job_titel">Job Title:</label>
						<input
							id="job_titel"
							name="job_titel_{id}"
							class="py-1 pl-2 pr-1 bg-white rounded-lg opacity-75"
							placeholder="Software Engineer"
							type="text"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label class="font-oswald" for="start_date">Start Date:</label>
						<input
							id="start_date"
							name="start_date_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							type="date"
						/>
					</fieldset>
					<fieldset class="flex flex-col gap-2">
						<label class="font-oswald" for="end_date">End Date:</label>
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
						<label class="font-oswald" for="summary">Summary:</label>
						<textarea
							id="summary"
							name="summary_{id}"
							class="p-2 bg-white rounded-lg opacity-75"
							placeholder="Type your summary here..."
						/>
					</fieldset>
				</div>
			{/each}

			<div class="flex items-center justify-center">
				<button class="hover:scale-110" on:click={() => numbers++}>
					<AddButton />
				</button>
			</div>
			<Button text="submit" />
		</div>
	</form>
</div>
