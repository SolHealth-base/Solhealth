'use client';

// import { useLocalStorage } from "@solana/wallet-adapter-react";
import { useEffect } from "react";
// import { useLocalStorage } from "../lib/hooks/use-local-storage";



const Auth = ({children}: {
    children: React.ReactNode
}) => {
    // const [value, setValue] = useLocalStorage('wallet', '')
    
    // if(value === null || !value) return null
    
  return (
    <div>
        {/* <button onClick={()=> setValue('')}>Set Value</button> */}
        {children}
    </div>
  )
}

export default Auth