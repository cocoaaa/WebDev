# -*- coding: utf-8 -*-
"""
Udacity WebDev Lec5 
Created on Mon Jan 25 10:29:58 2016
@author: hjsong
"""
#
#import urllib2
#from xml.dom import minidom
##1. URL
#p = urllib2.urlopen("http://www.google.com")
#c = p.read()
#print dir(p)
#p.url
#p.readline
#p.headers
#p.headers.items()
#p.headers['content-type']
#p.headers['server']

#2.Rss
#dom = minidom.parseString('''
#<breakfast_menu>
#   <food>
#       <name>Belgian Waffles</name>
#       <price>$5.95</price>
#       <description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
#       <calories>650</calories> </food>
#   <food>
#       <name>Strawberry Belgian Waffles</name>
#       <price>$7.95</price>
#       <description>Light Belgian waffles covered with strawberries and whipped cream</description>
#       <calories>900</calories> </food>
#   <food>
#       <name>Berry-Berry Belgian Waffles</name>
#       <price>$8.95</price>
#       <description>Light Belgian waffles covered with an assortment of fresh berries and whipped cream</description>
#       <calories>900</calories> </food>
#   <food>
#       <name>French Toast</name>
#       <price>$4.50</price>
#       <description>Thick slices made from our homemade sourdough bread</description>
#       <calories>600</calories> </food>
#   <food>
#       <name>Homestyle Breakfast</name>
#       <price>$6.95</price>
#       <description>Two eggs, bacon or sausage, toast, and our ever-popular hash browns</description>
#       <calories>950</calories> </food>
#</breakfast_menu>''')
#
#names = dom.getElementsByTagName("name")
#res = [n.childNodes[0].nodeValue for n in names]
#print res

#3. JSON
#import json
#j = '{"one": 1, "numbers": [1,2,3,5]}'
#json.loads(j)
#never do eval(j) - insecure

#quiz
#
#reddit_front = r"""{"kind": "Listing", "data": {	"modhash": "", "children": [{
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "funny","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srqb9","clicked": false,"title": "Using christmas lights as an extension","num_comments": 632,"score": 3262,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh33","link_flair_css_class": null,"author_flair_css_class": null,"downs": 8002,"is_self": false,"permalink": "/r/funny/comments/srqb9/using_christmas_lights_as_an_extension/","name": "t3_srqb9","created": 1335386727.0,"url": "http://i.imgur.com/crtCF.jpg","author_flair_text": null,"author": "talldarkandasian","created_utc": 1335361527.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 11264}}, {
#			"kind": "t3",	"data": {"domain": "imgur.com","banned_by": null,"media_embed": {},"subreddit": "pics","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srrqf","clicked": false,"title": "I've never felt so judged in all my life","num_comments": 161,"score": 1881,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://a.thumbs.redditmedia.com/QYUms1MKw7jPbTkH.jpg","subreddit_id": "t5_2qh0u","link_flair_css_class": null,"author_flair_css_class": null,"downs": 3060,"is_self": false,"permalink": "/r/pics/comments/srrqf/ive_never_felt_so_judged_in_all_my_life/","name": "t3_srrqf","created": 1335388714.0,"url": "http://imgur.com/dM8Cx","author_flair_text": null,"author": "erikarew","created_utc": 1335363514.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 4941}}, {
#			"kind": "t3",	"data": {"domain": "quickmeme.com","banned_by": null,"media_embed": {},"subreddit": "AdviceAnimals","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srrbx","clicked": false,"title": "Sitting Frog","num_comments": 157,"score": 2176,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://b.thumbs.redditmedia.com/NVRS9TvJoNklQPD1.jpg","subreddit_id": "t5_2s7tt","link_flair_css_class": "approved","author_flair_css_class": null,"downs": 5701,"is_self": false,"permalink": "/r/AdviceAnimals/comments/srrbx/sitting_frog/","name": "t3_srrbx","created": 1335388157.0,"url": "http://www.quickmeme.com/meme/3oyom1/","author_flair_text": null,"author": "mendicant","created_utc": 1335362957.0,"link_flair_text": "up and coming","media": null,"num_reports": null,"ups": 7877}}, {
#			"kind": "t3",	"data": {"domain": "nation.foxnews.com","banned_by": null,"media_embed": {},"subreddit": "politics","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srrch","clicked": false,"title": "Gingrich drops out","num_comments": 439,"score": 1401,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2cneq","link_flair_css_class": null,"author_flair_css_class": null,"downs": 880,"is_self": false,"permalink": "/r/politics/comments/srrch/gingrich_drops_out/","name": "t3_srrch","created": 1335388179.0,"url": "http://nation.foxnews.com/newt-gingrich/2012/04/25/newt-gingrich-will-suspend-his-campaign-next-tuesday-aides-say","author_flair_text": null,"author": "politicaldan","created_utc": 1335362979.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 2281}}, {
#			"kind": "t3",	"data": {"domain": "imgur.com","banned_by": null,"media_embed": {},"subreddit": "WTF","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srq6d","clicked": false,"title": "I work on this kids ride...the film human centipede comes to mind...","num_comments": 124,"score": 1626,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh61","link_flair_css_class": null,"author_flair_css_class": null,"downs": 2102,"is_self": false,"permalink": "/r/WTF/comments/srq6d/i_work_on_this_kids_ridethe_film_human_centipede/","name": "t3_srq6d","created": 1335386513.0,"url": "http://imgur.com/PVi38","author_flair_text": null,"author": "keepitkewlkez","created_utc": 1335361313.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 3728}}, {
#			"kind": "t3",	"data": {"domain": "en.wikipedia.org","banned_by": null,"media_embed": {},"subreddit": "todayilearned","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "sroux","clicked": false,"title": "TIL that today is DNA Day, as it was discovered on this day in 1953. Happy DNA day Reddit!","num_comments": 290,"score": 1852,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://b.thumbs.redditmedia.com/r5fCuCkTBw8m2e6m.jpg","subreddit_id": "t5_2qqjc","link_flair_css_class": null,"author_flair_css_class": null,"downs": 3036,"is_self": false,"permalink": "/r/todayilearned/comments/sroux/til_that_today_is_dna_day_as_it_was_discovered_on/","name": "t3_sroux","created": 1335384458.0,"url": "http://en.wikipedia.org/wiki/Molecular_Structure_of_Nucleic_Acids:_A_Structure_for_Deoxyribose_Nucleic_Acid","author_flair_text": null,"author": "mrthehonorable","created_utc": 1335359258.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 4888}}, {
#			"kind": "t3",	"data": {"domain": "imgur.com","banned_by": null,"media_embed": {},"subreddit": "gaming","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srohf","clicked": false,"title": "I work with industrial X-Ray systems... I digitally X-Rayed some of your favourite console controllers.","num_comments": 241,"score": 1563,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://e.thumbs.redditmedia.com/dCzmCrIM0Z5ZpWXL.jpg","subreddit_id": "t5_2qh03","link_flair_css_class": null,"author_flair_css_class": null,"downs": 1306,"is_self": false,"permalink": "/r/gaming/comments/srohf/i_work_with_industrial_xray_systems_i_digitally/","name": "t3_srohf","created": 1335383808.0,"url": "http://imgur.com/a/BHUsv#0","author_flair_text": null,"author": "Diabolikal49","created_utc": 1335358608.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 2869}}, {
#			"kind": "t3",	"data": {"domain": "youtube.com","banned_by": null,"media_embed": {"content": "&lt;iframe width=\"600\" height=\"338\" src=\"http://www.youtube.com/embed/4oYqdjzFMWE?fs=1&amp;feature=oembed\" frameborder=\"0\" allowfullscreen&gt;&lt;/iframe&gt;","width": 600,"scrolling": false,"height": 338},"subreddit": "videos","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srpn0","clicked": false,"title": "UPDATE: Father With Autistic Son Sends His Kid To School With A Wire, Exposes Bullying And Abuse By Teachers","num_comments": 363,"score": 1362,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://f.thumbs.redditmedia.com/AXcQM2cmxqi-XSke.jpg","subreddit_id": "t5_2qh1e","link_flair_css_class": null,"author_flair_css_class": null,"downs": 715,"is_self": false,"permalink": "/r/videos/comments/srpn0/update_father_with_autistic_son_sends_his_kid_to/","name": "t3_srpn0","created": 1335385746.0,"url": "http://www.youtube.com/watch?v=4oYqdjzFMWE&amp;feature=channel&amp;list=UL","author_flair_text": null,"author": "logicalrationaltruth","created_utc": 1335360546.0,"link_flair_text": null,"media": {"oembed": {"provider_url": "http://www.youtube.com/","description": "A","title": "Response to Teacher Bully - Evidence that the teacher still works in the school district","url": "http://www.youtube.com/watch?v=4oYqdjzFMWE","type": "video","author_name": "StuChaifetz","height": 338,"width": 600,"html": "&lt;iframe width=\"600\" height=\"338\" src=\"http://www.youtube.com/embed/4oYqdjzFMWE?fs=1&amp;feature=oembed\" frameborder=\"0\" allowfullscreen&gt;&lt;/iframe&gt;","thumbnail_width": 480,"version": "1.0","provider_name": "YouTube","thumbnail_url": "http://i1.ytimg.com/vi/4oYqdjzFMWE/hqdefault.jpg","thumbnail_height": 360,"author_url": "http://www.youtube.com/user/StuChaifetz"},"type": "youtube.com"},"num_reports": null,"ups": 2077}}, {
#			"kind": "t3",	"data": {"domain": "dailymail.co.uk","banned_by": null,"media_embed": {},"subreddit": "worldnews","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srngc","clicked": false,"title": "Unimaginable horror as helicopter-borne poachers massacre 22 elephants before hacking off their tusks and genitals","num_comments": 703,"score": 1381,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh13","link_flair_css_class": null,"author_flair_css_class": null,"downs": 1770,"is_self": false,"permalink": "/r/worldnews/comments/srngc/unimaginable_horror_as_helicopterborne_poachers/","name": "t3_srngc","created": 1335381880.0,"url": "http://www.dailymail.co.uk/news/article-2134696/Scene-unimaginable-horror-helicopter-borne-poachers-massacre-22-elephants.html","author_flair_text": null,"author": "alllie","created_utc": 1335356680.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 3151}}, {
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "aww","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srs6t","clicked": false,"title": "My Rottie giving my newborn niece some kisses. ","num_comments": 76,"score": 836,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://e.thumbs.redditmedia.com/dIL39j1Y6h-1pZuR.jpg","subreddit_id": "t5_2qh1o","link_flair_css_class": null,"author_flair_css_class": null,"downs": 287,"is_self": false,"permalink": "/r/aww/comments/srs6t/my_rottie_giving_my_newborn_niece_some_kisses/","name": "t3_srs6t","created": 1335389294.0,"url": "http://i.imgur.com/8qoMh.jpg","author_flair_text": null,"author": "NIUJager","created_utc": 1335364094.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 1123}}, {
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "atheism","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srkyv","clicked": false,"title": "I saw this in my AP history review book...","num_comments": 311,"score": 1640,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://e.thumbs.redditmedia.com/gsKvw--4ua50LkQF.jpg","subreddit_id": "t5_2qh2p","link_flair_css_class": null,"author_flair_css_class": null,"downs": 3125,"is_self": false,"permalink": "/r/atheism/comments/srkyv/i_saw_this_in_my_ap_history_review_book/","name": "t3_srkyv","created": 1335376281.0,"url": "http://i.imgur.com/Gsirb.jpg","author_flair_text": null,"author": "bonzaibuddha","created_utc": 1335351081.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 4765}}, {
#			"kind": "t3",	"data": {"domain": "mattrichardson.com","banned_by": null,"media_embed": {},"subreddit": "technology","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srk8x","clicked": false,"title": "This camera doesn't take pictures. It prints descriptions.","num_comments": 392,"score": 1643,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh16","link_flair_css_class": null,"author_flair_css_class": null,"downs": 2943,"is_self": false,"permalink": "/r/technology/comments/srk8x/this_camera_doesnt_take_pictures_it_prints/","name": "t3_srk8x","created": 1335374242.0,"url": "http://mattrichardson.com/Descriptive-Camera/","author_flair_text": null,"author": "OvidPerl","created_utc": 1335349042.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 4586}}, {
#			"kind": "t3",	"data": {"domain": "vimeo.com","banned_by": null,"media_embed": {"content": "&lt;iframe src=\"http://player.vimeo.com/video/39145634\" width=\"600\" height=\"338\" frameborder=\"0\" webkitallowfullscreen mozallowfullscreen allowfullscreen&gt;&lt;/iframe&gt;","width": 600,"scrolling": false,"height": 338},"subreddit": "movies","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srk3x","clicked": false,"title": "I've spent the past 10 months creating this timelapse-movie. It would really mean a lot to me if you watched it!","num_comments": 435,"score": 1287,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh3s","link_flair_css_class": null,"author_flair_css_class": null,"downs": 1752,"is_self": false,"permalink": "/r/movies/comments/srk3x/ive_spent_the_past_10_months_creating_this/","name": "t3_srk3x","created": 1335373908.0,"url": "http://vimeo.com/39145634","author_flair_text": null,"author": "5oclockhero","created_utc": 1335348708.0,"link_flair_text": null,"media": {"type": "vimeo.com","oembed": {"provider_url": "http://vimeo.com/","description": "The final product of almost half a year of shooting. I made this movie as a school assignment called the 100 point project of free choice. The inspiration to make a timelapse movie came from the beautiful footage by TSO Photography and the Timescapes crew.","title": "Nature - Time 4 timelapse","author_name": "Pontus Rudolfson","height": 338,"width": 600,"html": "&lt;iframe src=\"http://player.vimeo.com/video/39145634\" width=\"600\" height=\"338\" frameborder=\"0\" webkitallowfullscreen mozallowfullscreen allowfullscreen&gt;&lt;/iframe&gt;","thumbnail_width": 960,"version": "1.0","provider_name": "Vimeo","thumbnail_url": "http://b.vimeocdn.com/ts/269/873/269873303_960.jpg","type": "video","thumbnail_height": 540,"author_url": "http://vimeo.com/rudolfson"}},"num_reports": null,"ups": 3039}}, {
#			"kind": "t3",	"data": {"domain": "self.AskReddit","banned_by": null,"media_embed": {},"subreddit": "AskReddit","selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;In all my 26 years I had this phobia in my head that eating alone anywhere was incredibly odd.  Not sure why, but all my life I vowed I&amp;#39;d never do it (same as going to the movies alone). I went and had a meal before my night shift at work last week and didn&amp;#39;t even think twice about it. It was actually kind of nice... So Reddit, what about you?&lt;/p&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;","selftext": "In all my 26 years I had this phobia in my head that eating alone anywhere was incredibly odd.  Not sure why, but all my life I vowed I'd never do it (same as going to the movies alone). I went and had a meal before my night shift at work last week and didn't even think twice about it. It was actually kind of nice... So Reddit, what about you?","likes": null,"saved": false,"id": "srnb9","clicked": false,"title": "Ate alone at a restaurant for the first time last week. And it wasn't even that bad. Reddit, what things did you think would be awkward to do until you actually did them?","num_comments": 1595,"score": 772,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh1i","link_flair_css_class": null,"author_flair_css_class": null,"downs": 759,"is_self": true,"permalink": "/r/AskReddit/comments/srnb9/ate_alone_at_a_restaurant_for_the_first_time_last/","name": "t3_srnb9","created": 1335381656.0,"url": "http://www.reddit.com/r/AskReddit/comments/srnb9/ate_alone_at_a_restaurant_for_the_first_time_last/","author_flair_text": null,"author": "GirlRiot","created_utc": 1335356456.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 1531}}, {
#			"kind": "t3",	"data": {"domain": "phys.org","banned_by": null,"media_embed": {},"subreddit": "science","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srj8u","clicked": false,"title": "Japanese astronomers said Wednesday they had found a cluster of galaxies 12.72 billion light-years away from Earth, which they claim is the most distant cluster ever discovered.","num_comments": 192,"score": 1090,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_mouw","link_flair_css_class": null,"author_flair_css_class": null,"downs": 770,"is_self": false,"permalink": "/r/science/comments/srj8u/japanese_astronomers_said_wednesday_they_had/","name": "t3_srj8u","created": 1335371699.0,"url": "http://phys.org/news/2012-04-japan-astronomers-distant-galaxy-cluster.html","author_flair_text": null,"author": "DrJulianBashir","created_utc": 1335346499.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 1860}}, {
#			"kind": "t3",	"data": {"domain": "youtube.com","banned_by": null,"media_embed": {"content": "&lt;iframe width=\"600\" height=\"338\" src=\"http://www.youtube.com/embed/98P-gu_vMRc?fs=1&amp;feature=oembed\" frameborder=\"0\" allowfullscreen&gt;&lt;/iframe&gt;","width": 600,"scrolling": false,"height": 338},"subreddit": "Music","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srqu9","clicked": false,"title": "Electric Light Orchestra-Mr. Blue Sky. (The best song to listen to on your daily commute!)","num_comments": 34,"score": 300,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh1u","link_flair_css_class": null,"author_flair_css_class": null,"downs": 87,"is_self": false,"permalink": "/r/Music/comments/srqu9/electric_light_orchestramr_blue_sky_the_best_song/","name": "t3_srqu9","created": 1335387502.0,"url": "http://www.youtube.com/watch?v=98P-gu_vMRc","author_flair_text": null,"author": "888alltheway","created_utc": 1335362302.0,"link_flair_text": null,"media": {"oembed": {"provider_url": "http://www.youtube.com/","description": "music","title": "ELO - Mr.Blue Sky (Original Promo)","url": "http://www.youtube.com/watch?v=98P-gu_vMRc","type": "video","author_name": "alaf22","height": 338,"width": 600,"html": "&lt;iframe width=\"600\" height=\"338\" src=\"http://www.youtube.com/embed/98P-gu_vMRc?fs=1&amp;feature=oembed\" frameborder=\"0\" allowfullscreen&gt;&lt;/iframe&gt;","thumbnail_width": 480,"version": "1.0","provider_name": "YouTube","thumbnail_url": "http://i2.ytimg.com/vi/98P-gu_vMRc/hqdefault.jpg","thumbnail_height": 360,"author_url": "http://www.youtube.com/user/alaf22"},"type": "youtube.com"},"num_reports": null,"ups": 387}}, {
#			"kind": "t3",	"data": {"domain": "self.IAmA","banned_by": null,"media_embed": {},"subreddit": "IAmA","selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;proof: &lt;a href=\"http://i.imgur.com/2n8hx.jpg\"&gt;http://i.imgur.com/2n8hx.jpg&lt;/a&gt;&lt;/p&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;","selftext": "proof: http://i.imgur.com/2n8hx.jpg","likes": null,"saved": false,"id": "srn8n","clicked": false,"title": "IAmA Truck Driver. Ask me anything","num_comments": 539,"score": 308,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qzb6","link_flair_css_class": null,"author_flair_css_class": null,"downs": 154,"is_self": true,"permalink": "/r/IAmA/comments/srn8n/iama_truck_driver_ask_me_anything/","name": "t3_srn8n","created": 1335381531.0,"url": "http://www.reddit.com/r/IAmA/comments/srn8n/iama_truck_driver_ask_me_anything/","author_flair_text": null,"author": "Traki00","created_utc": 1335356331.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 462}}, {
#			"kind": "t3",	"data": {"domain": "reddit.com","banned_by": null,"media_embed": {},"subreddit": "bestof","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "sqpu8","clicked": false,"title": "\"Just box this up, we're leaving.\"","num_comments": 61,"score": 658,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh3v","link_flair_css_class": null,"author_flair_css_class": null,"downs": 2261,"is_self": false,"permalink": "/r/bestof/comments/sqpu8/just_box_this_up_were_leaving/","name": "t3_sqpu8","created": 1335332074.0,"url": "http://www.reddit.com/r/AskReddit/comments/sq3zj/throwaway_time_what_is_the_one_illegal_immoral/c4g60r8?context=3","author_flair_text": null,"author": "dingofarmer2004","created_utc": 1335306874.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 2919}}, {
#			"kind": "t3",	"data": {"domain": "imgur.com","banned_by": null,"media_embed": {},"subreddit": "aww","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srl0q","clicked": false,"title": "yyyaaawwWWWWWNNNNN! ","num_comments": 89,"score": 1421,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://e.thumbs.redditmedia.com/4IvVGfQ18OdYwhkp.jpg","subreddit_id": "t5_2qh1o","link_flair_css_class": null,"author_flair_css_class": null,"downs": 2633,"is_self": false,"permalink": "/r/aww/comments/srl0q/yyyaaawwwwwwwnnnnn/","name": "t3_srl0q","created": 1335376415.0,"url": "http://imgur.com/sLJO9","author_flair_text": null,"author": "Jesta05","created_utc": 1335351215.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 4054}}, {
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "WTF","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srrvk","clicked": false,"title": "This person is without a doubt mentally disturbed. ","num_comments": 111,"score": 1049,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh61","link_flair_css_class": null,"author_flair_css_class": null,"downs": 845,"is_self": false,"permalink": "/r/WTF/comments/srrvk/this_person_is_without_a_doubt_mentally_disturbed/","name": "t3_srrvk","created": 1335388905.0,"url": "http://i.imgur.com/caW0J.jpg","author_flair_text": null,"author": "EatenOffTheWeb","created_utc": 1335363705.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 1894}}, {
#			"kind": "t3",	"data": {"domain": "reddit.com","banned_by": null,"media_embed": {},"subreddit": "bestof","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srpql","clicked": false,"title": "Jimmytherifle eloquently explains how a photon travels instantly","num_comments": 7,"score": 35,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh3v","link_flair_css_class": null,"author_flair_css_class": null,"downs": 22,"is_self": false,"permalink": "/r/bestof/comments/srpql/jimmytherifle_eloquently_explains_how_a_photon/","name": "t3_srpql","created": 1335385892.0,"url": "http://www.reddit.com/r/trees/comments/sr1go/an_amazing_quote_by_a_fellow_ent_a_while_back_on/c4gbu7e","author_flair_text": null,"author": "Hey_You_Asked","created_utc": 1335360692.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 57}}, {
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "funny","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srqmg","clicked": false,"title": "ICEBERG, ICEBERG!","num_comments": 90,"score": 2100,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "","subreddit_id": "t5_2qh33","link_flair_css_class": null,"author_flair_css_class": null,"downs": 3814,"is_self": false,"permalink": "/r/funny/comments/srqmg/iceberg_iceberg/","name": "t3_srqmg","created": 1335387175.0,"url": "http://i.imgur.com/kJczr.png","author_flair_text": null,"author": "StartCase","created_utc": 1335361975.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 5914}}, {
#			"kind": "t3",	"data": {"domain": "qkme.me","banned_by": null,"media_embed": {},"subreddit": "AdviceAnimals","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srr1k","clicked": false,"title": "Forever Sober","num_comments": 23,"score": 1112,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://e.thumbs.redditmedia.com/052MYf9DyZKgBgqF.jpg","subreddit_id": "t5_2s7tt","link_flair_css_class": null,"author_flair_css_class": null,"downs": 806,"is_self": false,"permalink": "/r/AdviceAnimals/comments/srr1k/forever_sober/","name": "t3_srr1k","created": 1335387801.0,"url": "http://qkme.me/3oyoen?id=223327247","author_flair_text": null,"author": "KOdaynik","created_utc": 1335362601.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 1918}}, {
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "aww","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srj3p","clicked": false,"title": "My Pet Tortoise wont sleep without his happy meal toy, If i take it out he'll search around his tank until he finds it","num_comments": 136,"score": 1426,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://c.thumbs.redditmedia.com/J-0ypu8VqKW9vleV.jpg","subreddit_id": "t5_2qh1o","link_flair_css_class": null,"author_flair_css_class": null,"downs": 1851,"is_self": false,"permalink": "/r/aww/comments/srj3p/my_pet_tortoise_wont_sleep_without_his_happy_meal/","name": "t3_srj3p","created": 1335371302.0,"url": "http://i.imgur.com/hv22B.jpg","author_flair_text": null,"author": "hobbsy89","created_utc": 1335346102.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 3277}}, {
#			"kind": "t3",	"data": {"domain": "i.imgur.com","banned_by": null,"media_embed": {},"subreddit": "pics","selftext_html": null,"selftext": "","likes": null,"saved": false,"id": "srk0k","clicked": false,"title": "The illusion of choice...","num_comments": 2611,"score": 2274,"approved_by": null,"over_18": false,"hidden": false,"thumbnail": "http://d.thumbs.redditmedia.com/Laq96kW8dWUveh_c.jpg","subreddit_id": "t5_2qh0u","link_flair_css_class": null,"author_flair_css_class": null,"downs": 20842,"is_self": false,"permalink": "/r/pics/comments/srk0k/the_illusion_of_choice/","name": "t3_srk0k","created": 1335373652.0,"url": "http://i.imgur.com/k0pv0.jpg","author_flair_text": null,"author": "mod83","created_utc": 1335348452.0,"link_flair_text": null,"media": null,"num_reports": null,"ups": 23116} }],
#		"after": "t3_srk0k", "before": null	}}
#"""
#
#def total_ups(reddit_str):
#    j = json.loads(reddit_str)
#    data = j['data'] #dirctionary
#    children = data['children']
#    count = 0
#    for c in children:
#        c_data = c['data']
#        count += c_data.get('ups', 0)
#    print count
#    return count
#
#total_ups(reddit_front)

#4. JSON Escape
#JSON must use double quotes to deliminate a string. No single quote as in python. So must escape any intext 
#double quotes.
#json.loads('{"story": "once up \\"on a time"}') #valid python, not valid json (use only one slash)
#json.loads(r'{"story": "once up \" on a time"}')
#
#json.dumps([1,2,3])
##print json.dumps({"one":1, "two":2})
#json.dumps({"one":1, "two": 'he says, "cool!"'}) # has two slashes
#print json.dumps({"one":1, "two": 'he says, "cool!"'}) #the printed version is the same as the actual valid json


##5. How to be a good citizen on the Internet
#-use a good user-agent
#    - in urllib2, can set headers on my requests
#- rate-limit yourself
#ex: 
#    ```python
#    import time
#    while more:
#        get_more()
#        time.sleep(1)
#    ```

#6. Other communication protocals
#- soap (microsoft)
#- protol buffers (google)
#- Thrift (facebook)
#- plain-text, fustom formats (not recommended, use json,xml, etc)


#7. 
#step 1. Get user ip, lat, long by sending a request to ip-api.com/json or ip-api.com/xml
#step 2. Send another request to google static map api to get the url for the static map image

#For practice, let's send it to ---/xml and practice parcing xml files using minidom module.
#import urllib2
#from xml.dom import minidom
#request = urllib2.Request("http://ip-api.com/xml")
#response = urllib2.urlopen(request)
#resp_str = response.read()
#dir(response)
#
#dom = minidom.parseString(resp_str) #string to xml DOM
#lat = str(dom.getElementsByTagName("lat")[0].childNodes[0].wholeText)
#lon = str(dom.getElementsByTagName("lon")[0].childNodes[0].wholeText)
#print lat, type(lat) #str
#print lon, type(lon) #str


#Using json this time
import json
request = urllib2.Request("http://ip-api.com/json")
response = urllib2.urlopen(request)
resp_str = response.read()
resp_json = json.loads(resp_str)
lat = resp_json['lat']
lon = resp_json['lon']
#print type(lat), type(lon) #float, float
lat = str(lat)
lon = str(lon)


#step2. Send the next request to google static map api to get the rul for the static map image
#https://developers.google.com/maps/documentation/static-maps/intro
zoom = str(13)
key ="AIzaSyC2oZC2Vd5lRnAgPQ_Svv2JTtkXVD6MR4w"
url_base ="https://maps.googleapis.com/maps/api/staticmap?center=%(lat)s,%(lon)s&size=512x512&zoom=%(zoom)s&key=%(key)s"%{"zoom":zoom, "lon": lon, "lat": lat, "key":key}
print url_base
#req = urllib2.Request(url_base)
#resp = urllib2.urlopen(req)
def getMapURL(location, zoom=13, key ="AIzaSyC2oZC2Vd5lRnAgPQ_Svv2JTtkXVD6MR4w"):
    location=str(location); zoom = str(zoom);
    url_base ="https://maps.googleapis.com/maps/api/staticmap?center=%(location)s&size=512x512&zoom=%(zoom)s&key=%(key)s"%{"zoom":zoom, "location": location, "key":key}
    return url_base #str
    
print getMapURL("42.3646,-71.1028")
