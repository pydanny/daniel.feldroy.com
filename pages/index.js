import Link from "next/link";
import utilStyles from "../styles/utils.module.css";
import MyDate from "../components/date";

import { getSortedPostsData } from "../lib/posts";
import generateRssFeed from "../lib/rss";

export async function getStaticProps() {
  const allPostsData = getSortedPostsData();
  const mostRecentPosts = allPostsData.slice(0, 3);

  const topIds = [
    "code-code-code",
    "thirty-minute-rule",
    "whats-the-best-thing-about-working-for-octopus-energy-part-1",
    "i-married-audrey-roy",
  ];
  const topPosts = allPostsData.filter(
    (post) => topIds.indexOf(post.id) !== -1
  );

  // render blog posts
  await generateRssFeed("django");
  await generateRssFeed("python");
  await generateRssFeed("");
  return {
    props: {
      mostRecentPosts,
      topPosts,
    },
  };
}

export default function Home({ mostRecentPosts, topPosts }) {
  return <>
    <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
      <h2 className={utilStyles.headingLg}>Recent Writings</h2>
      <ul className={utilStyles.list}>
        {mostRecentPosts.map(({ id, date, title, description }) => (
          <li className={utilStyles.listItem} key={id}>
            <Link href={`/posts/${id}`}>
              {title}
            </Link>
            <br />
            {description && (
              <>
                <small className={utilStyles.lightText}>{description}</small>
                <br />
              </>
            )}
            <small className={utilStyles.lightText}>
              <MyDate dateString={date} />
            </small>
          </li>
        ))}
      </ul>
    </section>

    <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
      <h2 className={utilStyles.headingLg}>Popular Articles</h2>
      <ul className={utilStyles.list}>
        {topPosts.map(({ id, date, title, description }) => (
          <li className={utilStyles.listItem} key={id}>
            <Link href={`/posts/${id}`}>
              {title}
            </Link>
            <br />
            {description && (
              <>
                <small className={utilStyles.lightText}>{description}</small>
                <br />
              </>
            )}
            <small className={utilStyles.lightText}>
              <MyDate dateString={date} />
            </small>
          </li>
        ))}
      </ul>
    </section>
    <h2 className={utilStyles.headingLg}>
      <Link href="/posts">
        Full Archive →
      </Link>
    </h2>
  </>;
}
