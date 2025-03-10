import React from "react";
import MessengerItem from "../components/MessengeItem";

interface Messenger {
  id: number;
  name: string;
  lastMessage: string;
}

const mockMessengers: Messenger[] = [
  { id: 1, name: "John Doe", lastMessage: "Hey, how are you?" },
  { id: 2, name: "Jane Smith", lastMessage: "Let’s meet tomorrow!" },
  { id: 3, name: "Alex Johnson", lastMessage: "Call me when you can." },
];

const MessengerListPage: React.FC = () => {
  return (
    <div className="container mt-4">
      <h1>Messengers</h1>
      <ul className="list-group">
        {mockMessengers.map((messenger) => (
          <MessengerItem key={messenger.id} messenger={messenger} />
        ))}
      </ul>
    </div>
  );
};

export default MessengerListPage;
