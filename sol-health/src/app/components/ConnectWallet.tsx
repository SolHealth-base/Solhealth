'use client';

import { WalletAdapterNetwork } from "@solana/wallet-adapter-base";
import { useWallet } from "@solana/wallet-adapter-react";
import { PhantomWalletAdapter } from "@solana/wallet-adapter-wallets";
import { clusterApiUrl } from "@solana/web3.js";
import { useMemo } from "react";

const ConnectWallet = () => {
    const network = WalletAdapterNetwork.Devnet;
    
    const endpoint = useMemo(() => clusterApiUrl(network), [network]);

    // Set up the list of wallets available to the user (only Phantom Wallet in this case)
    // useMemo is used to ensure the list is recomputed only if the `network` value changes
    const wallets = useMemo(() => [
        new PhantomWalletAdapter(), // Phantom Wallet is one of the most popular Solana wallets
    ], [network]);

    

    // Retrieve the current wallet using the Solana wallet adapter hook `useSolanaWallet`
    const wallet = useWallet();

    const handleClick = async ()=> {
        console.log('hi')
        await wallet.select(wallets[0].name);
        await wallet.connect()
        await wallet.publicKey?.toString();
    
    }
    // console.log(wallet.connected)
  return (
    <button onClick={handleClick} className='max-w-[350px] p-2.5 rounded-[10px] bg-[#FFFFFF] w-[60%] mx-auto text-[#001354]'>Connect Wallet</button>
  )
}

export default ConnectWallet