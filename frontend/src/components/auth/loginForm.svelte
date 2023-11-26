<script lang="ts">
	import user from "../../stores/user";
	import { goto } from "$app/navigation";
	import { variables } from "$lib/dotenv/dotenv";
	import Button from "../buttons/button.svelte";
	import { formErrors } from "./formErrors";
	import Cookies from "js-cookie";
	import { validateEmail, validatePassword } from "$lib/util/validation";
	import { writable } from "svelte/store";

	let email = writable("");
	let password = writable("");
	let validEmail = writable(true);
	let validPassword = writable(true);
	let formDisabled = writable(false);

	function formValid() {
		if ($email.length === 0 || $password.length === 0) {
			$formDisabled = true;
			$validEmail = validateEmail($email);
			$validPassword = validatePassword($password);
			return false;
		}
		if (validEmail && validPassword) {
			$formDisabled = false;
			return false;
		} else {
			$validEmail = false;
			$validPassword = false;
			$formDisabled = true;
			console.log($validEmail, $validPassword, $formDisabled);
			return true;
		}
	}

	async function handleLogin() {
		let csrftoken: string | undefined = Cookies.get("csrftoken");
		if (csrftoken == undefined) {
			return (csrftoken = "");
		}

		if (formValid() === true) {
			const response = await fetch(`${variables.API_ROOT}/api/user/login/`, {
				method: "POST",
				mode: "cors",
				credentials: "include",
				headers: {
					"Content-Type": "application/json",
					"X-CSRFToken": csrftoken
				},
				body: JSON.stringify({ email: email, password: password })
			});
			let data = await response.json();

			if (response.status === 200) {
				user.update(() => ({ ...data }));
				localStorage.setItem("user", JSON.stringify($user));
				goto(`/dashboard/`);
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
				bind:value={$email}
				on:blur={() => validEmail.set(validateEmail($email))}
			/>
			{#if !$validEmail}
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
				bind:value={$password}
				on:blur={() => validPassword.set(validatePassword($password))}
			/>
			{#if !$validPassword}
				<p class="text-error-200">{formErrors.password.check}</p>
			{/if}
		</fieldset>
		<Button text="Submit" disabled={$formDisabled} />
	</div>
</form>
