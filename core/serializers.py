def page_serializer(page):
	return {
		'username': page.username,
		'url' : page.url,
		'insta_id' : page.insta_id,
		'full_name' : page.full_name,
		'country_code' : page.country_code,
		'is_varified' : page.is_varified,
		'is_private' : page.is_private,
		'is_join_recently' : page.is_join_recently,
		'is_business_account' : page.is_business_account,
		'business_category_name' :  page.business_category_name,
		'num_posts' : page.num_posts,
		'num_follower' : page.num_follower,
		'num_following' : page.num_following,
		'biography' : page.biography,
	}
