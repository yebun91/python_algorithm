# 리스트
# 파이썬 리스트의 가장 좋은 점은 사실상 스택을 사용할지, 큐를 사용할지 고민하지 않아도 된다는 점이다.
# 리스트는 다양한 기능을 제공하면서도 O(1)에 실행 가능한 연산들도 몇 가지 있다.
# 리스트 마지막 요소를 .append()로 추가하거나, 리스트 마지막 요소를 pop()으로 추출하거나, 원하는 인덱스의 요소를 조회 하는 연산은 모두 O(1)이다.
# 반면 요소를 삭제하거나 규의 연산이기도 한 첫 번쨰 요소를 추출하는 pop(0)은 O(n)이다. 따라서 리스트에 주로 큐의 연산을 사용할 때는 주의가 필요하다.

# len(a) = O(1), a[i] = O(1), a[i:j] = O(k)
# i in a = O(n), a.count(elem) = O(n), a.index(elem) = O(n)
# a.append(elem) = O(1), a.pop = O(1), a.pop(0) = O(n)
# del a[i] = O(n), a.sort = O(n log n), min(a), max(a) = O(n), a.revers() = O(n)

import collections

a = list()
b = []  # 간단하게 선언할 수 있음.
c = [1, 2, 3]
print(c)
c.append(4)
print(c)
c.insert(3, 5)
print(c)
c.append('안뇽')
c.append(True)
print(c)
print(c[3])
print(c[1:3])
print(c[:3])
del c[1]
print(c)
c.remove(3)
print(c)
print(c.pop(3))
print(c)

# 딕셔너리
# 키/값 구조로 이루어진 딕셔너리를 말한다. 파이썬 3.7+에서는 입력 순서가 유지되며, 내부적으로는 해시 테이블로 구현되어 있다.

# len(a) = O(1), a[key] = O(1), a[key] = value = O(1), key in a = O(1)
# 이처럼 딕셔너리는 대부분의 연산이 O(1)에 처리 가능한 매우 우수한 자료형이다.

a = dict()
b = {}  # 중괄호를 써서 좀 더 간단하게 선언할 수 있다.
c = {'key1': 'value1', 'key2': 'value2'}
print(c)
c['key3'] = 'value3'
print(c)
print(c['key1'])
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키임당.')
print('key4' in a)
if 'key4' in a:
    print("존재하는 키")
else:
    print("존재하지 않는 키")
for key, value in c.items():
    print(key, value)
del c['key1']
print(c)

# defaultdict 객체
# 존재하지 않는 키를 조회할 경우 에러메시지를 출력하는 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.
d = collections.defaultdict(int)
d['A'] = 5
d['B'] = 4
print(d)
d['C'] += 1
print(d)
# C는 존재하지 않는 키다. 원래의 딕셔너리라면 keyError가 발생했겠지만 defaultdict 객체는 에러 없이 바로 +1 연산이 가능하고
# 이 경우 디폴트인 0을 기준으로 자동으로 생성한 후 여기에 1을 더해 최종적으로 1이 만들어진다.

# Counter 객체
# Counter 객체는 아이템에 대한 개수를 계산해 딕셔너리로 리턴하며, 다음과 같이 사용한다.
e = [1, 2, 3, 4, 5, 5, 5, 6, 6]
f = collections.Counter(e)
print(f)
# 개수를 자동으로 계산해주기 때문에 매우 편리하며 여러 분야에서 다양하게 활용된다.
print(f.most_common(2))
# 이처럼 가장 빈도가 높은 2개의 요소를 추출하면 [(5, 3), (6, 2)]를 결과로 추출한다.

# OrderedDict 객체
# 대부분의 언어에서 해시 테이블을 이용한 자료형은 입력 순서가 유지되지 않는다.
# 파이썬도 3.6 이하에서는 마찬가지였고 입력 순서가 유지되는 OrderedDict라는 별도의 객체를 제공했다.
# 다음과 같이 입력값을 부여할 경우 OrderedDict는 입력 그대로 순서가 유지된다.
print(collections.OrderedDict(
    {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}))
# 그러나 파이썬 3.7부터는 딕셔너리는 내부적으로 인텍스를 이용하며 입력 순서가 유지되도록 개선됐다.

type([])  # <Class 'list'>
type(())  # <Class 'tuple'>
type({})  # <Class 'dict'>
type({1})  # <Class 'set'>
# 딕셔너리와 집합은 같은 중괄호를 사용하지만 키의 존재 유무로 서로 다른 자료형으로 선언된다.
