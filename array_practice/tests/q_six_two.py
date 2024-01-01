test = {
  'name': 'Question six_two',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'six_two'
          >>> 'six_two' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'six_two'
          >>> # from its initial state (of ...)
          >>> six_two is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> six_two.shape == (4, 4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Are these integers of some sort?
          >>> six_two.dtype.type in np.sctypes['int']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(six_two == [[1, 1, 1, 1],
          ...                    [1, 1, 1, 1],
          ...                    [1, 1, 1, 2],
          ...                    [1, 6, 1, 1]])
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
