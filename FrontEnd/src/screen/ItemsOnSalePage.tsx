import { useNavigate } from "react-router";
import Button from "../components/Button";
import Dropdown from "../components/Dropdown";
import NavBar from "../components/NavBar";
import ProductCard from "../components/ProductCard";

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

const ItemsOnSalePage = () => {
  const navigate = useNavigate();
  const products: Product = {
    id: 1,
    name: "Hammer",
    price: 9.99,
    image: "src\\assets\\Hammer.png",
  };
  const types: string[] = ["Machine", "Motors", "Electronics"];

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
      {types.map((type) => (
        <ul>
          <Button onClick={() => null}>{type}</Button>
        </ul>
      ))}
      <center>
        <Dropdown
          title="OrderBy"
          prompts={["Recent", "Condition", "Price"]}
        ></Dropdown>
      </center>
      <div style={{ margin: "200px" }}>
        <ProductCard
          onButtonClick={() => navigate("/product")}
          product={products}
        ></ProductCard>
      </div>
    </div>
  );
};

export default ItemsOnSalePage;
