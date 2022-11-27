// Import from MUI
import { useTheme } from '@mui/material/styles';

// Import from project
import logo from './logo_CeDRI.png';

// --------- Componets Logo - Logo --------- \\
const Logo = () => {
    const theme = useTheme();

    return (
        <>
            <img src={logo} alt="CeDRI Logo" width="140" />
        </>
    );
};

export default Logo;
