import 'bootstrap/dist/css/bootstrap.css';
import '../styles.css';
import { UserProvider } from '../lib/context/userContext';

function MyApp({ Component, pageProps }) {
  return (
    <UserProvider>
      <Component {...pageProps} />
    </UserProvider>
  );
}

export default MyApp;
