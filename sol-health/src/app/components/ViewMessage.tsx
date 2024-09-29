'use client';



const Message = ({ text, userId } : {
    text: string,
    userId: string
}) => {
    if(userId === 'ai'){
        return (
            <div id={userId} className={`mb-2 flex ${userId !== 'ai' ? '' : 'flex-row-reverse'} justify-between`}>
                <div className={'w-[20%]'}/>
                <div dangerouslySetInnerHTML={{ __html: text }} className={`text-sm text-[#141414CC] font-normal leading-[22px] py-2.5 pr-2 px-[15px] ${userId !== 'ai'  ? 'w-[fit-content] bg-[#F7F7F7] rounded-t-[12px] rounded-br-[12px]' : 'w-[fit-content] bg-[#FEEDE7] rounded-t-[12px] rounded-bl-[12px]'}`} />
            </div>
        )
    }
    // console.log(user?.uid)
    return (
        <div id={userId} className={`mb-2 flex ${userId !== 'ai' ? '' : 'flex-row-reverse'} justify-between`}>
            <div className={'w-[20%]'}/>
            <div className={`text-sm text-[#141414CC] font-normal leading-[22px] py-2.5 pr-2 px-[15px] ${userId !== 'ai'  ? 'w-[fit-content] bg-[#F7F7F7] rounded-t-[12px] rounded-br-[12px]' : 'w-[fit-content] bg-[#FEEDE7] rounded-t-[12px] rounded-bl-[12px]'}`}>{text}</div>
        </div>
    )
}

const Messages = ({ msg } :{
    msg: {
        text: string,
        id: string
    }[]
}) => {

    

  return (
    <div className="mt-4 min-h-8 pb-[150px]">
        {
            msg.map((item, id) => (
                <Message text={item.text} key={id} userId={item?.id}/>
            ))
        }
    </div>
  )
}

export default Messages