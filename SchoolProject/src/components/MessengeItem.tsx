import React from "react";

interface Messenger {
  id: number;
  name: string;
  lastMessage: string;
}

interface MessengerItemProps {
  messenger: Messenger;
}

const MessengerItem: React.FC<MessengerItemProps> = ({ messenger }) => {
  return (
    <li className="list-group-item d-flex justify-content-between align-items-center">
      <div>
        <h5 className="mb-1">{messenger.name}</h5>
        <p className="mb-0 text-muted">{messenger.lastMessage}</p>
      </div>
      <button className="btn btn-sm btn-primary">Open</button>
    </li>
  );
};

export default MessengerItem;
