"use client";

type Props = { code: string };

export default function CodeEditor({ code }: Props) {
  return (
    <div className="flex flex-col h-full">
      <h3 className="font-semibold mb-2">Generated Python code</h3>
      <textarea
        className="flex-1 w-full bg-slate-900 border border-slate-700 rounded-md text-xs p-2 font-mono"
        value={code}
        readOnly
      />
      <p className="text-xs text-slate-500 mt-1">
        Copy this into a local Python file and run with your data to reproduce the visualization.
      </p>
    </div>
  );
}
