import { Box, Button, CssBaseline, ThemeProvider, Typography, createTheme, } from "@mui/material"
import { Outlet, Link as RouterLink } from "react-router-dom"
import AppBar from '@mui/material/AppBar'

const darkTheme = createTheme({
    palette: {
      mode: 'dark'
    }
  });

export default function RootLayout() {
    return (
        <ThemeProvider theme={darkTheme}>
        <CssBaseline />
        <Box >
            <AppBar >
                <nav className="flex-container">
                    <Typography variant="h4" sx={{ my: 1,  mx: 3  }} >Tuotelista </Typography>
                    <Button component={RouterLink} variant="outlined" to="/" sx={{ ml: 1}}>Tuotelista</Button>
                    <Button component={RouterLink} variant="outlined" to="../luotuote" sx={{ mx: 1 }}>Luo uusi tuote</Button>
                    <Button component={RouterLink} variant="outlined" to="../muokkaatuote">Muokkaa tuotteita</Button>
                </nav>
            </AppBar>
            
            <main>
                <Outlet/>
            </main>
        </Box>
        </ThemeProvider>
    )
}