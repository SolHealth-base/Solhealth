'use client';



const Message = ({ text, userId } : {
    text: string,
    userId: string
}) => {
    if(userId === 'ai'){
        return (
            <div id={userId} className={`mb-2 pl-2 flex ${userId !== 'ai' ? '' : 'flex-row-reverse'} justify-between`}>
                <div className={'w-[20%]'}/>
                <div dangerouslySetInnerHTML={{ __html: text }} style={{boxShadow: `${userId !== 'ai'  ? '' : '0px 0px 4px 0px #00000040'}`}} className={`text-sm text-[#141414CC] font-normal leading-[21px] py-2.5 pr-2  px-[19.5px] ${userId !== 'ai'  ? 'w-[fit-content] rounded-t-[12px] rounded-br-[12px]' : 'w-[fit-content] border border-[#FFFFFF33] bg-[#FFFFFF33] rounded-r-[20px] rounded-tl-[20px]'}`} />
            </div>
        )
    }
    

    // console.log(user?.uid)
    return (
        <div id={userId} className={`mb-2 pr-2 flex ${userId !== 'ai' ? '' : 'flex-row-reverse'} justify-between`}>
            <div className={'w-[20%]'}/>
            <div className={`text-sm text-[#FFFFFF] font-normal leading-[21px] py-2.5 pr-2 px-[16.5px] ${userId !== 'ai'  ? 'w-[fit-content] bg-[#001354] rounded-l-[20px] rounded-tr-[20px]' : 'w-[fit-content] bg-[#FEEDE7] rounded-t-[12px] rounded-bl-[12px]'}`}>{text}</div>
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
    <div className="mt-4 min-h-8 pb-[150px] overflow-auto">
        {
            msg.map((item, id) => (
                <Message text={item.text} key={id} userId={item?.id}/>
            ))
        }
    </div>
  )
}

export default Messages