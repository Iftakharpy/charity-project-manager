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
}

export interface UserEndpointResponse{
	success: boolean;
    data: User
}

export type UserState = {
	isLoggedIn: false,
	profile: null
} | {
	isLoggedIn: true,
	profile: User
}
