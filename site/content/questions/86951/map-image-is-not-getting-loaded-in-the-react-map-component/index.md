+++
type = "question"
title = "Map image is not getting loaded in the react map component"
description = '''Map image is failing to load in the react application when requests are made to the URLs https://b.tile.openstreetmap.de/2/0/1.png https://c.tile.openstreetmap.de/2/1/1.png https://a.tile.openstreetmap.de/2/2/1.png https://b.tile.openstreetmap.de/2/3/1.png And response message says Failed to load re...'''
date = "2023-03-20T07:52:00Z"
lastmod = "2023-03-20T13:50:00Z"
weight = 86951
keywords = [ "error" ]
aliases = [ "/questions/86951" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map image is not getting loaded in the react map component](/questions/86951/map-image-is-not-getting-loaded-in-the-react-map-component)

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
<span id="post-86951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86951-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Map image is failing to load in the react application when requests are made to the URLs <a href="https://b.tile.openstreetmap.de/2/0/1.png">https://b.tile.openstreetmap.de/2/0/1.png</a> <a href="https://c.tile.openstreetmap.de/2/1/1.png">https://c.tile.openstreetmap.de/2/1/1.png</a> <a href="https://a.tile.openstreetmap.de/2/2/1.png">https://a.tile.openstreetmap.de/2/2/1.png</a> <a href="https://b.tile.openstreetmap.de/2/3/1.png">https://b.tile.openstreetmap.de/2/3/1.png</a> And response message says Failed to load response data: No data found for resource with given identifier</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '23, 07:52</strong></p>
<img src="https://secure.gravatar.com/avatar/2533f4cf9b14a12161dc7ab9d6129808?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sheetal%20Karnawadi&#39;s gravatar image" />
<p><span>Sheetal Karn...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sheetal Karnawadi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86951" class="comments-container">
<span id="86954"></span>
<div id="comment-86954" class="comment">
<div id="post-86954-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same problem from 3 day almost. Italy here. Thanks Who can help me. Silvano</p>
</div>
<div id="comment-86954-info" class="comment-info">
<span class="comment-age">(20 Mar '23, 12:49)</span> <span class="comment-user userinfo">SILVANO</span>
</div>
</div>
</div>
<div id="comment-tools-86951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86951-form-container" class="comment-form-container">
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

<span id="86955"></span>

<div id="answer-container-86955" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86955-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Failed to load response data: No data found for resource with given identifier</p>
</blockquote>
<p>Do you get an actual error number back (404, 418, something else) or does it just time out? If it just times out my guess is that it's a proxy issue - your web browser (where you can presumably access <a href="https://c.tile.openstreetmap.de/2/1/1.png">https://c.tile.openstreetmap.de/2/1/1.png</a> etc.) has a proxy configured, but wherever you are running your application (in terms of both hardware and software) is not seeing that.</p>
<p>It's tangential to your issue, but you are encouraged to remove "c" etc. now and just use e.g. <a href="https://tile.openstreetmap.de/2/1/1.png">https://tile.openstreetmap.de/2/1/1.png</a> now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Mar '23, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-86955" class="comments-container">
&#10;</div>
<div id="comment-tools-86955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86955-form-container" class="comment-form-container">
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

