+++
type = "question"
title = "Is there any correlation between ways in OpenStreetMaps?"
description = '''Hello All, Currently I am working on finding all the intersecting nodes present in a region of OpenSteetMap. I wrote a program in python, which is working fine for small areas. But if I run the same program for the whole Niedersachsen, it takes many days to complete. My code is comparing each way wi...'''
date = "2013-04-22T10:01:00Z"
lastmod = "2013-04-22T11:18:00Z"
weight = 21705
keywords = [ "openstreetmap", "ways", "intersection", "python" ]
aliases = [ "/questions/21705" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there any correlation between ways in OpenStreetMaps?](/questions/21705/is-there-any-correlation-between-ways-in-openstreetmaps)

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
<span id="post-21705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello All,</p>
<p>Currently I am working on finding all the intersecting nodes present in a region of OpenSteetMap. I wrote a program in python, which is working fine for small areas. But if I run the same program for the whole Niedersachsen, it takes many days to complete. My code is comparing each way with all other ways present in the map, to find intersecting nodes. This method is not efficient for very large data. I can optimize my code if somehow I just restrict the comparison of ways to small region only, not for the whole region. May be there is some correlation between way ids, which I need to know. Or maybe I somehow identify the smallest possible region, which may include all the correlated ways. Please advise.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '13, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f5d31b13d0fced1a8297e7d9e9385a53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tfarooqi&#39;s gravatar image" />
<p><span>tfarooqi</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tfarooqi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Apr '13, 10:27</strong> </span></p>
</div>
</div>
<div id="comments-container-21705" class="comments-container">
&#10;</div>
<div id="comment-tools-21705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21705-form-container" class="comment-form-container">
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

<span id="21711"></span>

<div id="answer-container-21711" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21711-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tfarooqi has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no correlation between node IDs and area.</p>
<p>Assuming that you really want to find intersecting <em>nodes</em> (as opposed to non-noded intersections), use the following algorithm:</p>
<ul>
<li>Use a hash table to store "link counters"</li>
<li>Process all ways; each time a node is referenced by a way, increase the node's link counter in your hash table by one</li>
<li>when finished, look at your hash table - all node IDs with a link counter greater than one are junction or intersection nodes.</li>
<li>If you only want to find nodes where ways cross (and not those where one way ends on a node belonging to another way) then modify step 2 and only look at all inner nodes of the way (ignoring the end nodes).</li>
</ul>
<p>Another option for solving your problem is computing a bounding box for every way (i.e. the minimum and maximum latitude and longitude), and then restrict comparison to ways whose bounding boxes intersect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Apr '13, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-21711" class="comments-container">
<span id="21713"></span>
<div id="comment-21713" class="comment">
<div id="post-21713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was thinking on the same direction of creating a hash table.But I thought there must be a better way. Using the bounding box to restrict the way comparison is also a good idea but I think finding the intersection of bounding box will lead to the same issue which I am currently facing</p>
</div>
<div id="comment-21713-info" class="comment-info">
<span class="comment-age">(22 Apr '13, 11:06)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
<span id="21714"></span>
<div id="comment-21714" class="comment">
<div id="post-21714-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But I thank you Mr. Ramm for your valueable comments.</p>
</div>
<div id="comment-21714-info" class="comment-info">
<span class="comment-age">(22 Apr '13, 11:18)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
</div>
<div id="comment-tools-21711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21711-form-container" class="comment-form-container">
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

