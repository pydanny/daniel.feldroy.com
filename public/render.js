  marked.setOptions({
    gfm: true,
    breaks: true, // Optional: Treat single line breaks as <br>
    highlight: function (code, lang) {
      // Use highlight.js with a fallback for unknown languages
      const validLang = hljs.getLanguage(lang) ? lang : 'plaintext';
      return hljs.highlight(code, { language: validLang }).value;
    }    
  });

//   const html = marked.parse(markdown);

    // Find all elements with the "marked" class and convert content
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.marked').forEach(el => {
    const markdown = el.textContent;
    const html = marked.parse(markdown);
    el.innerHTML = html;

    el.querySelectorAll('pre code').forEach(block => {
    hljs.highlightElement(block);
    });    
  });
 });