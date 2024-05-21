import { test, expect } from '@playwright/test';

test.describe.serial('Testaa koko nettisivun', () => {

  test('tarkista tuotelistan sivut', async ({ page }) => {
    await page.goto('http://localhost:5173/');
    await page.getByRole('link', { name: 'Tuotelista' }).click();
    await page.getByRole('heading', { name: 'Tuotelista' }).click();
    await page.getByRole('link', { name: 'Luo uusi tuote' }).click();
    await page.getByRole('button', { name: 'Lähetä tuote' }).click();
    await page.getByRole('link', { name: 'Muokkaa tuotteita' }).click();
  });


  test('luo tuote', async ({ page }) => {
    await page.goto('http://localhost:5173/');
    await page.getByRole('link', { name: 'Luo uusi tuote' }).click();
    await page.getByLabel('Nimi *').click();
    await page.getByLabel('Nimi *').fill('Playwright');
    await page.getByLabel('Hinta *').click();
    await page.getByLabel('Hinta *').fill('90000');
    await page.getByLabel('Kuvaus *').click();
    await page.getByLabel('Kuvaus *').fill('Testataan Playwright.');
    await page.locator('input[name="tuotekuva"]').click();
    await page.locator('input[name="tuotekuva"]').setInputFiles('./playwrighttests/widetest.jpg');
    await page.getByRole('button', { name: 'Lähetä tuote' }).click();
  });


  test('muokkaa tuote', async ({ page }) => {
    await page.goto('http://localhost:5173/muokkaatuote');
    await page.locator('.MuiCardContent-root > .MuiButtonBase-root').first().click();
    await page.getByLabel('Nimi *').click();
    await page.getByLabel('Nimi *').fill('Playwright muokkasi tämän');
    await page.getByLabel('Hinta *').click();
    await page.getByLabel('Hinta *').fill('12121212');
    await page.getByLabel('Kuvaus *').click();
    await page.getByLabel('Kuvaus *').fill('Plapla.');
    await page.getByRole('button', { name: 'Poista kuva' }).click();
    await page.locator('input[name="tuotekuva"]').click();
    await page.locator('input[name="tuotekuva"]').setInputFiles('./playwrighttests/widetest.jpg');
    await page.getByRole('button', { name: 'Päivitä tuote' }).click();
  });


  test('poista tuote', async ({ page }) => {
    await page.goto('http://localhost:5173/');
    await page.getByRole('link', { name: 'Muokkaa tuotteita' }).click();
    await page.locator('.MuiCardContent-root > .MuiButtonBase-root').last().click();
    await page.getByRole('button', { name: 'Poista tuote' }).click();
  });

});