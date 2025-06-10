+++
type = "question"
title = "island tagging issue"
description = '''I am armchair mapping Singö in Sweden, and have added a small islet called Skorven https://www.openstreetmap.org/way/806299103#map=17/60.16293/18.78259 The islet rendering fails - I think I may need to add it as a member of the multipolygon?  I am reluctant to &#x27;experiment&#x27; in case I break the coastl...'''
date = "2020-05-20T07:39:00Z"
lastmod = "2020-05-20T08:56:00Z"
weight = 74921
keywords = [ "islet", "sweden", "tagging", "coastline" ]
aliases = [ "/questions/74921" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [island tagging issue](/questions/74921/island-tagging-issue)

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
<span id="post-74921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74921-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am armchair mapping Singö in Sweden, and have added a small islet called Skorven <a href="https://www.openstreetmap.org/way/806299103#map=17/60.16293/18.78259">https://www.openstreetmap.org/way/806299103#map=17/60.16293/18.78259</a></p>
<p>The islet rendering fails - I think I may need to add it as a member of the multipolygon?</p>
<p>I am reluctant to 'experiment' in case I break the coastline and flood Sweden :-D</p>
<p>I would be really grateful for any help correcting the tagging.</p>
<p>Chas66</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islet" rel="tag" title="see questions tagged &#39;islet&#39;">islet</span> <span class="post-tag tag-link-sweden" rel="tag" title="see questions tagged &#39;sweden&#39;">sweden</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '20, 07:39</strong></p>
<img src="https://secure.gravatar.com/avatar/12ac37473087d7d6d667c276a879eec0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chas66&#39;s gravatar image" />
<p><span>chas66</span><br />
<span class="score" title="220 reputation points">220</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chas66 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '20, 08:02</strong> </span></p>
</div>
</div>
<div id="comments-container-74921" class="comments-container">
&#10;</div>
<div id="comment-tools-74921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74921-form-container" class="comment-form-container">
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

<span id="74923"></span>

<div id="answer-container-74923" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74923-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chas66 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As it is tidal it will need <code>natural=coastline</code> on the outer way. Note that coastline is special in that the order of the nodes must be so that the land is on the left side of the way as drawn.</p>
<p>Coastline rendering is also a little special and takes longer than other features as it needs a fair amount of pre-processing, so once you have added this tag you will need to be patient.</p>
<p>Further information is <a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 08:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-74923" class="comments-container">
&#10;</div>
<div id="comment-tools-74923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74924"></span>

<div id="answer-container-74924" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74924-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-74924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd say you have to add <code>natural=coastline</code> to the islet. But be aware that coastlines are processes at much bigger intervals than other data on the standard map style.</p>
<p>Please refer to the wiki for more information:<br />
<a href="https://wiki.openstreetmap.org/wiki/Coastline">https://wiki.openstreetmap.org/wiki/Coastline</a><br />
<a href="https://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline">https://wiki.openstreetmap.org/wiki/Tag:natural%3Dcoastline</a></p>
<p>Also have a look how other islets in the area are tagged.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '20, 08:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-74924" class="comments-container">
&#10;</div>
<div id="comment-tools-74924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74924-form-container" class="comment-form-container">
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

