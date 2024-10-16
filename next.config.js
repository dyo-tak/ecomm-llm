/** @type {import('next').NextConfig} */
const nextConfig = {
    experimental: {
      serverActions: true,
      serverComponentsExternalPackages: ['mongoose', 'cheerio'],
    },
    images: {
      domains: ['m.media-amazon.com']
    }
  }
  
  module.exports = nextConfig