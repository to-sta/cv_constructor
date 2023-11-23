<script lang="ts">
	import type { NavItemType } from "../../lib/types/navItems";
	import Navbrand from "./navbar/navbrand.svelte";
	import Cookies from "js-cookie";
	import { variables } from "$lib/dotenv/dotenv";
	import user from "../../stores/user";

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

<header>
	<nav class="bg-transparent shadow-md">
		<div class="flex flex-wrap items-center justify-between max-w-screen-xl p-4 mx-auto">
			<!-- Navbar Brand -->
			<Navbrand />
			<!-- Burger Menu -->
			<button
				data-collapse-toggle="navbar-default"
				type="button"
				class="inline-flex items-center justify-center w-10 h-10 p-2 text-sm text-black rounded-lg md:hidden focus:outline-none focus:ring-2 focus:ring-primary-400 hover:bg-primary-300"
				aria-controls="navbar-default"
				aria-expanded="false"
				on:click={() => (isOpen = !isOpen)}
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
			<div class="{isOpen ? '' : 'hidden'} w-full md:block md:w-auto" id="navbar-default">
				<ul class="flex flex-col p-4 mt-4 font-medium md:p-0 md:flex-row md:space-x-8 md:mt-0">
					{#each navitems as navitem}
						<li>
							<a
								href="/{navitem.path}"
								class="block py-2 pl-3 pr-4 rounded-md md:rounded-none md:bg-transparent md:p-0 hover:bg-primary-100 md:hover:bg-transparent md:hover:text-primary-400"
								aria-current="page">{navitem.text}</a
							>
						</li>
					{/each}
					<li>
						<a
							class="block py-2 pl-3 pr-4 rounded-md md:rounded-none md:bg-transparent md:p-0 hover:bg-primary-100 md:hover:bg-transparent md:hover:text-primary-400"
							href="/auth"
							on:click={handleLogout}>Logout</a
						>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</header>
