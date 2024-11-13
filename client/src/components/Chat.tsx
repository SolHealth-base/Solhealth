"use client";
import { useState } from "react";
import SendMessage from "@/views/Chat/SendMessage";
import Messages from "@/views/Chat/ViewMessage";
import ChatHeader from "@/views/Chat/ChatHeader";

type Response = {
  response: string;
};
export type Sender = "ai" | "user";

export type Message = {
  id: Sender;
  text: string;
};

const getData = async (url: string, query: string) => {
  const data = {
    query: query,
  };
  try {
    const response = await fetch(url, {
      method: "POST", // Specifies the request method
      headers: {
        "Content-Type": "application/json", // Specify that we are sending JSON
      },
      body: JSON.stringify(data), // Convert data to JSON string
      cache: "no-store",
    });

    // console.log('hi')
    // Check if response is OK
    if (response.ok) {
      const jsonResponse = await response.json(); // Parse the JSON response
      // console.log("Success:", jsonResponse); // Log the successful response
      return jsonResponse as Response; // Optionally return the response for further use
    } else {
      console.error("HTTP Error:", response.status); // Log the error status
    }
  } catch (error) {
    console.error("Error:", error); // Catch and log any errors
  }
};
const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);

  const fetchMsg = (question: string) => {
    // console.log(e)
    if (!question) return;
    setMessages((prev) => [
      ...prev,
      {
        text: question,
        id: "user",
      },
    ]);
    const data = getData(
      "https://ohtf0m9m6e.execute-api.us-east-1.amazonaws.com/dev/chat",
      question
    );
    data.then((res) => {
      console.log(res?.response);
      if (res)
        setMessages((prev) => [
          ...prev,
          {
            text: res.response,
            id: "ai",
          },
        ]);
    });
  };

  return (
    <div className="relative">
      <ChatHeader />
      <div className="min-h-40 mt-20">
        <Messages msg={messages} />
      </div>
      <SendMessage sendMsg={fetchMsg} />
    </div>
  );
};
export default Chat;
