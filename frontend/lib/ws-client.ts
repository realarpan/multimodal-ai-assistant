export function createWebSocketClient() {
  const url = process.env.NEXT_PUBLIC_WEBSOCKET_URL || "ws://localhost:8000/ws";
  const ws = new WebSocket(url);
  return ws;
}
