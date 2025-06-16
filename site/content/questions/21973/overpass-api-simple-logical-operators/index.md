+++
type = "question"
title = "Overpass API / simple logical operators"
description = '''The question https://help.openstreetmap.org/questions/21941/can-not-find-rdby-putgarden-denmark-ferry-route-with-navigator-from-mapfactor gave me the idea to query the DB for all nodes that are tagged barrier=... and do not have an access tag, so I can specifically check those in my area. (How) can ...'''
date = "2013-04-29T14:43:00Z"
lastmod = "2013-04-29T15:47:00Z"
weight = 21973
keywords = [ "overpass" ]
aliases = [ "/questions/21973" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass API / simple logical operators](/questions/21973/overpass-api-simple-logical-operators)

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
<span id="post-21973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21973-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The question <a href="/questions/21941/can-not-find-rdby-putgarden-denmark-ferry-route-with-navigator-from-mapfactor">https://help.openstreetmap.org/questions/21941/can-not-find-rdby-putgarden-denmark-ferry-route-with-navigator-from-mapfactor</a> gave me the idea to query the DB for all nodes that are tagged barrier=... and do not have an access tag, so I can specifically check those in my area.</p>
<p>(How) can this be done in OverpassQL? Does OverpassQL or some other API have support for "not"-style operators? I couldn't find documentation stating this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '13, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '13, 14:44</strong> </span></p>
</div>
</div>
<div id="comments-container-21973" class="comments-container">
&#10;</div>
<div id="comment-tools-21973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21973-form-container" class="comment-form-container">
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

<span id="21975"></span>

<div id="answer-container-21975" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21975-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-21975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gormo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like there's ["key"!="value"], or ["key"!~"value"] if you want to use regular expressions.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Negation">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Negation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '13, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-21975" class="comments-container">
<span id="21976"></span>
<div id="comment-21976" class="comment">
<div id="post-21976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Great, thanks!</p>
<p>Shame on my google fu...</p>
</div>
<div id="comment-21976-info" class="comment-info">
<span class="comment-age">(29 Apr '13, 15:47)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-21975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21975-form-container" class="comment-form-container">
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

