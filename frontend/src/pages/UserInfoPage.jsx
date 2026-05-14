import { useState } from "react";
import { Link } from "react-router-dom";

export default function UserInfoPage() {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleShowUserInfo = async () => {
    setIsLoading(true);

    try {
      const response = await fetch("/api/users/me", {
        method: "GET",
        credentials: "include",
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "No se pudo obtener la información del usuario",
        );
      }

      setUser(data);
    } catch (error) {
      setUser(null);
      alert(
        `Hubo un error al obtener la información del usuario: ${error.message}`,
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="page single-page">
      <article className="card reveal single-card user-card">
        <h2>Mostrar información del usuario</h2>

        <div className="user-actions">
          <button
            type="button"
            onClick={handleShowUserInfo}
            disabled={isLoading}
          >
            {isLoading ? "Cargando..." : "Mostrar información"}
          </button>

          <Link to="/login" className="text-link">
            Volver al login
          </Link>
        </div>

        {user && (
          <section className="user-info">
            <p>
              <strong>ID:</strong> {user.id}
            </p>

            <p>
              <strong>Nombre:</strong> {user.full_name}
            </p>

            <p>
              <strong>Nombre de usuario:</strong> {user.username}
            </p>

            <div className="password-box">
              <strong>Contraseña hasheada:</strong>
              <p>{user.password_hash}</p>
            </div>
          </section>
        )}
      </article>
    </main>
  );
}
