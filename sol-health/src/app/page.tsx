
import Chat from "./components/Chat";
import LoadingPage from "./components/LoadingPage";
import SignUp from "./components/SignUp";
// import TransferSol from "./components/TransferValue";
import WalletContextProvider from "./components/WalletContextProvider";

export default function Home() {
  return (
    <div className="">
      {/* <TransferSol /> */}
      {/* <WalletContextProvider>
        <Chat />
      </WalletContextProvider> */}
      {/* <LoadingPage /> */}
      <SignUp />
    </div>
  );
}
