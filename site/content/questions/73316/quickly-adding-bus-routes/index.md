+++
type = "question"
title = "Quickly adding bus routes"
description = '''I&#x27;m working on adding missing bus lines as well but it&#x27;s taking me forever to add relations street by street on the route. Is there a quicker way to add bus routes (in entirety) to OSM without going step by step? For example, I tried highlighting my route by holding the shift key along each street b...'''
date = "2020-03-02T22:30:00Z"
lastmod = "2020-03-03T23:11:00Z"
weight = 73316
keywords = [ "id", "busroutes" ]
aliases = [ "/questions/73316" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Quickly adding bus routes](/questions/73316/quickly-adding-bus-routes)

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
<span id="post-73316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73316-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on adding missing bus lines as well but it's taking me forever to add relations street by street on the route. Is there a quicker way to add bus routes (in entirety) to OSM without going step by step?</p>
<p>For example, I tried highlighting my route by holding the shift key along each street but found no way to a single bus route relation at one time. Is this possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-busroutes" rel="tag" title="see questions tagged &#39;busroutes&#39;">busroutes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '20, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/70ca8a1b99d781d5b1f87d5eab857636?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michaela&#39;s gravatar image" />
<p><span>Michaela</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michaela has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>02 Mar '20, 23:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span></p>
</div>
</div>
<div id="comments-container-73316" class="comments-container">
<span id="73317"></span>
<div id="comment-73317" class="comment">
<div id="post-73317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have converted this to a new question rather than an answer to an old one.</p>
</div>
<div id="comment-73317-info" class="comment-info">
<span class="comment-age">(02 Mar '20, 23:25)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-73316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73316-form-container" class="comment-form-container">
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

<span id="73349"></span>

<div id="answer-container-73349" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73349-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are using JOSM, you can definitely add several members to a relation. One way is to select the ways, and right-click on the relation in the relation list, and choose "add members" (or something, mine is french). An other way is to keep the relation window open (double-click on the relation to open it, there's also a dedicated button), and use the arrow between right (selected ways) and left (already in the relation) panels. The bonus is that you can check continuity.</p>
<p>Side note, it's probably a bad idea to add several streets to a bus route relation at once, because you have to check at each crossing that the street is not going further than you want, or cut the way and select only the good part. That's probably where PT_Assistant comes handy, but I've never used it.</p>
<p>If you're using iD, in my humble opinion you should not try to work on bus routes.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73349" class="comments-container">
&#10;</div>
<div id="comment-tools-73349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73349-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73319"></span>

<div id="answer-container-73319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/PT_Assistant">PT_Assistant plugin</a> for JOSM has some tricks to speed up this process. I'm not so familiar with it, but user <a href="https://www.openstreetmap.org/user/Polyglot">Polyglot</a> is probably willing to get you started.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 04:04</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-73319" class="comments-container">
&#10;</div>
<div id="comment-tools-73319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73319-form-container" class="comment-form-container">
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

