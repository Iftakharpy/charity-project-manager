export type FormProps = React.ComponentPropsWithoutRef<'form'> & ({
	errors?: string[];
	formHeaderText: string;
	formHeaderProps?: Omit<React.ComponentPropsWithoutRef<'header'>, 'children'>
} | {
	errors?: string[];
	formHeaderText?: undefined;
	formHeaderProps?: React.ComponentPropsWithoutRef<'header'>
})
