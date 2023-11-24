<script lang="ts">
	import MenuButton from "../../../buttons/menuButton.svelte";
	import Icon from "../../../icons/icon.svelte";

	const menuButtons = [
		{
			text: "PersonalInformation",
			icon: "Person"
		},
		{
			text: "WorkExperience",
			icon: "Work"
		},
		{
			text: "AcademicExperience",
			icon: "Education"
		},
		{
			text: "Skill",
			icon: "Skill"
		},
		{
			text: "Interest",
			icon: "Interest"
		},
		{
			text: "Reference",
			icon: "Reference"
		},
		{
			text: "Language",
			icon: "Language"
		}
	];
</script>

<div class="flex flex-col h-screen gap-4 p-4 pt-8 bg-primary-100">
	{#each menuButtons as menuButton}
		<MenuButton text={menuButton.text}>
			<Icon icon={menuButton.icon} height="2em" width="2em" />
		</MenuButton>
	{/each}
</div>
