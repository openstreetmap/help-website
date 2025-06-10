+++
type = "question"
title = "error nomination geocode with wget"
description = '''Hi, i&#x27;m try to use the reverse geocode provider: http://nominatim.openstreetmap.org/reverse?lat=-0.24136&amp;amp;lon=-80.48281 i can do that with my browser, but when i make the same request from my server (opengts server) i receive an error. I think the error is because the web server detect this is no...'''
date = "2015-09-15T22:37:00Z"
lastmod = "2015-09-17T06:07:00Z"
weight = 45261
keywords = [ "nominatim", "wget", "reversegeocoding", "error" ]
aliases = [ "/questions/45261" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error nomination geocode with wget](/questions/45261/error-nomination-geocode-with-wget)

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
<span id="post-45261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45261-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i'm try to use the reverse geocode provider: <a href="http://nominatim.openstreetmap.org/reverse?lat=-0.24136&amp;lon=-80.48281">http://nominatim.openstreetmap.org/reverse?lat=-0.24136&amp;lon=-80.48281</a></p>
<p>i can do that with my browser, but when i make the same request from my server (opengts server) i receive an error. I think the error is because the web server detect this is not a browser and refused connection.</p>
<p>how can i use this web services with my server? please your help</p>
<p>++++</p>
<pre><code> this is the error message sending with terminal:
&#10; [root@gps]# wget http://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281
 [1] 16844
 [2] 16845
 [3] 16846
 [4] 16847
 [5] 16848
 [6] 16849
 [2]   Done                    limit=1
 [3]   Done                    addressdetails=1
 [4]   Done                    zoom=18
 [5]-  Done                    email=
 [root@bitacoragps bitacoragps]# --2015-09-15 23:35:14--  http://nominatim.openstreetmap.org/reverse?format=xml
 Resolving nominatim.openstreetmap.org... 128.40.45.204
 Connecting to nominatim.openstreetmap.org|128.40.45.204|:80... failed: Connection refused.</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-wget" rel="tag" title="see questions tagged &#39;wget&#39;">wget</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '15, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a64c09f76fb862e5d6ba7f2eb71bb2f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HugoAlejo&#39;s gravatar image" />
<p><span>HugoAlejo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HugoAlejo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '15, 06:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45261" class="comments-container">
<span id="45317"></span>
<div id="comment-45317" class="comment">
<div id="post-45317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Scai has found the issue here, but this is still relevant in general: Chances are quite good, that you are guessing right (maybe due to a missing identification of your client). Please check and obey the services usage policy which you are using. In this case: <span>Nominatim.openstreetmap.org/Usage_policy</span>. This is important because we are just a project living on donations which cannot handle every load. :-)</p>
<p>If you just send some requests the default user agent identification may be tolerable, but please change it if those are many requests (I do not know your server software). I think it should be something like this (nominatim's email parameter filled in (and/or a new user agent): <code>wget "http://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=HugoA@example.com&amp;lat=-0.24136&amp;lon=98.48281" --user-agent=HugoAOpenGTS</code></p>
<p>Note, that I am no server admin, but setting a good user agent and ensuring to not do too many requests per time frame would be a first try.</p>
</div>
<div id="comment-45317-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 06:07)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45261" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45261-form-container" class="comment-form-container">
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

<span id="45269"></span>

<div id="answer-container-45269" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45269-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to quote the URL because it contains special characters such as <code>&amp;</code>. Try this instead:</p>
<blockquote>
<p>wget "http://nominatim.openstreetmap.org/reverse?format=xml&amp;limit=1&amp;addressdetails=1&amp;zoom=18&amp;email=&amp;lat=-0.24136&amp;lon=98.48281"</p>
</blockquote>
<p>Some background information: As you can see in your output, wget actually only tries to open <a href="http://nominatim.openstreetmap.org/reverse?format=xml"><code>http://nominatim.openstreetmap.org/reverse?format=xml</code></a> (everything before the first <code>&amp;</code>) due to the fact that your shell interprets <code>&amp;</code> in a special way. It assumes the program and all of its arguments end at right before the <code>&amp;</code> and puts it into the background (that's what the <code>&amp;</code> is for). That's why you are seeing the <em>[1] 16844</em>, <em>[2] 16845</em> and so on which are the PIDs of the programs put into the background. And this URL wget is trying to retrieve won't ever give you an useful response.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '15, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Sep '15, 08:41</strong> </span></p>
</div>
</div>
<div id="comments-container-45269" class="comments-container">
<span id="45316"></span>
<div id="comment-45316" class="comment">
<div id="post-45316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>oh, yes, indeed! thanks, I missed that.</p>
</div>
<div id="comment-45316-info" class="comment-info">
<span class="comment-age">(17 Sep '15, 06:01)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45269-form-container" class="comment-form-container">
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

