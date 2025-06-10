+++
type = "question"
title = "Tags for Mine Extents"
description = '''Hi, I would like to map the Coal mines of the Hunter Valley in NSW, Australia. There are a number of things I would like to map, which don&#x27;t seem to have valid tags listed in the wiki:  Boundary of Mine Lease ( Above ground ) - usually significantly larger than the actual mine, but still inaccessibl...'''
date = "2013-09-04T22:20:00Z"
lastmod = "2013-09-06T16:01:00Z"
weight = 26126
keywords = [ "landuse", "man_made" ]
aliases = [ "/questions/26126" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tags for Mine Extents](/questions/26126/tags-for-mine-extents)

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
<span id="post-26126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26126-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I would like to map the Coal mines of the Hunter Valley in NSW, Australia.</p>
<p>There are a number of things I would like to map, which don't seem to have valid tags listed in the wiki:</p>
<ul>
<li>Boundary of Mine Lease ( Above ground ) - usually significantly larger than the actual mine, but still inaccessible to the public, and often contains many private roads.</li>
<li>Boundary of Mine Lease ( Below ground ) - same, but no indications on the surface.</li>
<li>Boundary of actual mined area below ground and underground passages (if available)</li>
<li>Mineral stockpile areas such as here: <a href="http://goo.gl/maps/DpSmX">Kooragang Island (google maps)</a></li>
<li>Conveyor belts for transporting coal</li>
</ul>
<p>Please advise which tags I should use for these.</p>
<p>Thanks,</p>
<p>Evan</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-man_made" rel="tag" title="see questions tagged &#39;man_made&#39;">man_made</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '13, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dd71eb6754ee216d8f526217d492e4e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ozhiker&#39;s gravatar image" />
<p><span>ozhiker</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ozhiker has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26126" class="comments-container">
&#10;</div>
<div id="comment-tools-26126" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26126-form-container" class="comment-form-container">
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

<span id="26156"></span>

<div id="answer-container-26156" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26156-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Evan,</p>
<p>i'll suggest a few things, other peope will probably suggest different things.</p>
<blockquote>
<p>Boundary of Mine Lease ( Above ground ) - usually significantly larger than the actual mine, but still inaccessible to the public, and often contains many private roads.</p>
</blockquote>
<p>If the area is designated as "private" on the ground as with a fence or signs, tag it as a polygon with <code>access=private</code> and <code>name=XY Coal mine site</code></p>
<blockquote>
<p>Boundary of Mine Lease ( Below ground ) - same, but no indications on the surface.</p>
</blockquote>
<p>I'd not input the data to OSM if it is not verifiable by other members of the OSM community. Where do you get the knowledge of the lease area from? Is it public?</p>
<blockquote>
<p>Boundary of actual mined area below ground and underground passages (if available)</p>
</blockquote>
<p>Same as above, but i would be even more reluctant to import such data into OSM. It will get outdates pretty soon, also (at least here in germany) the exact mine plans are considered very sensitive information and not disseminated to the public. They will get outdated soon, as the mining activity progesses.</p>
<blockquote>
<p>Mineral stockpile areas such as here: Kooragang Island (google maps)</p>
</blockquote>
<p>Use <code>landuse=landfill</code> or <code>landuse=spoil_heap</code></p>
<blockquote>
<p>Conveyor belts for transporting coal</p>
</blockquote>
<p>The one I know of is tagged <code>aerialway=goods</code> <a href="http://www.openstreetmap.org/browse/way/94255954">http://www.openstreetmap.org/browse/way/94255954</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '13, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-26156" class="comments-container">
<span id="26162"></span>
<div id="comment-26162" class="comment">
<div id="post-26162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would not consider a polygon with a name and access tag as valid. A tag qualifying the closed way is required. We even don't know if it is an area ! Look also "man_made=conveyor" Try "landuse=stockpile"</p>
<p>All these points should be discussed on the tagging@openstreetmap.org mailing list</p>
</div>
<div id="comment-26162-info" class="comment-info">
<span class="comment-age">(06 Sep '13, 16:01)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-26156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26156-form-container" class="comment-form-container">
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

