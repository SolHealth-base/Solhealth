import { useState } from "react";

const SendMessage = ({ sendMsg }: { sendMsg: (text: string) => void }) => {
  const [text, setText] = useState("");
  const handleSubmit = () => {
    sendMsg(text);
    setText("");
  };
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      e.preventDefault();
      if (text) handleSubmit();
    }
  };
  return (
    <div className="fixed mt-4 bottom-0 left-0 w-full bg-slate-600 p-3 flex items-center">
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="h-12 p-3 text-black w-full rounded focus-visible:outline-none"
        onKeyDown={handleKeyDown}
        placeholder="Ask SolHealth your Health related questions"
      />
      <button
        onClick={handleSubmit}
        className="ml-3 h-12 bg-black text-white p-3 rounded"
      >
        Send
      </button>
    </div>
  );
};

export default SendMessage;
