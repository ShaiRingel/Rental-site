interface Props {
  children: string;
}

const Alert = ({ children }: Props) => {
  return (
    <div className="alert alert-info" role="alert">
      {children}
    </div>
  );
};

export default Alert;
