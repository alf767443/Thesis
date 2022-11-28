import { useState } from 'react';

// material-ui
import { Grid, SvgIcon } from '@mui/material';

// project import
import debugBoxe from 'graphs/debugBox';
import { OdometryCard } from 'tables/Position//Odometry/index';
import SalesColumnChart from 'graphs/SalesColumnChart';
import DinamicGrid from 'components/DinamicGrid';
import MonthlyBarChart from './MonthlyBarChart';
import BatteryIcon from 'graphs/battery/batteryIcon';
import App from 'graphs/queueActions'
;

// assets
import { GiftOutlined, MessageOutlined, SettingOutlined } from '@ant-design/icons';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const DashboardDefault = () => {
    return (
        <Grid container rowSpacing={4.5} columnSpacing={2.75}>
            {/* Main block */}
            <BatteryIcon percent={0.5} width={100} heigth={100} />
            <App show={10}/>
        </Grid>
    );
};

export default DashboardDefault;
