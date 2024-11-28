import * as React from "react"

import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger,
} from "@/components/ui/drawer"
import ConnectWallet from "./ConnectWallet"

export function DrawerDemo() {

  return (
    <Drawer>
      <DrawerTrigger asChild>
        <button className='max-w-[350px] p-2.5 rounded-[10px] bg-[#001354] w-[60%] text-[#FFFFFF]'>Get Started</button>
      </DrawerTrigger>
      <DrawerContent className="bg-[#001354] outline-none text-[#FFFFFF]">
        <div className="mx-auto w-full max-w-sm">
          <DrawerHeader>
            <DrawerTitle className="text-[40px] font-normal leading-[40px] mb-[15px]">Welcome back</DrawerTitle>
            <DrawerDescription className="text-xl text-[#FFFFFF] leading-[25px] font-normal mb-[43px]">Connect wallet to get
            fast responses </DrawerDescription>
          </DrawerHeader>
          <div className="w-full pb-0 mx-auto text-center">
            {/* connect button rendered here */}
            <ConnectWallet />
            {/* <WalletMultiButton /> */}
          </div>
          <DrawerFooter>
            {/* <Button>Submit</Button> */}
            <DrawerClose asChild>
              {/* <WalletMultiButton /> */}
        
              <button className='max-w-[350px] p-2.5 rounded-[10px] bg-[#FFFFFF] w-[60%] mx-auto text-[#001354] mb-6'>Cancel</button>
            </DrawerClose>
          </DrawerFooter>
        </div>
      </DrawerContent>
    </Drawer>
  )
}
