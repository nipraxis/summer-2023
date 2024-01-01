test = {
  'name': 'Question off_stripe',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'off_stripe'
          >>> 'off_stripe' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'off_stripe'
          >>> # from its initial state (of ...)
          >>> off_stripe is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> off_stripe.shape == (6, 6)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Are these integers of some sort?
          >>> off_stripe.dtype.type in np.sctypes['float']
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(off_stripe == [[0., 0., 0., 0., 0., 0.],
          ...                       [2., 0., 0., 0., 0., 0.],
          ...                       [0., 3., 0., 0., 0., 0.],
          ...                       [0., 0., 4., 0., 0., 0.],
          ...                       [0., 0., 0., 5., 0., 0.],
          ...                       [0., 0., 0., 0., 6., 0.]])
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
