"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
              "theme=light; sessionToken=abc123", "theme"
            ],
            "answer": "light"
        },
        {
            "input": [
              "_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true", "ffo"
            ],
            "answer": "true"
        }
        
    ],
    "Extra": [
        {
            "input": ["domain=checkio.org; theme=dark", "domain"],
            "answer": "checkio.org"
        },
        {
            "input": ["ffo=false; domain=google.com; expires=Sunday, 20-May-2018 00:00:00 GMT", "expires"],
            "answer": "Sunday, 20-May-2018 00:00:00 GMT"
        },
	{
            "input": ["USER=Mr.Smith; path=/home", "path"],
            "answer": '/home'
        },
	{
            "input": ["USER=name=Unknown; domain=bbc.com", "USER"],
            "answer": 'name=Unknown'
        }
    ]
}
