import Head from "next/head";
import Link from "next/link";
import Layout, { siteTitle } from "../../components/layout";
import utilStyles from "../../festyles/utils.module.css";
import MyDate from "../../components/date";

import { getSortedPostsData } from "../../lib/stories";

export async function getStaticProps() {
  const allPostsData = getSortedPostsData();

  return {
    props: {
      allPostsData,
    },
  };
}

export default function Home({ allPostsData }) {
  return (
    <Layout>
      <Head>
        <title>Daniel Roy Greenfeld</title>
        <meta
          name="description"
          content="Inside the head of Daniel Roy Greenfeld"
        />
        <meta name="og:title" content="Daniel Roy Greenfeld" />
        <meta property="og:site_name" content="Daniel Roy Greenfeld" />

        <meta
          property="og:image"
          content="https://daniel.feldroy.com/images/profile.jpg"
        />
        {/* Twitter card tags */}
        <meta name="twitter:title" content="Daniel Roy Greenfeld" />
        <meta
          name="twitter:image"
          content="https://daniel.feldroy.com/images/profile.jpg"
        />
      </Head>
      <p>
        Our short stories are a mixture of humor, joy, fantasy, horror, and
        adventure, with a bit of space travel and fried chicken thrown in.
      </p>
      <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
        <ul className={utilStyles.list}>
          {allPostsData.map(({ id, date, title, description, author }) => (
            <li className={utilStyles.listItem} key={id}>
              <Link href={`/stories/${id}`}>
                {title} 
              </Link>
              <br />
              <small>{author}</small>
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
    </Layout>
  );
}
