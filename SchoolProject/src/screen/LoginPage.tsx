import TextBox from "../components/TextBox";
import Button from "../components/Button";
import { useNavigate } from "react-router-dom";

function LoginPage() {
  let loginInputs = {
    Username: "text",
    Password: "password",
    GroupNumber: "text",
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
      <h1>Login page:</h1>
      <ul key="LoginFields" style={{ listStyleType: "none" }}>
        {Object.keys(loginInputs).map((input, index) => (
          <li key={input + "Key"}>
            <TextBox key={input} type={Object.values(loginInputs)[index]}>
              {input}
            </TextBox>
          </li>
        ))}
      </ul>
      <br />
      <a href="#" onClick={() => navigate("/forgotpassword")} color="Gray">
        Forgot Password?
      </a>
      <br />
      <Button
        onClick={() => {
          Object.keys(loginInputs).map((input) =>
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

export default LoginPage;
