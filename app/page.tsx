import Image from "next/image";
import Searchbar from "@/components/Searchbar";
import HerpCarousal from "@/components/HerpCarousal";
import { getAllProducts } from "@/lib/actions";
import { scrapeAmazonProductList } from "@/lib/scraper/productListScrapper";
import ProductCard from "@/components/ProductCard";

const page = async () => {
  const allProducts = await getAllProducts();
  // const temp = scrapeAmazonProductList();

  return (
    <>
      <section className="px-6 md:px-20 py-24">
        <div className="flex max-xl:flex-col gap-16">
          <div className="flex flex-col justify-center">
            <p className="small-text">
              Smart Shopping Starts Here:
              <Image
                src="/assets/icons/arrow-right.svg"
                alt="arrow-right"
                width={16}
                height={16}
              />
            </p>
            <h1 className="head-text ">
              Unleash the Power of
              <span className="text-blue-700"> Ecomm SLM</span>
            </h1>
            <p className="mt-6">
              Paste your amazon product link below and we will provide you with
              ecomm SLM.
            </p>
            <Searchbar />
          </div>

          <HerpCarousal />
        </div>
      </section>

      <section className="trending-section">
        <h2 className="section-text">Trending</h2>

        <div className="grid grid-cols-2 sm:grid md:grid-cols-4 gap-x-8 gap-y-16">
          {allProducts
            ?.slice()
            .reverse()
            .map((product) => (
              <ProductCard key={product._id} product={product} />
            ))}
        </div>
      </section>
    </>
  );
};

export default page;
