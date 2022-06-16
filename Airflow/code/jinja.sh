#!/bin/bash

# NO Jinja


# dag 정보와 task 정보를 Jinja template으로 불러올 수 있습니다.
echo "{{ dag }}, {{ task }}"

echo "ds : {{ ds }}"
echo "ds_nodash : {{ ds_nodash }}"
echo "prev_ds : {{ prev_ds }}"
echo "prev_ds_nodash : {{ prev_ds_nodash }}"
echo "next_ds : {{ next_ds }}"
echo "next_ds_nodash : {{ next_ds_nodash }}"
echo "yesterday_ds : {{ yesterday_ds }}"
echo "yesterday_ds_nodash : {{ yesterday_ds_nodash }}"
echo "tomorrow_ds : {{ tomorrow_ds }}"
echo "tomorrow_ds_nodash : {{ tomorrow_ds_nodash }}"
echo "ts : {{ ts }}"
echo "ts_nodash : {{ ts_nodash }}"
echo "ts_nodash_with_tz : {{ ts_nodash_with_tz }}"
echo "macros.ds_add(ds, 2) : {{ macros.ds_add(ds, 2) }}"
echo "macros.ds_add(ds, -2) : {{ macros.ds_add(ds, -2) }}"
echo "macros.ds_format(ds, '%Y-%m-%d', '%Y__%m__%d'): {{ macros.ds_format(ds, '%Y-%m-%d', '%Y__%m__%d') }}"
echo "macros.datetime.now() : {{ macros.datetime.strftime(macros.datetime.now(), '%Y%m%d%H') }}"


# dag 정보와 task 정보를 Jinja template으로 불러올 수 있습니다.
echo "{{ dag }}, {{ task }}"

# dag file에서 전달해 준 test 파라미터는 다음과 같이 쓸 수 있습니다.
echo "{{ params.test }}"

# execution_date를 표현합니다.
echo "execution_date : {{ execution_date }}"
echo "ds: {{ds}}"

# macros를 이용하여 format과 날짜 조작이 가능합니다.
echo "the day after tommorow with no dash format"
echo "{{ macros.ds_format(macros.ds_add(ds, days=2),'%Y-%m-%d', '%Y%m%d') }}"

# for, if 예제입니다.
{% for i in range(5) %}
	echo "{{ i }} {{ ds }}"
  {% if i%2 == 0  %}
		echo "{{ ds_nodash }}"
  {% endif %}
{% endfor %}
