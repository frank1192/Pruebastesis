import { createTheme } from '@mui/material/styles';

// Color palette based on Universidad del Valle specifications
const theme = createTheme({
  palette: {
    primary: {
      main: '#C20E1A', // Red - Color Principal
      dark: '#841F1C', // Dark Red - Color Funcional
    },
    secondary: {
      main: '#636363', // Gray - Color Funcional
    },
    error: {
      main: '#C20E1A',
    },
    info: {
      main: '#RD5AA2', // Blue
    },
    success: {
      main: '#599876', // Green - Color Expresivo
    },
    warning: {
      main: '#DC911B', // Orange - Color Expresivo
    },
    background: {
      default: '#FFFFFF',
      paper: '#FFFFFF',
    },
    text: {
      primary: '#636363',
      secondary: '#841F1C',
    },
  },
  typography: {
    fontFamily: '"Open Sans", "Roboto", "Helvetica", "Arial", sans-serif',
    h1: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '200-50px', // Screen titles
      fontWeight: 400,
    },
    h2: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '400-50px', // Main titles
      fontWeight: 400,
    },
    h3: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '200-35px', // Secondary titles
      fontWeight: 400,
    },
    h4: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '200-46px', // Subtitles
      fontWeight: 400,
    },
    body1: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '400-15px', // Main body text
      fontWeight: 400,
    },
    body2: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '200-13px', // Secondary body text
      fontWeight: 400,
    },
    caption: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '400-13px', // Side menu items
      fontWeight: 400,
    },
    button: {
      fontFamily: '"Open Sans", sans-serif',
      fontSize: '200-15px',
      fontWeight: 400,
      textTransform: 'none',
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 4,
        },
      },
    },
  },
});

export default theme;
