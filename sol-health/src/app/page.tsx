
import Chat from "./components/Chat";
import WalletContextProvider from "./components/WalletContextProvider";

export default function Home() {
  return (
    <div className="">
      <WalletContextProvider>
        <Chat />
      </WalletContextProvider>
    </div>
  );
}
