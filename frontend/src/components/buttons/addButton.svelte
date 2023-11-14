<script lang="ts">
	export let disabled: boolean = false;
</script>

<button
	class="p-1 font-bold bg-black rounded-full opacity-7 text-primary-300"
	{disabled}
	type="submit"
	><svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24" {...$$props}
		><path fill="currentColor" d="M11 13H5v-2h6V5h2v6h6v2h-6v6h-2v-6Z" /></svg
	></button
>
