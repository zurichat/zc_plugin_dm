import { SubscribeToChannel } from '@zuri/utilities';
export default function centrifugeClient(room_id, centrifigoCallback) {
  return SubscribeToChannel(room_id, centrifigoCallback);
}
