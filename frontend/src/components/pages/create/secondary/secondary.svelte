<script lang="ts">
	import PersonalInformation from "./options/personalInformation.svelte";
	import Workexperience from "./options/workexperience.svelte";
	import Language from "./options/language.svelte";
	import Reference from "./options/reference.svelte";
	import AcademicExperience from "./options/academicExperience.svelte";
	import Skill from "./options/skill.svelte";
	import Intrest from "./options/intrest.svelte";
	import { sidebarOption } from "../../../../stores/sidebarOption";
	import MenuExpandButton from "../../../buttons/menuExpandButton.svelte";

	const components: any = {
		PersonalInformation,
		Workexperience,
		Language,
		Reference,
		AcademicExperience,
		Skill,
		Intrest
	};

	let menuOpen: boolean = true;

	$: if ($sidebarOption) {
		menuOpen = true;
	}
</script>

<div class="flex">
	<div class="relative flex flex-col h-screen gap-4 p-4 pt-8 bg-primary-200">
		<div class="overflow-y-auto overflow-x-hidden pr-4 scroll-m-10 {menuOpen ? '' : 'hidden'}">
			<svelte:component this={components[$sidebarOption]} />
		</div>
		<button
			class="absolute flex items-center justify-center w-8 h-8 bg-black rounded-full hover:bg-secondary-100 -right-4"
			on:click={() => (menuOpen = !menuOpen)}
		>
			<MenuExpandButton isOpen={menuOpen} />
		</button>
	</div>
</div>
