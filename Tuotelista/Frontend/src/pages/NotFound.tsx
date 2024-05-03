import { Box, Typography } from "@mui/material";
import { Link } from "react-router-dom";

export default function NotFound() {
    return (
        <Box>
            <Typography variant="h3">Sivu ei löytynyt!</Typography>

            <p/>

            <Typography>Takaisin <Link to="/">Kotisivulle</Link></Typography>

        </Box>
    )
}