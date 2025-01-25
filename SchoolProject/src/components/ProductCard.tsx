import React from "react";

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

interface ProductCardProps {
  product: Product;
  onButtonClick: () => void;
}

const ProductCard: React.FC<ProductCardProps> = ({
  product,
  onButtonClick,
}) => {
  return (
    <div className="card" style={{ width: "200px", height: "300px" }}>
      <center>
        <img
          src={product.image}
          className="card-img-top"
          alt={product.name}
          style={{ width: "150px", height: "150px" }}
        />
        <div className="card-body">
          <h5 className="card-title">{product.name}</h5>
          <p className="card-text">${product.price.toFixed(2)}</p>
          <button
            className="btn btn-primary"
            onClick={() => onButtonClick(product.id)}
          >
            Add to Cart
          </button>
        </div>
      </center>
    </div>
  );
};

export default ProductCard;
