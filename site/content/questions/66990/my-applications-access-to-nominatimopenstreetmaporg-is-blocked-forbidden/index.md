+++
type = "question"
title = "My application&#x27;s access to nominatim.openstreetmap.org is blocked: forbidden"
description = '''My original goal is it, to get nominatim access from a windows application, where users can search for places etc. We are doing this since many years quite well with other providers (with google, bing, mapquest etc.) and i wanted to add nominatim as well. This is a c++ application on windows using b...'''
date = "2018-11-29T20:39:00Z"
lastmod = "2018-11-30T11:10:00Z"
weight = 66990
keywords = [ "osm.org", "http_403_forbidden", "nominatim", "blocked" ]
aliases = [ "/questions/66990" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [My application's access to nominatim.openstreetmap.org is blocked: forbidden](/questions/66990/my-applications-access-to-nominatimopenstreetmaporg-is-blocked-forbidden)

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
<span id="post-66990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66990-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My original goal is it, to get nominatim access from a windows application, where users can search for places etc. We are doing this since many years quite well with other providers (with google, bing, mapquest etc.) and i wanted to add nominatim as well. This is a c++ application on windows using boost::asio for https / https access. https works well for all other services.</p>
<p>If I, instead, use <a href="https://help.openstreetmap.org/questions/66940/wget-to-nominatim-url-unable-to-establish-ssl-connection">wget, I get a "Unable to establish SSL connection." error</a> (other question entry).</p>
<p>I did further inspections on access from my application. Indeed i get a "blocked" result:</p>
<pre><code>Retrieving &quot;nominatim.openstreetmap.org/search?q=,berlin,,&amp;format=xml&amp;polygon=1&amp;addressdetails=1&quot;
Connect HTTPS
HTTPS: Resolve OK
HTTPS: Connect OK
HTTPS: Verifying &quot;/C=US/O=Let&#39;s Encrypt/CN=Let&#39;s Encrypt Authority X3&quot;
HTTPS: Verifying &quot;/CN=nominatim.openstreetmap.org&quot;
HTTPS: Handshake OK; Request header: GET /search?q=,berlin,,&amp;format=xml&amp;polygon=1&amp;addressdetails=1 HTTP/1.0^M
Host: nominatim.openstreetmap.org^M
Accept: */*^M
Connection: close^M
^M
&#10;HTTPS response
 Forbidden^M
Date: Thu, 29 Nov 2018 20:36:11 GMT^M
Server: Apache/2.4.29 (Ubuntu)^M
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload^M
Expect-CT: max-age=0, report-uri=&quot;https://openstreetmap.report-uri.com/r/d/ct/reportOnly&quot;^M
Upgrade: h2^M
Connection: Upgrade, close^M
Last-Modified: Mon, 02 Jan 2017 21:56:07 GMT^M
ETag: &quot;3a5-545239e6fbc4c&quot;^M
Accept-Ranges: bytes^M
Content-Length: 933^M
Content-Type: text/html; charset=utf-8^M
^M
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Access blocked&lt;/title&gt;
&lt;/head&gt;</code></pre>
<p>Why is this the case? I did not attempt any bulk requests. In total maybe some 10. Do i need a additional header field to my request?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-http_403_forbidden" rel="tag" title="see questions tagged &#39;http_403_forbidden&#39;">http_403_forbidden</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '18, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7b22f0b3304066470193db063a024ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stefanwoe&#39;s gravatar image" />
<p><span>stefanwoe</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stefanwoe has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '18, 22:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66990" class="comments-container">
&#10;</div>
<div id="comment-tools-66990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66990-form-container" class="comment-form-container">
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

<span id="66996"></span>

<div id="answer-container-66996" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66996-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-66996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="stefanwoe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Only 10 requests feels a bit strange to me, too - however, probably others have used the same library to access nominatim before you and may be using the same identification. Let me cite <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> : "Provide a valid HTTP Referer or User-Agent identifying the application (stock User-Agents as set by http libraries will not do)." You should set a custom HTTP User Agent and Referer for your application. Maybe simply its website (which would offer a possible way of contacting you in case the service operators see any problem).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '18, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-66996" class="comments-container">
<span id="67001"></span>
<div id="comment-67001" class="comment">
<div id="post-67001-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I added a Referer and individual User-agent. Indeed the blocked result disappears. Working as expected! Thanks.</p>
</div>
<div id="comment-67001-info" class="comment-info">
<span class="comment-age">(30 Nov '18, 11:10)</span> <span class="comment-user userinfo">stefanwoe</span>
</div>
</div>
</div>
<div id="comment-tools-66996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66996-form-container" class="comment-form-container">
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

