import { FieldValues } from "react-hook-form"
import { ThemeProvider, createTheme } from '@mui/material/styles'
import { Form, redirect, useLoaderData } from 'react-router-dom'
import axios from 'axios'
import { useState } from 'react'
import { Box, Button, Card, CardActions, CardContent, CardMedia, CssBaseline, TextField } from '@mui/material'

const darkTheme = createTheme({
  palette: {
    mode: 'dark'
  }
})

interface tuotelista {
  id: string
  nimi: string
  hinta: number
  kuvaus: string
  tuotekuva: string
}
  
export default function  Muokkaus() {
  const tuote = [useLoaderData()] as tuotelista[]
  const [show, setShow] = useState(true)
  const [hide, setHide] = useState(false)
  
  return (
    <ThemeProvider theme={darkTheme}>
    <CssBaseline />

    <>
    {tuote.map(tuote => (
      <Form key={ tuote.id } method="put" action={ tuote.id } encType="multipart/form-data">
        <Box >
          <TextField defaultValue={ tuote.id } name="id" sx={{ display: { xl: 'none', xs: 'block' } }} InputProps={{ readOnly: true, }} /><p/>
          <TextField defaultValue={ tuote.nimi } name="nimi" required label="Nimi" sx={{ mt: 3, width: 600 }} /><p/>
          <TextField defaultValue={ tuote.hinta } name="hinta" required label="Hinta" sx={{ width: 600 }} type="number" /><p/>
          <TextField defaultValue={ tuote.kuvaus } name="kuvaus" required label="Kuvaus" sx={{ width: 600 }} multiline rows={5} /><p/>
          
          <p/>
          <Box>
          {
            show?
            <Card variant="outlined" sx={{ maxWidth: 345 }} >
            <CardMedia sx={{ height: 295, width: 'auto'}} image={tuote.tuotekuva}/>
            <CardContent >
              <CardActions sx={{ justifyContent: "center" }}>
                <Button variant="outlined" onClick={()=>{setShow(!show); setHide(!hide)}}>Poista kuva</Button>
              </CardActions>
            </CardContent>
          </Card>
            :null
          }
          {
            hide?
            <TextField name="tuotekuva" required className="sr-only" type="file" />
            :null
            }<p/>
        </Box>
        <Button value="muokkaa" name="intent" variant="outlined" sx={{ mt: 3 }} type="submit">Päivitä tuote</Button> 
        <Button value="poista" name="intent" variant="outlined" sx={{ ml: 1, mt: 3 }} type="submit">Poista tuote</Button> 
      </Box>
    </Form>
    ))}
    </>
        
    </ThemeProvider>
  )
}

export const muokkaaTuote = async({request}: FieldValues) => {
  const data = await request.formData()
  const intent = data.get('intent')
  const submission = {
    id: data.get('id'),
    nimi: data.get('nimi'),
    hinta: data.get('hinta'),
    kuvaus: data.get('kuvaus'),
    tuotekuva: data.get('tuotekuva')
  }

  try { 
    
    if (intent === 'muokkaa') {
      await axios.put('http://localhost:8000/tuote/' + submission.id, submission, {headers: { "Content-Type": "multipart/form-data" }})
      return redirect('/muokkaatuote')
    } 
    else if (intent === 'poista') {
      await axios.delete('http://localhost:8000/tuote/' + submission.id)
      return redirect('/muokkaatuote')
    }
    }
  catch(error) {
    console.log(error)
  }
}