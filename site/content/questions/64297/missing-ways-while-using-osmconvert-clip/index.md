+++
type = "question"
title = "missing ways while using osmconvert clip"
description = '''I am using osmconvert to clip countries/regions from the planet.osm.pbf file. My end goal is creating a multimodal transport network, using (mostly) osm data. Mainly for academic purposes. To speed up this creation process, I am splitting up the planet file into countries/regions to create this netw...'''
date = "2018-06-21T09:04:00Z"
lastmod = "2018-06-22T10:14:00Z"
weight = 64297
keywords = [ "osmconvert", "clip" ]
aliases = [ "/questions/64297" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [missing ways while using osmconvert clip](/questions/64297/missing-ways-while-using-osmconvert-clip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64297-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using osmconvert to clip countries/regions from the planet.osm.pbf file. My end goal is creating a multimodal transport network, using (mostly) osm data. Mainly for academic purposes. To speed up this creation process, I am splitting up the planet file into countries/regions to create this network parallel. Recently, I have started to realize that I am missing quite some ways in the extracted/clipped files.</p>
<p>For example, openstreetmap.org shows a near complete and connected railway system for tanzania. In my extracted osm.pbf for tanzania (either using a bbox or a .poly file), I am missing quite some railway segments. The same issue is the case for the download.geofabrik.de extracts (at least in the case for Tanzania, where I started to realize this issue).</p>
<p>Perhaps good to emphasize: I am <strong>not</strong> missing these segments around the borders (this is ofcourse already addressed in the osmconvert wiki), it is really in the middle of the bbox/.poly file.</p>
<p>The osmconvert code I am using is:</p>
<pre><code>osmconvert64 planet-latest.osm.pbf -B=tanzania.poly --complete-ways -o=tanzania.osm.pbf&#39;</code></pre>
<p>Did anyone have this problem with osmconvert before? And more importantly, found a solution to the problem?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-clip" rel="tag" title="see questions tagged &#39;clip&#39;">clip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '18, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f56afcd82ff07e180554c51c4e7aec41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElcoK&#39;s gravatar image" />
<p><span>ElcoK</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElcoK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jun '18, 09:24</strong> </span></p>
</div>
</div>
<div id="comments-container-64297" class="comments-container">
<span id="64298"></span>
<div id="comment-64298" class="comment">
<div id="post-64298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without knowing exactly what you're doing it may be difficult for people to comment. Could you provide a bit more detail and some examples?</p>
</div>
<div id="comment-64298-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 09:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64299"></span>
<div id="comment-64299" class="comment">
<div id="post-64299-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are saying that the Geofabrik download for Tanzania is missing data, I would be interested in a way ID so I can check.</p>
</div>
<div id="comment-64299-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 09:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64300"></span>
<div id="comment-64300" class="comment">
<div id="post-64300-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik,</p>
<p>One example is Way: 396139210</p>
<p>At least, I don't see it in the file I've downloaded today (and yesterday) from geofabrik. It use to be there, and it is also on openstreetmap.org</p>
<p>If you open the lines from tanzania-latest.osm.pbf in QGIS and overlay this with the openstreetmap, you'll see that (for instance in Dar Es Salaam) also many roads are missing.</p>
</div>
<div id="comment-64300-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 09:43)</span> <span class="comment-user userinfo">ElcoK</span>
</div>
</div>
<span id="64301"></span>
<div id="comment-64301" class="comment">
<div id="post-64301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Must be an issue with QGIS then, since the way is definitely present in tanzania-latest.osm.pbf. Perhaps whatever logic QGIS applies is stumped by the fact that your way is part of relation 1183489 which is (at the time of writing with v99 being current) erroneously tagged as highway=residential?</p>
</div>
<div id="comment-64301-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 10:41)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64303"></span>
<div id="comment-64303" class="comment not_top_scorer">
<div id="post-64303-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've narrowed down the problem now. The reason why my confusion started was because some part of the railway in TZA (not the way I mentioned above) was missing (this is apparently deleted by someone, even though it is still there).</p>
<p>So the problem is not in the osmconvert clip (which is good to know!), but apparently something goes wrong in the ogr2ogr drivers when trying to directly load in the data (either through python directly or QGIS, as they were missing the quite often the same elements).</p>
<p>After extracting all line features from the pbf file by using the following code in python, I miss quite a lot of segments.</p>
<pre><code>driver=ogr.GetDriverByName(&#39;OSM&#39;)
data = ogr.Open(&#39;C://planet_osm//tanzania-latest.osm.pbf&#39;)
layer = data.GetLayer(&#39;lines&#39;)
&#10;features=[x for x in layer]
&#10;for feature in features:
    if feature.GetField(&#39;railway&#39;) is not None:
        osm_id = feature.GetField(&#39;osm_id&#39;)</code></pre>
</div>
<div id="comment-64303-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 11:21)</span> <span class="comment-user userinfo">ElcoK</span>
</div>
</div>
<span id="64309"></span>
<div id="comment-64309" class="comment not_top_scorer">
<div id="post-64309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My default ogr2ogr osm =&gt; geojson places railway in other tags for lines. It may be worth checking say against geojson for the same feature using overpass-turbo.</p>
</div>
<div id="comment-64309-info" class="comment-info">
<span class="comment-age">(21 Jun '18, 17:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="64317"></span>
<div id="comment-64317" class="comment">
<div id="post-64317-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hmm interesting point. As this is now turning into a osgeo/gdal question (why different results between ogr2ogr command line and python import), I will post that question at stackoverflow. Thanks for the help!</p>
</div>
<div id="comment-64317-info" class="comment-info">
<span class="comment-age">(22 Jun '18, 08:21)</span> <span class="comment-user userinfo">ElcoK</span>
</div>
</div>
<span id="64318"></span>
<div id="comment-64318" class="comment not_top_scorer">
<div id="post-64318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... which is this one, just for reference: <a href="https://gis.stackexchange.com/questions/287193/different-results-ogr2ogr-command-line-vs-osgeo-import-ogr-with-reading-osm-data">https://gis.stackexchange.com/questions/287193/different-results-ogr2ogr-command-line-vs-osgeo-import-ogr-with-reading-osm-data</a></p>
</div>
<div id="comment-64318-info" class="comment-info">
<span class="comment-age">(22 Jun '18, 10:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64297" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-64297-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

