import TextBox from "../components/TextBox";
import Button from "../components/Button";
import { useNavigate } from "react-router-dom";

function ForgotPasswordPage() {
  let forgotpasswordInputs = {
    Username: "text",
    UniqueCode: "text",
    GroupNumber: "text",
    NewPassword: "password",
  };
  const handleLogin = (value: string) => console.log(value);
  const navigate = useNavigate();

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "space-evenly",
      }}
    >
      <h1>Reset Password:</h1>
      <ul key="ForgotPasswordFields" style={{ listStyleType: "none" }}>
        {Object.keys(forgotpasswordInputs).map((input, index) => (
          <li key={input + "Key"}>
            <TextBox
              key={input}
              type={Object.values(forgotpasswordInputs)[index]}
            >
              {input}
            </TextBox>
          </li>
        ))}
      </ul>
      <br />

      <br />
      <Button
        onClick={() => {
          Object.keys(forgotpasswordInputs).map((input) =>
            handleLogin(
              (document.getElementById("Ipt" + input) as HTMLInputElement).value
            )
          );
          navigate("/");
        }}
      >
        Login
      </Button>
    </div>
  );
}

export default ForgotPasswordPage;
