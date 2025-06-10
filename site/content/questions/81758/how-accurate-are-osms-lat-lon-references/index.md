+++
type = "question"
title = "How accurate are OSM&#x27;s lat-lon references?"
description = '''How accurate are the lat-lon refs that Overpass produces? (I mean in notation terms: obviously the real-world accuracy depends on 10,000 things.) They seem to be always to 10 decimal places. My maths is terrible, but I think that means the 10th decimal place is indicating 0.01mm of distance (assumin...'''
date = "2021-09-15T15:59:00Z"
lastmod = "2021-09-16T19:30:00Z"
weight = 81758
keywords = [ "latitude", "lat-lon", "geodesy", "longitude" ]
aliases = [ "/questions/81758" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How accurate are OSM's lat-lon references?](/questions/81758/how-accurate-are-osms-lat-lon-references)

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
<span id="post-81758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How accurate are the lat-lon refs that Overpass produces? (I mean in notation terms: obviously the real-world accuracy depends on 10,000 things.)</p>
<p>They seem to be always to 10 decimal places. My maths is terrible, but I think that means the 10th decimal place is indicating 0.01mm of distance (assuming 111km per degree of latitude).</p>
<p>Is that right?? It seems unrealistically accurate, and maybe I've missed something.</p>
<p>The reason for asking is to ask Calc/Excel for '±100m from x/y'.</p>
<p>Thanks</p>
<pre><code>lat                                         
52.5802291381
&#10;52  111km                                       
    .5  11.1km                                  
        8   1.11km                              
            0   111m                            
                2   11.1m                       
                    2   1.11m                   
                        9   11.1cm              
                            1   1.11cm          
                                3   0.111cm     
                                    8   0.011cm 
                                        1   0.001cm</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-lat-lon" rel="tag" title="see questions tagged &#39;lat-lon&#39;">lat-lon</span> <span class="post-tag tag-link-geodesy" rel="tag" title="see questions tagged &#39;geodesy&#39;">geodesy</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '21, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/4f273f48fd8756729fc15f4fcf4aae2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eteb3&#39;s gravatar image" />
<p><span>eteb3</span><br />
<span class="score" title="295 reputation points">295</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eteb3 has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-81758" class="comments-container">
&#10;</div>
<div id="comment-tools-81758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81758-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="81765"></span>

<div id="answer-container-81765" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81765-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"How accurate something is" depends not on how accurately the data is stored, but how accurate the data was when it was first recorded. This applies whether you're looking at data in OSM or (say) how many hospitals Boris Johnson is actually going to build before 2030.</p>
<p>In the case of OSM you have to ask yourself "how accurately might someone have recorded something". I'd hope within the UK that someone adding something now would get the building it's in to within 10m either way, though of course they might simply pick the wrong building and be a few extra 10s of m out on top of that (hence SK53's 50-100 metres being in the right ballpark).</p>
<p>If you're comparing OSM with an external dataset then obviously you'll have to consider how accurate that data is too - if it contains "old" data (15 years or so?) then some of it in the UK might have been geocoded to the most significant part of the postcode. Even if not, any rural areas anything geocoded from just the postcode will be quite a way off.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '21, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81765" class="comments-container">
<span id="81771"></span>
<div id="comment-81771" class="comment">
<div id="post-81771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>geocoded to the most significant part of the postcode That's my understanding of how the lat-lon were produced on the external dataset.</p>
</blockquote>
</div>
<div id="comment-81771-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 07:33)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
</div>
<div id="comment-tools-81765" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81765-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81760"></span>

<div id="answer-container-81760" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81760-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the <a href="https://wiki.openstreetmap.org/wiki/Node">wiki</a>, nodes are stored in the OSM database with 7 decimal places. I just tested and I only get 7 decimal places from Overpass (Overpass Turbo or overpass-api.de). A different Overpass instance could theoretically be configured to return more decimal places, but any beyond the first 7 should always be 0 for nodes coming from the main OSM database (and those would be false precision).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '21, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-81760" class="comments-container">
<span id="81761"></span>
<div id="comment-81761" class="comment">
<div id="post-81761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My bad: I have two datasets from two sources, and I mixed them up. One is from Overpass, the other is from somewhere else.</p>
<p>You're right, my Overpass output gives 7 decimal places. Am I right that - in theory - that is still 1cm of precision?</p>
<p>Does that mean I can ask Excel to round both datasets to 3 decimal places, and I can then see if two lat-lons, which are dissimilar only in the right-most decimal places, are likely to represent the same on-the-ground object?</p>
</div>
<div id="comment-81761-info" class="comment-info">
<span class="comment-age">(15 Sep '21, 17:57)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
<span id="81763"></span>
<div id="comment-81763" class="comment">
<div id="post-81763-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't think that's a good strategy; there are plenty of much more sophisticated geospatial operators around &amp; available for instance in QGIS. A reasonable buffer for conflation in the UK in urban areas is 50-100 metres (i.e, roughly your 3 dp), but that may be too small in rural areas, particularly if geolocation of data is based on postcode centroid. I would translate datasets to British National Grid (guessing this is your PoW dataset) because you can do direct comparisons in metres (and in Excel if you wish).</p>
</div>
<div id="comment-81763-info" class="comment-info">
<span class="comment-age">(15 Sep '21, 21:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="81770"></span>
<div id="comment-81770" class="comment">
<div id="post-81770-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I will check out QGIS.</p>
<p>For the conversion to British National Grid, is there an algorithm that I can run through Excel, or a lookup table, or is it a question of going line by line? (I'm guessing 'surely not!' but possibly the solution is beyond my technical ability.)</p>
</div>
<div id="comment-81770-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 07:31)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
<span id="81780"></span>
<div id="comment-81780" class="comment">
<div id="post-81780-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At one point the OS provided an Excel addin, but the easiest way is with QGIS which will allow you to save data in another projection (I usually use Geojson &amp; havent experimented with CSV). You can also use the ogr2ogr command line tool. The key things are OSGB is identified as EPSG:27700 and WGS84 is EPSG:4326. (The minor complication is QGIS now provides a rather over rich range of reprojecting which can be confusing, but I think for your purposes the default should be fine).</p>
</div>
<div id="comment-81780-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 15:02)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="81783"></span>
<div id="comment-81783" class="comment">
<div id="post-81783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thank you. Look forward to a long weekend learning a new computer program some time soon!</p>
</div>
<div id="comment-81783-info" class="comment-info">
<span class="comment-age">(16 Sep '21, 19:30)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
</div>
<div id="comment-tools-81760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81760-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

