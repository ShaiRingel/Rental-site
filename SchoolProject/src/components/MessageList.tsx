import React from "react";

interface Message {
  id: number;
  text: string;
}

interface MessageListProps {
  messages: Message[];
}

const MessageList: React.FC<MessageListProps> = ({ messages }) => {
  return (
    <ul className="list-unstyled">
      {messages.map((message) => (
        <li key={message.id} className="mb-2">
          <div className="p-2 rounded bg-light">{message.text}</div>
        </li>
      ))}
    </ul>
  );
};

export default MessageList;
