import { useRouter } from "next/router"
import { DocsThemeConfig, useConfig } from "nextra-theme-docs"

const config: DocsThemeConfig = {
  logo: <b>Quran API</b>,
  project: {
    link: "https://github.com/Nusab19/Quran-API",
  },
  chat: {
    link: "https://discordid.netlify.app/?id=804035616420397086",
  },
  docsRepositoryBase: "https://github.com/Nusab19/Quran-API/tree/main/",
  footer: {
    text: `© Quran API 2023 - ${new Date().getFullYear()}. All rights reserved`
  },
  head: function useHead() { // TODO: Change the meta tag values
    const { title } = useConfig()
    const { route } = useRouter()
    console.log(title, route)

    const socialCard =
      route === '/' || !title
        ? 'https://nextra.site/og.jpeg'
        : `https://nextra.site/api/og?title=${title}`

    return (
      <>
        <meta name="msapplication-TileColor" content="#000" />
        <meta name="theme-color" content="#000" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta httpEquiv="Content-Language" content="en" />
        <meta
          name="description"
          content="Make beautiful websites with Next.js & MDX."
        />
        <meta
          name="og:description"
          content="Make beautiful websites with Next.js & MDX."
        />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:image" content={socialCard} />
        <meta name="twitter:site:domain" content="nextra.site" />
        <meta name="twitter:url" content="https://nextra.site" />
        <meta
          name="og:title"
          content={title ? title + ' – Nextra' : 'Nextra'}
        />
        <meta name="og:image" content={socialCard} />
        <meta name="apple-mobile-web-app-title" content="Nextra" />
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
        <link rel="icon" href="/favicon.png" type="image/png" />
        <link
          rel="icon"
          href="/favicon-dark.svg"
          type="image/svg+xml"
          media="(prefers-color-scheme: dark)"
        />
        <link
          rel="icon"
          href="/favicon-dark.png"
          type="image/png"
          media="(prefers-color-scheme: dark)"
        />
      </>
    )
  },
  sidebar: {
    titleComponent({ title, type }) {
      if (type === 'separator') {
        return <span className="cursor-default">{title}</span>
      }
      return <>{title}</>
    },
    defaultMenuCollapseLevel: 2,
    toggleButton: true
  },
  toc: {
    backToTop: true
  },
  banner: {
    dismissible: true,
    text: function Banner() {
      return (<a href="https://github.com/Nusab19/Quran-API" target="_blank">
        ⚠ This API is still in development! →</a>)
    }
  }
}

export default config;
