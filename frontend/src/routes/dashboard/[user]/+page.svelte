<script lang="ts">
	import user from "../../../stores/user";
</script>

<section class="max-w-screen-xl px-4 pb-4 mx-auto">
	<div class="py-4">
		<h1 class="text-2xl font-bold border-b-2 border-primary-300 font-oswald text">Your CV's</h1>
	</div>
	<div class="flex justify-center">
		<div
			class="flex flex-col items-center justify-center rounded-md shadow-md bg-primary-100 shadow-black/30 w-80 h-96"
		>
			<a href="/dashboard/{$user}/create">
				<div>
					<svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"
						><path
							fill="currentColor"
							d="M11 13H6q-.425 0-.713-.288T5 12q0-.425.288-.713T6 11h5V6q0-.425.288-.713T12 5q.425 0 .713.288T13 6v5h5q.425 0 .713.288T19 12q0 .425-.288.713T18 13h-5v5q0 .425-.288.713T12 19q-.425 0-.713-.288T11 18v-5Z"
						/></svg
					>
				</div>
				<div>
					<h3 class="text-lg font-semibold font-oswald">Add your CV</h3>
				</div>
			</a>
		</div>
	</div>

	<div class="py-4">
		<h1 class="text-2xl font-bold border-b-2 border-primary-300 font-oswald text">Example CV's</h1>
	</div>

	<div class="flex justify-between">
		<div class="rounded-md shadow-md bg-primary-100 shadow-black/30 w-80 h-96" />
		<div class="rounded-md shadow-md bg-primary-100 shadow-black/30 w-80 h-96" />
		<div class="rounded-md shadow-md bg-primary-100 shadow-black/30 w-80 h-96" />
	</div>

	<div class="py-4">
		<h1 class="text-2xl font-bold border-b-2 border-primary-300 font-oswald text">Tips</h1>
	</div>

	<div class="flex justify-between">
		<div class="bg-black h-96 w-96" />
	</div>
</section>
