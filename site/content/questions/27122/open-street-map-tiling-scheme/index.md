+++
type = "question"
title = "Open Street map tiling scheme"
description = '''I was just taking a look at the osm slippy map tiling scheme and i observed that although at zoom level 1 the split along y (latitude) seems exactly half (-85 deg to 0 deg to 85 deg), at zoom level 2 the splitting is quite uneven (0 to 66 deg to 85 deg). As a result if i try to download a tile assum...'''
date = "2013-10-13T15:32:00Z"
lastmod = "2013-10-14T13:17:00Z"
weight = 27122
keywords = [ "slippymap" ]
aliases = [ "/questions/27122" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Open Street map tiling scheme](/questions/27122/open-street-map-tiling-scheme)

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
<span id="post-27122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27122-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was just taking a look at the osm slippy map tiling scheme and i observed that although at zoom level 1 the split along y (latitude) seems exactly half (-85 deg to 0 deg to 85 deg), at zoom level 2 the splitting is quite uneven (0 to 66 deg to 85 deg). As a result if i try to download a tile assuming even splitting there seems to be significant difference. Can you tell me why the split is such and is there any way it could be mapped to a perfectly splitting tiling scheme?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '13, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/825e67b341af61d857045c0f3e858980?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raveesh&#39;s gravatar image" />
<p><span>raveesh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raveesh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27122" class="comments-container">
<span id="27123"></span>
<div id="comment-27123" class="comment">
<div id="post-27123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is your actual problem? If you want to determine the name of the slippy map tile for a given latitude, longitude and zoom level then just read the <a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">slippy map tilenames wiki page</a>.</p>
</div>
<div id="comment-27123-info" class="comment-info">
<span class="comment-age">(13 Oct '13, 15:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27124"></span>
<div id="comment-27124" class="comment">
<div id="post-27124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually in my app, i have a map with perfectly splitting tiling scheme(latitude -&gt; -90, -45, 0, 45, 90). I was trying to see if i could download and attach some osm images on top of these tiles for some particular country. But due to the difference the data is quite different from what i expect. Hence on Africa, i almost end up mapping Europe. My only question is why was it chosen to be uneven and how can i still make use of it in a perfecty even tiling scheme environment?</p>
</div>
<div id="comment-27124-info" class="comment-info">
<span class="comment-age">(13 Oct '13, 17:05)</span> <span class="comment-user userinfo">raveesh</span>
</div>
</div>
<span id="27125"></span>
<div id="comment-27125" class="comment">
<div id="post-27125-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know why it was chosen like this but the only solutions seems to be cutting and stitching. Use the formula to calculate which and how many OSM tiles are required in order to create a specific tile for your application. Then download them (without violating the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a>) and generate your tile from it. Or just use a <a href="https://wiki.openstreetmap.org/wiki/WMS#OSM_WMS_Servers">WMS server</a> which does all the magic for you.</p>
</div>
<div id="comment-27125-info" class="comment-info">
<span class="comment-age">(13 Oct '13, 17:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27122-form-container" class="comment-form-container">
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

<span id="27146"></span>

<div id="answer-container-27146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This has to do with the <a href="https://en.wikipedia.org/wiki/Map_projection">projection</a> being used. This is usually <a href="https://en.wikipedia.org/wiki/Mercator_projection">mercator</a>, which doesn't use the same scale near the equator and near the poles. The tiles always split the previous zoom's image evenly, but that original image may be deformed in ways you didn't expect.</p>
<p>However, it is possible to setup a slippymap with a different <a href="https://github.com/mapnik/mapnik/wiki/XMLConfigReference#map">projection setting for mapnik</a>. If you want all tiles from a given zoomlevel to span as many degrees latitude as longitude, try the <a href="https://en.wikipedia.org/wiki/Equirectangular_projection">equirectangular</a> projection. However, remember that no projection is perfect, and you'll need to deal with deformations one way or another.</p>
<p>One way to sidestep the deformation problem is to use a 3D renderer like <a href="http://marble.kde.org/">marble</a>, which takes the mercator-projected tiles from OSM and reprojects them on a globe.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '13, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-27146" class="comments-container">
&#10;</div>
<div id="comment-tools-27146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27146-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27126"></span>

<div id="answer-container-27126" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27126-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The splitting is not uneven. The map goes from -85 to +85 latitude on all zoom levels, and from coordinate "0" to coordinate "2**z-1" on all zoom levels.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '13, 17:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-27126" class="comments-container">
<span id="27127"></span>
<div id="comment-27127" class="comment">
<div id="post-27127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am sorry, i didnt get it. At zoom level 0 we have one tile covering the entire earth (-85 to +85 latitude and -180 to +180 longitude) . At zoom level 1 there are 4 tiles (-85 to 0 and 0 to 85 in latitude and -180 to 0 and 0 to 180 in longitude). But at zomm level 2 the split becomes uneven ( -85 to -66, -66 to 0, 0 to 66, 66 to 85 in latitude and -180 to -90, -90 to 0, 0 to 90, 90 to 180 in longitude). So in longitude it still remains perfectly half splitting but in latitude it doesnt. Am i wrong?</p>
</div>
<div id="comment-27127-info" class="comment-info">
<span class="comment-age">(13 Oct '13, 17:40)</span> <span class="comment-user userinfo">raveesh</span>
</div>
</div>
</div>
<div id="comment-tools-27126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27126-form-container" class="comment-form-container">
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

