interface Props {
  title?: string;
  prompts: string[];
}

function Dropdown({ title, prompts }: Props) {
  return (
    <div className="dropdown">
      <button
        className="btn btn-secondary dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        {title != null ? title : "DropDown Button"}
      </button>
      <ul className="dropdown-menu">
        {prompts.map((prompt) => (
          <li className="dropdown-item">{prompt}</li>
        ))}
      </ul>
    </div>
  );
}

export default Dropdown;
