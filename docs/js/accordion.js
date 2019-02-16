$(function(){
    //.pagetreeの中のdiv要素がクリックされたら
	$('.pagetree .pagetree-accordion').click(function(){
		//クリックされた.tocの中のdiv要素に隣接するul要素が開いたり閉じたりする。
		$(this).next('ul').slideToggle();
	});
});
