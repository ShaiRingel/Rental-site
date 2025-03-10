import { Component } from "react";
import MessageList from "../components/MessageList";
import MessageInput from "../components/MessageInput";

interface Message {
  id: number;
  text: string;
}

interface MessengerPageState {
  messages: Message[];
}

class MessengerPage extends Component<{}, MessengerPageState> {
  constructor(props: {}) {
    super(props);
    this.state = {
      messages: [],
    };
  }

  addMessage = (text: string) => {
    this.setState((prevState) => ({
      messages: [...prevState.messages, { id: Date.now(), text }],
    }));
  };

  render() {
    return (
      <div className="container mt-4">
        <div className="card shadow">
          <div className="card-header bg-primary text-white">
            <h5>Messenger</h5>
          </div>
          <div
            className="card-body"
            style={{ height: "400px", overflowY: "scroll" }}
          >
            <MessageList messages={this.state.messages} />
          </div>
          <div className="card-footer">
            <MessageInput onSend={this.addMessage} />
          </div>
        </div>
      </div>
    );
  }
}

export default MessengerPage;
