import { useState } from "react";
import { Link } from "react-router-dom";

const initialRegister = {
  full_name: "",
  username: "",
  password: ""
};

export default function RegisterPage() {
  const [registerForm, setRegisterForm] = useState(initialRegister);
  const [isRegistering, setIsRegistering] = useState(false);

  const onRegisterChange = (event) => {
    const { name, value } = event.target;
    setRegisterForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleRegister = async (event) => {
    event.preventDefault();
    setIsRegistering(true);

    try {
      const response = await fetch("/api/users", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(registerForm)
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Error al crear usuario");
      }

      setRegisterForm(initialRegister);
      alert(`Usuario creado: ${data.username}`);
    } catch (error) {
      alert(`Fallo al crear usuario: ${error.message}`);
    } finally {
      setIsRegistering(false);
    }
  };

  return (
    <main className="page single-page">
      <article className="card reveal single-card">
        <h2>Creación de usuario</h2>
        <form onSubmit={handleRegister} className="form">
          <label htmlFor="full_name">Nombre completo</label>
          <input
            id="full_name"
            name="full_name"
            type="text"
            value={registerForm.full_name}
            onChange={onRegisterChange}
            required
          />

          <label htmlFor="register_username">Nombre de usuario</label>
          <input
            id="register_username"
            name="username"
            type="text"
            value={registerForm.username}
            onChange={onRegisterChange}
            required
          />

          <label htmlFor="register_password">Contraseña</label>
          <input
            id="register_password"
            name="password"
            type="password"
            value={registerForm.password}
            onChange={onRegisterChange}
            required
            minLength={6}
          />

          <Link to="/login" className="text-link">
            Volver a login
          </Link>

          <button type="submit" disabled={isRegistering}>
            {isRegistering ? "Creando..." : "Crear usuario"}
          </button>
        </form>
      </article>
    </main>
  );
}
