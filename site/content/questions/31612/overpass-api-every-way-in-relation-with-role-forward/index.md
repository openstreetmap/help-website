+++
type = "question"
title = "Overpass API : Every way in relation with role forward ?"
description = '''Is it possible with the Overpass API to get every way in a relation where their role is forward.  For example relation 2418275 returns multiple ways. I wanted to retrieve only the node coordinates for the tram line (and not the platforms) '''
date = "2014-03-16T22:55:00Z"
lastmod = "2014-03-17T09:23:00Z"
weight = 31612
keywords = [ "overpass" ]
aliases = [ "/questions/31612" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API : Every way in relation with role forward ?](/questions/31612/overpass-api-every-way-in-relation-with-role-forward)

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
<span id="post-31612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31612-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible with the Overpass API to get every way in a relation where their role is forward.</p>
<p>For example <a href="https://www.openstreetmap.org/relation/2418275">relation 2418275</a> returns multiple ways. I wanted to retrieve only the node coordinates for the tram line (and not the platforms)<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '14, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e48f202fc43dcc628a45c41463d25c20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyro&#39;s gravatar image" />
<p><span>Kyro</span><br />
<span class="score" title="121 reputation points">121</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyro has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '14, 22:55</strong> </span></p>
</div>
</div>
<div id="comments-container-31612" class="comments-container">
&#10;</div>
<div id="comment-tools-31612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31612-form-container" class="comment-form-container">
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

<span id="31622"></span>

<div id="answer-container-31622" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31622-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kyro has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, it is possible to select members of a relation by their respective role: <code>&lt;recurse type="relation-way" role="forward" /&gt;</code>.</p>
<p>Example: <a href="http://overpass-turbo.eu/s/2MU">http://overpass-turbo.eu/s/2MU</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '14, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/eca34689e074411e0daca0d994f532b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tyr_asd&#39;s gravatar image" />
<p><span>tyr_asd</span><br />
<span class="score" title="1196 reputation points"><span>1.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tyr_asd has 11 accepted answers">64%</span></p>
</div>
</div>
<div id="comments-container-31622" class="comments-container">
<span id="31624"></span>
<div id="comment-31624" class="comment">
<div id="post-31624-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Exactly what I was looking for, Thx !</p>
</div>
<div id="comment-31624-info" class="comment-info">
<span class="comment-age">(17 Mar '14, 09:23)</span> <span class="comment-user userinfo">Kyro</span>
</div>
</div>
</div>
<div id="comment-tools-31622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31622-form-container" class="comment-form-container">
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

