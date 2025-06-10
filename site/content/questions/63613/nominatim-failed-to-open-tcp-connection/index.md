+++
type = "question"
title = "Nominatim. Failed to open TCP connection."
description = '''On 17 of May 2018 we faced with error “Errno::ENETUNREACH: Failed to open TCP connection to nominatim.openstreetmap.org:80 (Network is unreachable - connect(2) for &quot;nominatim.openstreetmap.org&quot; port 80)” on our server. On the another server we didn’t have this error with the same request. Also we ha...'''
date = "2018-05-22T13:27:00Z"
lastmod = "2018-05-22T20:37:00Z"
weight = 63613
keywords = [ "nominatim" ]
aliases = [ "/questions/63613" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim. Failed to open TCP connection.](/questions/63613/nominatim-failed-to-open-tcp-connection)

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
<span id="post-63613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On 17 of May 2018 we faced with error “Errno::ENETUNREACH: Failed to open TCP connection to nominatim.openstreetmap.org:80 (Network is unreachable - connect(2) for "nominatim.openstreetmap.org" port 80)” on our server. On the another server we didn’t have this error with the same request.</p>
<p>Also we had received next responses before error: “</p>
<address>
Apache/2.4.18 (Ubuntu) Server at nominatim.openstreetmap.org Port 80
</address>
&lt;/body&gt;&lt;/html&gt; Geocoding API's response was not valid JSON: &lt;!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"&gt; &lt;html&gt;&lt;head&gt; &lt;title&gt;301 Moved Permanently&lt;/title&gt; &lt;/head&gt;&lt;body&gt;
<h1 id="moved-permanently">Moved Permanently</h1>
<p>The document has moved</p>
<hr />
”
<p>Now service works fine. Could you please tell us why we had this error? Were we blocked on osm by IP?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '18, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e3d5afdddb8fb27b76d817cbf7bfda04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vitalyvi&#39;s gravatar image" />
<p><span>vitalyvi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vitalyvi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63613" class="comments-container">
&#10;</div>
<div id="comment-tools-63613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63613-form-container" class="comment-form-container">
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

<span id="63617"></span>

<div id="answer-container-63617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63617-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just tried visiting <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a> and it redirected to https, and the example links on the nominatim wiki page were updated from http to https in January, so it might be you need to update your calls to use https</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '18, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-63617" class="comments-container">
<span id="63624"></span>
<div id="comment-63624" class="comment">
<div id="post-63624-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's correct. Starting May/11th the nominatim.osm.org server(s) redirect http to https.</p>
</div>
<div id="comment-63624-info" class="comment-info">
<span class="comment-age">(22 May '18, 20:37)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-63617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63617-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

