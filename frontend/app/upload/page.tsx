"use client";

import { useState } from "react";
import UploadDropzone from "../../components/UploadDropzone";
import ChatInterface from "../../components/ChatInterface";
import CodeEditor from "../../components/CodeEditor";

export default function UploadPage() {
  const [fileId, setFileId] = useState<string | null>(null);
  const [fileType, setFileType] = useState<string | null>(null);
  const [generatedCode, setGeneratedCode] = useState<string>("");

  return (
    <div className="flex flex-1">
      <div className="w-1/3 border-r border-slate-800 p-4">
        <UploadDropzone
          onUploaded={(id, type) => {
            setFileId(id);
            setFileType(type);
          }}
        />
      </div>
      <div className="w-1/3 border-r border-slate-800 p-4">
        <ChatInterface fileId={fileId} fileType={fileType} onCodeReceived={setGeneratedCode} />
      </div>
      <div className="w-1/3 p-4">
        <CodeEditor code={generatedCode} />
      </div>
    </div>
  );
}
