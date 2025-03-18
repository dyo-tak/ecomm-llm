"use server";

import axios from "axios";
import * as cheerio from "cheerio";
import { scrapeAndStoreProduct } from "@/lib/actions";
import { lists } from "./lists";
// import { extractPrice, extractCurrency, extractDescription } from "../utils";

export async function scrapeAmazonProductList() {
    // const url = "https://www.amazon.in/s?k=laptop&page=3&crid=3K2PXU88V54DD&qid=1742230296&sprefix=laptop%2Caps%2C223&xpid=tmqJQ9sJunvz5&ref=sr_pg_3"
    // BrightData proxy configuration
    const username = String(process.env.BRIGHT_DATA_USERNAME);
    const password = String(process.env.BRIGHT_DATA_PASSWORD);
    const port = 22225;
    const session_id = (1000000 * Math.random()) | 0;

    const options = {
        auth: {
            username: `${username}-session-${session_id}`,
            password,
        },
        host: "brd.superproxy.io",
        port,
        rejectUnauthorized: false,
    };

    try {
        for (const url of lists) {
            const response = await axios.get(url, options);
            const $ = cheerio.load(response.data);


            const urlList = $(".a-link-normal.s-line-clamp-2.s-link-style.a-text-normal")
                .map((_, element) => {
                    return "https://www.amazon.in" + $(element).attr("href");
                })
                .get();

            for (const productUrl of urlList) {
                await scrapeAndStoreProduct(productUrl);
            }
        }


        console.log("done");
        // return urlList;
    } catch (error: any) {
        console.log(error);
    }
}

