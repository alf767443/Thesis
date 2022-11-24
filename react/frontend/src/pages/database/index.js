import { useState } from 'react';

// material-ui
import { Grid, Box, Typography, Stack } from '@mui/material';
import { TireRepair, Add } from '@mui/icons-material';
import MainCard from 'components/MainCard';
// project import
import DataBaseButtons from './buttons/button';
import { OdometryCard } from 'tables/Odometry/index';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const DataBase = () => {
    return (
        <Grid container rowSpacing={3} columnSpacing={1.25}>
            {/* Main block */}
            <DataBaseButtons href={'dbs/odometry'} Title={'Odometry'} Icon={TireRepair} />
        </Grid>
    );
};

export default DataBase;
