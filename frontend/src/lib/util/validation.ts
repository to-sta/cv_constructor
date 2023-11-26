export function validateEmail(email: string) {
	const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
	return email.match(validRegex) ? true : false;
}

export function validatePassword(password: string) {
	return password.length > 8 ? true : false;
}

export function validatePasswordMatch(password: string, confirmPassword: string) {
	return password === confirmPassword ? true : false;
}

export function validateUsername(username: string) {
	return username.length > 3 ? true : false;
}
