import { useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project import
import debugBoxe from 'graphs/debugBox';
import { OdometryCard } from 'tables/Position//Odometry/index';
import SalesColumnChart from 'graphs/SalesColumnChart';
import DinamicGrid from 'components/DinamicGrid';
import MonthlyBarChart from './MonthlyBarChart';

// assets
import { GiftOutlined, MessageOutlined, SettingOutlined } from '@ant-design/icons';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const DashboardDefault = () => {
    return (
        <Grid container rowSpacing={4.5} columnSpacing={2.75}>
            {/* Main block */}
            <OdometryCard />
        </Grid>
    );
};

export default DashboardDefault;
