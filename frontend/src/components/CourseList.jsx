import { useEffect, useState } from "react";
import api from "../services/api";

export default function CourseList() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    api.get("/courses").then(res => setCourses(res.data));
  }, []);

  return (
    <ul className="space-y-2">
      {courses.map(c => (
        <li key={c.id} className="p-3 border rounded shadow hover:bg-gray-50">
          {c.name} ({c.credits} credits) - {c.department}
        </li>
      ))}
    </ul>
  );
}

