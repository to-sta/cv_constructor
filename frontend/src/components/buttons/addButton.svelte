<script lang="ts">
	import Icon from "../icons/icon.svelte";
	export let disabled: boolean = false;
</script>

<button
	class="p-1 font-bold bg-black rounded-full fill-current opacity-7 text-primary-300 hover:bg-secondary-100"
	{disabled}
	type="submit"
>
	<Icon height="2em" icon="Plus" width="2em" />
</button>
