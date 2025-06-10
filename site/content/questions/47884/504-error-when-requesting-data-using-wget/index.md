+++
type = "question"
title = "504 error when requesting data using wget"
description = '''I am using wget to request data on the national borders of a few countries in Western Europe from the Overpass API. I use the following request: wget &quot;http://overpass-api.de/api/interpreter?data=[out:xml][timeout:3600];(relation(45.0,-6.0,56.0,15.5)[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;2&quot;];no...'''
date = "2016-02-03T22:12:00Z"
lastmod = "2016-02-04T18:58:00Z"
weight = 47884
keywords = [ "overpass", "wget" ]
aliases = [ "/questions/47884" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [504 error when requesting data using wget](/questions/47884/504-error-when-requesting-data-using-wget)

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
<span id="post-47884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47884-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using wget to request data on the national borders of a few countries in Western Europe from the Overpass API. I use the following request:</p>
<pre><code>wget &quot;http://overpass-api.de/api/interpreter?data=[out:xml][timeout:3600];(relation(45.0,-6.0,56.0,15.5)[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;2&quot;];node(r)-&gt;.admincentre;way(r);node(w););out;&quot; -O res.osm</code></pre>
<p>However, each time I get the following error response after a couple of minutes (the first part is in Dutch ;) ):</p>
<pre><code>HTTP-verzoek is verzonden; wachten op antwoord... 504 Gateway Timeout</code></pre>
<p>Is there any way to resolve this error? I set the timeout to 3600 seconds, but it seems to be ignored. Is that on purpose and is my request too large? If this is the case, are there other options to request my data when sticking to the Overpass API?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-wget" rel="tag" title="see questions tagged &#39;wget&#39;">wget</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '16, 22:12</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '16, 22:17</strong> </span></p>
</div>
</div>
<div id="comments-container-47884" class="comments-container">
<span id="47905"></span>
<div id="comment-47905" class="comment">
<div id="post-47905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you try one of the other <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">Overpass API instances</a>?</p>
</div>
<div id="comment-47905-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 11:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47919"></span>
<div id="comment-47919" class="comment">
<div id="post-47919-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You may try to get your data country by country and later stitch the results with osmconvert or something else depending what you do with the data. You can use capitals to run your query on.</p>
<p>Reasonability: Some borders are fairly complex. For example Italy (7,600 km border length) is ~10MB due to mostly having marine border and simple land border but a small luxembourg (359 km border length) is already ~3MB. Germany sits on 30MB of data.</p>
</div>
<div id="comment-47919-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 18:13)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="47922"></span>
<div id="comment-47922" class="comment">
<div id="post-47922-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>scai: I tried other overpass instances, but they yield the same error response. RM87: Ah, that's a nice approach. It works!</p>
</div>
<div id="comment-47922-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 18:51)</span> <span class="comment-user userinfo">Steijn</span>
</div>
</div>
</div>
<div id="comment-tools-47884" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47884-form-container" class="comment-form-container">
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

<span id="47923"></span>

<div id="answer-container-47923" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47923-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Overpass website gives the following information:</p>
<p><em>504 Gateway Timeout is sent if the server has already so much load that the request cannot be executed. In most cases, it is best to try again later. Please note that the server decides this based on the timeout and maxsize parameters of the request, so smaller values for them may also make the request acceptable.</em></p>
<p>So to me the problem seems to be related to the complexity of my request and the amount of requests made to the server at that moment. Cutting the requests in parts, as RM87 suggested earlier, indeed solves the problem.</p>
<p>However, is it possible to show some kind of traffic diagram of the Overpass instances? That way I can do my requests, I have several of them and also more complex, in the more quiet hours. :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '16, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47923" class="comments-container">
&#10;</div>
<div id="comment-tools-47923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47888"></span>

<div id="answer-container-47888" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47888-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>wget</code> has its own timeout. Try to specify the same timeout via <code>--read-timeout=3600</code>. The default read timeout is 900 seconds according to my manpage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Feb '16, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47888" class="comments-container">
<span id="47890"></span>
<div id="comment-47890" class="comment">
<div id="post-47890-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>hmm, I think the 504 is sent from the server because an upstream server (possibly the overpass interpreter) has not answered yet. See <a href="https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error">http error codes</a>. So, wget's own timeout should not have mattered - yet.</p>
</div>
<div id="comment-47890-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 09:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="47904"></span>
<div id="comment-47904" class="comment">
<div id="post-47904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are probably right. If a read timeout occurs then wget prints a different error message.</p>
</div>
<div id="comment-47904-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 11:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47921"></span>
<div id="comment-47921" class="comment">
<div id="post-47921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I added the timeout flag of wget to my request. However it doesn't seem to solve my problem. Thanks anyway. :)</p>
</div>
<div id="comment-47921-info" class="comment-info">
<span class="comment-age">(04 Feb '16, 18:49)</span> <span class="comment-user userinfo">Steijn</span>
</div>
</div>
</div>
<div id="comment-tools-47888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47888-form-container" class="comment-form-container">
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

