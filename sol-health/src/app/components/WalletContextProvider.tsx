'use client'
import React, { createContext, useContext, useMemo, ReactNode, useEffect } from 'react';
import { ConnectionProvider, WalletProvider, useLocalStorage, useWallet as useSolanaWallet } from '@solana/wallet-adapter-react';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import { WalletModalProvider, WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { clusterApiUrl } from '@solana/web3.js';

import '@solana/wallet-adapter-react-ui/styles.css';

// Define the type for the WalletContext
type WalletContextType = ReturnType<typeof useSolanaWallet> | null;

// Create a context to store and manage wallet data with the correct type
const WalletContext = createContext<WalletContextType>(null);

// Define props for the WalletContextProvider component
interface WalletContextProviderProps {
    children: ReactNode;
}

// Create a provider component to wrap around the app and provide wallet functionality
const WalletContextProvider: React.FC<WalletContextProviderProps> = ({ children }) => {
    
    // Define the network for the Solana wallet adapter (Devnet in this case, which is for development and testing purposes)
    const network = WalletAdapterNetwork.Devnet;
    const [walletAddress, setIsWallet] = useLocalStorage<null | string>('wallet-address', null)

    // Create the endpoint (URL) for connecting to the Solana network based on the selected network
    // useMemo is used to memoize the result and recompute it only if the `network` value changes
    const endpoint = useMemo(() => clusterApiUrl(network), [network]);

    // Set up the list of wallets available to the user (only Phantom Wallet in this case)
    // useMemo is used to ensure the list is recomputed only if the `network` value changes
    const wallets = useMemo(() => [
        new PhantomWalletAdapter(), // Phantom Wallet is one of the most popular Solana wallets
    ], [network]);

    

    // Retrieve the current wallet using the Solana wallet adapter hook `useSolanaWallet`
    const wallet = useSolanaWallet();
    
    useEffect(()=>{
        if(!wallet.connected){
            console.log('false')
        }
    }, [])

    // useEffect(()=>{
    //     if(!wallet.connected){
    //         console.log('false')
    //     }
    // }, [])
    // Return the wallet context provider, which wraps the child components with wallet functionality
    return (
        // Provide a connection to the Solana network (Devnet in this case)
        <ConnectionProvider endpoint={endpoint}>

            {/* Provide the wallet functionality with the list of available wallets */}
            <WalletProvider wallets={wallets} autoConnect>

                {/* Provide a modal for selecting wallets (used by the WalletMultiButton) */}
                <WalletModalProvider>

                    {/* Provide the wallet context to the entire app, so child components can access wallet functionality */}
                    <WalletContext.Provider value={wallet}>
                        {/* Render child components (the rest of your app) */}
                        {children}

                        {/* Add a wallet connect button to the top right corner of the app */}
                        <div className="fixed top-0 right-0 m-4">
                            <WalletMultiButton />  {/* Button that allows users to connect/disconnect their wallet */}
                        </div>
                    </WalletContext.Provider>
                </WalletModalProvider>
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Hook to access the wallet context in any component within the app
export const useWallet = (): WalletContextType => {
    const context = useContext(WalletContext);  // Access the context value

    // If the context is not within a WalletContextProvider, throw an error
    if (context === null) {
        throw new Error('useWallet must be used within a WalletContextProvider');
    }

    // Return the current wallet context (this provides access to wallet-related data and functions)
    return context;
};

// Export the WalletContextProvider as the default export, so it can be imported and used to wrap the entire app
export default WalletContextProvider;
