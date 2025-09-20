import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

test('renders the app without crashing', () => {
  render(<App />);
  // Basic smoke test to ensure the app renders
  expect(document.querySelector('.App')).toBeInTheDocument();
});