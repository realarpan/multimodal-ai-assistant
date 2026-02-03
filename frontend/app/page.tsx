import Link from "next/link";

export default function HomePage() {
  return (
    <div className="flex-1 flex flex-col items-center justify-center gap-4">
      <h2 className="text-2xl font-semibold">Real-Time Multimodal AI Assistant</h2>
      <p className="text-slate-300 max-w-xl text-center">
        Upload images, audio, or text and chat with an AI that can analyze scenes, transcribe speech,
        reason over content, and generate executable Python code.
      </p>
      <div className="flex gap-4">
        <Link href="/upload" className="px-4 py-2 bg-emerald-500 text-black rounded-md">
          Get started
        </Link>
        <a
          href="https://github.com/your-username/multimodal-ai-assistant"
          className="px-4 py-2 border border-slate-600 rounded-md"
        >
          View on GitHub
        </a>
      </div>
    </div>
  );
}
