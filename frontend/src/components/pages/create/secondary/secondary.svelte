<script lang="ts">
	import PersonalInformation from "./options/personalInformation.svelte";
	import WorkExperience from "./options/workexperience.svelte";
	import Language from "./options/language.svelte";
	import Reference from "./options/reference.svelte";
	import AcademicExperience from "./options/academicExperience.svelte";
	import Skill from "./options/skill.svelte";
	import Interest from "./options/interest.svelte";
	import { sidebarOption } from "../../../../stores/sidebarOption";
	import MenuExpandButton from "../../../buttons/menuExpandButton.svelte";

	const components: Record<
		string,
		| typeof PersonalInformation
		| typeof WorkExperience
		| typeof Language
		| typeof Reference
		| typeof AcademicExperience
		| typeof Skill
		| typeof Interest
	> = {
		PersonalInformation,
		WorkExperience,
		Language,
		Reference,
		AcademicExperience,
		Skill,
		Interest
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
