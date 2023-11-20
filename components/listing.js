import utilStyles from "../festyles/utils.module.css";

export default function Listing({ id, description, date }) {
  return (
    <li key={id}>
      <Link href={`/posts/${id}`}>
        <a>{title}</a>
      </Link>
      <br />
      {description && (
        <>
          <small>{description}</small>
          <br />
        </>
      )}
      <small>
        <MyDate dateString={date} />
      </small>
    </li>
  );
}
