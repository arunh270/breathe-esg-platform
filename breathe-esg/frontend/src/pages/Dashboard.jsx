import { useEffect, useState } from "react";
import api from "../api/api";

export default function Dashboard() {

  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const response = await api.get(
      "/emissions/"
    );

    setRecords(response.data);
  };

  return (
    <div className="p-8">

      <h1 className="text-3xl mb-6">
        ESG Dashboard
      </h1>

      <table className="w-full border">

        <thead>
          <tr>
            <th>Scope</th>
            <th>Category</th>
            <th>CO2e</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {records.map((record) => (
            <tr key={record.id}>

              <td>{record.scope}</td>

              <td>{record.category}</td>

              <td>{record.co2e_kg}</td>

              <td>{record.status}</td>

            </tr>
          ))}
        </tbody>

      </table>

    </div>
  );
}