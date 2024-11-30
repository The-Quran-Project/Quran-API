const GetBaseUrl = ({ suffix = "" }) => {
    const BASE_URL = (process.env.BASE_URL || "http://127.0.0.1:3000") + suffix;
    return (
      <a href={BASE_URL} className="text-blue-400">
        <code>{BASE_URL}</code>
      </a>
    );
  };
  
  export default GetBaseUrl;
  