+++
type = "question"
title = "Tile server can&#x27;t render the .osm data converted by JOSM"
description = '''Hi All I got the map data source in .shp formate so I use JOSM to save it as .osm format and then osm2pgsql it into database. However the converted .osm seems not be able to properly rendered by my tile server because there is nothing showing in my browser while my other map layers can still show no...'''
date = "2015-09-13T09:06:00Z"
lastmod = "2015-09-14T04:27:00Z"
weight = 45218
keywords = [ "josm", "tiles", "render" ]
aliases = [ "/questions/45218" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile server can't render the .osm data converted by JOSM](/questions/45218/tile-server-cant-render-the-osm-data-converted-by-josm)

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
<span id="post-45218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45218-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All</p>
<p>I got the map data source in .shp formate so I use JOSM to save it as .osm format and then osm2pgsql it into database. However the converted .osm seems not be able to properly rendered by my tile server because there is nothing showing in my browser while my other map layers can still show normally.</p>
<p>I have checked there is some meta tiles generated like 136.meta, 8.meta, etc in the renderd folder /var/lib/mod_tile/layer/. However my browser does not show anything. I am running my own tile server by the way following the switch2osm tutorial.</p>
<p>The only thing difference between the converted .osm and normal .osm is that JOSM editor assigned negative ids to the nodes in the map. Is that the reason why this is happening? How should I solve this?</p>
<p>Thanks guys.</p>
<p><img src="http://help.openstreetmap.org/upfiles/Screenshot_from_2015-09-13_15:43:07.png" alt="alt text" /> <img src="http://help.openstreetmap.org/upfiles/Screenshot_from_2015-09-14_11:19:43.png" alt="alt text" /> <img src="http://help.openstreetmap.org/upfiles/Screenshot_from_2015-09-14_11:22:30.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '15, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0cd6d6bd835d840ee1df1f5a3310d099?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dalishi&#39;s gravatar image" />
<p><span>dalishi</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dalishi has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '15, 04:28</strong> </span></p>
</div>
</div>
<div id="comments-container-45218" class="comments-container">
&#10;</div>
<div id="comment-tools-45218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45218-form-container" class="comment-form-container">
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

<span id="45223"></span>

<div id="answer-container-45223" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45223-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-45223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are your meta tiles perhaps all the same size? Then they're likely empty. Perhaps because the OSM data you created was either not imported at all (count the number of objects in your postgres tables) or the data was imported, but did not have the proper tags. What kind of shape files did you use and what did you expect to see on the map?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '15, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-45223" class="comments-container">
<span id="45228"></span>
<div id="comment-45228" class="comment">
<div id="post-45228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi <a href="http://help.openstreetmap.org/users/104/frederik-ramm"></a><a href="http://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a> thanks for your reply. I followed your checking advices. (1)The meta tiles are of different size. (2) count number of objects: 23. Please check my previous post where I added the screen shot. (3) The tags. The JOSM converted .osm does include certain tags. Please also see my added screen shot. But I am not quite sure what is the "proper tags" you mentioned that is necessary for rendering. The .shp file is from our own team which is generated by ArcGIS. We want to render the data just as we render the osm data.</p>
</div>
<div id="comment-45228-info" class="comment-info">
<span class="comment-age">(14 Sep '15, 04:27)</span> <span class="comment-user userinfo">dalishi</span>
</div>
</div>
</div>
<div id="comment-tools-45223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45223-form-container" class="comment-form-container">
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

