import Head from 'next/head'
import Link from 'next/link'
import Layout, { siteTitle } from '../../components/layout'
import utilStyles from '../../styles/utils.module.css'
import Date from '../../components/date'

import { getSortedPostsByTagData, getAllTags } from '../../lib/tags'

export async function getStaticProps({ params }) {
  const allTagsData = getSortedPostsByTagData(params.tag)
  return {
    props: {
      allTagsData
    }
  }
}

export async function getStaticPaths() {
  const tags = getAllTags()
  paths = []
  return {
    paths,
    fallback: false
  }
}

export default function Home({ allTagsData }) {
  return (
    <Layout home>
      <Head>
        <title>{siteTitle}</title>
      </Head>
      <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
        <h2 className={utilStyles.headingLg}>Blog</h2>
        <ul className={utilStyles.list}>
          {allTagsData.map(({ id, date, title }) => (
            <li className={utilStyles.listItem} key={id}>
              <Link href={`/posts/${id}`}>
                <a>{title}</a>
              </Link>
              <br />
              <small className={utilStyles.lightText}>
                <Date dateString={date} />
              </small>
            </li>
          ))}
        </ul>
      </section>
    </Layout>
  )
}
