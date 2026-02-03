"use client";

import { useState } from "react";
import axios from "axios";

const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

type Props = {
  onUploaded: (fileId: string, fileType: string) => void;
};

export default function UploadDropzone({ onUploaded }: Props) {
  const [progress, setProgress] = useState<number>(0);
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setError(null);
    setUploading(true);
    setProgress(0);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(`${backendUrl}/upload`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
        onUploadProgress: (evt) => {
          if (evt.total) {
            setProgress(Math.round((evt.loaded * 100) / evt.total));
          }
        }
      });
      onUploaded(res.data.file_id, res.data.file_type);
    } catch (err: any) {
      setError(err?.response?.data?.detail || "Upload failed");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="space-y-4">
      <h3 className="font-semibold">Upload media</h3>
      <input type="file" onChange={handleFileChange} className="text-sm" />
      {uploading && (
        <div className="w-full bg-slate-800 rounded-full h-2">
          <div className="bg-emerald-500 h-2 rounded-full" style={{ width: `${progress}%` }} />
        </div>
      )}
      {error && <p className="text-red-400 text-sm">{error}</p>}
    </div>
  );
}
