
import SendMessage from "./SendMessage"
import Messages from "./ViewMessage"

const Chat = () => {

  return (
    <div className='relative'>
      <div className=" mt-20">
      {/* overflow-y-auto h-[70vh] pb-20 */}
        <Messages />
      </div>
      <SendMessage />
    </div>
  )
}

export default Chat