import { useState } from 'react';

// material-ui
import { Grid, Box, Typography, Stack } from '@mui/material';
import MainCard from 'components/MainCard';
// project import
import OdometryButton from './buttons/odometry';
import Odometry from './odometry';

// ==============================|| DASHBOARD - DEFAULT ||============================== //

const DataBase = () => {
    return (
        <Grid container rowSpacing={3} columnSpacing={1.25}>
            {/* Main block */}
            <OdometryButton />
        </Grid>
    );
};

export default DataBase;
