test = {
  'name': 'Question a',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'a'
          >>> 'a' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The variable 'a' should contain an array.
          >>> isinstance(a, np.ndarray)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # a should be shape (3, 4)
          >>> a.shape == (3, 4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Please check the array values.
          >>> np.all(a == [[2, 7, 12, 0],
          ...              [3, 9, 3, 4],
          ...              [4, 0, 1,  3]])
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
