'use client';

import { useWallet } from '@solana/wallet-adapter-react';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { useEffect } from 'react';

const ConnectWallet = () => {
//  const jj= useWallet()
//  const handleClick = () => {
//   console.log(jj.publicKey?.toString())
//  }
  return (
   <>
     {/* <button onClick={handleClick}  className='max-w-[350px] p-2.5 rounded-[10px] bg-[#FFFFFF] w-[60%] mx-auto text-[#001354]'>Connect Wallet</button> */}

     <WalletMultiButton />
   </>
  )
}

export default ConnectWallet