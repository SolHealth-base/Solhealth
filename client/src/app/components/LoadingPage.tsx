import localFont from "next/font/local";
import Image from "next/image";
import Loader from "./Loader";

const mightyMarine = localFont({
    src: "../fonts/GeistMonoVF.woff",
    variable: "--font-geist-mono",
    weight: "100 900",
  });
const LoadingPage = () => {
  return (
    <div className={`${mightyMarine.variable} antialiased bg-[#040715] h-[100vh] w-[100vw] flex items-center justify-center`}>
      <div>
        <Image 
          src={'/cross.svg'}
          alt="cross icon"
          height={89}
          width={99}
          className="mx-auto mb-[42px]"
        />
        <h3 className="text-[50px] text-[#FFFFFF] text-center font-medium leading-[30px] mb-7">Solhealth</h3>
        <Loader />
      </div>
    </div>
  )
}

export default LoadingPage