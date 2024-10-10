import './App.css'
import Grid from '@mui/material/Grid'
import Card from '@mui/material/Card'
import CardContent from '@mui/material/CardContent'
import CardMedia from '@mui/material/CardMedia'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import { ThemeProvider, createTheme } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'
import Divider from '@mui/material/Divider'
import Paper from '@mui/material/Paper'
import { styled } from '@mui/material/styles'
import { useLoaderData } from 'react-router-dom'

const darkTheme = createTheme({
  palette: {
    mode: 'dark'
  }
})

const Item = styled(Paper)(({ }) => ({
  textAlign: 'center',
}))

interface tuotelista {
  id: number
  nimi: string
  hinta: number
  kuvaus: string
  tuotekuva: string
}

export default function App() {
  const message = useLoaderData() as tuotelista[]
  
  return (
    <ThemeProvider theme={darkTheme}>
    <CssBaseline />
    
    <Box >
    <Divider sx={{ my: 2 }} />

    <Box sx={{ }}>
      <Grid 
        container 
        spacing={2} 
        columns={17}
        sx={{overflow:"auto"}}
        wrap="wrap"
      >
        {message.map(message => (
            <Grid 
              key={message.id} 
              item 
            >
              <Item>
                <Card sx={{ width: 345 }} variant="outlined" >
                  <CardMedia sx={{ height: 295}} image={message.tuotekuva}/>
                  <CardContent >
                    <Typography gutterBottom variant="h5" component="div"> {message.nimi} </Typography>
                    <Typography> {message.hinta} € </Typography>
                    <Typography> {message.kuvaus} </Typography>
                  </CardContent>
                </Card>
              </Item>
            </Grid>
        ))}
      </Grid>
    </Box>
    </Box>
    
    </ThemeProvider>
  )
  }
