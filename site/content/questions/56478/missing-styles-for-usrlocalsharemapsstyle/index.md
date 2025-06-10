+++
type = "question"
title = "Missing styles for /usr/local/share/maps/style"
description = '''I have been following this link to install on my centos 7 http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c. First I cant unzip this unzip ~/ne_10m_populated_places_simple.zip and also the rest of the folder does not exist. Coming to this steps  cd ne_10m_populated_places_simple  unzip ~/ne_10m_p...'''
date = "2017-06-06T20:24:00Z"
lastmod = "2017-06-06T21:06:00Z"
weight = 56478
keywords = [ "style" ]
aliases = [ "/questions/56478" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Missing styles for /usr/local/share/maps/style](/questions/56478/missing-styles-for-usrlocalsharemapsstyle)

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
<span id="post-56478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56478-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been following this link to install on my centos 7 <a href="http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c.">http://qiita.com/nkmrtkhd/items/642ae1b8a996cc46d85c.</a> First I cant unzip this unzip ~/ne_10m_populated_places_simple.zip and also the rest of the folder does not exist. Coming to this steps cd ne_10m_populated_places_simple unzip ~/ne_10m_populated_places_simple.zip cd .. unzip ~/master.zip unzip ~/simplified-land-polygons-complete-3857.zip unzip ~/land-polygons-split-3857.zip mkdir osm-bright-master/shp mv land-polygons-split-3857 osm-bright-master/shp/ mv simplified-land-polygons-complete-3857 osm-bright-master/shp/ mv ne_10m_populated_places_simple osm-bright-master/shp/</p>
<pre><code>cd osm-bright-master/shp/land-polygons-split-3857
shapeindex land_polygons.shp
cd ../simplified-land-polygons-complete-3857/
shapeindex simplified_land_polygons.shp
cd ../..
&#10;vi osm-bright/osm-bright.osm2pgsql.mml
&#10;cp ~/configure.py .
./make.py
cd ../OSMBright/
carto project.mml &gt; OSMBright.xml</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '17, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56478" class="comments-container">
&#10;</div>
<div id="comment-tools-56478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56478-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="56482"></span>

<div id="answer-container-56482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56482-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What I suspect has happened is that the layout of the Natural Earth website has changed since osmbright was packaged. When I wrote <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1604_tileserver_load#Natural_Earth_Data">these instructions</a> I modified the "get-shapefiles.sh" script so that it worked with the new layout of that site.</p>
<p>You can either figure out what is missing manually (by looking at the script and seeing what it is trying to do), or try my version linked above. I'm not 100% sure what natural earth data osm-bright needs, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '17, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56482" class="comments-container">
&#10;</div>
<div id="comment-tools-56482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56482-form-container" class="comment-form-container">
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

