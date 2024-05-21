import Link from "next/link";
import Image from "next/image";
import utilStyles from "../../festyles/utils.module.css";
import MyDate from "../../components/date";
import Metatags from "../../components/metatags";

import { getAllTags, getSortedPostsByTagData } from "../../lib/tags";

export async function getStaticProps({ params }) {
  const allTagsData = getSortedPostsByTagData(params.id);
  return {
    props: {
      allTagsData,
      tag: params.id,
    },
  };
}

export async function getStaticPaths() {
  let paths = [];
  for (const path of getAllTags()) {
    paths.push({ params: { id: path.id } });
  }
  return {
    paths,
    fallback: false,
  };
}

export default function Home({ allTagsData, tag }) {
  const prettyTag = `${tag[0].toUpperCase()}${tag.slice(1)}`;
  const meta = {
    title: `${prettyTag} Articles (${allTagsData.length})`,
    og_url: `https://daniel.feldroy.com/tags/${tag}`,
  };
  return <>
    <Metatags meta={meta} />
    <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
      {tag == "TIL" ? (
        <div className="row">
          <div className="column left-25">
            <Image src="/logos/til-1.png" width={128} height={128} alt="TIL" />
          </div>
          <div className="column right-75">
            <h2 className={utilStyles.headingLg}>
              Articles ({allTagsData.length})
            </h2>
          </div>
        </div>
        
      ) : (
        <h2 className={utilStyles.headingLg}>
          {prettyTag} Articles ({allTagsData.length})
        </h2>
      )}
      <ul className={utilStyles.list}>
        {allTagsData.map(({ id, date, title, description }) => (
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
  </>;
}
