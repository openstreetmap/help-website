+++
type = "question"
title = "Oauth request fails on the test server with &quot;Internal Server Error&quot;."
description = '''Hello! We receive &quot;500 Internal Server Error&quot; every time when sending requests to the test server using this URL:  http://api06.dev.openstreetmap.org/oauth/request_token and our Consumer Key and Consumer Secret. The requests are build via different libraries and Postman app. We also tested once agai...'''
date = "2016-12-05T09:09:00Z"
lastmod = "2017-03-22T15:41:00Z"
weight = 53243
keywords = [ "oauth" ]
aliases = [ "/questions/53243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Oauth request fails on the test server with "Internal Server Error".](/questions/53243/oauth-request-fails-on-the-test-server-with-internal-server-error)

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
<span id="post-53243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53243-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello! We receive "500 Internal Server Error" every time when sending requests to the test server using this URL: <a href="http://api06.dev.openstreetmap.org/oauth/request_token">http://api06.dev.openstreetmap.org/oauth/request_token</a> and our Consumer Key and Consumer Secret. The requests are build via different libraries and Postman app. We also tested once against the main server just to check if our Consumer Key and Consumer Secret are valid and we received a proper response with Token and Token Secret. Can you please give us a hint on what can be wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '16, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/bb46259512c7f1c54b1579632ff2b864?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tester4321&#39;s gravatar image" />
<p><span>tester4321</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tester4321 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53243" class="comments-container">
<span id="53244"></span>
<div id="comment-53244" class="comment">
<div id="post-53244-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to be clear - the api06 dev server and the live server use completely different sets of accounts. Can you login to the dev server from e.g. <a href="http://master.apis.dev.openstreetmap.org/">http://master.apis.dev.openstreetmap.org/</a> ?</p>
</div>
<div id="comment-53244-info" class="comment-info">
<span class="comment-age">(05 Dec '16, 09:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53243" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53243-form-container" class="comment-form-container">
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

<span id="55238"></span>

<div id="answer-container-55238" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I encountered similar problem and dug down to find out origin of the problem.</p>
<p>There may be two type of origins:</p>
<ol>
<li>Redirection. Protocol of dev server have been changed to HTTPS from HTTP. The DEV server returns 301 (Moved Permanently) response for HTTP request, but some framework doesn't handle it.</li>
<li>Certificate hostname mismatch. HTTPS connection does confirming identify of the target server as well as encrypting contents. Basic confirming procedure is done by comparing hostname with commonName field in the certificate. The DEV server utilizes virtual host. It means that the server's action will be different for each requested domain. For this scheme is working, it is needed to send domain name when you retrieve certificate. However, some old SSL library or languages doesn’t have such feature. The DEV server returns a certificate for ‘apis.openstreetmap.org’ when no domain specified and identifying procedure fails.</li>
</ol>
<p>Solution:</p>
<ol>
<li>Replace http:// to https://. Note that it will introduce the second problem.</li>
<li>If there is no change in server then you can do two things – 1) Upgrade your framework or language with latest version. 2) Disable identifying process (I checked some framework and languages, but they didn’t give this option. You may modify core library manually) However, I think that it would better to hand it over to OSM developers.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '17, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/13d95f413ff7e39e26a9e7af4d4c6dfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nrimbo&#39;s gravatar image" />
<p><span>nrimbo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nrimbo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '17, 15:59</strong> </span></p>
</div>
</div>
<div id="comments-container-55238" class="comments-container">
&#10;</div>
<div id="comment-tools-55238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55238-form-container" class="comment-form-container">
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

