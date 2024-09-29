
import Chat from "./components/Chat";
// import TransferSol from "./components/TransferValue";
import WalletContextProvider from "./components/WalletContextProvider";

export default function Home() {
  return (
    <div className="">
      {/* <TransferSol /> */}
      <WalletContextProvider>
        <Chat />
      </WalletContextProvider>
    </div>
  );
}
