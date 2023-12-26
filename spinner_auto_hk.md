'''
Spinner automation script
1. Auto-MD
2. NNP
3. Spinner

설정해줘야하는 것
1. auto-md
- batch.j에서
    - md_src 경로
- configure.yaml에서
    - 물질명
    - POTCAR 경로
- main.py에서
    - Output 경로(이미 설정되어 있긴 함)
- prdf/batch.j에서
    - pos2lammps 경로(prdf폴더에 있음)
    - lmp_serial 경로

2. NNP
- input.yaml에서
    - param의 원소와 param 경로
    - gpu/cpu 사용 여부
- structure_list에서
    - melt, quench, anneal 데이터(OUTCAR) 경로
continue.py로 자동생성 해준다던데 그걸 봐야할듯

3. Spinner
- 
'''