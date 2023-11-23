<script lang="ts">
	import CvTemplate from "../../components/cv/cvTemplate.svelte";
</script>

<main class="w-full h-screen bg-slate-200">
	<div class="flex items-center justify-center w-full h-full">
		<div class="fixed items-center justify-center p-2 rounded-xl right-10 top-8 bg-primary-300 hover:bg-primary-400">
			<a class="flex gap-2" href="/dashboard">
				<svg class="text-black" xmlns="http://www.w3.org/2000/svg" width="1.5em" height="1.5em" viewBox="0 0 24 24"><path fill="current" d="m7.825 13l4.9 4.9q.3.3.288.7t-.313.7q-.3.275-.7.288t-.7-.288l-6.6-6.6q-.15-.15-.213-.325T4.425 12q0-.2.063-.375T4.7 11.3l6.6-6.6q.275-.275.688-.275t.712.275q.3.3.3.713t-.3.712L7.825 11H19q.425 0 .713.288T20 12q0 .425-.288.713T19 13H7.825Z"/></svg>
				<span class="font-oswald">Back to Dashboard</span>
			</a>
		</div>
		<div class="bg-white shadow-xl shadow-black/40 w-[210mm] h-[297mm]">
			<CvTemplate />
		</div>
	</div>
</main>
