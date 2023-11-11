<script lang="ts">
	export let text: string = "";
	export let disabled: boolean = false;
</script>

<button
    class="px-4 py-2 font-bold bg-black rounded-full text-primary-300"
    disabled={disabled}
    type="submit"
	>{text}</button
>
