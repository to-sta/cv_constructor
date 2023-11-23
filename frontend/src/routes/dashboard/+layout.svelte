<script lang="ts">
	import Header from "../../components/layout/Header.svelte";
	import Footer from "../../components/layout/footer.svelte";
	import type { NavItemType } from "../../lib/types/navItems";

	let homeItems: NavItemType[] = [
		{ text: "Home", path: "/home" },
		{ text: "About", path: "/about" },
		{ text: "Contact", path: "/contact" }
	];
</script>

<Header navitems={homeItems} />
<main>
	<slot />
</main>
<Footer />
