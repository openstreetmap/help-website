+++
type = "question"
title = "Search amenities with Nominatim"
description = '''I am looking for a possibility to query for places like restaurants, pubs etc in the suroundings of a given address. Unfortunately I&#x27;m a bit confused about the Nominatim documentation: It is written that there are special keywords like pub or restaurant but I can not find how to actually use them.  ...'''
date = "2016-10-22T22:35:00Z"
lastmod = "2019-03-01T20:26:00Z"
weight = 52646
keywords = [ "query", "nominatim" ]
aliases = [ "/questions/52646" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Search amenities with Nominatim](/questions/52646/search-amenities-with-nominatim)

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
<span id="post-52646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52646-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a possibility to query for places like restaurants, pubs etc in the suroundings of a given address.</p>
<p>Unfortunately I'm a bit confused about the <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim documentation</a>: It is written that there are special keywords like pub or restaurant but I can not find how to actually use them.</p>
<p>Can you help me and give an example how to find all restaurant 1km within a given address?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '16, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/184999104034d85f3b6114f1dd685fa3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="acgjheeb&#39;s gravatar image" />
<p><span>acgjheeb</span><br />
<span class="score" title="101 reputation points">101</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="acgjheeb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52646" class="comments-container">
<span id="68211"></span>
<div id="comment-68211" class="comment">
<div id="post-68211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>May be overpass-turbo is more suitable for your task? See <a href="/questions/20616/how-to-find-a-nearest-toilet-in-openstreetmap/20633">https://help.openstreetmap.org/questions/20616/how-to-find-a-nearest-toilet-in-openstreetmap/20633</a></p>
</div>
<div id="comment-68211-info" class="comment-info">
<span class="comment-age">(01 Mar '19, 20:26)</span> <span class="comment-user userinfo">Mappist</span>
</div>
</div>
</div>
<div id="comment-tools-52646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52646-form-container" class="comment-form-container">
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

<span id="52664"></span>

<div id="answer-container-52664" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="acgjheeb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is an example query <a href="http://nominatim.openstreetmap.org/search.php?q=pubs+near+farm+road%2C+brighton&amp;format=jsonv2">http://nominatim.openstreetmap.org/search.php?q=pubs+near+farm+road%2C+brighton&amp;format=jsonv2</a> and <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN">https://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN</a> lists the special phrases which are possible. You can't specify a radius, but a bounding box (&amp;viewbox=...&amp;bounded=1) limits the results to a bounding box.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '16, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-52664" class="comments-container">
<span id="52833"></span>
<div id="comment-52833" class="comment">
<div id="post-52833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer! Now I understand how the operator is meant to be used.</p>
</div>
<div id="comment-52833-info" class="comment-info">
<span class="comment-age">(05 Nov '16, 15:43)</span> <span class="comment-user userinfo">acgjheeb</span>
</div>
</div>
</div>
<div id="comment-tools-52664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52664-form-container" class="comment-form-container">
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

