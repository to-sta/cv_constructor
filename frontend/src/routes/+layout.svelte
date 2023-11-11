<script>
	import Header from "../components/layout/Header.svelte";
	import "../app.css";
	import Footer from "../components/layout/footer.svelte";
</script>

<div class="app">
	<div class="flex flex-col justify-between min-h-screen">
		<Header />
		<main>
			<slot />
		</main>
		<Footer />
	</div>
</div>
