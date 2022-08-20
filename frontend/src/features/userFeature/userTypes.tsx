export interface LoginCredentials{
	email: string;
	password: string;
}

export interface User{
	id: number;
	first_name: string;
	last_name: string;
	email: string;
	phone_number: string;
	profile_picture: string;
	groups: string[];
	user_permissions: string[];
	is_active: boolean;
	is_staff: boolean;
	is_superuser: boolean;
	last_login: string;
	date_joined: string;
	session_expires_at: string;
}

export type UserEndpointResponse =  {
	success: true;
    data: User;
} | {
	success: false;
	errors: {[key:string]: string[]}
}

export type UserState = {
	isLoggedIn: false,
	profile: null
} | {
	isLoggedIn: true,
	profile: User
}
