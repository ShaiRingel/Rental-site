import { useLocation, useNavigate } from "react-router-dom";

interface NavLink {
  name: string;
  path: string;
}

interface Props {
  children: string;
  navLinks: NavLink[];
}

const NavBar = ({ children, navLinks }: Props) => {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand mb-0 h1">{children}</a>
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div className="navbar-nav">
            {navLinks.map((link) => (
              <a
                key={link.path}
                className={
                  location.pathname === link.path ||
                  (link.path === "/ItemsOnSale" && location.pathname === "/")
                    ? "nav-link active"
                    : "nav-link"
                }
                aria-current={
                  location.pathname === link.path ? "page" : undefined
                }
                href="#"
                onClick={(e) => {
                  e.preventDefault();
                  navigate(link.path);
                }}
              >
                {link.name}
              </a>
            ))}
            <img
              src="src/assets/notifications2.svg"
              alt="Notifications"
              width={35}
              height={35}
            />
          </div>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
