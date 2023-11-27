<script lang="ts">
	import Icon from "../icons/icon.svelte";
	export let text: string = "Download";
</script>

<button class="flex items-center justify-center h-10 rounded-lg shadow-lg">
	<div class="w-8 h-full rounded-l-lg shadow-lg bg-primary-300" />
	<div class="flex items-center justify-center h-full px-4 text-xl font-oswald bg-primary-100">
		<span>{text}</span>
	</div>

	<div class="flex items-center justify-center h-full px-4 bg-white rounded-r-lg fill-red-500">
		<Icon height="1.75em" icon="PDF" width="1.75em" />
	</div>
</button>
