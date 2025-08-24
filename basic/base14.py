# セット

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

# 和集合(2つの集合を重複なしに結合)
u = s | t
u = s.union(t)
print(sorted(u))

# 積集合(2つの集合の共通要素)
u = s & t
u = s.intersection(t)
print(sorted(u))

# 差集合(sにあってtにない要素)
u = s - t
u = s.difference(t)
print(sorted(u))

# 対称差集合(2つの集合のどちらかにあって共通要素にない要素)
u = s ^ t
u = s.symmetric_difference(t)
print(sorted(u))

s |= t
print(s)

# issubset, issuperset, isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

# 部分集合かどうか
print(s.issubset(t))
# 上位集合かどうか
print(t.issuperset(s))
# 共通要素がないかどうか
print(t.isdisjoint(s))
print(t.isdisjoint(u))