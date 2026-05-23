const DEFAULT_API_BASE =
  typeof window === "undefined"
    ? "http://localhost:8000"
    : window.location.origin;

const normalizeBase = (value) => {
  if (!value) return DEFAULT_API_BASE;
  return value.replace(/\/+$/, "");
};

export const API_BASE_URL = normalizeBase(
  import.meta.env.VITE_API_BASE_URL || DEFAULT_API_BASE,
);

const normalizePath = (path = "") => {
  if (!path) return "";
  return path.startsWith("/") ? path : `/${path}`;
};

export function apiUrl(path = "") {
  return `${API_BASE_URL}${normalizePath(path)}`;
}

export function controlesUrl(path = "") {
  const suffix = path ? `/controles${normalizePath(path)}` : "/controles";
  return `${API_BASE_URL}${suffix}`;
}

export function mediaUrl(path = "") {
  if (!path) return "";
  if (/^https?:\/\//i.test(path)) return path;
  return `${API_BASE_URL}${normalizePath(path)}`;
}
