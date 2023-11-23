<script lang="ts">
	export let text: string = "";
	export let disabled: boolean = false;
</script>

<button
	class="flex items-center justify-center gap-2 px-4 py-2 bg-black rounded-full hover:bg-secondary-100 font-oswald text-primary-300"
	{disabled}
	type="submit"
>
	<slot />
	<span>{text}</span>
</button>
