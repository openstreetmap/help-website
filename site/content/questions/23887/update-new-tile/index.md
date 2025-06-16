+++
type = "question"
title = "Update new Tile"
description = '''Hi. Please tell me where I can download the current-rendered map (Ukraine)and also that you can install for map updates. For example if splashed in a location that be opened up the existing map, while sending a request to update this locationand also if available did render a new Tile Thank you.'''
date = "2013-07-02T07:57:00Z"
lastmod = "2013-07-02T16:21:00Z"
weight = 23887
keywords = [ "update" ]
aliases = [ "/questions/23887" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Update new Tile](/questions/23887/update-new-tile)

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
<span id="post-23887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. Please tell me where I can download the current-rendered map (Ukraine)and also that you can install for map updates. For example if splashed in a location that be opened up the existing map, while sending a request to update this locationand also if available did render a new Tile</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '13, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d03eafc773f715ef9a0e5f9286c2dc7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Mityankin&#39;s gravatar image" />
<p><span>Michael Mity...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Mityankin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23887" class="comments-container">
<span id="23904"></span>
<div id="comment-23904" class="comment">
<div id="post-23904-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Double post! <a href="http://forum.openstreetmap.org/viewtopic.php?id=21713">http://forum.openstreetmap.org/viewtopic.php?id=21713</a></p>
</div>
<div id="comment-23904-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 16:21)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-23887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23887-form-container" class="comment-form-container">
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

<span id="23898"></span>

<div id="answer-container-23898" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23898-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-23898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Michael Mityankin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a whole country, generally you shouldn't seek to download the standard OpenStreetMap rendered map in tile format. Requesting so many tiles puts too much load on our servers, and is therefore discouraged or forbidden by our <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy</a>.</p>
<p>Instead, you should download the raw (unrendered) data for your country. The best source for this is <a href="http://download.geofabrik.de/">Geofabrik's extract service</a>.</p>
<p>You can then use a renderer on your computer to take this data and make a lovely map out of it. The best-known renderer is Mapnik, for which <a href="http://www.mapbox.com/tilemill/">TileMill</a> provides a (fairly) understandable package and frontend.</p>
<p>You can keep your map up-to-date by downloading 'diff' files and applying them to it, but since these include all changes all over the world, your database will soon balloon way beyond the size of Ukraine. It's probably better just to download a new extract from Geofabrik every week.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jul '13, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-23898" class="comments-container">
<span id="23899"></span>
<div id="comment-23899" class="comment">
<div id="post-23899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The specifics my map is necessary that the actual map of certain areas scattered across the country. For this do not want to render maps of the whole country (large load on the server). Part on this and asked how can be configured when opening location my maps update + render if available (to display at next time), opening at this moment the old data.</p>
</div>
<div id="comment-23899-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 12:26)</span> <span class="comment-user userinfo">Michael Mity...</span>
</div>
</div>
<span id="23903"></span>
<div id="comment-23903" class="comment">
<div id="post-23903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. whis Planet.osm/diffs I'll keep an updated database ? But rendering? my server dies, interminable rendering</p>
</div>
<div id="comment-23903-info" class="comment-info">
<span class="comment-age">(02 Jul '13, 14:46)</span> <span class="comment-user userinfo">Michael Mity...</span>
</div>
</div>
</div>
<div id="comment-tools-23898" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23898-form-container" class="comment-form-container">
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

