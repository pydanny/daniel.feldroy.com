import Link from "next/link";
import utilStyles from "../festyles/utils.module.css";

import { getAllTags } from "../lib/tags";

export async function getStaticProps() {
  const allTagsData = getAllTags();
  return {
    props: {
      allTagsData,
      title: "All tags",
    },
  };
}

export default function Home({ allTagsData }) {
  return <>
    <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
      <h2 className={utilStyles.headingLg}>Tags</h2>
      <p className={utilStyles.listItem}>
        {allTagsData.map(({ id, value }) => (
          <>
            <Link key={id} href={`/tags/${id}`}>

              {id}({value})
            </Link>{" "}
          </>
        ))}
      </p>
    </section>
  </>;
}
