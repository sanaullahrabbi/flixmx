module.exports = {
  content: [
    './templates/*/*.{html,js}',
    './templates/**',
  ],
  theme: {
    extend: {
      fontFamily: {
        'quicksand': 'Quicksand, sans-serif',
        'montserrat': 'Montserrat, sans-serif',
        'poppins': 'Poppins, sans-serif',
      },
      width: {
        'col-7': 'calc(14.29% - 0.5rem)',
        'col-6': 'calc(16.67% - 0.5rem)',
        'col-5': 'calc(20% - 0.5rem)',
        'col-4': 'calc(25% - 0.5rem)',
        'col-3': 'calc(33.33% - 0.5rem)',
        'col-2': 'calc(50% - 0.5rem)',
      }
    },
  },
  darkMode: 'class',
  plugins: [],
}