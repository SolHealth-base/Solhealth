import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Auth from "./components/Auth";
import WalletContextProvider from "./components/WalletContextProvider";
import ProtectedRoute from "./components/ProtectedRoute";


const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "SOLHEALTH",
  description: "A health-care system built on solana ecosystem.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-[#040715]`}
      >
        <Auth>
          <WalletContextProvider>
            <ProtectedRoute>
              {children}
            </ProtectedRoute>
          </WalletContextProvider>
        </Auth>
      </body>
    </html>
  );
}
