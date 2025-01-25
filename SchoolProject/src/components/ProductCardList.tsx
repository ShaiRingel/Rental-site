import React from "react";
import ProductCard from "./ProductCard";

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

const mockProducts: Product[] = [
  {
    id: 1,
    name: "Wireless Headphones",
    price: 99.99,
    image: "https://via.placeholder.com/150",
  },
  {
    id: 2,
    name: "Smart Watch",
    price: 199.99,
    image: "https://via.placeholder.com/150",
  },
  {
    id: 3,
    name: "Gaming Mouse",
    price: 49.99,
    image: "https://via.placeholder.com/150",
  },
];

const ProductListPage: React.FC = () => {
  const handleAddToCart = (productId: number) => {
    alert(`Product ${productId} added to cart!`);
  };

  return (
    <div className="container mt-4">
      <h2>Product List</h2>
      <div className="row">
        {mockProducts.map((product) => (
          <div key={product.id} className="col-md-4 mb-4">
            <ProductCard
              product={product}
              onButtonClick={() => handleAddToCart}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProductListPage;
