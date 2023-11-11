<script lang="ts">
	import auth from "../../stores/auth";

	export let leftText: string = "";
	export let rightText: string = "";

	let loginSignUp: boolean;
	auth.subscribe((value) => (loginSignUp = value));
</script>

<div class="flex items-center h-10 border border-black rounded-full bg-black/30">
	<button
		class="flex items-center justify-center w-1/2 h-full font-bold rounded-full transition-all duration-100 {!loginSignUp
			? 'border-2 border-black bg-primary-300'
			: ''}"
		on:click={() => {
			auth.update((val) => !val);
		}}>{leftText}</button
	>
	<button
		class="flex items-center justify-center w-1/2 h-full font-bold rounded-full transition-all duration-100 {loginSignUp
			? 'border-2 border-black bg-primary-300'
			: ''}"
		class:loginSignUp={"border-2 border-black bg-primary-300"}
		on:click={() => {
			auth.update((val) => !val);
		}}>{rightText}</button
	>
</div>
