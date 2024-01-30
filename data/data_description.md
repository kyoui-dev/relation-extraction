# Data description

## id
- 각 데이터를 구분하는 key

## sentence
- 문장 데이터

## subject_entity
- subject_word, 문장 내 subject_word가 위치한 index, subject_type에 관한 정보를 포함

## object_entitiy
- object_word, 문장 내 object_word가 위치한 index, object_type에 관한 정보를 포함

## entity_type
  - ORG: 조직 혹은 단체
  - PER: 사람
  - POH: 그 외 고유 명사
  - DAT: 날짜 혹은 시간
  - LOC: 위치, 장소
  - NOH: 그 외 숫자를 나타내는 데이터

## source
- 데이터가 수집된 출처
    - wikipedia, wikitree, policy_briefing

## label
- subject entity와 object entity 간 의미론적 관계

### no_relation
- 관계 없음

### org:top_members/employees
- 조직의 대표자 또는 구성원
- expected_entity_type: {subject_type: 'ORG', object_type:'PER'}

### org:members
- 조직에 속한 조직, A⊃B
- expected_entity_type: {subject_type: 'ORG', object_type: 'ORG'}

### org:product
- 조직에서 생산된 제품 또는 상품
- expected_entity_type {subject_type: 'ORG', object_type: 'POH'}

### per:title
- 사람의 직업상 지위를 나타내는 공식 또는 비공식 명칭
- expected_entity_type: {subject_type: 'PER', object_type: 'POH'}

### org:alternate_names
- 조직이 불리는 다른 이름
- expected_entity_type: {subject_type: 'ORG', object_type: 'ORG'}

### per:employee_of
- 사람이 일하는 조직
- expected_entity_type: {subject_type: 'PER', object_type: 'ORG'}

### org:place_of_headquarters
- 조직의 본사가 위치한 장소
- expected_entity_type: {subject_type: 'ORG', object_type:'LOC'}

### per:product
- 사람이 만든 제품 또는 예술품
- expected_entity_type: {subject_type: 'PER', object_type: 'POH'}

### org:number_of_employees/members
- 조직에 구성된 총 구성원 수
- expected_entity_type: {subject_type: 'ORG', object_type: 'NOH'}

### per:children
- 사람의 자녀
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### per:place_of_residence
- 사람이 거주하는 장소
- expected_entity_type: {subject_type: 'PER', object_type: 'LOC'}

### per:alternate_names
- 사람이 불리는 다른 이름
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### per:other_family
- 사람의 부모, 자녀, 형제자매 및 배우자 이외의 가족
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### per:colleagues
- 사람과 함께 일하는 사람
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### per:origin
- 사람의 출신 또는 국적
- expected_entity_type: {subject_type: 'PER', object_type: 'LOC'}

### per:siblings
- 사람의 형제자매
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### per:spouse
- 사람의 배우자
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### org:founded
- 조직이 설립된 날짜
- expected_entity_type: {subject_type: 'ORG', object_type:'DAT'}

### org:political/religious_affiliation
- 조직이 소속된 정치/종교 단체, A⊂B
- expected_entity_type: {subject_type: 'ORG', object_type: 'ORG'}

### org:member_of
- 조직이 속한 조직, A⊂B
- expected_entity_type: {subject_type: 'ORG', object_type: 'ORG'}

### per:parents
- 사람의 부모
- expected_entity_type: {subject_type: 'PER', object_type: 'PER'}

### org:dissolved
- 조직이 해산된 날짜
- expected_entity_type: {subject_type: 'ORG', object_type:'DAT'}

### per:schools_attended
- 사람이 다녔던 학교
- expected_entity_type: {subject_type: 'PER', object_type: 'ORG'}

### per:date_of_death
- 사람이 사망한 날짜
- expected_entity_type: {subject_type: 'PER', object_type: 'DAT'}

### per:date_of_birth
- 사람이 태어난 날짜
- expected_entity_type: {subject_type: 'PER', object_type: 'DAT'}

### per:place_of_birth
- 사람이 태어난 장소
- expected_entity_type: {subject_type: 'PER', object_type: 'LOC'}

### per:place_of_death
- 사람이 사망한 장소
- expected_entity_type: {subject_type: 'PER', object_type: 'LOC'}

### org:founded_by
- 조직을 설립한 사람
- expected_entity_type: {subject_type: 'ORG', object_type: 'PER'}

### per:religion
- 사람이 믿는 종교
- expected_entity_type: {subject_type: 'PER', object_type: 'ORG'}