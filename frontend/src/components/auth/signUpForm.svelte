<script lang="ts">
	// import { goto } from "$app/navigation";
	import { variables } from "$lib/dotenv/dotenv";
	import auth from "../../stores/auth";
	import Button from "../buttons/button.svelte";
	import { formErrors } from "./formErrors";

	let username: string = "";
	let email: string = "";
	let password: string = "";
	let confirmPassword: string = "";

	let validUsername: boolean = true;
	let validEmail: boolean = true;
	let validPassword: boolean = true;
	let validPasswordMatch: boolean = true;

	let formDisabled: boolean = false;

	function validateUsername() {
		if (username.length > 3) {
			return (validUsername = true);
		} else {
			return (validUsername = false);
		}
	}

	function validateEmail() {
		let validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
		if (email.match(validRegex)) {
			console.log("Email is valid");
			return (validEmail = true);
		} else {
			return (validEmail = false);
		}
	}

	function validatePassword() {
		// Checks if the password has more than 8 characters
		if (password.length > 8) {
			return (validPassword = true);
		} else {
			return (validPassword = false);
		}
	}

	function validatePasswordMatch() {
		if (password === confirmPassword) {
			return (validPasswordMatch = true);
		} else {
			return (validPasswordMatch = false);
		}
	}

	function formValid() {
		if (validUsername && validEmail && validPassword && validPasswordMatch) {
			return (formDisabled = false);
		} else {
			return (formDisabled = true);
		}
	}

	async function handleSignUp() {
		if (formValid() === true) {
			const response = await fetch(`${variables.API_ROOT}/api/user/register/`, {
				method: "POST",
				headers: {
					"Content-Type": "application/json"
				},
				body: JSON.stringify({
					user_name: username,
					email: email,
					password: password
				})
			});

			if (response.status < 299) {
				auth.update((val) => !val);
				console.log(auth);
			}
		}
	}
</script>

<form on:submit|preventDefault={handleSignUp}>
	<div class="flex flex-col gap-4">
		<fieldset class="flex flex-col">
			<label for="username">Username:</label>
			<input
				class="py-1 pl-2 bg-transparent border-b border-black placeholder:text-gray-700/80 focus:border-b-2 focus:outline-none focus:ring-0"
				id="username"
				name="username"
				type="text"
				placeholder="Your Username"
				bind:value={username}
				on:blur={validateUsername}
			/>
			{#if !validUsername}
				<p class="text-error-200">{formErrors.email}</p>
			{/if}
		</fieldset>
		<fieldset class="flex flex-col">
			<label for="email">Email:</label>
			<input
				class="py-1 pl-2 bg-transparent border-b border-black placeholder:text-gray-700/80 focus:border-b-2 focus:outline-none focus:ring-0"
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
		<fieldset class="flex flex-col">
			<label for="password">Password:</label>
			<input
				class="py-1 pl-2 bg-transparent border-b border-black focus:border-b-2 focus:outline-none focus:ring-0"
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
		<fieldset class="flex flex-col pb-4">
			<label for="confirmPassword">Confirm Password:</label>
			<input
				class="py-1 pl-2 bg-transparent border-b border-black focus:border-b-2 focus:outline-none focus:ring-0"
				id="confirmPassword"
				name="confirmPassword"
				type="password"
				bind:value={confirmPassword}
				on:blur={validatePasswordMatch}
			/>
			{#if !validPasswordMatch}
				<p class="text-error-200">{formErrors.password.match}</p>
			{/if}
		</fieldset>
		<Button text="Submit" disabled={formDisabled}/>
	</div>
</form>
