'use client';

import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';


const ConnectWallet = () => {

  return (
   <>
     {/* <button onClick={handleClick}  className='max-w-[350px] p-2.5 rounded-[10px] bg-[#FFFFFF] w-[60%] mx-auto text-[#001354]'>Connect Wallet</button> */}

     <WalletMultiButton />
   </>
  )
}

export default ConnectWallet