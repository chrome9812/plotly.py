import plotly
from plotly.graph_objs import *
import plotly.tools as tls
from nose.tools import raises
import numpy as np


@raises(Exception)
def unequal_xy_length():
    data = tls.Quiver(x=[1, 2], y=[1], u=[1, 2], v=[1, 2])


@raises(Exception)
def unequal_uv_length():
    data = tls.Quiver(x=[1, 2], y=[1, 3], u=[1], v=[1, 2])


@raises(Exception)
def test_wrong_kwarg():
    data = tls.Quiver(stuff='not gonna work')


def test_one_arrow():
    nan = np.nan
    trace1 = Scatter(
            x=[0., 1., nan],
            y=[0., 1., nan],
            mode='lines',
            name='Barb',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    trace2 = Scatter(
            x=[0.82069826, 1., 0.61548617, nan],
            y=[0.61548617,  1.,  0.82069826, nan],
            mode='lines',
            name='Arrow',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    expected = Data([trace1, trace2])

    data = tls.Quiver(x=[0], y=[0], u=[1], v=[1], scale=1)

    np.testing.assert_almost_equal(data[0]['y'], expected[0]['y'])
    np.testing.assert_almost_equal(data[0]['x'], expected[0]['x'])
    np.testing.assert_almost_equal(data[1]['y'], expected[1]['y'])
    np.testing.assert_almost_equal(data[1]['x'], expected[1]['x'])
    assert data[0].keys() == expected[0].keys()


def test_complicated():
    nan = np.nan
    trace1 = Scatter(
            x=[0.0, 0.1, nan, 0.0, 0.1, nan, 0.0, 0.1, nan, 0.0, 0.1, nan,
               0.7853981633974483, 0.856108841516103, nan, 0.7853981633974483,
               0.856108841516103, nan, 0.7853981633974483, 0.856108841516103,
               nan, 0.7853981633974483, 0.856108841516103, nan,
               1.5707963267948966, 1.5707963267948966, nan, 1.5707963267948966,
               1.5707963267948966, nan, 1.5707963267948966, 1.5707963267948966,
               nan, 1.5707963267948966, 1.5707963267948966, nan,
               2.356194490192345, 2.2854838120736902, nan, 2.356194490192345,
               2.2854838120736902, nan, 2.356194490192345, 2.2854838120736902,
               nan, 2.356194490192345, 2.2854838120736902, nan],
            y=[0.0, 0.0, nan, 0.7853981633974483, 0.856108841516103, nan,
               1.5707963267948966, 1.6707963267948966, nan, 2.356194490192345,
               2.4269051683109994, nan, 0.0, 0.0, nan, 0.7853981633974483,
               0.856108841516103, nan, 1.5707963267948966, 1.6707963267948966,
               nan, 2.356194490192345, 2.4269051683109994, nan, 0.0, 0.0, nan,
               0.7853981633974483, 0.856108841516103, nan, 1.5707963267948966,
               1.6707963267948966, nan, 2.356194490192345, 2.4269051683109994,
               nan, 0.0, 0.0, nan, 0.7853981633974483, 0.856108841516103, nan,
               1.5707963267948966, 1.6707963267948966, nan, 2.356194490192345,
               2.4269051683109994, nan],
            mode='lines',
            name='Barb',
            line=Line(color='rgb(114, 132, 314)', width=2)
            )
    trace2 = Scatter(
            x=[0.07690301168721783, 0.1, 0.07690301168721783, nan,
               0.0836679629390453, 0.1, 0.07013806043539038, nan,
               0.08647009749634509, 0.1, 0.06733592587809059, nan,
               0.08366796293904528, 0.1, 0.07013806043539039, nan,
               0.8397768044551484, 0.856108841516103, 0.8397768044551484, nan,
               0.8465417557069758, 0.856108841516103, 0.8330118532033208, nan,
               0.8493438902642756, 0.856108841516103, 0.830209718646021, nan,
               0.8465417557069758, 0.856108841516103, 0.8330118532033208, nan,
               nan, 1.5707963267948966, nan, nan, 1.577561278046724,
               1.5707963267948966, 1.564031375543069, nan, 1.5803634126040238,
               1.5707963267948966, 1.5612292409857693, nan, 1.577561278046724,
               1.5707963267948966, 1.564031375543069, nan, 2.3018158491346448,
               2.2854838120736902, 2.3018158491346448, nan, 2.3085808003864723,
               2.2854838120736902, 2.2950508978828172, nan, 2.3113829349437722,
               2.2854838120736902, 2.2922487633255177, nan, 2.3085808003864723,
               2.2854838120736902, 2.2950508978828172, nan],
            y=[-0.009567085809127246, 0.0, 0.009567085809127246, nan,
               0.8302097186460211, 0.856108841516103, 0.8493438902642756, nan,
               1.6381322526729871, 1.6707963267948966, 1.6572664242912416, nan,
               .4010060454409174, 2.4269051683109994, 2.420140217059172, nan,
               -0.00676495125182746, 0.0, 0.00676495125182746, nan,
               0.8330118532033208, 0.856108841516103, 0.8465417557069758, nan,
               1.640934387230287, 1.6707963267948966, 1.6544642897339419, nan,
               2.4038081799982174, 2.4269051683109994, 2.4173380825018724, nan,
               nan, 0.0, nan, nan, 0.8397768044551484, 0.856108841516103,
               0.8397768044551484, nan, 1.6476993384821144, 1.6707963267948966,
               1.6476993384821144, nan, 2.410573131250045, 2.4269051683109994,
               2.410573131250045, nan, 0.0067649512518274495, 0.0,
               -0.0067649512518274495, nan, 0.8465417557069758,
               0.856108841516103, 0.8330118532033208, nan, 1.6544642897339419,
               1.6707963267948966, 1.640934387230287, nan, 2.4173380825018724,
               2.4269051683109994, 2.4038081799982174, nan],
            mode='lines',
            name='Arrow',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    expected = Data([trace1, trace2])

    x, y = np.meshgrid(np.arange(0, np.pi, .5), np.arange(0, np.pi, .5))
    u = np.cos(x)
    v = np.sin(y)
    data = tls.Quiver(x, y, u, v, scale=.1, angle=np.pi/8,
                      arrow_scale=.25, barb_width=2)

    np.testing.assert_almost_equal(data[0]['y'], expected[0]['y'])
    np.testing.assert_almost_equal(data[0]['x'], expected[0]['x'])
    # np.testing.assert_almost_equal(data[1]['y'], expected[1]['y'])
    # np.testing.assert_almost_equal(data[1]['x'], expected[1]['x'])
    assert data[0].keys() == expected[0].keys()
