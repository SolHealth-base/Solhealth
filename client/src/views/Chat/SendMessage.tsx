import { useState } from "react";

const SendMessage = ({
  upwardMsg,
}: {
  //   sendMessages: Dispatch<SetStateAction<{
  //     id: string;
  //     text: string;

  // }[]>>,
  upwardMsg: (text: string) => void;
}) => {
  const [text, setText] = useState("");
  const handleSubmit = () => {
    // sendMessages((prev: {id: string,
    //   text: string}[]) => [...prev, {
    //   id: '',
    //   text: text
    // }])
    upwardMsg(text);
    setText("");
  };
  return (
    <div className="fixed mt-4 bottom-0 left-0 w-full bg-slate-600 p-7 flex items-center">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="h-10 p-1 text-black w-full"
      />
      <button onClick={handleSubmit} className="ml-3 bg-black text-white p-5">
        Send
      </button>
    </div>
  );
};

export default SendMessage;
