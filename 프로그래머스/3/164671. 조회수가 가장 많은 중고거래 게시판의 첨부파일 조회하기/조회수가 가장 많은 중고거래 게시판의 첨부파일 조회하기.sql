-- 코드를 입력하세요
# SELECT concat('/home/grep/src/',b.board_id,'/',b.file_id ,b.file_name, b.file_ext) as file_path
# from used_goods_board a join used_goods_file b on a.board_id = b.board_id
# where a.views = (select max(views) from used_goods_board)
# -- 게시글 하나에 여러개의 상품 이미지 및 동영상이 있을 수 있기 때문에 이런식으로 찾아야 함.
# -- a.views desc = x
# order by b.file_id desc;

select concat('/home/grep/src/', b.board_id, '/', b.file_id, b.file_name, b.file_ext) as file_path
from used_goods_board a join used_goods_file b on a.board_id = b.board_id
where a.views = (select max(views) from used_goods_board)
order by b.file_id desc
;





















