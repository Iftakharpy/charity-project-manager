export type InputProps = React.ComponentPropsWithoutRef<'input'> & ({
	labelText: string,
	name: string;
	labelProps?: Omit<React.ComponentPropsWithoutRef<'label'>, 'children'>;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
} | {
	labelText: undefined,
	name: string;
	labelProps?: React.ComponentPropsWithoutRef<'label'>;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
})


export type SelectProps = React.ComponentPropsWithoutRef<'select'> & ({
	labelText: string,
	name: string;
	labelProps?: Omit<React.ComponentPropsWithoutRef<'label'>, 'children'>;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
} | {
	labelText: undefined,
	name: string;
	labelProps?: React.ComponentPropsWithoutRef<'label'>;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
})


export type TextareaProps = React.ComponentPropsWithoutRef<'textarea'> & ({
	labelText: string,
	name: string;
	labelProps?: Omit<React.ComponentPropsWithoutRef<'label'>, 'children'>;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
} | {
	labelText: undefined,
	name: string;
	labelProps?: React.ComponentPropsWithoutRef<'label'>;
	containerProps?: Omit<React.ComponentPropsWithoutRef<'div'>, 'children'>;
})
