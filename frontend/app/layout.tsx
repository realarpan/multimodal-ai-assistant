import "./globals.css";
import { ReactNode } from "react";

export const metadata = {
  title: "Real-Time Multimodal AI Assistant",
  description: "Vision + Audio + Text + Code"
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100">
        <div className="min-h-screen flex flex-col">
          <header className="border-b border-slate-800 p-4 flex items-center justify-between">
            <h1 className="font-semibold">Multimodal AI Assistant</h1>
            <span className="text-xs text-slate-400">Built with ❤️ for AI/ML 2026</span>
          </header>
          <main className="flex-1 flex">{children}</main>
        </div>
      </body>
    </html>
  );
}
