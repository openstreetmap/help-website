+++
type = "question"
title = "Separating existing commercial building into two buildings"
description = '''Disclaimer ... new to OpenStreetMaps. Never edited. The buildings where I work are indicated as one building on the map. They are connected by a common breezeway, but are actually two distinct buildings with two addresses. Can the existing outline be split in two, or should I delete it and re-create...'''
date = "2018-07-02T21:56:00Z"
lastmod = "2018-07-03T04:20:00Z"
weight = 64488
keywords = [ "building", "outlines" ]
aliases = [ "/questions/64488" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Separating existing commercial building into two buildings](/questions/64488/separating-existing-commercial-building-into-two-buildings)

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
<span id="post-64488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64488-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Disclaimer ... new to OpenStreetMaps. Never edited.</p>
<p>The buildings where I work are indicated as one building on the map. They are connected by a common breezeway, but are actually two distinct buildings with two addresses. Can the existing outline be split in two, or should I delete it and re-create two new outlines?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-outlines" rel="tag" title="see questions tagged &#39;outlines&#39;">outlines</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '18, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/42d352b971a44ad58ca170ca32115a65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RWHTX&#39;s gravatar image" />
<p><span>RWHTX</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RWHTX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64488" class="comments-container">
&#10;</div>
<div id="comment-tools-64488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64488-form-container" class="comment-form-container">
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

<span id="64491"></span>

<div id="answer-container-64491" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64491-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer depends a lot on what software you're using to edit the map. In this situation, I'd use JOSM along with the "utilplugin2" plugin, which provides a "Split Object" function under the "More Tools" menu. You can select nodes to indicate the dividing line and use the Split Object function, and presto, two buildings.</p>
<p>JOSM has a steep learning curve though, so if you've never done any editing at all it might be easier to start with the built-in web-based editor Id, which includes a beginners tutorial. But Id does not (best I know) have any automatic way to split a building. If I had to do this task with Id, I'd just build two new buildings over the existing one, re-using the existing nodes as much as possible to maintain the shape, then delete the original. But it's always better IMO to recycle than delete.</p>
<p>Also be aware that it's perfectly normal for a single building to have multiple addresses, so leaving it as a single building might be just as "correct" in some sense. For multi-address buildings, the norm is to not add any <code>addr:*</code> tags to the building itself, but rather create a node inside the perimeter for each address (near that address's entrance, if there are separate entrances) and add the <code>addr:*</code> tags to those nodes. Eg, <a href="https://www.openstreetmap.org/way/55932520">https://www.openstreetmap.org/way/55932520</a></p>
<p>See also <a href="https://wiki.openstreetmap.org/wiki/Beginners%27_guide">https://wiki.openstreetmap.org/wiki/Beginners%27_guide</a> for some basic background on contributing to the map.</p>
<p>Good luck! j</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '18, 00:51</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '18, 00:58</strong> </span></p>
</div>
</div>
<div id="comments-container-64491" class="comments-container">
<span id="64493"></span>
<div id="comment-64493" class="comment">
<div id="post-64493-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In addition to this answer, you could always make the outline smaller so it fits around one of the 2 buildings and draw a new rectangle or polygon for the second building. No need for a special tool to split a building.</p>
</div>
<div id="comment-64493-info" class="comment-info">
<span class="comment-age">(03 Jul '18, 04:20)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-64491" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64491-form-container" class="comment-form-container">
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

