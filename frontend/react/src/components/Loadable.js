// eslint-disable-next-line react/display-name
import { Suspense } from 'react';

// project import
import Loader from './Loader';

// ==============================|| LOADABLE - LAZY LOADING ||============================== //

const Loadable = (Component) => (props) =>

    Loadable.displayName = 'Loadable';
    (
        <Suspense fallback={<Loader />}>
            <Component {...props} />
        </Suspense>
    );


export default Loadable;

