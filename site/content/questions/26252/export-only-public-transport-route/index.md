+++
type = "question"
title = "Export only public transport route"
description = '''Hi, I would like to export (or modify the exported file) such that I get only the transportation route. Any suggestions? Michele'''
date = "2013-09-10T13:42:00Z"
lastmod = "2013-09-12T16:53:00Z"
weight = 26252
keywords = [ "bus", "export", "transportation" ]
aliases = [ "/questions/26252" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export only public transport route](/questions/26252/export-only-public-transport-route)

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
<span id="post-26252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26252-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I would like to export (or modify the exported file) such that I get only the transportation route.</p>
<p>Any suggestions?</p>
<p>Michele</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-transportation" rel="tag" title="see questions tagged &#39;transportation&#39;">transportation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '13, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e4cbc52cb75352bd5d87c42e65f6952d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aliekor&#39;s gravatar image" />
<p><span>aliekor</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aliekor has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26252" class="comments-container">
&#10;</div>
<div id="comment-tools-26252" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26252-form-container" class="comment-form-container">
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

<span id="26268"></span>

<div id="answer-container-26268" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26268-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can query <a href="http://wiki.osm.org/wiki/Overpass_API">Overpass API</a> with a query like the following:</p>
<pre><code>(rel[network=VRS][ref=636];&gt;;);
out meta;</code></pre>
<p>It searches for the bus line 636 in the network VRS. Other tags can be used for selecting in the same way. For convenience the query as a link: <a href="http://overpass-turbo.eu/s/112">http://overpass-turbo.eu/s/112</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '13, 08:13</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-26268" class="comments-container">
<span id="26274"></span>
<div id="comment-26274" class="comment">
<div id="post-26274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, but how can i get the boundaries of the map I am exporting?</p>
</div>
<div id="comment-26274-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 09:27)</span> <span class="comment-user userinfo">aliekor</span>
</div>
</div>
<span id="26302"></span>
<div id="comment-26302" class="comment">
<div id="post-26302-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The boundaries are just the smallest/largest lat and lon values of the appearing nodes. So it is straightforward to determine them.</p>
</div>
<div id="comment-26302-info" class="comment-info">
<span class="comment-age">(12 Sep '13, 08:54)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="26310"></span>
<div id="comment-26310" class="comment">
<div id="post-26310-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@aliekor</span>: or do you want to limit the area by a bounding box where the query should be made from?</p>
<p>If yes, this is possible: Read <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a> very intensively ... there are many possibilities.</p>
</div>
<div id="comment-26310-info" class="comment-info">
<span class="comment-age">(12 Sep '13, 16:53)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-26268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26268-form-container" class="comment-form-container">
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

