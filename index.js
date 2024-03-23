import TrendGraph from './src/components/TrendGraph';
import MultiGraph from './src/components/MultiGraph';
import LinearTrendChart from './src/components/Trends/LinearTrendChart';
import MovingAverageTrendChart from './src/components/Trends/MovingAverageTrendChart';
import ExponentialSmoothingChart from './src/components/Trends/ExponentialSmoothingChart';
import OutlierIQRScatterChart from './src/Outlier/OutlierIQRScatterChart';
import OutlierZScoreScatterChart from './src/Outlier/OutlierZScoreScatterChart';
import OutlierKNNScatterChart from './src/Outlier/OutlierKNNScatterChart';
import ARIMAForecastChart from './src/components/Forcasting/ARIMAForecastChart';
import SARIMAForecastChart from './src/components/Forcasting/SARIMAForecastChart';


export default{ TrendGraph , MultiGraph , LinearTrendChart , MovingAverageTrendChart , ExponentialSmoothingChart , OutlierIQRScatterChart , OutlierZScoreScatterChart , OutlierKNNScatterChart , ARIMAForecastChart , SARIMAForecastChart };