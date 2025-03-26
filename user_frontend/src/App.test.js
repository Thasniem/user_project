import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { BrowserRouter } from "react-router-dom";
import { AuthContext } from "./App";
import App from "./App";

const renderWithRouter = (ui, { route = '/' } = {}) => {
  window.history.pushState({}, 'Test page', route);
  return render(ui, { wrapper: BrowserRouter });
};

describe('App Component', () => {
  beforeEach(() => {
    localStorage.clear();
    jest.clearAllMocks();
  });

  test('renders login page for unauthenticated users', () => {
    renderWithRouter(<App />);
    expect(screen.getByText(/Login/i)).toBeInTheDocument();
  });

  test('redirects to dashboard for authenticated users', async () => {
    localStorage.setItem('token', 'fake-token');
    renderWithRouter(<App />);
    await waitFor(() => {
      expect(screen.getByText(/Dashboard/i)).toBeInTheDocument();
    });
  });

  test('sidebar is not visible when user is not authenticated', () => {
    renderWithRouter(<App />);
    expect(screen.queryByTestId('sidebar')).not.toBeInTheDocument();
  });

  test('successful login redirects to dashboard', async () => {
    renderWithRouter(<App />, { route: '/login' });
    
    fireEvent.change(screen.getByLabelText(/Email/i), {
      target: { value: 'test@example.com' },
    });
    fireEvent.change(screen.getByLabelText(/Password/i), {
      target: { value: 'password123' },
    });
    
    fireEvent.click(screen.getByRole('button', { name: /Login/i }));
    
    await waitFor(() => {
      expect(screen.getByText(/Dashboard/i)).toBeInTheDocument();
    });
  });

  test('logout removes token and redirects to login', async () => {
    localStorage.setItem('token', 'fake-token');
    renderWithRouter(<App />);
    
    const logoutButton = await screen.findByText(/Logout/i);
    fireEvent.click(logoutButton);
    
    expect(localStorage.getItem('token')).toBeNull();
    expect(screen.getByText(/Login/i)).toBeInTheDocument();
  });
});