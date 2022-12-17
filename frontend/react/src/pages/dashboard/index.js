// material-ui
import { Grid } from '@mui/material';

// project import
import BatteryTimePlot from 'graphs/battery/batteryTimePlot';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const DashboardDefault = () => {
    return (
        <Grid container rowSpacing={1.75} columnSpacing={2}>
            {/* Main block */}
            <Grid item sx={{ mb: -2.25 }}>
                <BatteryTimePlot />
            </Grid>
        </Grid>
    );
};

export default DashboardDefault;
