/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                // Custom black and white palette if needed
                'brand-black': '#000000',
                'brand-white': '#ffffff',
                'brand-gray': '#f3f4f6',
            },
        },
    },
    plugins: [],
}
