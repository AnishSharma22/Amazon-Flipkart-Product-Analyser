import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Product Recommendation Engine',
  description: 'Next level product recommendation engine',
  icons: "https://i.pinimg.com/564x/16/df/e4/16dfe40ae4f39e0e76674f3fbb3bf626.jpg",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  )
}
