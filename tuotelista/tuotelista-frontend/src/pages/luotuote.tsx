import './App.css'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import { ThemeProvider, createTheme } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'
import TextField from '@mui/material/TextField'
import { Form, redirect } from 'react-router-dom'
import axios from 'axios'
import { FieldValues } from 'react-hook-form'

const darkTheme = createTheme({
    palette: {
      mode: 'dark'
    }
  })

export default function Luotuote() {
  
  return (
  <ThemeProvider theme={darkTheme}>
  <CssBaseline />
  <Box >   
  <Form method="post" action="/luotuote" encType="multipart/form-data">

    <TextField name="nimi" required label="Nimi" sx={{ width: 600 }} /><p/>
    <TextField name="hinta" required label="Hinta" sx={{ width: 600 }} type="number" /><p/>
    <TextField name="kuvaus" required label="Kuvaus" sx={{ width: 600 }} multiline rows={5} /><p/>
    <TextField name="tuotekuva" required className="sr-only" type="file" /><p/>

    <Button variant="outlined" type='submit'>Lähetä tuote</Button>
  </Form>   
  </Box>
  </ThemeProvider>
  )
}

export const postTuote = async({request}: FieldValues) => {

  const data = await request.formData()
  const submission = {
    nimi: data.get('nimi'),
    hinta: data.get('hinta'),
    kuvaus: data.get('kuvaus'),
    tuotekuva: data.get('tuotekuva')
  }
  try {
    await axios.post(
      'http://localhost:8000/tuote/', submission, {headers: { "Content-Type": "multipart/form-data" }}
    )
    return redirect('/')
  }
  catch(error) {
    console.log(error)
  }
}