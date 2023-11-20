import Image from "next/image";
import Script from "next/script";
import Link from "next/link";

import Layout from "../../components/layout";
import utilStyles from "../../festyles/utils.module.css";

export async function getStaticProps() {
  return {
    props: {
      title: "Tech Books",
      description: "With Audrey, I co-write dairy-themed technical books.",
      og_url: "https://daniel.feldroy.com/books/tech",
    },
  };
}

export default function TechBooks() {
  return <>
    <article>
      <div className={utilStyles.backToHome}>
        <Link href="/books">
          ← Back to books
        </Link>
      </div>
      <h1>Tech Books I Have Co-Authored</h1>
      <p>With Audrey, I co-write dairy-themed technical books.</p>
      <ul className={utilStyles.list}>
        <li className={utilStyles.listItem}>
          <Image
            src="/images/book-TSD3-800.jpg"
            height="514"
            width="360"
          ></Image>
          <h2>Two Scoops of Django 3.x </h2>
          <p>
            The 5th edition of Two Scoops of Django is out. With over 500
            pages of material, you'll find best practices that will improve
            all your Django projects.
          </p>
          <p>
            <a
              href="https://transactions.sendowl.com/packages/772159/A329F48B/purchase"
              rel="nofollow"
            >
              <img src="https://transactions.sendowl.com/assets/external/buy-now.png" />
            </a>
          </p>

          <hr />
        </li>

        <li className={utilStyles.listItem}>
          <Image
            src="/images/AWOD-2021-06-29-8x10-Wedge-Front_1080x.png"
            height="450"
            width="360"
          ></Image>
          <h2>A Wedge of Django</h2>
          <p>
            Our guided walkthrough tutorial where we build a real
            production-quality Django 3.2 web application from the ground up.
          </p>
          <p>
            <a
              href="https://transactions.sendowl.com/packages/754641/749E0298/purchase"
              rel="nofollow"
            >
              <img src="https://transactions.sendowl.com/assets/external/buy-now.png" />
            </a>
          </p>
        </li>
      </ul>
      <Script
        type="text/javascript"
        src="https://transactions.sendowl.com/assets/sendowl.js"
        strategy="afterInteractive"
      ></Script>
    </article>
  </>;
}
