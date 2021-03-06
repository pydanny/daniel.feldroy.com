import Head from "next/head";
import Image from "next/image";
import styles from "./layout.module.css";
import utilStyles from "../styles/utils.module.css";
import Link from "next/link";

const name = "Daniel Roy Greenfeld";
export const siteTitle = "Daniel Roy Greenfeld";

function TopLinks() {
  return (
    <p>
      <Link href="/about">
        <a>About</a>
      </Link>{" "}
      |{" "}
      <Link href="/posts">
        <a>Articles</a>
      </Link>{" "}
      |{" "}
      <Link href="/books">
        <a>Books</a>
      </Link>{" "}
      |{" "}
      <Link href="/jobs">
        <a>Jobs</a>
      </Link>{" "}
      |{" "}
      <Link href="/news">
        <a>News</a>
      </Link>{" "}
      |{" "}
      <Link href="/tags">
        <a>Tags</a>
      </Link>
    </p>
  );
}

export default function Layout({ children, home, meta = {} }) {
  const date = new Date();
  const copyright = `All rights reserved ${date.getFullYear()}, Daniel Roy Greenfeld`;
  return (
    <div className={styles.container}>
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
        <title>{meta.title ? meta.title : "Daniel Roy Greenfeld"}</title>
        <meta
          content={
            meta.description
              ? meta.description
              : "Inside the head of Daniel Roy Greenfeld"
          }
          name="description"
        />
        <meta
          content={
            meta.description
              ? meta.description
              : "Inside the head of Daniel Roy Greenfeld"
          }
          name="twitter:description"
        />
        <meta property="og:type" content="website" />
        <meta property="og:site_name" content="Daniel Roy Greenfeld" />
        <meta
          property="og:url"
          content={meta.og_url ? meta.og_url : "https://daniel.feldroy.com"}
        />
        <meta name="twitter:site" content="@pydanny" />
        <meta name="twitter:creator" content="@pydanny" />
        <meta
          name="twitter:title"
          content={meta.title ? meta.title : "Daniel Roy Greenfeld"}
        />
        twitter:image
        {meta.image ? (
          <>
            <meta
              property="og:image"
              content={`https://daniel.feldroy.com${meta.image}`}
            />
          </>
        ) : (
          <>
            <meta
              property="og:image"
              content="https://daniel.feldroy.com/images/profile.jpg"
            />
          </>
        )}
        {meta.twitter_image ? (
          <meta
            name="twitter:image"
            content={`https://daniel.feldroy.com${meta.twitter_image}`}
          />
        ) : (
          <meta
            name="twitter:image"
            content="https://daniel.feldroy.com/images/profile.jpg"
          />
        )}
      </Head>
      <header className={styles.header}>
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
            <h1 className={utilStyles.heading2Xl}>{name}</h1>
            <p>Inside the head of Daniel Roy Greenfeld</p>
            <TopLinks />
          </>
        ) : (
          <>
            <Link href="/">
              <a>
                <Image
                  priority
                  src="/images/profile.jpg"
                  className={utilStyles.borderCircle}
                  height={108}
                  width={108}
                  alt={name}
                />
              </a>
            </Link>
            <h2 className={utilStyles.headingLg}>
              <Link href="/">
                <a>{name}</a>
              </Link>
            </h2>
            <TopLinks />
          </>
        )}
      </header>
      <main>{children}</main>
      {!home && (
        <div className={styles.backToHome}>
          <Link href="/">
            <a>??? Back to home</a>
          </Link>
        </div>
      )}
      <footer className={styles.footer}>
        <p>
          <a href="https://twitter.com/pydanny">Twitter</a> |{" "}
          <a href="/feeds/atom.xml">Atom Feed</a>
        </p>
        <p>{copyright}</p>
      </footer>
    </div>
  );
}
