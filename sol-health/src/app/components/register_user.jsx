const handleDeposit = async () => {
    if (!window.solana) {
        alert('Please Install Phantom or Solflare.');
        return;
    }

    try {
        // if user is connected then save the address in the database
        //  we'll have to implement a better check later because generating wallet is infinite so users may never exhaust their credits
        // 1: extract user address
        const userWallet = window.solana.publicKey.toString();
        ////////////////////////////////////////////////
        // here now you input the database code to reg user
        
        alert('Registration successful!');
    } catch (error) {
        console.error('Registration failed:', error);
        alert('Registration failed.');
    }
};