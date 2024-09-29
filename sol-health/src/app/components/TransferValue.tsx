// This works with the code i sent before
//::ChatGPT made contributions to this code a bit. But it has been tested and works perf..
// hit me up if you encounter an issue , I know you can fix it tho..
'use client'
import React, { useState, useCallback } from 'react';
import { useConnection, useWallet } from '@solana/wallet-adapter-react';
import { Keypair, PublicKey, SystemProgram, Transaction } from '@solana/web3.js';
import { WalletNotConnectedError } from '@solana/wallet-adapter-base';

const TransferSol = () => {
    const { connection } = useConnection();
    const { publicKey, sendTransaction } = useWallet();
    const [amount, setAmount] = useState('');

    const onClick = useCallback(async () => {
        if (!publicKey) throw new WalletNotConnectedError();
      

        // custom address for receiving subscriptions on our systems
        const receiverAddress = "4E84Vpv4G27TW7pWjwNgA6Vz9VMbeVJvWg8VxWZfZhWC"

        const lamports = parseFloat(amount) * 1e9; // Convert SOL to lamports
        const receiver = new PublicKey(receiverAddress);

        const transaction = new Transaction().add(
            SystemProgram.transfer({
                fromPubkey: publicKey,
                toPubkey: receiver,
                lamports,
            })
        );

        if (!receiverAddress || !amount) {
            alert('Please provide a valid address and amount.');
            return;
        }

        const {
            context: { slot: minContextSlot },
            value: { blockhash, lastValidBlockHeight }
        } = await connection.getLatestBlockhashAndContext();

        const signature = await sendTransaction(transaction, connection, { minContextSlot });

        await connection.confirmTransaction({ blockhash, lastValidBlockHeight, signature });
        window.alert('Transaction successful! Signature: ' + signature);
        console.log("trx:", signature);

        // here we'll sort how long user subscribed based on payment, we may have to restrict it to minimum of 1month subscription

    }, [publicKey, sendTransaction, connection, amount]);

    return (
        <div className="transfer-sol">
            <h2>Make Payment in Sol to Subscribe</h2>
            {/* please set minimum here brotha */}
            <input
                type="number"
                placeholder="Enter amount in SOL"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                className="mt-2 p-2 border border-gray-300 rounded"
            />
            <button
                onClick={onClick}
                className="mt-4 px-6 py-3 bg-blue-500 text-white rounded-full shadow-lg hover:bg-blue-600 focus:outline-none"
            >
                {/* name of button, you can change it to whatever */}
                PAY
            </button>
        </div>
    );
};

export default TransferSol;
