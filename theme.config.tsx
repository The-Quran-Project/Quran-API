import { useRouter } from "next/router";
import { DocsThemeConfig } from "nextra-theme-docs";

const config: DocsThemeConfig = {
  i18n: [{ locale: "en", text: "English" }],
  useNextSeoProps() {
    const { asPath } = useRouter();
    if (asPath !== "/") {
      return {
        titleTemplate: "%s", // Sets the title to just the page name, no suffix
      };
    }
    return {
      title: "Quran API - Quran For Everyone",
    };
  },
  banner: {
    key: "tafsir",
    dismissible: true,
    text: (
      <a href="/getting-started/get-tafsir">
        🎉 Tafsir of each verse is now available.{" "}
        <span className="text-blue-500">See Here →</span>
      </a>
    ),
  },
  logo: (
    <span className="logo">
      <img src="/logo.svg" width={30} height={30} alt="Quran API Logo" />
      <span>Quran API</span>
    </span>
  ),
  project: {
    link: "https://github.com/The-Quran-Project/Quran-API",
  },
  chat: {
    link: "https://t.me/AlQuranDiscussion",
    icon: (
      <svg
        viewBox="0 0 24 24"
        width={24}
        height={24}
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill="currentColor"
          d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"
        />
      </svg>
    ),
  },
  docsRepositoryBase:
    "https://github.com/The-Quran-Project/Quran-API/tree/main/",
  footer: {
    text: `© Quran API 2023 - ${new Date().getFullYear()}. All rights reserved`,
  },
  head: function useHead() {
    const socialCard = "/cover.png";

    return (
      <>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta httpEquiv="Content-Language" content="en" />
        <meta name="og:image" content={socialCard} />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:image" content={socialCard} />
        <meta name="twitter:site:domain" content="quranapi.pages.dev" />
        <meta name="twitter:url" content="https://quranapi.pages.dev" />
        <meta name="msapplication-TileColor" content="#000" />
        <meta name="theme-color" content="#000" />
        <meta name="apple-mobile-web-app-title" content="Quran API" />
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
        <link
          rel="icon"
          href="/favicon-dark.svg"
          type="image/svg+xml"
          media="(prefers-color-scheme: dark)"
        />
        <meta
          name="google-site-verification"
          content="WPPXho-ehsTzL41OYAECiVP8ilWMxfxjHtHwQUsu1FU"
        />
      </>
    );
  },
  sidebar: {
    titleComponent({ title, type }) {
      if (type === "separator") {
        return <span className="cursor-default">{title}</span>;
      }
      return <>{title}</>;
    },
    defaultMenuCollapseLevel: 2,
    toggleButton: true,
  },
  toc: {
    backToTop: true,
  },
};

export default config;
