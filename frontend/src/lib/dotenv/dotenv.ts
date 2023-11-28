import type { Variables } from "$lib/interfaces/variables";

const API_ROOT: string = import.meta.env.VITE_API_ROOT;

export const variables: Variables = { API_ROOT: API_ROOT };
