import Layout, { siteTitle } from "../components/layout";
import "../festyles/global.css";

export default function App({ Component, pageProps }) {
  return (
    <Layout
      meta={pageProps.markdoc ? pageProps.markdoc.frontmatter : pageProps}
    >
      <Component {...pageProps} />
    </Layout>
  );
}
