<script lang="ts">
	import type { inputType } from "$lib/types/inputType";

	export let label:string;
	export let name:string;
	export let placeholder:string;
	export let type: inputType;
	export let errorMessage:string;
    export let min:string | undefined = undefined;
    export let max:string | undefined = undefined;

	let value:string = "";
    let error:boolean = false;

	function validateInput() {
		if (value === "") {
            error = true;
        } else {
            error = false;
        }
	}
</script>

<fieldset class="flex flex-col gap-2">
	<label for={name} class="font-oswald">{label}</label>
	<input
		id={name}
		{name}
		class="py-1 pl-2 bg-white rounded-lg opacity-75"
		{placeholder}
		{...{type}}
        {min}
        {max}
		bind:value={value}
		on:blur={validateInput}
	/>
	{#if error}
		<p class="text-error-200">{errorMessage}</p>
	{/if}
</fieldset>
