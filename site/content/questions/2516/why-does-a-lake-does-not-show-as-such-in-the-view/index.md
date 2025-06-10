+++
type = "question"
title = "Why does a lake does not show as such in the view?"
description = '''I have drawn in a lake and the tags are the same as several others that I have done but the lake does not show in the OSM &quot;view&quot;. The name shows but the lake does not. Can&#x27;t find anything different about this looking at other lakes I have done. The main tag is natural=water and I have double checked...'''
date = "2011-01-28T15:00:00Z"
lastmod = "2011-01-28T18:52:00Z"
weight = 2516
keywords = [ "water", "natural", "lake" ]
aliases = [ "/questions/2516" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does a lake does not show as such in the view?](/questions/2516/why-does-a-lake-does-not-show-as-such-in-the-view)

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
<span id="post-2516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2516-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-2516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have drawn in a lake and the tags are the same as several others that I have done but the lake does not show in the OSM "view". The name shows but the lake does not. Can't find anything different about this looking at other lakes I have done. The main tag is natural=water and I have double checked that the outline I made is one single connected way. I have given the rendering several days to show up.</p>
<p>You can look at this by going to "Hidden Valley Lake, IN".</p>
<p>What am I missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '11, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/5628aa29417d4023bd222cda5a55fad7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="discus277&#39;s gravatar image" />
<p><span>discus277</span><br />
<span class="score" title="299 reputation points">299</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="discus277 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2516" class="comments-container">
&#10;</div>
<div id="comment-tools-2516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2516-form-container" class="comment-form-container">
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

<span id="2519"></span>

<div id="answer-container-2519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2519-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The problem in this case is that the ends of the way you drew haven't joined correctly. If you look at: <a href="http://www.openstreetmap.org/browse/way/96105269"></a><a href="http://www.openstreetmap.org/browse/way/96105269"></a><a href="http://www.openstreetmap.org/browse/way/96105269">http://www.openstreetmap.org/browse/way/96105269</a> you would expect for a closed way (representing an area) that the first and last node IDs would match. If you look closely the last node actually matches the second node in the list. The first node seems to be hidden under the node where the way joins (in Potlatch 1). I dragged the join node slightly and the extra node appeared. Select that node and delete it and I think the then closed way should render correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '11, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2519" class="comments-container">
<span id="2523"></span>
<div id="comment-2523" class="comment">
<div id="post-2523-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You were right. I went back and looked at the area your node pointed to and found some extra nodes hiding there. Also found a couple of zig zags at the other end of the lake.</p>
<p>It now displays as a lake. Thanks</p>
</div>
<div id="comment-2523-info" class="comment-info">
<span class="comment-age">(28 Jan '11, 18:52)</span> <span class="comment-user userinfo">discus277</span>
</div>
</div>
</div>
<div id="comment-tools-2519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2519-form-container" class="comment-form-container">
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

