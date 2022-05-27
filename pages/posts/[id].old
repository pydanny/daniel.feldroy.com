import Link from "next/link";

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
    og_url: `https://daniel.feldroy.com/posts/${postData.id}`,
  };
  return (
    <>
      <article>
        <h1 className={utilStyles.headingXl}>{postData.title}</h1>
        <div className={utilStyles.lightText}>
          <MyDate dateString={postData.date} />
        </div>
        <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
        <section>
          <hr />
          Tags:
          {postData.tags.map((tag) => (
            <span key={tag}>
              {" "}
              <Link href={`/tags/${tag}`}>{tag}</Link>
            </span>
          ))}
        </section>
      </article>
    </>
  );
}
