export type FormProps = React.ComponentPropsWithoutRef<'form'> & ({
	formHeaderText: string;
	formHeaderProps?: Omit<React.ComponentPropsWithoutRef<'header'>, 'children'>
} | {
	formHeaderText?: undefined;
	formHeaderProps?: React.ComponentPropsWithoutRef<'header'>
})
