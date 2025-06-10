+++
type = "question"
title = "How to deal with datasets of (proposed) historical objects"
description = '''Recently I came across a map feature in my vicinity where someone entered a highway proposed in the early 20th century, which was never built. The highway is tagged abandoned=yes, abandoned:construction=motorway, abandoned:highway=construction and highway=proposed. It shows up like a proposed or und...'''
date = "2015-04-28T14:03:00Z"
lastmod = "2015-04-28T15:01:00Z"
weight = 42639
keywords = [ "proposed", "abandoned", "historical" ]
aliases = [ "/questions/42639" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to deal with datasets of (proposed) historical objects](/questions/42639/how-to-deal-with-datasets-of-proposed-historical-objects)

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
<span id="post-42639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42639-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently I came across a map feature in my vicinity where someone entered a <a href="http://www.openstreetmap.org/way/332527954#map=15/48.9790/12.0981">highway proposed in the early 20th century</a>, which was never built. The highway is tagged <code>abandoned=yes</code>, <code>abandoned:construction=motorway</code>, <code>abandoned:highway=construction</code> and <code>highway=proposed</code>. It shows up like a proposed or under construction highway on the map and it looks like the user that added it is or was adding lots of such motorway that were planned or partially realized by the German authorities in the early 20th century. However, it looks like construction actually never started or at least only some very basic preparation work was done since there aren't any obvious hints for it neither on aerial imagery nor directly visible in the landscape.</p>
<p>At first look I though "oh nice, they're building a bypass to the often crowded interchange further west..." until I realized that this thing was abandoned long time ago. I also understand that it might be interesting from a historical point of view, but then I think it shouldn't be on a map contemporary map as it is displayed as under construction bus is actually never going to happen.</p>
<p>So my question is, how to deal with that? Should I contact the guy that added them? Is there some general discussion board where such cases can be disputed with a wider audience?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-proposed" rel="tag" title="see questions tagged &#39;proposed&#39;">proposed</span> <span class="post-tag tag-link-abandoned" rel="tag" title="see questions tagged &#39;abandoned&#39;">abandoned</span> <span class="post-tag tag-link-historical" rel="tag" title="see questions tagged &#39;historical&#39;">historical</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '15, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/08858c52af8d4cabb3fef25d99a94a5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bbauer&#39;s gravatar image" />
<p><span>bbauer</span><br />
<span class="score" title="86 reputation points">86</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bbauer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42639" class="comments-container">
&#10;</div>
<div id="comment-tools-42639" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42639-form-container" class="comment-form-container">
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

<span id="42640"></span>

<div id="answer-container-42640" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42640-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42640-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-42640-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bbauer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To your last question, if you are wondering what a user has mapped or why they did it a certain way, you should definitely contact them, with with a private OSM message or comment on the changeset (which is public).</p>
<p>To the larger question, OSM runs on the general principle "<a href="http://wiki.openstreetmap.org/wiki/Good_practice#Map_what.27s_on_the_ground">map what's on the ground</a>", which would tend to mean that something like what you describe should not be in the database.</p>
<p>However, there is not complete consensus about this. For example, there was a long <a href="https://lists.openstreetmap.org/pipermail/talk-us/2015-April/thread.html">discussion</a> in April 2015 on talk-us (multiple threads) about whether <a href="http://wiki.openstreetmap.org/wiki/Key:abandoned:*">abandoned</a> (not used, but still with evidence on the ground) and/or <a href="http://wiki.openstreetmap.org/wiki/Demolished_Railway">razed</a> (completely removed) railroads should be kept in OSM. There was general consensus to keep abandoned-tagged features, but disagreement about razed-tagged features. Many argued against keeping them in OSM for the above reasons, but some, especially railway mappers, argued to keep them in OSM. A "third way" that was also discussed is for historical objects to be moved to <a href="http://www.openhistoricalmap.org">OpenHistoricalMap</a>, but that project is still a work in progress.</p>
<p>As the above also shows, a place to discuss these issues is on the <a href="http://wiki.openstreetmap.org/wiki/Mailing_lists#Country-Specific_Lists">local OSM mailing list</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '15, 15:01</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-42640" class="comments-container">
&#10;</div>
<div id="comment-tools-42640" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42640-form-container" class="comment-form-container">
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

