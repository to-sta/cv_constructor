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

	let menuOpen: boolean = true;
</script>

<div class="flex">
	<div class="relative flex flex-col h-screen gap-4 p-4 pt-8 bg-primary-200">
		<div class="overflow-y-auto overflow-x-hidden pr-4 scroll-m-10 {menuOpen ? '' : 'hidden'}">
			{#if $sidebarOption === "PersonalInformation"}
				<PersonalInformation />
			{/if}
			{#if $sidebarOption === "WorkExperience"}
				<Workexperience />
			{/if}
			{#if $sidebarOption === "Language"}
				<Language />
			{/if}
			{#if $sidebarOption === "Reference"}
				<Reference />
			{/if}
			{#if $sidebarOption === "AcademicExperience"}
				<AcademicExperience />
			{/if}
			{#if $sidebarOption === "Skill"}
				<Skill />
			{/if}
			{#if $sidebarOption === "Intrest"}
				<Intrest />
			{/if}
		</div>
		<button
			class="absolute flex items-center justify-center w-8 h-8 bg-black rounded-full -right-4 hover:scale-110"
			on:click={() => (menuOpen = !menuOpen)}
		>
			<MenuExpandButton isOpen={menuOpen} />
		</button>
	</div>
</div>
