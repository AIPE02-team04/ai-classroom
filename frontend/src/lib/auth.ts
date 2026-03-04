import { create } from "zustand";

interface User {
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  [key: string]: unknown;
}

interface AuthState {
  user: User | null;
  sessionUuid: string | null;
  isLoggedIn: boolean;
  setUser: (user: User) => void;
  clearUser: () => void;
  setSessionUuid: (uuid: string | null) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  sessionUuid: null,
  isLoggedIn: false,
  setUser: (user) => set({ user, isLoggedIn: true }),
  clearUser: () => set({ user: null, isLoggedIn: false, sessionUuid: null }),
  setSessionUuid: (uuid) => set({ sessionUuid: uuid }),
  logout: () => set({ user: null, isLoggedIn: false, sessionUuid: null }),
}));
