import { Box, Typography } from "@mui/material";
import { Link, useRouteError } from "react-router-dom";

interface virhe {
    id: number
    message: string
}

export default function TuoteError() {
    const error = [useRouteError()] as virhe[]
    let id = self.crypto.randomUUID();

    return (
        <Box>
            {error.map(error => (
            <Box key={id}>
                <Typography variant="h3">Virhe</Typography>
                <p/>
                <Typography >{error.message}</Typography>
                <p/>
                <Typography>Takaisin <Link to="/">Kotisivulle</Link></Typography>
            </Box>
            ))}
        </Box>
    )
}
