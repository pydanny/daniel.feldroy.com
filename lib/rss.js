const Feed = require("feed").Feed;
import remark from "remark";
import html from "remark-html";
const fs = require("fs");
import { getSortedPostsDataWithHtml } from "./posts";

export async function generateRssFeed(tag) {
  if (process.env.NODE_ENV === "development") {
    return;
  }

  const baseUrl = "https://daniel.feldroy.com";
  const date = new Date();
  const author = {
    name: "Daniel Roy Greenfeld",
    email: "daniel@feldroy.com",
    link: "https://daniel.feldroy.com",
  };

  const feed = new Feed({
    title: `Daniel Roy Greenfeld`,
    description: "Inside the head of Daniel Roy Greenfeld",
    id: baseUrl + "/",
    link: baseUrl,
    language: "en",
    image: `${baseUrl}/images/pydanny-cartwheel.png`,
    favicon: `${baseUrl}/favicon.ico`,
    copyright: `All rights reserved ${date.getFullYear()}, Daniel Roy Greenfeld`,
    updated: date,
    generator: "Next.js using Feed for Node.js",
    feedLinks: {
      rss2: `${baseUrl}/feeds/feed.xml`,
    },
    author,
  });

  const posts = getSortedPostsDataWithHtml().slice(0, 2);

  for (const post of posts) {
    if (tag.length > 0 && post.tags.indexOf(tag) === -1) {
      continue;
    }

    const url = `${baseUrl}/posts/${post.id}`;
    const processedContent = await remark().use(html).process(post.content);
    const contentHtml = processedContent.toString();
    let category = [];
    for (const tag of post.tags) {
      category.push({ term: tag});
    }

    feed.addItem({
      title: post.title,
      id: url,
      link: url,
      description: post.description,
      content: contentHtml,
      author: [author],
      contributor: [author],
      date: new Date(post.date),
      category: category,
    });
  }

  fs.mkdirSync("./public/feeds", { recursive: true });
  if (tag.length > 0) {
    fs.writeFileSync(`./public/feeds/${tag}.atom.xml`, feed.atom1());
  } else {
    fs.writeFileSync(`./public/feeds/atom.xml`, feed.atom1());
  }
}

export default generateRssFeed;
