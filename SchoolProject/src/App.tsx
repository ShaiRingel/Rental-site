import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./screen/LoginPage";
import NotificationPage from "./screen/NotificationPage";
import MessangerPage from "./screen/MessengerPage";
import MessangersPage from "./screen/MessangersPage";
import ForgotPasswordPage from "./screen/ForgotPasswordPage";
import ItemsOnSalePage from "./screen/ItemsOnSalePage";
import WantedItemsPage from "./screen/WantedItemsPage";
import MyItemsPage from "./screen/MyItemsPage";
import ProductPage from "./screen/ProductPage";

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route index element={<ItemsOnSalePage />} />
          <Route path="/ItemsOnSale" element={<ItemsOnSalePage />} />
          <Route path="/MyItems" element={<MyItemsPage />} />
          <Route path="/WantedItems" element={<WantedItemsPage />} />
          <Route path="/Login" element={<LoginPage />} />
          <Route path="/Notification" element={<NotificationPage />} />
          <Route path="/Messanger" element={<MessangerPage />} />
          <Route path="/Messangers" element={<MessangersPage />} />
          <Route path="/ForgotPassword" element={<ForgotPasswordPage />} />
          <Route path="/Product" element={<ProductPage />}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
