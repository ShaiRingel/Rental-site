interface Props {
  children: string;
  onClick: (item: string) => void;
}

const Button = ({ children, onClick }: Props) => {
  return (
    <div className="btn btn-primary" onClick={() => onClick(children)}>
      {children}
    </div>
  );
};

export default Button;
