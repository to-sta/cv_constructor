<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Personal Information</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			<div class="flex gap-3">
				<fieldset class="flex flex-col gap-2">
					<label class="font-oswald" for="first_name">First name:</label>
					<input
						id="first_name"
						name="first_name"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="Max"
						type="text"
					/>
				</fieldset>
				<fieldset class="flex flex-col gap-2">
					<label class="font-oswald" for="last_name">Last name:</label>
					<input
						id="last_name"
						name="last_name"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="Mustermann"
						type="text"
					/>
				</fieldset>
				<fieldset class="flex flex-col gap-2">
					<label class="font-oswald" for="date_of_birth">Date of birth:</label>
					<input
						id="date_of_birth"
						name="date_of_birth"
						class="py-1 pl-2 pr-1 bg-white rounded-lg opacity-75"
						placeholder="Mustermann"
						type="date"
					/>
				</fieldset>
			</div>
			<div class="flex gap-3">
				<fieldset class="flex flex-col gap-2">
					<label class="font-oswald" for="email">Email:</label>
					<input
						id="email"
						name="email"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="example@provider.com"
						type="email"
					/>
				</fieldset>
				<fieldset class="flex flex-col gap-2">
					<label class="font-oswald" for="phone">Phone:</label>
					<input
						id="phone"
						name="phone"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="example@provider.com"
						type="tel"
					/>
				</fieldset>
			</div>
			<div>
				<fieldset class="flex flex-col gap-2">
					<label class="font-oswald" for="image">Profile Image:</label>
					<input
						id="image"
						name="image"
						class="w-3/4 py-2 pl-2 bg-white rounded-lg opacity-75"
						placeholder="example@provider.com"
						type="file"
					/>
				</fieldset>
			</div>
			<Button text="submit" />
		</div>
	</form>
</div>
