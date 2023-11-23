<script lang="ts">
	import MenuButton from "../../../buttons/menuButton.svelte";
	import Icon from "../../../icons/icon.svelte";
</script>

<div>
	<div>
		<div class="flex flex-col h-screen gap-4 p-4 pt-8 bg-primary-100">
			<MenuButton
				text="PersonalInformation"
				>
				<Icon icon="Person" height="2em" width="2em"/>
			</MenuButton>
			<MenuButton
				text="WorkExperience"
			>
			<Icon icon="Work" height="2em" width="2em"/>
			</MenuButton>
			<MenuButton
				text="AcademicExperience"
			>
			<Icon icon="Education" height="2em" width="2em"/>
			</MenuButton>
			<MenuButton
				text="Skill"
			>
			<Icon icon="Skill" height="2em" width="2em"/>
			</MenuButton>
			<MenuButton
				text="Intrest"
			>
			<Icon icon="Interest" height="2em" width="2em"/>
			</MenuButton>
			<MenuButton
				text="Reference"
			>
			<Icon icon="Reference" height="2em" width="2em"/>
			</MenuButton>
			<MenuButton
				text="Language"
			>
			<Icon icon="Language" height="2em" width="2em"/>
			</MenuButton>
		</div>
	</div>
</div>
