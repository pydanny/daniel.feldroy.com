import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import remark from 'remark'
import html from 'remark-html'

const postsDirectory = path.join(process.cwd(), 'posts')

export function getAllTags() {
  // Get file names under /posts
  const fileNames = fs.readdirSync(postsDirectory)
  let tags = {}
  for (const fileName of fileNames) {
    const id = fileName.replace(/\.md$/, '')
    // Read markdown file as string
    const fullPath = path.join(postsDirectory, fileName)
    const fileContents = fs.readFileSync(fullPath, 'utf8')

    // Use gray-matter to parse the post metadata section
    const matterResult = matter(fileContents)
    for (const tag of matterResult.data.tags) {
      if (tags.hasOwnProperty(tag)) {
        tags[tag]++
      } else {
        tags[tag] = 1
      }
    }
  }

  let allTagsData = []
  for (const [id, value] of Object.entries(tags)) {
    allTagsData.push(
      { id, value }
    )
  }

  return allTagsData.sort((a, b) => {
    if (a.value < b.value) {
      return 1
    } else {
      return -1
    }
  })
}

