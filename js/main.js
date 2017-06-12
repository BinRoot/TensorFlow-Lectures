$('[data-toggle="popover"]').popover({
    trigger: 'hover',
        'placement': 'bottom'
});

//// nav-bar visual improvements
var path = window.location.pathname;
var dropdown_dict = {
    'my-dropdown-getting-started': ['lec_workshop', 'lec_ml', 'lec_tf_intro', 'lec_tf_install', 'lec_tensorboard'],
    'my-dropdown-classic-algs': ['lec_reg', 'lec_class', 'lec_cnn', 'lec_rnn', 'lec_autoencoder'],
    'my-dropdown-embeddings': ['lec_w2v_paper', 'lec_w2v.html', 'lec_w2v_tb', 'lec_w2v_optimized', 'lec_sense2vec_paper'],
    'my-dropdown-extra': ['lec_queue', 'lec_serving']
};
var break_out = false;
for (var dropdown_name in dropdown_dict) {
    if (dropdown_dict.hasOwnProperty(dropdown_name)) {
	for (var page_idx = 0; page_idx < dropdown_dict[dropdown_name].length; page_idx++) {
	    if (path.includes(dropdown_dict[dropdown_name][page_idx])) {
		// bold the dropdown
		$('.' + dropdown_name).css('font-weight', 'bold');
		
		// bold the item in the dropdown
		var all_lis = $($('.' + dropdown_name).parent().children()[1]).find('a');
		for (var li_idx = 0; li_idx < all_lis.length; li_idx++) {
		    if(path.includes($(all_lis[li_idx]).attr('href'))) {
			$(all_lis[li_idx]).css('font-weight', 'bold');
		    }
		}

		// quit searching
		break_out = true;
		break;
	    }
	} // end for
	if (break_out) break;
    }
}
