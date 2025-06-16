+++
type = "question"
title = "Surface area, address and gps coordinates of marked buildings"
description = '''Hi, is there an index lying around somewhere containing a list of all marked buildings with their address, gps coordinates and surface area? Thanks '''
date = "2013-04-14T10:59:00Z"
lastmod = "2013-05-21T17:25:00Z"
weight = 21518
keywords = [ "buildings", "geocoding" ]
aliases = [ "/questions/21518" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Surface area, address and gps coordinates of marked buildings](/questions/21518/surface-area-address-and-gps-coordinates-of-marked-buildings)

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
<span id="post-21518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, is there an index lying around somewhere containing a list of all marked buildings with their address, gps coordinates and surface area? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Apr '13, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/945b96ea66806f9d7554e3ca0b3d33af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="melnik&#39;s gravatar image" />
<p><span>melnik</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="melnik has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '13, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-21518" class="comments-container">
&#10;</div>
<div id="comment-tools-21518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21518-form-container" class="comment-form-container">
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

<span id="22606"></span>

<div id="answer-container-22606" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22606-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is no. The data's all in a big database, but you'll need to extract the data that you're interested in and calculate e.g. the surface area.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Beginners_Guide_1.3">This page</a> of the beginner's guide explains the sort of data that there is - nodes (each with a latitude and longitude), ways (connected nodes) and relations. Buildings will typically be closed ways (as on that page) or <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygons</a> (one or more outer areas from which one or more inner areas must be subtracted).</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Building">This page</a> explains a bit about how buildings are mapped.</p>
<p>In order to obtain the data, you'll either want to process an XML data extract (see the links from <a href="http://planet.openstreetmap.org/">this page</a>) or use a querying mechanism such as <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> to fetch it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '13, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-22606" class="comments-container">
&#10;</div>
<div id="comment-tools-22606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22606-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21519"></span>

<div id="answer-container-21519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21519-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Melnik, since were all contributing to a database, the answer should be yes. But I don’t expect its just waiting there for you. You should do some programming to get it. What do you mean by coordinates of a building, the centre, the surroundings ? Success making a query with the right defenitions, it ll be a hell of a job and dont forget the size of the results worldwide ! You should ask yourself if you want it all at the same time or bit by bit. And the last question is why or whats the use of it ? Greetz, welcome and happy mapping.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '13, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-21519" class="comments-container">
&#10;</div>
<div id="comment-tools-21519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21519-form-container" class="comment-form-container">
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

