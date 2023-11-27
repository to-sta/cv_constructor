<script lang="ts">
	import { writable } from "svelte/store";
	import { variables } from "$lib/dotenv/dotenv";
	import auth from "../../stores/auth";
	import Button from "../buttons/button.svelte";
	import { formErrors } from "./formErrors";
	import {
		validateEmail,
		validatePassword,
		validatePasswordMatch,
		validateUsername
	} from "$lib/util/validation";

	let username = writable("");
	let email = writable("");
	let password = writable("");
	let confirmPassword = writable("");

	let validEmail = writable(true);
	let validPassword = writable(true);
	let validUsername = writable(true);
	let validPasswordMatch = writable(true);

	let formDisabled = writable(false);

	function formValid() {
		if (
			$username.length === 0 ||
			$email.length === 0 ||
			$password.length === 0 ||
			$confirmPassword.length === 0
		) {
			$formDisabled = true;
			$validUsername = validateUsername($username);
			$validEmail = validateEmail($email);
			$validPassword = validatePassword($password);
			$validPasswordMatch = validatePasswordMatch($password, $confirmPassword);
			return false;
		}
		if ($validUsername && $validEmail && $validPassword && $validPasswordMatch) {
			$formDisabled = false;
			return true;
		} else {
			$formDisabled = true;
			return false;
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

			if (response.status === 201) {
				auth.update((val) => !val);
			}
		}
	}
</script>

<form on:submit|preventDefault={handleSignUp}>
	<div class="flex flex-col gap-4">
		<fieldset class="flex flex-col">
			<label for="username">Username:</label>
			<input
				id="username"
				name="username"
				class="py-1 pl-2 bg-transparent border-b border-black placeholder:text-gray-700/80 focus:border-b-2 focus:outline-none focus:ring-0"
				placeholder="Your Username"
				type="text"
				bind:value={$username}
				on:blur={() => validUsername.set(validateUsername($username))}
			/>
			{#if !$validUsername}
				<p class="text-error-200">{formErrors.email}</p>
			{/if}
		</fieldset>
		<fieldset class="flex flex-col">
			<label for="email">Email:</label>
			<input
				id="email"
				name="email"
				class="py-1 pl-2 bg-transparent border-b border-black placeholder:text-gray-700/80 focus:border-b-2 focus:outline-none focus:ring-0"
				placeholder="Your Email"
				type="text"
				bind:value={$email}
				on:blur={() => validEmail.set(validateEmail($email))}
			/>
			{#if !$validEmail}
				<p class="text-error-200">{formErrors.email}</p>
			{/if}
		</fieldset>
		<fieldset class="flex flex-col">
			<label for="password">Password:</label>
			<input
				id="password"
				name="password"
				class="py-1 pl-2 bg-transparent border-b border-black focus:border-b-2 focus:outline-none focus:ring-0"
				type="password"
				bind:value={$password}
				on:blur={() => validPassword.set(validatePassword($password))}
			/>
			{#if !$validPassword}
				<p class="text-error-200">{formErrors.password.check}</p>
			{/if}
		</fieldset>
		<fieldset class="flex flex-col pb-4">
			<label for="confirmPassword">Confirm Password:</label>
			<input
				id="confirmPassword"
				name="confirmPassword"
				class="py-1 pl-2 bg-transparent border-b border-black focus:border-b-2 focus:outline-none focus:ring-0"
				type="password"
				bind:value={$confirmPassword}
				on:blur={() => validPasswordMatch.set(validatePasswordMatch($password, $confirmPassword))}
			/>
			{#if !$validPasswordMatch}
				<p class="text-error-200">{formErrors.password.match}</p>
			{/if}
		</fieldset>
		<Button disabled={$formDisabled} text="Submit" />
	</div>
</form>
