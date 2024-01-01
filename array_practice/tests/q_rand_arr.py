test = {
  'name': 'Question rand_arr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'rand_arr'
          >>> 'rand_arr' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Should be an array
          >>> isinstance(rand_arr, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> rand_arr.shape == (3, 5)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
        # Quick test for limits on means.
        # arr = rng.standard_normal(size=(10000, 15))
        # means = np.mean(arr, axis=1)
        # print(means.min(), means.max())
          'code': r"""
          >>> # If these are really from a standard normal
          >>> # the mean of all the numbers should be between -1 and 1
          >>> -1 < np.mean(rand_arr) < 1
          True
          >>> # Likewise the standard deviation should be between 0.35 and 1.9
          >>> 0.35 < np.std(rand_arr) < 1.9
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
