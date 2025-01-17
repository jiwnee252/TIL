## git 명령어

git config --global alias.st status

git add -A / 모든 수정사항 저장

git commit -a / add and commit
______________

git config --global --list

git config --unset --global user.name  
git config --unset --global user.email

git config --global user.name name  
git config --global user.email email
______________

git commit시  
i 텍스트 입력  
esc 입력 종료  
:wq 나가기
______________

git remote -v 현재 로컬 저장소에 등록된 원격 저장소 목록 보기  
git remote rm 원격_저장소_이름 현재 로컬 저장소에 등록된 원격 저장소 삭제 
______________

git reset --옵션 --commitid 특정 commit으로 되돌아가고 이후의 commit은 삭제  
--soft 삭제된 commit의 기록을 staging area에 남김  
--mixed 삭제된 commit의 기록을 wordking directory에 남김 (기본 옵션)   
--hard 삭제된 commit의 기록을 남기지 않음  
______________

git reflog

______________

git restore --staged <file> staging area에 올라간 파일 unstage하기기

______________


#### 참고

git commit message convention  

gitignore.io

git help / 도움말  
git help commit

git flow