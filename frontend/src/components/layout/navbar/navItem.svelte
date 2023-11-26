<script lang="ts">
	export let text: string;
	export let path: string;
</script>

<li>
	<a
		href="/{path}"
		class="block py-2 pl-3 pr-4 rounded-md md:rounded-none md:bg-transparent md:p-0 hover:bg-primary-100 md:hover:bg-transparent md:hover:text-primary-400"
		aria-current="page">{text}</a
	>
</li>
