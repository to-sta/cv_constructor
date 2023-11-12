<script lang="ts">
	import type { NavItemType } from "./navItems";
	import Navbrand from "./navbar/navbrand.svelte";

	export let navitems: NavItemType[] = [];
</script>

<header>
	<nav class="bg-transparent">
		<div class="flex flex-wrap items-center justify-between max-w-screen-xl p-4 mx-auto">
			<!-- Navbar Brand -->
			<Navbrand />
			<!-- Burger Menu -->
			<button
				data-collapse-toggle="navbar-default"
				type="button"
				class="inline-flex items-center justify-center w-10 h-10 p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
				aria-controls="navbar-default"
				aria-expanded="false"
			>
				<span class="sr-only">Open main menu</span>
				<svg
					class="w-5 h-5"
					aria-hidden="true"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 17 14"
				>
					<path
						stroke="currentColor"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M1 1h15M1 7h15M1 13h15"
					/>
				</svg>
			</button>
			<!-- Navbar Links -->
			<div class="hidden w-full md:block md:w-auto" id="navbar-default">
				<ul class="flex flex-col p-4 mt-4 font-medium md:p-0 md:flex-row md:space-x-8 md:mt-0">
					{#each navitems as navitem}
						<li>
							<a
								href="/{navitem.path}"
								class="block py-2 pl-3 pr-4 md:bg-transparent md:p-0"
								aria-current="page">{navitem.text}</a
							>
						</li>
					{/each}
				</ul>
			</div>
		</div>
	</nav>
	<!-- <nav>
		<ul>
			<li aria-current={$page.url.pathname === "/" ? "page" : undefined}>
				<a href="/">Home</a>
			</li>
			<li aria-current={$page.url.pathname === "/about" ? "page" : undefined}>
				<a href="/about">About</a>
			</li>
			<li aria-current={$page.url.pathname.startsWith("/sverdle") ? "page" : undefined}>
				<a href="/sverdle">Sverdle</a>
			</li>
		</ul>
	</nav> -->
</header>
