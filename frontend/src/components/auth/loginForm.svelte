<script lang="ts">
	import user from "../../stores/user";
	import { goto } from "$app/navigation";
	import { variables } from "$lib/dotenv/dotenv";
	import Button from "../buttons/button.svelte";
	import { formErrors } from "./formErrors";

	let email: string = "";
	let password: string = "";
	let validEmail: boolean = true;
	let validPassword: boolean = true;
	let formDisabled: boolean = false;

	function validateEmail() {
		let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
		if (email.match(validRegex)) {
			validEmail = true;
			return true;
		} else {
			validEmail = false;
			return false;
		}
	}

	function validatePassword() {
		// Checks if the password has more than 8 characters
		if (password.length > 8) {
			validPassword = true;
			return true;
		} else {
			validPassword = false;
			return false;
		}
	}

	function formValid() {
		if (validEmail && validPassword) {
			formDisabled = false;
			return true;
		} else {
			formDisabled = true;
			return false;
		}
	}

	async function handleLogin() {
		console.log(formDisabled, validPassword, validEmail, formValid());
		if (formValid() === true) {
			const response = await fetch(`${variables.API_ROOT}/api/user/login/`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({ email: email, password: password })
			});
			let data = await response.json();

			if (response.status === 200) {
				user.update(() => ({ ...data }));
				goto(`/home/${data.user_name}`);
			}
		}
	}
</script>

<form on:submit|preventDefault={handleLogin}>
	<div class="flex flex-col gap-4">
		<fieldset class="flex flex-col">
			<label for="email">Email:</label>
			<input
				class="py-1 pl-2 bg-transparent border-0 border-b border-black placeholder:text-gray-700/80 focus:border-b-2 focus:outline-none focus:ring-0"
				id="email"
				name="email"
				type="text"
				placeholder="Your Email"
				bind:value={email}
				on:blur={validateEmail}
			/>
			{#if !validEmail}
				<p class="text-error-200">{formErrors.email}</p>
			{/if}
		</fieldset>
		<fieldset class="flex flex-col pb-4">
			<label for="password">Password:</label>
			<input
				class="py-1 pl-2 bg-transparent border-b border-black placeholder:text-gray-700/80 focus:border-b-2 focus:outline-none focus:ring-0"
				id="password"
				name="password"
				type="password"
				bind:value={password}
				on:blur={validatePassword}
			/>
			{#if !validPassword}
				<p class="text-error-200">{formErrors.password.check}</p>
			{/if}
		</fieldset>
		<Button text="Submit" disabled={formDisabled} />
	</div>
</form>
