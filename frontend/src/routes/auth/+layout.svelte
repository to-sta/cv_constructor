<script lang="ts">
	import Footer from "../../components/layout/footer.svelte";
</script>

<div class="flex flex-col justify-between min-h-screen">
	<div></div>
	<main>
		<slot />
	</main>
	<Footer />
</div>
