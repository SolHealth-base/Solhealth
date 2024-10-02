'use client';

import { useLocalStorage, useWallet } from "@solana/wallet-adapter-react";
import React, { useEffect, } from "react";
import { useRouter } from "next/navigation";

const ProtectedRoute = ( { children } : {
    children: React.ReactNode
}) => {

    const { connected, publicKey } = useWallet();
    const router = useRouter();
    const [value, setValue] = useLocalStorage<null | string | undefined>('wallet', null)

    useEffect(()=>{
        setValue(publicKey?.toString())
    }, [connected])
    // if(isLoading && value === null) return <LoadingPage />
    // console.log(value)
    if(value === undefined)  router.push('/signup')
    if(value) router.push('/')
    
  return (
    <main>
        {children}
    </main>
  )
}

export default ProtectedRoute