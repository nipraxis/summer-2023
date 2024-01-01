test = {
  'name': 'Question rand_arr_10_20',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'rand_arr_10_20'
          >>> 'rand_arr_10_20' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Should be an array
          >>> isinstance(rand_arr_10_20, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> rand_arr_10_20.shape == (10, 20)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        # Quick test for limits on means.
        # arr = rng.standard_normal(size=(10000, 200))
        # means = np.mean(arr, axis=1)
        # print(means.min(), means.max())
          'code': r"""
          >>> # If these are really from a standard normal
          >>> # the mean of all the numbers should be between -0.26 and 0.26
          >>> -0.26 < np.mean(rand_arr_10_20) < 0.26
          True
          >>> # Likewise the standard deviation should be between 0.79 and 1.19
          >>> 0.79 < np.std(rand_arr_10_20) < 1.19
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
