+++
type = "question"
title = "How to get stream URL"
description = '''Hello to all of you I have the same need of Mr. gfheiche has described in this question I&#x27;ve followed the instructions but this web radio www.deejay.it looks to use another streaming method, maybe they encrypt the streaming query? Can you kindly help with this? Thank you for any kind hint or help to...'''
date = "2015-12-22T00:02:00Z"
lastmod = "2016-01-09T12:29:00Z"
weight = 48668
keywords = [ "url", "stream" ]
aliases = [ "/questions/48668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get stream URL](/questions/48668/how-to-get-stream-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48668-score" class="post-score" title="current number of votes">0</div><span id="post-48668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello to all of you</p><p>I have the same need of Mr. gfheiche has described in <a href="https://ask.wireshark.org/questions/13425/streaming-url">this question</a></p><p>I've followed the instructions but this web radio www.deejay.it looks to use another streaming method, maybe they encrypt the streaming query?</p><p>Can you kindly help with this?</p><p>Thank you for any kind hint or help to find the stream address</p><p>Regards Cor</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '15, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/70e84fc36e2c706223bf8c3539bc245b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Corsari&#39;s gravatar image" /><p><span>Corsari</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Corsari has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Dec '15, 06:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-48668" class="comments-container"></div><div id="comment-tools-48668" class="comment-tools"></div><div class="clear"></div><div id="comment-48668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49027"></span>

<div id="answer-container-49027" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49027-score" class="post-score" title="current number of votes">0</div><span id="post-49027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I followed my own instructions and found this ;-)</p><pre><code>GET /crossdomain.xml HTTP/1.1
Host: radiodeejay-lh.akamaihd.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://video.repubblica.it/common/static/player/2014/flash/player/player_v1d_1j.swf
Connection: keep-alive

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 250
Date: Sat, 09 Jan 2016 20:21:22 GMT
Connection: keep-alive

&lt;cross-domain-policy&gt;&lt;allow-access-from domain=&quot;*&quot;/&gt;&lt;allow-http-request-headers-from domain=&quot;*&quot; headers=&quot;*&quot;/&gt;&lt;/cross-domain-policy&gt;GET /z/[email protected]/manifest.f4m?b=48-96&amp;hdcore=2.11.3&amp;g=EVLDGMFXEXII HTTP/1.1
Host: radiodeejay-lh.akamaihd.net
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://video.repubblica.it/common/static/player/2014/flash/player/player_v1d_1j.swf
Connection: keep-alive

etc.
etc.</code></pre><p>The important part seems to be this (down a few 'lines' in the TCP stream output).</p><pre><code>GET /z/[email protected]/96_2aa17ce68776b9da-p_Seg1-Frag242061810?b=48-96&amp;als=0,3,0,2,0,NaN,0,0,0,51,f,1209032,1209048.59,t,s,EVLDGMFXEXII,2.11.3,51&amp;hdcore=2.11.3 HTTP/1.1</code></pre><p>And yes, they are using a different streaming client pulling the content from the Akamai CDN, so I doubt there is a direct link you can use.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '16, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jan '16, 12:40</strong> </span></p></div></div><div id="comments-container-49027" class="comments-container"></div><div id="comment-tools-49027" class="comment-tools"></div><div class="clear"></div><div id="comment-49027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

