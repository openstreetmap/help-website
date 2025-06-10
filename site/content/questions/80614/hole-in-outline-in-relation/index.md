+++
type = "question"
title = "Hole in Outline in Relation"
description = '''Hi, I&#x27;m mapping a hospital close to me with quite a complex Shape. I&#x27;ve mapped all the different parts of it with building:part=yes and put it into a relation with the role=part. This relation (a) is of type=building. See: Relation a Then I created a second relation (b) with the outline of all the p...'''
date = "2021-06-18T09:02:00Z"
lastmod = "2021-06-18T11:59:00Z"
weight = 80614
keywords = [ "building", "hole", "outlines", "relations", "multipolygon" ]
aliases = [ "/questions/80614" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Hole in Outline in Relation](/questions/80614/hole-in-outline-in-relation)

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
<span id="post-80614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80614-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm mapping a hospital close to me with quite a complex Shape. I've mapped all the different parts of it with building:part=yes and put it into a relation with the role=part. This relation (a) is of type=building. See: <a href="https://www.openstreetmap.org/relation/12854916">Relation a</a></p>
<p>Then I created a second relation (b) with the outline of all the parts but gave it the role=outer. Additionally I created a line that represents the hole of that building and gave it the role=inner. Here: <a href="https://www.openstreetmap.org/relation/12856287">Relation b</a></p>
<p>Eventually relation b becomes a part of relation a with the role=outline.</p>
<p>But it does not seem to work 100%. What am I missing here? I don't wanna mess around any more and thought I'd just ask. Google didn't rely help or I haven't found my exact problem.</p>
<p>(see my related post on <a href="https://www.reddit.com/r/openstreetmap/comments/o1rpcu/hole_in_outline_in_relation/">reddit</a>)</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-hole" rel="tag" title="see questions tagged &#39;hole&#39;">hole</span> <span class="post-tag tag-link-outlines" rel="tag" title="see questions tagged &#39;outlines&#39;">outlines</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '21, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/8c7a4a95dbbacda96c7b31c63e19f613?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="som-tam&#39;s gravatar image" />
<p><span>som-tam</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="som-tam has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80614" class="comments-container">
&#10;</div>
<div id="comment-tools-80614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80614-form-container" class="comment-form-container">
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

<span id="80617"></span>

<div id="answer-container-80617" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80617-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="som-tam has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When a building is mapped with a multipolygon, the tags for the building as a whole go only onto the multipolygon relation, not on the outer way. So you should remove the <code>building=hospital</code> tag from <a href="https://www.openstreetmap.org/way/955078388">w955078388</a>. Apart from that, the mapping looks correct to me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '21, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-80617" class="comments-container">
<span id="80618"></span>
<div id="comment-80618" class="comment">
<div id="post-80618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's it. Thank you.</p>
</div>
<div id="comment-80618-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 11:05)</span> <span class="comment-user userinfo">som-tam</span>
</div>
</div>
<span id="80619"></span>
<div id="comment-80619" class="comment">
<div id="post-80619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also no need to use relations to map building parts, you can just rely on the geometrical relationships</p>
</div>
<div id="comment-80619-info" class="comment-info">
<span class="comment-age">(18 Jun '21, 11:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80617-form-container" class="comment-form-container">
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

