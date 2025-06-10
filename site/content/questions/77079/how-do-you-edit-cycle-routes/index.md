+++
type = "question"
title = "How do you edit cycle routes"
description = '''Hello! I&#x27;ve been getting interested in the various bike routes across the US. In particular the East Coast Greenway. I noticed a discrepancy between what is on the East Coast Greenway Website (which I believe is freely available) https://map.greenway.org/?loc=15,39.95298,-75.14820  And what is curre...'''
date = "2020-10-13T21:06:00Z"
lastmod = "2020-10-19T18:47:00Z"
weight = 77079
keywords = [ "editing", "tagging", "cycleway" ]
aliases = [ "/questions/77079" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you edit cycle routes](/questions/77079/how-do-you-edit-cycle-routes)

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
<span id="post-77079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77079-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I've been getting interested in the various bike routes across the US. In particular the East Coast Greenway. I noticed a discrepancy between what is on the East Coast Greenway Website (which I believe is freely available)</p>
<p><a href="https://map.greenway.org/?loc=15,39.95298,-75.14820">https://map.greenway.org/?loc=15,39.95298,-75.14820</a></p>
<p>And what is currently in Open Street map, particularly the connection from Philadelphia across the Ben Franklin Bridge. I noticed that these kind of paths seem to be notated using tags, but didn't feel confident to undo current tags and redo them to match the current greenway. Does anybody have any suggestions for best practices in editing these bike routes? Double tag first then delete incorrect tags? Delete first then redo? Is there a better tool?</p>
<p>Any guidance is much appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-cycleway" rel="tag" title="see questions tagged &#39;cycleway&#39;">cycleway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '20, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0eeda9ad2431bdadc8d9f97d7e71e700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="benbyday&#39;s gravatar image" />
<p><span>benbyday</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="benbyday has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77079" class="comments-container">
<span id="77107"></span>
<div id="comment-77107" class="comment">
<div id="post-77107-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note: OSM goes primarily with signage on the ground, which may not be the same as as websites/documentation.</p>
</div>
<div id="comment-77107-info" class="comment-info">
<span class="comment-age">(14 Oct '20, 19:56)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="77158"></span>
<div id="comment-77158" class="comment">
<div id="post-77158-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I took the route myself and the section I'm thinking of did not have signage for what is in OSM currently. Based on my trip, what is currently on the greenway website is almost certainly correct.</p>
</div>
<div id="comment-77158-info" class="comment-info">
<span class="comment-age">(19 Oct '20, 18:47)</span> <span class="comment-user userinfo">benbyday</span>
</div>
</div>
</div>
<div id="comment-tools-77079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77079-form-container" class="comment-form-container">
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

<span id="77094"></span>

<div id="answer-container-77094" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77094-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-77094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Routes of any kind are typically modelled with route relations, not with direct tagging on the objects themselves.</p>
<p>Essentially a route relation is simply an ordered list of the ways the route traverses, so nothing that is conceptually complicated. The route relation further holds the tags that describe the route, for example a name of a ref value.</p>
<p>I would recommend discussing the specific issue on the US mailing list, there are a number of participants that are very knowledgeable about US cycle infrastructure and can surely help.</p>
<p>See also</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Relation:route">https://wiki.openstreetmap.org/wiki/Relation:route</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Cycle_routes">https://wiki.openstreetmap.org/wiki/Cycle_routes</a></li>
<li><a href="https://lists.openstreetmap.org/listinfo/talk-us">https://lists.openstreetmap.org/listinfo/talk-us</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Oct '20, 08:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Oct '20, 08:21</strong> </span></p>
</div>
</div>
<div id="comments-container-77094" class="comments-container">
&#10;</div>
<div id="comment-tools-77094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77094-form-container" class="comment-form-container">
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

