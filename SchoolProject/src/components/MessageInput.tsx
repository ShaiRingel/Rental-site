import React, { Component } from "react";

interface MessageInputProps {
  onSend: (text: string) => void;
}

interface MessageInputState {
  message: string;
}

class MessageInput extends Component<MessageInputProps, MessageInputState> {
  constructor(props: MessageInputProps) {
    super(props);
    this.state = {
      message: "",
    };
  }

  handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    this.setState({ message: e.target.value });
  };

  handleSend = () => {
    if (this.state.message.trim()) {
      this.props.onSend(this.state.message);
      this.setState({ message: "" });
    }
  };

  handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      this.handleSend();
    }
  };

  render() {
    return (
      <div className="input-group">
        <input
          type="text"
          className="form-control"
          placeholder="Type a message..."
          value={this.state.message}
          onChange={this.handleChange}
          onKeyPress={this.handleKeyPress}
        />
        <button className="btn btn-primary" onClick={this.handleSend}>
          Send
        </button>
      </div>
    );
  }
}

export default MessageInput;
