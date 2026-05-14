import { useState } from "react";
import { Link } from "react-router-dom";

const initialLogin = {
  username: "",
  password: ""
};

export default function LoginPage() {
  const [loginForm, setLoginForm] = useState(initialLogin);
  const [isLoggingIn, setIsLoggingIn] = useState(false);

  const onLoginChange = (event) => {
    const { name, value } = event.target;
    setLoginForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    setIsLoggingIn(true);

    try {
      const body = new URLSearchParams();
      body.append("username", loginForm.username);
      body.append("password", loginForm.password);

      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        credentials: "include",
        body
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Error de autenticacion");
      }

      setLoginForm(initialLogin);
      alert(`Usuario Autenticado. Token: ${data.access_token}`);
    } catch (error) {
      alert(`Fallo de autenticacion: ${error.message}`);
    } finally {
      setIsLoggingIn(false);
    }
  };

  return (
    <main className="page single-page">
      <article className="card reveal single-card">
        <h2>Autenticar usuario</h2>
        <form onSubmit={handleLogin} className="form">
          <label htmlFor="login_username">Nombre de usuario</label>
          <input
            id="login_username"
            name="username"
            type="text"
            value={loginForm.username}
            onChange={onLoginChange}
            required
          />

          <label htmlFor="login_password">Contraseña</label>
          <input
            id="login_password"
            name="password"
            type="password"
            value={loginForm.password}
            onChange={onLoginChange}
            required
          />

          <Link to="/crear-cuenta" className="text-link">
            Crear cuenta de usuario
          </Link>

          <button type="submit" disabled={isLoggingIn}>
            {isLoggingIn ? "Entrando..." : "Entrar"}
          </button>
        </form>
      </article>
    </main>
  );
}
