import * as React from 'react';
import { Icon, IconButton, Box, Typography, Stack } from '@mui/material';
import TireRepairIcon from '@mui/icons-material/TireRepair';
import MainCard from 'components/MainCard';

import styles from './styles';

const Title = () => {
    return <>Odometry</>;
};

export default function ContainedButtons() {
    return (
        <MainCard sx={styles.maincard.sx} content={styles.maincard.content}>
            <Box sx={styles.box.sx}>
                <Stack spacing={styles.stack.spacing} direction={styles.stack.direction} alignItems={styles.stack.alignItems}>
                    <Typography variant={styles.typography.variant} color={styles.typography.color}>
                        <Title />
                    </Typography>
                    <IconButton
                        color={styles.icon.color}
                        style={styles.button.style}
                        iconStyle={styles.icon.style}
                        sx={styles.button.sx}
                        href="odometry"
                    >
                        <TireRepairIcon sx={styles.icon.style} />
                    </IconButton>
                </Stack>
            </Box>
        </MainCard>
    );
}
