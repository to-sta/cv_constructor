<script lang="ts">
	import LoginForm from "../../components/auth/loginForm.svelte";
	import SignUpForm from "../../components/auth/signUpForm.svelte";
	import Switch from "../../components/auth/switch.svelte";
	import auth from "../../stores/auth";

	let loginSignUp: boolean;
	auth.subscribe((value) => (loginSignUp = value));
</script>

<svelte:head>
	<title>Login/SignUp</title>
	<meta name="description" content="Login and SignUp Page" />
</svelte:head>

<section>
	<div
		class="flex flex-col items-center justify-center max-w-screen-xl gap-4 p-4 mx-auto sm:flex-row"
	>
		<!-- Login/SignUp Card -->
		<div>
			<!-- Card -->
			<div class="w-[400px] bg-black/30 rounded-3xl shadow-lg shadow-black/30 p-8">
				<!-- Form -->
				<div class="flex flex-col w-full h-full gap-6">
					<div class="flex justify-center">
						<div class="p-2 rounded-full bg-primary-300">
							<svg xmlns="http://www.w3.org/2000/svg" width="4em" height="4em" viewBox="0 0 24 24"
								><path
									fill="currentColor"
									d="M12 12q-1.65 0-2.825-1.175T8 8q0-1.65 1.175-2.825T12 4q1.65 0 2.825 1.175T16 8q0 1.65-1.175 2.825T12 12Zm-8 8v-2.8q0-.85.438-1.563T5.6 14.55q1.55-.775 3.15-1.163T12 13q1.65 0 3.25.388t3.15 1.162q.725.375 1.163 1.088T20 17.2V20H4Z"
								/></svg
							>
						</div>
					</div>
					<Switch leftText="Login" rightText="SignUp" />

					{#if loginSignUp}
						<SignUpForm />
					{:else}
						<LoginForm />
					{/if}
				</div>
			</div>
		</div>
	</div>
</section>
