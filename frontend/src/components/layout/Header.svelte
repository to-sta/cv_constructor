<script lang="ts">
	import type { NavItemType } from "../../lib/types/navItems";
	import Navbrand from "./navbar/navbrand.svelte";
	import Cookies from "js-cookie";
	import { variables } from "$lib/dotenv/dotenv";
	import user from "../../stores/user";
	import NavItem from "./navbar/navItem.svelte";

	export let navitems: NavItemType[] = [];
	let isOpen: boolean = false;

	async function handleLogout() {
		let csrftoken: string | undefined = Cookies.get("csrftoken");

		if (csrftoken == undefined) {
			return (csrftoken = "");
		}

		const response = await fetch(`${variables.API_ROOT}/api/user/logout/`, {
			method: "POST",
			mode: "cors",
			credentials: "include",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": csrftoken
			}
		});

		if (response.status == 200) {
			localStorage.removeItem("user");
			user.set(null);
		}
	}
</script>

<header class="pb-20">
	<nav class="absolute w-full bg-white shadow-md">
		<div class="flex flex-wrap items-center justify-between max-w-screen-xl p-4 mx-auto">
			<!-- Navbar Brand -->
			<Navbrand />
			<!-- Burger Menu -->
			<button
				class="inline-flex items-center justify-center w-10 h-10 p-2 text-sm text-black rounded-lg md:hidden focus:outline-none focus:ring-2 focus:ring-primary-400 hover:bg-primary-300"
				aria-controls="navbar-default"
				aria-expanded="false"
				data-collapse-toggle="navbar-default"
				type="button"
				on:click={() => (isOpen = !isOpen)}
			>
				<span class="sr-only">Open main menu</span>
				<svg
					class="w-5 h-5"
					aria-hidden="true"
					fill="none"
					viewBox="0 0 17 14"
					xmlns="http://www.w3.org/2000/svg"
				>
					<path
						d="M1 1h15M1 7h15M1 13h15"
						stroke="currentColor"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
					/>
				</svg>
			</button>
			<!-- Navbar Links -->
			<div id="navbar-default" class="{isOpen ? '' : 'hidden'} w-full md:block md:w-auto">
				<ul class="flex flex-col py-4 mt-4 font-medium md:p-0 md:flex-row md:space-x-8 md:mt-0">
					{#each navitems as navitem}
						<NavItem {...navitem} />
					{/each}
					<NavItem path="auth" text="Logout" on:click={handleLogout} />
				</ul>
			</div>
		</div>
	</nav>
</header>
