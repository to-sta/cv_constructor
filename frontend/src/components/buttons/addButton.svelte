<script lang="ts">
	import Icon from "../icons/icon.svelte";
	export let disabled: boolean = false;
</script>

<button
	class="p-1 font-bold bg-black rounded-full opacity-7 text-primary-300"
	{disabled}
	type="submit"
>
<Icon icon="Add" height="2em" width="2em"/>
</button>
