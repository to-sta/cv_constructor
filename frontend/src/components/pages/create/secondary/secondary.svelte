<script lang="ts">
	import PersonalInformation from "./options/personalInformation.svelte";
	import Workexperience from "./options/workexperience.svelte";
	import Language from "./options/language.svelte";
	import Reference from "./options/reference.svelte";
	import AcademicExperience from "./options/academicExperience.svelte";
	import Skill from "./options/skill.svelte";
	import Intrest from "./options/intrest.svelte";

	export let choice: string = "PersonalInformation";
	let menuClosed: boolean = false;
</script>

<div class="flex">
	<div class="relative flex flex-col h-screen gap-4 p-4 pt-8 bg-primary-200">
		<div class={menuClosed ? "" : "hidden"}>
			{#if choice === "PersonalInformation"}
				<PersonalInformation />
			{/if}
			{#if choice === "WorkExperience"}
				<Workexperience />
			{/if}
			{#if choice === "Language"}
				<Language />
			{/if}
			{#if choice === "Reference"}
				<Reference />
			{/if}
			{#if choice === "AcademicExperience"}
				<AcademicExperience />
			{/if}
			{#if choice === "Skill"}
				<Skill />
			{/if}
			{#if choice === "Intrest"}
				<Intrest />
			{/if}
		</div>
		<button
			class="absolute flex items-center justify-center w-8 h-8 bg-black rounded-full -right-4"
			on:click={() => (menuClosed = !menuClosed)}
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				width="1.5em"
				height="1.5em"
				viewBox="0 0 24 24"
				class="text-primary-300"
				><path
					fill="currentColor"
					d="m7.825 13l4.9 4.9q.3.3.288.7t-.313.7q-.3.275-.7.288t-.7-.288l-6.6-6.6q-.15-.15-.213-.325T4.425 12q0-.2.063-.375T4.7 11.3l6.6-6.6q.275-.275.688-.275t.712.275q.3.3.3.713t-.3.712L7.825 11H19q.425 0 .713.288T20 12q0 .425-.288.713T19 13H7.825Z"
				/></svg
			>
		</button>
	</div>
</div>
