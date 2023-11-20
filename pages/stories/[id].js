import Head from "next/head";
import Link from "next/link";

import Layout from "../../components/layout";
import { getAllPostIds, getPostData } from "../../lib/stories";
import MyDate from "../../components/date";
import utilStyles from "../../festyles/utils.module.css";
import "highlight.js/styles/gml.css";

export async function getStaticPaths() {
  const paths = getAllPostIds();
  return {
    paths,
    fallback: false,
  };
}

export async function getStaticProps({ params }) {
  const postData = await getPostData(params.id);
  return {
    props: {
      postData,
    },
  };
}

export default function Story({ postData }) {
  const domain = "https://daniel.feldroy.com/";
  return (
    <Layout>
      <Head>
        <title>
          {postData.title} by {postData.author}
        </title>
        <meta name="description" content={postData.description} />
        <meta property="og:title" content={postData.title} />
        <meta property="og:type" content="website" />
        <meta
          property="og:url"
          content={`https://daniel.feldroy.com/stories/${postData.id}`}
        />

        {postData.description ? (
          <meta name="og:description" content={postData.description} />
        ) : (
          <meta
            name="og:description"
            content="Inside the Head of Daniel Roy Greenfeld"
          />
        )}

        {/* Twitter card tags */}
        <meta name="twitter:title" content={postData.title} />

        {postData.image ? (
          <>
            <meta
              property="og:image"
              content={`https://daniel.feldroy.com${postData.image}`}
            />
            <meta
              name="twitter:image"
              content={`https://daniel.feldroy.com${postData.image}`}
            />
          </>
        ) : (
          <>
            <meta
              property="og:image"
              content="https://daniel.feldroy.com/images/profile.jpg"
            />
            <meta
              name="twitter:image"
              content="https://daniel.feldroy.com/images/profile.jpg"
            />
          </>
        )}

        {/* Twitter card tags */}
        <meta name="twitter:description" content={postData.description} />
      </Head>
      <article>
        <div className={utilStyles.backToHome}>
          <Link href="/stories">
            ← Back to stories
          </Link>
        </div>

        <h1>{postData.title}</h1>
        <div>{postData.author}</div>
        <div className={utilStyles.lightText}>
          <MyDate dateString={postData.date} />
        </div>
        {postData.description && (
          <div>
            <small className={utilStyles.lightText}>
              {postData.description}
            </small>
            <br />
          </div>
        )}
        <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
      </article>
    </Layout>
  );
}
