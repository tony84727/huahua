FROM python:3.9.6-buster
RUN pip install pipenv --no-cache-dir
COPY Pipfile ./
COPY Pipfile.lock ./
COPY . .
RUN pipenv install --system --deploy && rm Pipfile Pipfile.lock && pip uninstall -y pipenv
CMD [ "python", "./bot.py" ]