COVERAGE_TMPDIR=.coverage-html
PY3_TMPDIR=.py3tmp
NAME=etreehtml

default: all

all: test test-py25 test-py2to3 test-py3

test:
	nosetests --with-coverage --cover-erase --cover-package etreehtml --cover-html "--cover-html-dir=${COVERAGE_TMPDIR}" test_${NAME}.py
	@rm -f test_${NAME}.py,cover

test-py25:
	python2.5 test_${NAME}.py
	rm -f ${NAME}.pyc

test-py2to3:
	mkdir -p '${PY3_TMPDIR}'
	cp ${NAME}.py test_${NAME}.py '${PY3_TMPDIR}'
	2to3 -w -n --no-diffs '${PY3_TMPDIR}/${NAME}.py' '${PY3_TMPDIR}/test_${NAME}.py'
	python3 '${PY3_TMPDIR}/test_${NAME}.py'
	rm -rf '${PY3_TMPDIR}'

test-py3:
	python3 test_${NAME}.py

coverage-display: test
	xdg-open '${COVERAGE_TMPDIR}/${NAME}.html'

cd: coverage-display


clean:
	rm -fr -- '${PYTEST_TMP}' '${COVERAGE_TMPDIR}' .coverage '${PY3_TMPDIR}' ${NAME}.pyc ${NAME}.py,cover

.PHONY: default all gen-pytest-script test test-py25 test-py2to3 test-py3 coverage coverage-display cd clean
