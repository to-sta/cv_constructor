<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";

	let numbers: number = 1;
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Reference</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			{#each Array(numbers) as id}
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label class="font-oswald" for="name">Name:</label>
						<input
							id="name"
							name="name_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Berlin, Germany"
							type="text"
						/>
					</fieldset>
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
				</div>
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
						<label class="font-oswald" for="phone">Phone:</label>
						<input
							id="phone"
							name="phone_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="example@provider.com"
							type="tel"
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
