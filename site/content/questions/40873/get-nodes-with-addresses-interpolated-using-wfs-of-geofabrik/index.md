+++
type = "question"
title = "Get nodes with addresses interpolated using WFS of geofabrik"
description = '''Hi, I&#x27;m trying to get the list of nodes with this url: http://tools.geofabrik.de/osmi/view/addresses/wxs?SERVICE=WFS&amp;amp;VERSION=1.0.0&amp;amp;REQUEST=GetFeature&amp;amp;BBOX=-74.0135,45.3269,-73.2436,45.8393&amp;amp;TYPENAME=nodes_with_addresses_interpolated What i&#x27;m doing wrong?'''
date = "2015-02-09T03:46:00Z"
lastmod = "2015-02-09T19:25:00Z"
weight = 40873
keywords = [ "wfs", "interpolation" ]
aliases = [ "/questions/40873" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get nodes with addresses interpolated using WFS of geofabrik](/questions/40873/get-nodes-with-addresses-interpolated-using-wfs-of-geofabrik)

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
<span id="post-40873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40873-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to get the list of nodes with this url:</p>
<p><a href="http://tools.geofabrik.de/osmi/view/addresses/wxs?SERVICE=WFS&amp;VERSION=1.0.0&amp;REQUEST=GetFeature&amp;BBOX=-74.0135,45.3269,-73.2436,45.8393&amp;TYPENAME=nodes_with_addresses_interpolated">http://tools.geofabrik.de/osmi/view/addresses/wxs?SERVICE=WFS&amp;VERSION=1.0.0&amp;REQUEST=GetFeature&amp;BBOX=-74.0135,45.3269,-73.2436,45.8393&amp;TYPENAME=nodes_with_addresses_interpolated</a></p>
<p>What i'm doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wfs" rel="tag" title="see questions tagged &#39;wfs&#39;">wfs</span> <span class="post-tag tag-link-interpolation" rel="tag" title="see questions tagged &#39;interpolation&#39;">interpolation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '15, 03:46</strong></p>
<img src="https://secure.gravatar.com/avatar/e649c64bb5987efee0342b7f99487742?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JFDionne&#39;s gravatar image" />
<p><span>JFDionne</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JFDionne has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40873" class="comments-container">
&#10;</div>
<div id="comment-tools-40873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40873-form-container" class="comment-form-container">
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

<span id="40879"></span>

<div id="answer-container-40879" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40879-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-40879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Request seems syntactically ok and works with smaller bounding boxes, just not with this one. Tracing the MapServer on the backend shows that there seems to be some mutex lockup in the MapServer - some kind of bug but I can't see why exactly. Will have to debug further. For the time being, try requesting a smaller box several times.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '15, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40879" class="comments-container">
<span id="40894"></span>
<div id="comment-40894" class="comment">
<div id="post-40894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seem to work, thank but, maybe i'm not using it correctly, I don't want to "slow down the server", I'm trying to get a list of all street with housenumber (with the interpolation) of a Region. It is the right way to do it?</p>
</div>
<div id="comment-40894-info" class="comment-info">
<span class="comment-age">(09 Feb '15, 19:25)</span> <span class="comment-user userinfo">JFDionne</span>
</div>
</div>
</div>
<div id="comment-tools-40879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40879-form-container" class="comment-form-container">
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

