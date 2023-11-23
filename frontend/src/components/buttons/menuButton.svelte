<script lang="ts">
	import { sidebarOption } from "../../stores/sidebarOption";

    export let text: string = "";

    const updateSidebarOption = (clicked: string) => {
		sidebarOption.update(() => clicked);
		console.log(clicked);
	};
</script>

<button
	class="p-2 rounded-xl bg-primary-300 hover:bg-primary-400"
	on:click={() => {
		updateSidebarOption(text);
	}}
>
	<slot />
</button>
