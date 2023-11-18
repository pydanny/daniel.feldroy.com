import Head from "next/head";
import Link from "next/link";

export default function Metatags({ meta = {} }) {
  return (
    <Head>
      <title>{meta.title ? meta.title : "Daniel Roy Greenfeld"}</title>
      <meta
        content={
          meta.description
            ? meta.description
            : "Inside the head of Daniel Roy Greenfeld"
        }
        name="description"
        key="description"
      />
      <meta
        content={
          meta.description
            ? meta.description
            : "Inside the head of Daniel Roy Greenfeld"
        }
        name="twitter:description"
        key="twitter:description"
      />
      <meta property="og:type" key="og:type" content="website" />
      <meta
        property="og:site_name"
        key="og:site_name"
        content="Daniel Roy Greenfeld"
      />
      <meta
        property="og:url"
        key="og:url"
        content={meta.og_url ? meta.og_url : "https://daniel.feldroy.com"}
      />
      {/* <meta name="twitter:site" key="twitter:site" content="@pydanny" /> */}
      <meta name="twitter:creator" key="twitter:creator" content="@pydanny" />
      <meta name="twitter:card" content="summary" />
      <meta
        name="twitter:title"
        key="twitter:title"
        content={meta.title ? meta.title : "Daniel Roy Greenfeld"}
      />
      {meta.image ? (
        <>
          <meta
            property="og:image"
            key="og:image"
            content={`https://daniel.feldroy.com${meta.image}`}
          />
        </>
      ) : (
        <>
          <meta
            property="og:image"
            key="og:image"
            content="https://daniel.feldroy.com/images/profile.jpg"
          />
        </>
      )}
      {meta.twitter_image ? (
        <meta
          name="twitter:image"
          key="twitter:image"
          content={`https://daniel.feldroy.com${meta.twitter_image}`}
        />
      ) : (
        <meta
          name="twitter:image"
          key="twitter:image"
          content="https://daniel.feldroy.com/images/profile.jpg"
        />
      )}
    </Head>
  );
}
