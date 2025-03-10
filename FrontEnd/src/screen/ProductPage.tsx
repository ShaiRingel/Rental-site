interface Product {
  id: number;
  name: string;
  condition: string;
  price?: number;
  rentedTime?: number;
  image: string;
  description: string;
}

function ProductPage() {
  const product: Product = {
    id: 1,
    name: "Strategy Hammer",
    image: "src\\assets\\Hammer.png",
    condition: "Like new",
    price: 0,
    description:
      "This project was used only once and we don't have a use for it any more",
  };

  return (
    <div>
      <center>
        <h1>{product.name}</h1>
      </center>
      <img
        src={product.image}
        style={{ width: "600px", height: "600px" }}
      ></img>
      <center>
        <p>Products Condition: {product.condition}</p>
        {product.price != null ? (
          product.price === 0 ? (
            <p>Products price: Free</p>
          ) : (
            <p>Products price: {product.price}</p>
          )
        ) : null}
        {product.rentedTime != null ? (
          <p>Products price: {product.price}</p>
        ) : null}
      </center>
      <h2>Details</h2>
      <p style={{ border: "10" }}>{product.description}</p>
    </div>
  );
}

export default ProductPage;
