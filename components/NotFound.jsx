import { usePathname } from "next/navigation";
import { NotFoundPage } from "nextra-theme-docs";
import ApiPage from "./ApiPage";

const NotFound = () => {
  const pathname = usePathname();
  if (pathname == "/api" || pathname == "/api/") {
    return <ApiPage />;
  }
  return (
    <div suppressHydrationWarning>
      <h1 className="text-4xl font-bold my-5">Path not found</h1>
      This page does not exist. Please check the URL or go back to the{" "}
      <a href="/" className="text-blue-500">
        homepage.
      </a>
      <br />
      <br />
      <br />
      <NotFoundPage />
    </div>
  );
};

export default NotFound;
