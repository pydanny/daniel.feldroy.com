import Link from "next/link";
import utilStyles from "../../festyles/utils.module.css";
import MyDate from "../../components/date";
import { useRouter } from "next/router";
import MiniSearch from "minisearch";

import { getSortedPostsData } from "../../lib/posts";

export async function getStaticProps() {
  const allPostsData = getSortedPostsData();
  const yearsBlogging = new Date().getFullYear() - 2005;

  return {
    props: {
      allPostsData,
      yearsBlogging,
      title: "Full archive of Daniel Roy Greenfeld",
      description: `Everything written by Daniel Roy Greenfeld for the past ${yearsBlogging} years`,
    },
  };
}

export default function Home({ allPostsData, yearsBlogging }) {
  // search setup
  const router = useRouter();
  const q = router.query.q || "";
  let postsData = allPostsData;
  if (q !== "") {
    let miniSearch = new MiniSearch({
      fields: ["id", "title", "description"], // fields to index for full-text search
      storeFields: ["id", "title", "date", "description"], // fields to return with search results
    });

    miniSearch.addAll(allPostsData);
    postsData = miniSearch.search(q);
  }
  return <>
    <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
      {q === "" && (
        <>
          <h1>All Articles ({allPostsData.length})</h1>
          <p>
            Everything written by Daniel Roy Greenfeld for the past{" "}
            {yearsBlogging} years
          </p>
        </>
      )}

      {q !== "" && (
        <>
          <h1>
            {postsData.length} articles on "{router.query.q}"
          </h1>
        </>
      )}

      <ul className={utilStyles.list}>
        {postsData.map(({ id, date, title, description }) => (
          <li className={utilStyles.listItem} key={id}>
            {/* <h2 className={utilStyles.headingLg}>2022</h2> */}
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
  </>;
}
