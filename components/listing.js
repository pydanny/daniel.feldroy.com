import utilStyles from "../festyles/utils.module.css";

export default function Listing({ id, description, date }) {
  return (
    <li className={utilStyles.listItem} key={id}>
      <Link href={`/posts/${id}`}>
        <a>{title}</a>
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
  );
}
