import Image from "next/image";
import Link from "next/link";
import Metatags from "../../components/metatags";

import { getAllPostIds, getPostData } from "../../lib/posts";
import MyDate from "../../components/date";
import utilStyles from "../../styles/utils.module.css";
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

export default function Post({ postData }) {
  const domain = "https://daniel.feldroy.com/";
  const meta = {
    title: postData.title,
    description: postData.description,
    image: postData.image,
    twitter_image: postData.twitter_image,
    og_url: `https://daniel.feldroy.com/posts/${postData.id}`,
  };
  return <>
    <Metatags meta={meta} />
    <article>
      <h1 className={utilStyles.headingXl}>{postData.title}</h1>
      <div className={utilStyles.lightText}>
        <MyDate dateString={postData.date} />
      </div>
      <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
      {postData.tags.filter((tag) => tag !== "TIL").length > 0 && (
        <>
        <hr />
          <section className={utilStyles.center}>
            <Link href="/tags/TIL">
              <Image src="/logos/til-1.png" name="TIL Logo" width="288" height="288" />
            </Link>
          </section>
        </>
      )}
      <section>
        <hr />
        Tags:
        {postData.tags.map((tag) => (
          <span key={tag}>
            {" "}
            <Link href={`/tags/${tag}`} legacyBehavior>{tag}</Link>
          </span>
        ))}
      </section>
    </article>
  </>;
}
