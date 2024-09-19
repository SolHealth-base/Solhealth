'use client';



const Message = ({ text, userId } : {
    text: string,
    userId: string
}) => {

    // console.log(user?.uid)
    return (
        <div id={userId} className={`mb-2 flex ${true? '' : 'flex-row-reverse'} justify-between`}>
            <div className={'w-[20%]'}/>
            <div className={`text-sm text-[#141414CC] font-normal leading-[22px] py-2.5 pr-2 px-[15px] ${true ? 'w-[fit-content] bg-[#F7F7F7] rounded-t-[12px] rounded-br-[12px]' : 'w-[fit-content] bg-[#FEEDE7] rounded-t-[12px] rounded-bl-[12px]'}`}>{text}</div>
        </div>
    )
}

const Messages = () => {

  return (
    <div className="mt-4">
        <Message text="hey" userId="L7egZf4DoZOYLeHLwN8ZAaKNg4o1"/>
        <Message text="hey" userId="6"/>
        <Message text="What's up?" userId="L7egZf4DoZOYLeHLwN8ZAaKNg4o1"/>
        <Message text="I've been trying to get hold of you since" userId="L7egZf4DoZOYLeHLwN8ZAaKNg4o1"/>
        <Message text="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque enim quaerat, quas excepturi temporibus consectetur maiores deleniti alias atque tempora dolor sed eveniet voluptatum magni qui veritatis culpa quo voluptatem illum, cumque reiciendis aut? Non fugit saepe incidunt a." userId="L7egZf4DoZOYLeHLwN8ZAaKNg4o1"/>
        <Message text="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque enim quaerat, quas excepturi temporibus consectetur maiores deleniti alias atque tempora dolor sed eveniet voluptatum magni qui veritatis culpa quo voluptatem illum, cumque reiciendis aut? Non fugit saepe incidunt a." userId="L7egZf4DoZOYLeHLwN8ZAaKNg4o"/> 
        <Message text="I've been trying to get hold of you since" userId="L7egZf4DoZOYLeHLwN8ZAaKNg4o1"/>       
    </div>
  )
}

export default Messages