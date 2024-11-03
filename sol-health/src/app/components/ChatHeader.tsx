import Image from "next/image"

const ChatHeader = () => {
  return (
    <div className="mt-[40px]">
        <div className="flex items-center justify-between">
            <div />
            <h2 className="text-[#FFFFFF] text-xs leading-[14px]">SolHealth Chatbot</h2>
            <div />
        </div>
        <div className="mt-[50px]">
            <div className="flex items-center justify-center">
                <Image 
                    src={'/robot.svg'}
                    alt="robot image"
                    height={79.57}
                    width={75.3}
                />
            </div>
            <h3 className="text-[#FFFFFF] w-[100%] px-4 text-center mx-auto">I&apos;m here to support with any health-related questions you may have.</h3>
            <h3 className="text-[#FFFFFF] w-[100%] px-4 text-center mx-auto">How can I help you?</h3>
        </div>
    </div>
  )
}

export default ChatHeader