<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Intrests</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			<div class="flex gap-3">
				<fieldset class="flex flex-col gap-2">
					<label for="first_name" class="font-oswald">Language</label>
					<input
						id="first_name"
						name="first_name"
						class="py-1 pl-2 bg-white rounded-lg opacity-75"
						placeholder="Football"
						type="text"
					/>
				</fieldset>
			</div>
			<Button text="add" />
		</div>
	</form>
</div>
