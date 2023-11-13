<script lang="ts">
	import { browser } from "$app/environment";
	import { goto } from "$app/navigation";
	import user from "../stores/user";

	if (browser) {
		console.log($user);
		if ($user == null) {
			goto("/auth");
		}
	}
</script>
