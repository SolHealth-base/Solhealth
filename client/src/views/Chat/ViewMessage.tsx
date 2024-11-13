"use client";

import { type Message, type Sender } from "@/components/Chat";
import { useEffect, useRef } from "react";

const Message = ({ text, id }: { text: string; id: Sender }) => {
  const isAi = id === "ai";
  return (
    <div
      className={`mb-2 pl-2 flex justify-between ${
        !isAi && "flex-row-reverse"
      }`}
      data-sender={id}
    >
      <div
        dangerouslySetInnerHTML={{ __html: text }}
        style={{
          boxShadow: `${isAi && "0px 0px 4px 0px #00000040"}`,
        }}
        className={`text-sm text-white font-normal leading-[21px] p-4 w-[90%] ${
          !isAi
            ? "bg-[#001354] rounded-l-[20px] rounded-tr-[20px]"
            : "border border-[#FFFFFF33] bg-[#FFFFFF33] rounded-r-[20px] rounded-tl-[20px]"
        }`}
      />
    </div>
  );
};

const Messages = ({ msg }: { msg: Message[] }) => {
  const messageEndRef = useRef<HTMLDivElement | null>(null);

  const scrollToBottom = () => {
    messageEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  useEffect(() => {
    scrollToBottom();
  }, [msg]);

  return (
    <div className="mt-4 min-h-8 pb-14 flex flex-col gap-4 mb-14">
      {msg.map((item, id) => (
        <Message text={item.text} key={id} id={item?.id} />
      ))}
      <div ref={messageEndRef} />
    </div>
  );
};

export default Messages;
