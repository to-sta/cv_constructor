<script lang="ts">
	import CvTemplate from "../../components/cv/cvTemplate.svelte";
	import Button from "../../components/buttons/button.svelte";
	import Icon from "../../components/icons/icon.svelte";
</script>

<svelte:head>
	<title>Create CV</title>
	<meta name="description" content="Create CV" />
</svelte:head>

<main class="w-full h-screen bg-slate-200">
	<div class="flex items-center justify-center w-full h-full">
		<a class="absolute z-10 top-5 right-10" href="/dashboard">
			<Button text={"Back to Dashboard"}>
				<div class="fill-current text-primary-300">
					<Icon icon="Left" height="1.5em" width="1.5em" />
				</div>
			</Button>
		</a>
		<div class="bg-white shadow-xl shadow-black/40 w-[210mm] h-[297mm]">
			<CvTemplate />
		</div>
	</div>
</main>
