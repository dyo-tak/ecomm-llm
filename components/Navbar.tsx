import Image from "next/image";
import Link from "next/link";
import { Inter } from "next/font/google";

const inter = Inter({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"],
  display: "swap",
});
const navIcons = [
  { src: "/assets/icons/search.svg", alt: "search" },
  // { src: "/assets/icons/black-heart.svg", alt: "heart" },
  // { src: "/assets/icons/user.svg", alt: "user" },
];

const Navbar = () => {
  return (
    <header className="w-full">
      <nav className="nav">
        <Link href="/" className="flex items-center gap-1">
          <Image
            src="/assets/icons/logo.png"
            width={27}
            height={27}
            alt="logo"
          />

          <div className={inter.className}>
            <p className="nav-logo {style}">
              Ecomm<span className="text-blue-600">SLM </span>
            </p>
          </div>
        </Link>

        <Link href="/search" className="flex items-center gap-5">
          {navIcons.map((icon) => (
            <Image
              key={icon.alt}
              src={icon.src}
              alt={icon.alt}
              width={28}
              height={28}
              className="object-contain"
            />
          ))}
        </Link>
      </nav>
    </header>
  );
};

export default Navbar;
