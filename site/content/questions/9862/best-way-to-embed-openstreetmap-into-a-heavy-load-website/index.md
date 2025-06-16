+++
type = "question"
title = "Best way to embed OpenStreetMap into a heavy load website?"
description = '''I am the project manager of a new website which uses an interactive map as part of the main functionality. We were originally going to use Google Maps, but as most of you probably know, they have started floating the idea of charging for using their services. As a result, I&#x27;m looking into alternativ...'''
date = "2012-01-09T14:36:00Z"
lastmod = "2012-01-09T14:57:00Z"
weight = 9862
keywords = [ "map", "javascript" ]
aliases = [ "/questions/9862" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to embed OpenStreetMap into a heavy load website?](/questions/9862/best-way-to-embed-openstreetmap-into-a-heavy-load-website)

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
<span id="post-9862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9862-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am the project manager of a new website which uses an interactive map as part of the main functionality. We were originally going to use Google Maps, but as most of you probably know, they have started floating the idea of charging for using their services. As a result, I'm looking into alternatives.</p>
<p>We require an interactive map that we can script on top of (i.e. we pull data from our database and overlay it in some way using JavaScript). Is hosting our own set of data files (the planet.osm for instance) our only option? What kind of requirements would we need if that is the case? What is the minimum amount of disk space we'd need?</p>
<p>Apologies if this isn't the right forum for such questions.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '12, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/7ac42249874c4efd853e421e558f2b59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rsaesha&#39;s gravatar image" />
<p><span>Rsaesha</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rsaesha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9862" class="comments-container">
&#10;</div>
<div id="comment-tools-9862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9862-form-container" class="comment-form-container">
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

<span id="9863"></span>

<div id="answer-container-9863" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9863-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-9863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a heavy load web site the best option is likely hosting your own tiles (not planet.osm - but the individual PNG files that make up the map). Commercial tile hosting is an alternative (see <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">Wiki</a>).</p>
<p>If you want to host your own tiles, the keeping and handing out of tiles is usually the smallest problem; producing and updating tiles (and updating the database from which they are produced) is more demanding. The amount of hardware you need to throw at this depends on how current your data needs to be, and how much of the world you want to show. The bottleneck is usually disk performance. If you don't need regular updates and your area of interest is limited - say, an average European country only - you can afford to pre-produce all tiles and then rest; else you'll need a server that is able to produce tiles on demand. Such a server with world-wide coverage starts at approximately 32 GB of RAM, 300 GB of SSD for the database, and 8 CPU cores. A little standard HD tile storage will also be required. There's a good <a href="https://wiki.openstreetmap.org/wiki/Minutely_Mapnik">setup documentation</a> on the Wiki and all the software required is open source, but of course professional help is available in that department as well ;)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '12, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '12, 14:54</strong> </span></p>
</div>
</div>
<div id="comments-container-9863" class="comments-container">
<span id="9865"></span>
<div id="comment-9865" class="comment">
<div id="post-9865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt we'd need regular updates. Our service deals mainly with business location rather than producing an accurate route. We'd still ideally want world-wide coverage though.</p>
</div>
<div id="comment-9865-info" class="comment-info">
<span class="comment-age">(09 Jan '12, 14:57)</span> <span class="comment-user userinfo">Rsaesha</span>
</div>
</div>
</div>
<div id="comment-tools-9863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9863-form-container" class="comment-form-container">
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

