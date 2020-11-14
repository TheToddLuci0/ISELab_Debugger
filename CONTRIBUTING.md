# Contribution Guide
This project was done as an academic work, and will likely not receive active
development after my graduation. That said, I am happy to accept pull requests.


## Guidelines
1. Follow [PEP 8](https://pep8.org/)
1. Additions must be useful in the educational lab environments (in other words,
there's no point writing support for an obscure protocol like 9P or Token Ring)

## Process for Adding New Protocols
1. Add an action in [actions.py](./base/actions.py) to test the protocol
1. Build a form in [forms.py](base/forms.py) to gather the user data needed to test
1. Build a service check template in [base/templates/base/services](base/templates/base/services)
   1. You should include helpful resolution steps for errors your check detects
1. Build a view in [views.py](base/views.py) to route the requests
1. Add a URL path to [urls.py](ISELab_debugger/urls.py)
1. (Optional, but encouraged) Write tests for your code