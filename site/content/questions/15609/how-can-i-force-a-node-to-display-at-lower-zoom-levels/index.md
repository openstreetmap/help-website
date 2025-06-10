+++
type = "question"
title = "How can I force a node to display at lower zoom levels?"
description = '''Given an area with extremely few nodes (e.g. open ocean), it would make sense to display certain nodes (e.g. the only buoy on a 10-km radius) at more zoom levels than it would normally would. Is there a way to indicate this in the node definition, or otherwise force this sort of display, maybe with ...'''
date = "2012-08-29T04:10:00Z"
lastmod = "2013-07-15T11:34:00Z"
weight = 15609
keywords = [ "zoomlevel", "node", "zoom", "display" ]
aliases = [ "/questions/15609" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I force a node to display at lower zoom levels?](/questions/15609/how-can-i-force-a-node-to-display-at-lower-zoom-levels)

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
<span id="post-15609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15609-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given an area with extremely few nodes (e.g. open ocean), it would make sense to display certain nodes (e.g. the only buoy on a 10-km radius) at more zoom levels than it would normally would.</p>
<p>Is there a way to indicate this in the node definition, or otherwise force this sort of display, maybe with a URL parameter? I'm not limited to an OpenStreetMaps solution. If this requires CloudMade or OpenLayers or some OpenSeaMap hack, that'd be fine too.</p>
<p>Example: <a href="http://map.openseamap.org/map/?zoom=11&amp;lat=37.35481&amp;lon=-122.88121&amp;layers=BFTFFFTFFFF0FF">NOAA buoy 46012</a>. Zoom level 11 shows nothing, even though there would be plenty of space to show the buoy. It takes zoom level 14 to show the buoy, and by then, it's out of any useful context, surrounded by plain sea tiles.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '12, 04:10</strong></p>
<img src="https://secure.gravatar.com/avatar/fb5e3a539b1e23c54b080b6d12b411c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dandv&#39;s gravatar image" />
<p><span>dandv</span><br />
<span class="score" title="401 reputation points">401</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dandv has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15609" class="comments-container">
&#10;</div>
<div id="comment-tools-15609" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15609-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="15612"></span>

<div id="answer-container-15612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15612-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The map you get on osm.org is composed of individual static images. You can right click on the map and choose "View image" or similar in your browser and you will see one individual image. There is no way to dynamically change the rendering of these images. So the answer to your question is: no.</p>
<p>The only way to achieve this would be to render your own map from the raw OSM data and choose to make buoys more prominent in your stylesheet. How to set up a tile rendering server is covered on the <a href="http://switch2osm.org/serving-tiles/">switch2osm.org</a> site but it is not a simple thing for a worldwide map. You can also render your own map using applications like Maperitive although that will only do a limited area.</p>
<p>Or you could talk to the operators of OpenSeaMap and convince them to adjust their style instead if you think buoys should be more prominent.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 05:26</strong></p>
<img src="https://secure.gravatar.com/avatar/43ae79d3345e19f30ea5f2ea64a9f7bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToeBee&#39;s gravatar image" />
<p><span>ToeBee</span><br />
<span class="score" title="976 reputation points">976</span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToeBee has 6 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-15612" class="comments-container">
<span id="15622"></span>
<div id="comment-15622" class="comment">
<div id="post-15622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re. prominence of buoys - that's a particular case, and the easiest. But in principle, if a node is surrounded by nothing for a certain distance, it should be displayed at lower zoom levels, as long as it doesn't touch other nodes. This may not be trivial to implement, but it would elegantly solve the problem of buoys, or, say, features in deserts. The only drawback is that the nodes might suggest a larger map feature than in reality, but we do that routinely with POIs as well.</p>
</div>
<div id="comment-15622-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 08:19)</span> <span class="comment-user userinfo">dandv</span>
</div>
</div>
<span id="15624"></span>
<div id="comment-15624" class="comment">
<div id="post-15624-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Mapnik (the software that renders the tiles) does have an algorithm for de-cluttering crowded areas. This is why not every POI in the middle of a big city gets rendered. But that's just removing things that conflict. I don't think it has the ability to "re-clutter" things from a higher zoom and I'm not sure you can assign any kind of priority. This would be one way of doing it though... render buoys at a lower zoom but make them low priority so they get de-cluttered quicker than other things. But I think you'll have to take that up with the mapnik devs.</p>
</div>
<div id="comment-15624-info" class="comment-info">
<span class="comment-age">(29 Aug '12, 08:40)</span> <span class="comment-user userinfo">ToeBee</span>
</div>
</div>
</div>
<div id="comment-tools-15612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15612-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15616"></span>

<div id="answer-container-15616" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15616-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to see a point from the data on the map, you can use this <a href="http://osm.dumoulin63.net/xapiviewer/?oom=11&amp;lat=37.59868&amp;lon=-122.83862&amp;layers=B0T&amp;zoom=10&amp;icon=http%3A%2F%2Fwww.geoinfo.com.vn%2FUserFiles%2FImage%2FSkyWave_buoy-icon.png&amp;request=man_made%3Dbuoy">online tool</a>, and ask for your wanted tag to get all objects with this tag. I have had the same frustration than you a lot of times, so I've found this way to display data that aren't (and maybe will never be) on standards map renders.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 07:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15616" class="comments-container">
&#10;</div>
<div id="comment-tools-15616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15616-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15630"></span>

<div id="answer-container-15630" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15630-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In <a href="http://map.openseamap.org/map/?zoom=11&amp;lat=37.35481&amp;lon=-122.88121&amp;layers=BFTFFFTFFFF0FF">your particular example</a> it might be worth raising it with the OpenSeaMap devs** - perhaps you may be able to persuade them that a single buoy in the open ocean is worth rendering at a higher zoom level.</p>
<p>If that's not an option, then as ToeBee suggests rendering your own maps is probably the way to go. Various questions have been asked on this before here - try reading the answers to a search like <a href="http://help.openstreetmap.org/search/?q=rendering&amp;Submit=search&amp;t=question">this</a> or <a href="http://help.openstreetmap.org/search/?q=maperitive&amp;Submit=search&amp;t=question">this</a>.</p>
<p>** There are some mailing lists mentioned on <a href="http://wiki.openstreetmap.org/wiki/OpenSeaMap">this wiki page</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15630" class="comments-container">
<span id="24248"></span>
<div id="comment-24248" class="comment">
<div id="post-24248-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The openseamap-develop mailing list is hosted on Sourceforge - gah! Can't search.</p>
</div>
<div id="comment-24248-info" class="comment-info">
<span class="comment-age">(15 Jul '13, 10:51)</span> <span class="comment-user userinfo">dandv</span>
</div>
</div>
<span id="24251"></span>
<div id="comment-24251" class="comment">
<div id="post-24251-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Posted on <a href="https://sourceforge.net/mailarchive/message.php?msg_id=31169830">openseamap-develop</a>.</p>
</div>
<div id="comment-24251-info" class="comment-info">
<span class="comment-age">(15 Jul '13, 11:34)</span> <span class="comment-user userinfo">dandv</span>
</div>
</div>
</div>
<div id="comment-tools-15630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15630-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15641"></span>

<div id="answer-container-15641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15641-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Probably not satisfactory, but you can, for example, do <a href="http://www.openstreetmap.org/?lat=37.357&amp;lon=-122.881&amp;zoom=10&amp;layers=M&amp;node=664318897">this</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '12, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/e3fd0c6e01ccf0d708c0d2fba9a03467?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdoerr&#39;s gravatar image" />
<p><span>sdoerr</span><br />
<span class="score" title="1461 reputation points"><span>1.5k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdoerr has 3 accepted answers">8%</span></p>
</div>
</div>
<div id="comments-container-15641" class="comments-container">
&#10;</div>
<div id="comment-tools-15641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15641-form-container" class="comment-form-container">
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

