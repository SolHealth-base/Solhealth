'use client'
import { useEffect, useState } from "react"
import SendMessage from "./SendMessage"
import Messages from "./ViewMessage"

const getData = async (url : string, query: string) => {
  const data = {
      query: query
  }
  try {
      const response = await fetch(url, {
        method: 'POST', // Specifies the request method
        headers: {
          'Content-Type': 'application/json', // Specify that we are sending JSON
        },
        body: JSON.stringify(data), // Convert data to JSON string
      });
  
      // Check if response is OK
      if (response.ok) {
        const jsonResponse = await response.json(); // Parse the JSON response
        // console.log('Success:', jsonResponse); // Log the successful response
        return jsonResponse; // Optionally return the response for further use
      } else {
        console.error('HTTP Error:', response.status); // Log the error status
      }
    } catch (error) {
      console.error('Error:', error); // Catch and log any errors
    }
}
const Chat =  () => {
  const [messages, setMessages] = useState<{
    id: string,
    text: string
  }[]>([]);
console.log(messages)
  useEffect(()=>{
    if(messages[messages.length - 1]?.text === undefined) return
    const jj = getData('http://34.226.123.43/chat', messages[messages.length - 1]?.text);
    jj.then(res => setMessages(prev => [...prev, {
      id: 'ai',
      text: res?.response
    }]))
  }, [messages])
  return (
    <div className='relative'>
      <div className=" mt-20">
      {/* overflow-y-auto h-[70vh] pb-20 */}
        <Messages msg={messages}/>
      </div>
      <SendMessage sendMessages={setMessages} />
    </div>
  )
}

export default Chat