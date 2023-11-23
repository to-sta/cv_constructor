<script lang="ts">
	import user from "../../stores/user";
	import Icon from "../../components/icons/icon.svelte";
</script>

<section class="max-w-screen-xl px-4 pb-4 mx-auto">
	<div class="py-4">
		<h1 class="text-2xl font-bold border-b-2 border-primary-300 font-oswald text">Your CV's</h1>
	</div>
	<div class="flex justify-center">
		<div
			class="flex flex-col items-center justify-center rounded-md shadow-md bg-primary-100 shadow-black/30 w-80 h-96"
		>
			<a class="flex flex-col items-center justify-center" href="/create">
				<div>
					<Icon icon="Plus" width="4em" height="4em"/>
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
