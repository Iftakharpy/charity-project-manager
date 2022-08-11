export type ButtonProps = (React.ComponentPropsWithoutRef<'button'> & {
	buttonText?: string;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
})
