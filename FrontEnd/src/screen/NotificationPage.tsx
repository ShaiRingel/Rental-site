import { useState } from "react";
import Alert from "../components/Alert";

interface Notification {
  id: number;
  message: string;
}

const NotificationPage = () => {
  const [notifications] = useState<Notification[]>([
    { id: 1, message: "First notification" },
    { id: 2, message: "Second notification" },
    { id: 3, message: "Third notification" },
    { id: 4, message: "Fourth notification" },
    { id: 5, message: "Fifth notification" },
  ]);

  return (
    <div className="container mt-5">
      <h1>Notification Page</h1>

      <br />

      {notifications.map((notification) => (
        <Alert key={notification.id}>{notification.message}</Alert>
      ))}
    </div>
  );
};

export default NotificationPage;
