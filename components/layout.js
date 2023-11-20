import Head from "next/head";
import Image from "next/image";
import utilStyles from "../festyles/utils.module.css";
import Link from "next/link";
import Metatags from "./metatags";

const name = "Daniel Roy Greenfeld";
export const siteTitle = "Daniel Roy Greenfeld";

function TopLinks() {
  return (
    <p>
      <Link href="/about">
        About
      </Link>{" "}
      |{" "}
      <Link href="/posts">
        Articles
      </Link>{" "}
      |{" "}
      <Link href="/books">
        Books
      </Link>{" "}
      |{" "}
      <Link href="/jobs">
        Jobs
      </Link>{" "}
      |{" "}
      <Link href="/news">
        News
      </Link>{" "}
      |{" "}
      <Link href="/tags">
        Tags
      </Link>
    </p>
  );
}

export default function Layout({ children, home, meta = {} }) {
  const date = new Date();
  const copyright = `All rights reserved ${date.getFullYear()}, Daniel Roy Greenfeld`;
  return (
    <>
      <Head>
        <link
          href="/favicon/apple-touch-icon.png"
          rel="apple-touch-icon"
          sizes="180x180"
        />
        <link
          href="/favicon/favicon-32x32.png"
          rel="icon"
          sizes="32x32"
          type="image/png"
        />
        <link
          href="/favicon/favicon-16x16.png"
          rel="icon"
          sizes="16x16"
          type="image/png"
        />
        <link href="/favicon/site.webmanifest" rel="manifest" />
        <link
          color="#5bbad5"
          href="/favicon/safari-pinned-tab.svg"
          rel="mask-icon"
        />
      </Head>
      <Metatags meta={meta} />
      <header>
        {home ? (
          <>
            <Image
              priority
              src="/images/profile.jpg"
              className={utilStyles.borderCircle}
              height={144}
              width={144}
              alt={name}
            />
            <h1>{name}</h1>
            <p>Inside the head of Daniel Roy Greenfeld</p>
            <TopLinks />
          </>
        ) : (
          <>
            {meta.notoplinks ? (
              <></>
            ) : (
              <>
                <Link href="/">

                  <Image
                    priority
                    src="/images/profile.jpg"
                    className={utilStyles.borderCircle}
                    height={108}
                    width={108}
                    alt={name}
                  />

                </Link>
                <h2>
                    {name}
                </h2>
                <TopLinks />
              </>
            )}
          </>
        )}
      </header>
      <main>{children}</main>
      {!home && (
        <div>
          <Link href="/">
            ← Back to home
          </Link>
        </div>
      )}
      <footer>
        <p>
          <a href="https://fosstodon.org/@danielfeldroy">Mastodon</a> |{" "}
          <a href="https://www.linkedin.com/in/danielfeldroy/">LinkedIn</a> |{" "}
          <a href="https://twitter.com/pydanny">Twitter</a> |{" "}
          <a href="/feeds/atom.xml">Atom Feed</a>
        </p>
        <p>{copyright}</p>
      </footer>
    </>
  );
}
