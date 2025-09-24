import Header from '../components/header';
import CardsContainer from '../components/cardsContainer';
import ProductsHistory from '../components/productsHistory';

function Home() {
  return (
    <div className="App">
      <Header />
      <CardsContainer />
      <ProductsHistory />
    </div>
  );
}

export default Home;