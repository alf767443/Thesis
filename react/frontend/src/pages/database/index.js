import { useState } from 'react';

// material-ui
import { Grid, Box, Typography, Stack } from '@mui/material';
import { TireRepair, BatteryCharging90, BatterySaver, QrCode2, Explore, GpsFixed } from '@mui/icons-material';
import MainCard from 'components/MainCard';
// project import
import DataBaseButtons from './buttons/button';
import { OdometryCard } from 'tables/Odometry/index';

// ==============================|| DASHBOARD - DEFAULT ||============================== //
const screenSize = {
    xs: 12,
    sm: 6,
    md: 3,
    lg: 3
};

const DataBase = () => {
    return (
        <Grid container rowSpacing={3} columnSpacing={1.25}>
            {/* Main block */}
            <Grid item xs={screenSize.xs} sm={screenSize.sm} md={screenSize.md} lg={screenSize.lg}>
                <DataBaseButtons href={'dbs/odometry'} Title={'Odometry'} Icon={TireRepair} />
            </Grid>
            <Grid item xs={screenSize.xs} sm={screenSize.sm} md={screenSize.md} lg={screenSize.lg}>
                <DataBaseButtons href={'dbs/batteryCharge'} Title={'Battery status'} Icon={BatteryCharging90} />
            </Grid>
            <Grid item xs={screenSize.xs} sm={screenSize.sm} md={screenSize.md} lg={screenSize.lg}>
                <DataBaseButtons href={'dbs/batteryPhysical'} Title={'Battery physical status'} Icon={BatterySaver} />
            </Grid>
            <Grid item xs={screenSize.xs} sm={screenSize.sm} md={screenSize.md} lg={screenSize.lg}>
                <DataBaseButtons href={'dbs/fiducial'} Title={'Fiducial marks'} Icon={QrCode2} />
            </Grid>
            <Grid item xs={screenSize.xs} sm={screenSize.sm} md={screenSize.md} lg={screenSize.lg}>
                <DataBaseButtons href={'dbs/gyroscope'} Title={'Gyroscope'} Icon={Explore} />
            </Grid>
            <Grid item xs={screenSize.xs} sm={screenSize.sm} md={screenSize.md} lg={screenSize.lg}>
                <DataBaseButtons href={'dbs/globalPosition'} Title={'Global position'} Icon={GpsFixed} />
            </Grid>
        </Grid>
    );
};

export default DataBase;
