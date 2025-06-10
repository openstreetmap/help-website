+++
type = "question"
title = "Overpass turbo: request rejected"
description = '''Using overpass turbp, I often - but quite irregularly - receive this error message:  It says that the request is rejected due to &quot;e.g. server not found, request blocked by browser addon, request redirected, internal server errors, etc.&quot; I checked browser settings, the query itself, ran it on differe...'''
date = "2021-09-13T16:52:00Z"
lastmod = "2021-09-30T13:27:00Z"
weight = 81727
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/81727" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo: request rejected](/questions/81727/overpass-turbo-request-rejected)

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
<span id="post-81727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81727-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using overpass turbp, I often - but quite irregularly - receive this <strong>error</strong> message:</p>
<p><img src="https://help.openstreetmap.org/upfiles/err.jpg" alt="alt text" /></p>
<p>It says that the request is <strong>rejected</strong> due to "e.g. server not found, request blocked by browser addon, request redirected, internal server errors, etc." I checked browser settings, the query itself, ran it on different devices, checked the status of Overpass etc. Sometimes, it affects even the smallest queries, e.g. the default one when loading overpass turbo.</p>
<p>Here, some more information, there seems to be issues with both XML and Java. The messages are from the browser's <strong>debugging</strong> tool (F12):</p>
<p><img src="https://help.openstreetmap.org/upfiles/err2.jpg" alt="alt text" /></p>
<p>Has someone experienced the same problem (No 'Access-Control-Allow-Origin' header present, Cannot read property 'getBaseLayer')? How did you solve it? It seems always to be related to <em>turbo.4decdd916893e57ee8ff.js</em>. <strong>Thanks for all hints!</strong></p>
<p>Below, all details of the debugging messages in text format:</p>
<pre><code>Access to XMLHttpRequest at &#39;https://overpass.openstreetmap.fr/api/interpreterinterpreter&#39; from origin &#39;https://overpass-turbo.eu&#39; has been blocked by CORS policy: No &#39;Access-Control-Allow-Origin&#39; header is present on the requested resource.
turbo.4decdd916893e57ee8ff.js:66 Uncaught TypeError: Cannot read property &#39;getBaseLayer&#39; of undefined
    at Object.j.a.handlers.onDone (turbo.4decdd916893e57ee8ff.js:66)
    at e (turbo.4decdd916893e57ee8ff.js:40)
    at Object.error (turbo.4decdd916893e57ee8ff.js:40)
    at u (turbo.4decdd916893e57ee8ff.js:24)
    at Object.fireWith [as rejectWith] (turbo.4decdd916893e57ee8ff.js:24)
    at i (turbo.4decdd916893e57ee8ff.js:24)
    at XMLHttpRequest.&lt;anonymous&gt; (turbo.4decdd916893e57ee8ff.js:24)
j.a.handlers.onDone @ turbo.4decdd916893e57ee8ff.js:66
e @ turbo.4decdd916893e57ee8ff.js:40
error @ turbo.4decdd916893e57ee8ff.js:40
u @ turbo.4decdd916893e57ee8ff.js:24
fireWith @ turbo.4decdd916893e57ee8ff.js:24
i @ turbo.4decdd916893e57ee8ff.js:24
(anonymous) @ turbo.4decdd916893e57ee8ff.js:24
error (async)
send @ turbo.4decdd916893e57ee8ff.js:24
ajax @ turbo.4decdd916893e57ee8ff.js:24
run_query @ turbo.4decdd916893e57ee8ff.js:40
(anonymous) @ turbo.4decdd916893e57ee8ff.js:66
(anonymous) @ turbo.4decdd916893e57ee8ff.js:66
e.parse @ turbo.4decdd916893e57ee8ff.js:58
(anonymous) @ turbo.4decdd916893e57ee8ff.js:58
(anonymous) @ turbo.4decdd916893e57ee8ff.js:82
(anonymous) @ turbo.4decdd916893e57ee8ff.js:66
success @ turbo.4decdd916893e57ee8ff.js:66
u @ turbo.4decdd916893e57ee8ff.js:24
fireWith @ turbo.4decdd916893e57ee8ff.js:24
i @ turbo.4decdd916893e57ee8ff.js:24
(anonymous) @ turbo.4decdd916893e57ee8ff.js:24
load (async)
send @ turbo.4decdd916893e57ee8ff.js:24
ajax @ turbo.4decdd916893e57ee8ff.js:24
t @ turbo.4decdd916893e57ee8ff.js:66
e.get @ turbo.4decdd916893e57ee8ff.js:66
e.getBest @ turbo.4decdd916893e57ee8ff.js:66
s @ turbo.4decdd916893e57ee8ff.js:82
e.parse @ turbo.4decdd916893e57ee8ff.js:58
getQuery @ turbo.4decdd916893e57ee8ff.js:66
update_map @ turbo.4decdd916893e57ee8ff.js:66
onRunClick @ turbo.4decdd916893e57ee8ff.js:66
dispatch @ turbo.4decdd916893e57ee8ff.js:24
_.handle @ turbo.4decdd916893e57ee8ff.js:24
turbo.4decdd916893e57ee8ff.js:24 POST https://overpass.openstreetmap.fr/api/interpreterinterpreter net::ERR_FAILED</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '21, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '21, 13:51</strong> </span></p>
</div>
</div>
<div id="comments-container-81727" class="comments-container">
&#10;</div>
<div id="comment-tools-81727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81727-form-container" class="comment-form-container">
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

<span id="82004"></span>

<div id="answer-container-82004" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82004-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scai has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks to <em>mmd-osm</em>, it works fine now! As explained on <a href="https://github.com/osm-fr/infrastructure/issues/324">https://github.com/osm-fr/infrastructure/issues/324</a>, the main problem was that I had <strong>multiple data sources</strong> in the code including two incorrect ones and one that is running on an older release. Instead of:</p>
<pre><code>// Alternative API
//{{data:overpass,server=https://overpass.kumi.systems/api/}}
//{{data:overpass,server=https://overpass-api.de/api/interpreter}}
//{{data:overpass,server=https://overpass.openstreetmap.fr/api/interpreter}}</code></pre>
<p>it should have been:</p>
<pre><code>// Alternative API
//{{data:overpass,server=https://overpass.kumi.systems/api/}}
//{{data:overpass,server=https://overpass-api.de/api/}}</code></pre>
<p>Even though all these lines were commented out, overpass turbo still works with them and that caused problems. Might be better to use the settings menu of overpass turbo instead and not to add them in the code at all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '21, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '21, 09:45</strong> </span></p>
</div>
</div>
<div id="comments-container-82004" class="comments-container">
<span id="82005"></span>
<div id="comment-82005" class="comment">
<div id="post-82005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This answer describes what solved my problem. Unfortunately, I cannot mark it as "accepted answer"; could one of the admins please do so, thanks! I hope that marking this question as "answered" can help others that have the same problem and spare those that want to help solving a problem to put more time on this one. Thanks!</p>
</div>
<div id="comment-82005-info" class="comment-info">
<span class="comment-age">(30 Sep '21, 12:38)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="82010"></span>
<div id="comment-82010" class="comment">
<div id="post-82010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have marked it as accepted.</p>
</div>
<div id="comment-82010-info" class="comment-info">
<span class="comment-age">(30 Sep '21, 13:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82004-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81779"></span>

<div id="answer-container-81779" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The request is made on <a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> which seems to contact <a href="https://overpass.openstreetmap.fr">https://overpass.openstreetmap.fr</a> for executing the query. As both servers belong to a different domain, the CORS policy has to allow this. This means that the server on openstreetmap.fr has to allow requests from servers from another domain. Such a CORS policy is typically in place to avoid front-ends with bad intentions from using a back-end server.</p>
<p>In case this does not work, it is a server configuration error. There is nothing you can do as a user of the system. Of course, you can contact the maintainers of that server to inform them about the problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '21, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-81779" class="comments-container">
<span id="81787"></span>
<div id="comment-81787" class="comment">
<div id="post-81787-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer <a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a>! I am wondering whether and how one can specify the server which overpass turbo is contacting. I tried {{data:overpass,server=}} with each of the following: <a href="https://overpass.kumi.systems/api/,">https://overpass.kumi.systems/api/,</a> <a href="https://overpass-api.de/api/interpreter,">https://overpass-api.de/api/interpreter,</a> <a href="https://overpass.openstreetmap.fr/api/interpreter">https://overpass.openstreetmap.fr/api/interpreter</a> which I found on <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances,">https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances,</a> but the query always ends up with <a href="https://overpass.openstreetmap.fr/.">https://overpass.openstreetmap.fr/.</a> Funny thing is that the same query on another laptop gets processed by another server and there it works.</p>
</div>
<div id="comment-81787-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 07:39)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
<span id="81788"></span>
<div id="comment-81788" class="comment">
<div id="post-81788-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also added the question on the issue reporting page of the French OSM team: overpass.openstreetmap.fr <a href="https://github.com/osm-fr/infrastructure/issues/324#issue-998580758.">https://github.com/osm-fr/infrastructure/issues/324#issue-998580758.</a></p>
</div>
<div id="comment-81788-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 07:46)</span> <span class="comment-user userinfo">Gåseborg</span>
</div>
</div>
</div>
<div id="comment-tools-81779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81779-form-container" class="comment-form-container">
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

