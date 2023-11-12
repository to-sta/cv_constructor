<script lang="ts">
	import Header from "../../components/layout/Header.svelte";
	import Footer from "../../components/layout/footer.svelte";
</script>

<div class="flex flex-col justify-between min-h-screen">
	<Header />
	<main>
		<slot />
	</main>
	<Footer />
</div>
