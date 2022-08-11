export type ButtonProps = (React.ComponentPropsWithoutRef<'button'> & {
	buttonText: undefined;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
}) | (Omit<React.ComponentPropsWithoutRef<'button'>, 'children'> & {
	buttonText: string;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
})

