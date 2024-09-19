'use client';

const SendMessage = () => {
  return (
    <div className="absolute bottom-0 left-0 w-full bg-slate-600 p-7 flex items-center">
        <textarea className="h-10 p-1 text-black w-full" />
        <button  className="ml-3 bg-black text-white p-5">Send</button>
    </div>
  )
}

export default SendMessage