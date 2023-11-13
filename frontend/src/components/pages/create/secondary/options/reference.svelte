<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Work Experience</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			<div class="flex gap-3">
				<fieldset class="flex flex-col gap-2">
					<label for="name" class="font-oswald">Name:</label>
					<input
						id="name"
						name="name"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="Berlin, Germany"
						type="text"
					/>
				</fieldset>
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
			</div>
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
					<label for="phone" class="font-oswald">Phone:</label>
					<input
						id="phone"
						name="phone"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="example@provider.com"
						type="tel"
					/>
				</fieldset>
			</div>
			<Button text="add" />
		</div>
	</form>
</div>
