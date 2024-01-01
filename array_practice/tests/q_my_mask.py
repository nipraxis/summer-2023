test = {
  'name': 'Question my_mask',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'my_mask'
          >>> 'my_mask' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'my_mask'
          >>> # from its initial state (of ...)
          >>> my_mask is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> my_mask.shape == (3, 4)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Are these Boolean values.
          >>> my_mask.dtype == np.dtype(bool)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(my_mask == [[False, True, True, False],
          ...                    [False, True,  False, False],
          ...                    [False, False, False, False]])
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
