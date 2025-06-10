+++
type = "question"
title = "How to embed a map in my https site?"
description = '''How can I embed a map in a secure site (https) without getting &quot;not secure content loading&quot; warning?'''
date = "2012-03-01T19:23:00Z"
lastmod = "2014-05-25T17:45:00Z"
weight = 10920
keywords = [ "map", "embed", "secure", "https" ]
aliases = [ "/questions/10920" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to embed a map in my https site?](/questions/10920/how-to-embed-a-map-in-my-https-site)

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
<span id="post-10920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10920-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I embed a map in a secure site (https) without getting "not secure content loading" warning?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-secure" rel="tag" title="see questions tagged &#39;secure&#39;">secure</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Mar '12, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e0427810f89ae4b8cc5f4b5bdf44624d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SymphoX&#39;s gravatar image" />
<p><span>SymphoX</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SymphoX has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10920" class="comments-container">
&#10;</div>
<div id="comment-tools-10920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10920-form-container" class="comment-form-container">
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

<span id="10937"></span>

<div id="answer-container-10937" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10937-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The openstreetmap infrastructure is only providing ssl for sensetive data like passwords. Map tiles are not considered sensetive enough to justify ssl. Read more of the discussion <a href="http://trac.openstreetmap.org/ticket/3914">here</a>.</p>
<p>Remember that osm is not aimed at delivering service to mappers and not to the end users but rather relies on external organisations to provide the service for the end user. You may have an easier time convincing <a href="http://open.mapquest.co.uk/">MapQuest</a>, <a href="http://mapbox.com/">MapBox</a> or <a href="http://www.bing.com/maps/explore/#5003/s=w/5872/style=Mapnik&amp;pid=50735">Bing</a> to give you maps over ssl.</p>
<p>You could also run a proxy on your own server that translates your users' HTTPS requests to HTTP.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Mar '12, 01:43</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '12, 19:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-10937" class="comments-container">
&#10;</div>
<div id="comment-tools-10937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10937-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33463"></span>

<div id="answer-container-33463" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33463-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SSL is available on the a/b/c tile serving URLs since a couple of months.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '14, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/bf10a7dc3c157875e00bdedbd27b8cd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Miller&#39;s gravatar image" />
<p><span>Paul Miller</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Miller has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33463" class="comments-container">
&#10;</div>
<div id="comment-tools-33463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33463-form-container" class="comment-form-container">
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

