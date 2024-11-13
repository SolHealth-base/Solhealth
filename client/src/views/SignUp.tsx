import Image from "next/image";
import { DrawerDemo } from "@/components/Drawer";

const SignUp = () => {
  return (
    <div className="mx-auto flex flex-col items-center justify-center">
      <div />
      <div
        style={{
          background: "linear-gradient(180deg, #FFFFFF 0%, #3C4980 88.5%)",
        }}
        className="w-[307px] mt-5 h-[307px] rounded-full flex items-center justify-center mb-[45px]"
      >
        <Image
          src={"/robot.svg"}
          alt="robot image"
          width={240}
          height={254}
          priority
        />
      </div>
      <h3 className="mb-[50px] text-[32px] font-normal leading-10 text-center text-[#FFFFFF]">
        Easily access AI Health assistant chatbot{" "}
      </h3>
      <DrawerDemo />
    </div>
  );
};

export default SignUp;
