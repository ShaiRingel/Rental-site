import NavBar from "../components/NavBar";

const MainPage = () => {
  return (
    <div>
      <NavBar
        navLinks={[
          { name: "Sales", path: "/ItemsOnSale" },
          { name: "Requested", path: "/WantedItems" },
          { name: "My Items", path: "/MyItems" },
        ]}
      >
        Rental Services
      </NavBar>
    </div>
  );
};

export default MainPage;
