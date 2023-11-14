<script lang="ts">
	import { sidebarOption } from "../../../../stores/sidebarOption";

	const updateSidebarOption = (clicked: string) => {
		sidebarOption.update((value) => (value = clicked));
	};
</script>

<div>
	<div>
		<div class="flex flex-col h-screen gap-4 p-4 pt-8 bg-primary-100">
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("PersonalInformation");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
					><path
						fill="currentColor"
						d="M12 12q-1.65 0-2.825-1.175T8 8q0-1.65 1.175-2.825T12 4q1.65 0 2.825 1.175T16 8q0 1.65-1.175 2.825T12 12Zm-8 6v-.8q0-.85.438-1.563T5.6 14.55q1.55-.775 3.15-1.163T12 13q1.65 0 3.25.388t3.15 1.162q.725.375 1.163 1.088T20 17.2v.8q0 .825-.588 1.413T18 20H6q-.825 0-1.413-.588T4 18Z"
					/></svg
				>
			</button>
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("WorkExperience");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
					><path
						fill="currentColor"
						d="m13.783 15.172l2.121-2.121l5.996 5.996l-2.121 2.121zM17.5 10c1.93 0 3.5-1.57 3.5-3.5c0-.58-.16-1.12-.41-1.6l-2.7 2.7l-1.49-1.49l2.7-2.7c-.48-.25-1.02-.41-1.6-.41C15.57 3 14 4.57 14 6.5c0 .41.08.8.21 1.16l-1.85 1.85l-1.78-1.78l.71-.71l-1.41-1.41L12 3.49a3 3 0 0 0-4.24 0L4.22 7.03l1.41 1.41H2.81l-.71.71l3.54 3.54l.71-.71V9.15l1.41 1.41l.71-.71l1.78 1.78l-7.41 7.41l2.12 2.12L16.34 9.79c.36.13.75.21 1.16.21z"
					/></svg
				>
			</button>
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("AcademicExperience");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 20 20"
					><path
						fill="currentColor"
						fill-rule="evenodd"
						d="M9.664 1.319a.75.75 0 0 1 .672 0a41.059 41.059 0 0 1 8.198 5.424a.75.75 0 0 1-.254 1.285a31.372 31.372 0 0 0-7.86 3.83a.75.75 0 0 1-.84 0a31.508 31.508 0 0 0-2.08-1.287V9.394c0-.244.116-.463.302-.592a35.504 35.504 0 0 1 3.305-2.033a.75.75 0 0 0-.714-1.319a37 37 0 0 0-3.446 2.12A2.216 2.216 0 0 0 6 9.393v.38a31.293 31.293 0 0 0-4.28-1.746a.75.75 0 0 1-.254-1.285a41.059 41.059 0 0 1 8.198-5.424ZM6 11.459a29.848 29.848 0 0 0-2.455-1.158a41.029 41.029 0 0 0-.39 3.114a.75.75 0 0 0 .419.74c.528.256 1.046.53 1.554.82c-.21.324-.455.63-.739.914a.75.75 0 1 0 1.06 1.06c.37-.369.69-.77.96-1.193a26.61 26.61 0 0 1 3.095 2.348a.75.75 0 0 0 .992 0a26.547 26.547 0 0 1 5.93-3.95a.75.75 0 0 0 .42-.739a41.053 41.053 0 0 0-.39-3.114a29.925 29.925 0 0 0-5.199 2.801a2.25 2.25 0 0 1-2.514 0c-.41-.275-.826-.541-1.25-.797a6.985 6.985 0 0 1-1.084 3.45a26.503 26.503 0 0 0-1.281-.78A5.487 5.487 0 0 0 6 12v-.54Z"
						clip-rule="evenodd"
					/></svg
				>
			</button>
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("Skill");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 32 32"
					><path fill="currentColor" d="M30 30h-8V4h8zm-10 0h-8V12h8zm-10 0H2V18h8z" /></svg
				>
			</button>
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("Intrest");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
					><path
						fill="currentColor"
						d="m2 11l5-9l5 9H2Zm5 10q-1.65 0-2.825-1.175T3 17q0-1.65 1.175-2.825T7 13q1.65 0 2.825 1.175T11 17q0 1.65-1.175 2.825T7 21Zm6 0v-8h8v8h-8Zm4-10q-1.425-1.2-2.388-2.025t-1.537-1.45Q12.5 6.9 12.25 6.35T12 5.175q0-1.125.788-1.9T14.75 2.5q.675 0 1.263.313t.987.862q.4-.55.988-.862T19.25 2.5q1.175 0 1.963.775t.787 1.9q0 .625-.25 1.175t-.825 1.175q-.575.625-1.538 1.45T17 11Z"
					/></svg
				>
			</button>
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("Reference");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
					><path
						fill="currentColor"
						d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5S5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05c1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"
					/></svg
				>
			</button>
			<button
				class="p-2 rounded-xl bg-primary-300"
				on:click={() => {
					updateSidebarOption("Language");
				}}
			>
				<svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 24 24"
					><path
						fill="currentColor"
						d="M2.825 17.75q-.175-.25-.4-.438t-.475-.337Q2.925 16 3.4 14.712t.475-2.662v-1.9H11.5v3.675H4.925q-.2 1.15-.675 2.2T2.825 17.75Zm2.225-4.825h5.275V11.05H5.05v1.875Zm-2.6-1.95q-.125-.275-.3-.5t-.375-.425q1.525-.65 2.85-1.6t2.425-2.2h1.1q1.175 1.2 2.588 2.063T13.65 9.9q-.225.225-.413.475t-.312.525q-1.425-.725-2.788-1.563T7.65 7.376q-1.075 1.2-2.388 2.1t-2.812 1.5Zm2.425 6.775v-3.5h7v3.5h-1.1v-2.525h-4.8v2.525h-1.1Zm.45-8.075v-.9h4.725v.9H5.325ZM4.4 12.4v-.85h6.675v.85H4.4Zm.825 4.975v-.95h6.05v.95h-6.05ZM17.55 15.65q.7 0 1.363-.325t1.212-.925v-2.65q-.575.075-1.063.175t-.912.225q-1.125.35-1.688.875T15.9 14.25q0 .65.45 1.025t1.2.375Zm-.575 1.7q-1.425 0-2.25-.813t-.825-2.212q0-1.3.825-2.125t2.65-1.325q.575-.15 1.263-.275t1.487-.225q-.05-1.175-.55-1.713t-1.55-.537q-.65 0-1.287.238T15.1 9.2l-.8-1.4q.825-.625 1.938-1.012T18.5 6.4q1.775 0 2.7 1.1t.925 3.2v6.425H20.45L20.3 16q-.7.625-1.538.988t-1.787.362Z"
					/></svg
				>
			</button>
		</div>
	</div>
</div>
