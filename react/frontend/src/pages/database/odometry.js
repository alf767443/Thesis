// Import from MUI
import { Grid } from '@mui/material';
// Import from project
import { OdometryCard } from 'tables/Odometry';

// --------- database - odometry --------- \\
const Odometry = () => {
    return (
        <Grid container rowSpacing={0} columnSpacing={0}>
            {/* Main block */}
            <OdometryCard />
        </Grid>
    );
};

export default Odometry;
