+++
type = "question"
title = "House reported in wrong township"
description = '''A search for my home address from the openstreetmap.org main window used to return an incorrect location in a neighboring township. I corrected the location by adding a point with an address tag containing house number field and an explicit city field. Now when I search for the address the map shows...'''
date = "2019-03-08T16:11:00Z"
lastmod = "2019-03-09T06:48:00Z"
weight = 68332
keywords = [ "incorrect", "nominatim", "address" ]
aliases = [ "/questions/68332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [House reported in wrong township](/questions/68332/house-reported-in-wrong-township)

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
<span id="post-68332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A search for my home address from the openstreetmap.org main window used to return an incorrect location in a neighboring township. I corrected the location by adding a point with an address tag containing house number field and an explicit city field. Now when I search for the address the map shows the correct location, but it still reports the wrong township. How can I correct this. (It reports Dexter Township rather than Lima Township.) How can I correct this?</p>
<p>My concern is in this area: <a href="https://www.openstreetmap.org/#map=19/42.34082/-83.98158">https://www.openstreetmap.org/#map=19/42.34082/-83.98158</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '19, 16:11</strong></p>
<img src="https://secure.gravatar.com/avatar/87cc29515008b4c6ea6d15a979a20c54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Gourlay&#39;s gravatar image" />
<p><span>John Gourlay</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Gourlay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '19, 10:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-68332" class="comments-container">
&#10;</div>
<div id="comment-tools-68332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68332-form-container" class="comment-form-container">
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

<span id="68333"></span>

<div id="answer-container-68333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The system that powers the search associates each address with a street, associates each street with a city and then pulls the city from the street (as I see you've speculated about when you added the address point).</p>
<p>I think there are some plans to also index addr:city from addresses.</p>
<p>I guess adding a named driveway that is in the correct township would get it to work. That sort of thing is sort of frowned on, fudging the data a bit for a particular piece of software.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '19, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-68333" class="comments-container">
<span id="68335"></span>
<div id="comment-68335" class="comment">
<div id="post-68335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are many streets that cross political boundaries. Does this answer imply that such streets must be broken into segments, one for each municipality?</p>
</div>
<div id="comment-68335-info" class="comment-info">
<span class="comment-age">(08 Mar '19, 22:53)</span> <span class="comment-user userinfo">John Gourlay</span>
</div>
</div>
<span id="68336"></span>
<div id="comment-68336" class="comment">
<div id="post-68336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What about a street that follows the boundary between two municipalities? Houses on one side will belong to one city and houses on the other side will belong to the other city.</p>
</div>
<div id="comment-68336-info" class="comment-info">
<span class="comment-age">(08 Mar '19, 22:56)</span> <span class="comment-user userinfo">John Gourlay</span>
</div>
</div>
<span id="68337"></span>
<div id="comment-68337" class="comment">
<div id="post-68337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not exactly sure but I think it picks up the street being in two cities.</p>
<p>There's situations where it doesn't work out very well, for sure.</p>
</div>
<div id="comment-68337-info" class="comment-info">
<span class="comment-age">(09 Mar '19, 03:21)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="68338"></span>
<div id="comment-68338" class="comment">
<div id="post-68338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim does not solve the problem of streets that are on the boundary of two towns. Please note that Nominatim is not used in all OSM-based applications. Apps such as OsmAnd, Magic Earth, Mapfactor Navigator use their own algorithms to determine addresses.</p>
</div>
<div id="comment-68338-info" class="comment-info">
<span class="comment-age">(09 Mar '19, 06:48)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-68333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68333-form-container" class="comment-form-container">
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

