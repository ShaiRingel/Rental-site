interface Props {
  children: string;
  width?: number;
  height?: number;
  type:
    | string
    | "button"
    | "checkbox"
    | "color"
    | "date"
    | "datetime-local"
    | "email"
    | "file"
    | "hidden"
    | "image"
    | "month"
    | "number"
    | "password"
    | "radio"
    | "range"
    | "reset"
    | "search"
    | "submit"
    | "tel"
    | "text"
    | "time"
    | "url"
    | "week";
}

const TextBox = ({ children, width = NaN, height = NaN, type }: Props) => {
  return (
    <>
      <div>
        {children && (
          <>
            <label>{children + ":"}</label>
            <br />
          </>
        )}
        <input
          id={"Ipt" + children}
          type={type}
          style={{
            width: isNaN(width) ? undefined : width,
            height: isNaN(height) ? undefined : height,
            borderTop: "0px solid #000",
            borderRight: "0px solid #000",
            borderLeft: "0px solid #000",
            borderBottom: "2px solid #000",
          }}
        ></input>
      </div>
    </>
  );
};

export default TextBox;
