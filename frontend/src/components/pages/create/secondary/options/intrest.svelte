<script lang="ts">
	import Button from "../../../../buttons/button.svelte";
	import AddButton from "../../../../buttons/addButton.svelte";

	let numbers: number = 1;
</script>

<div>
	<h1 class="text-3xl font-bold border-b-2 border-black font-oswald">Intrests</h1>
</div>
<div>
	<form>
		<div class="space-y-4">
			{#each Array(numbers) as id}
				<div class="flex gap-3">
					<fieldset class="flex flex-col gap-2">
						<label for="intrest" class="font-oswald">Intrest</label>
						<input
							id="intrest"
							name="intrest_{id}"
							class="py-1 pl-2 bg-white rounded-lg opacity-75"
							placeholder="Football"
							type="text"
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
