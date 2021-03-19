+++
type = "question"
title = "How to log https headers"
description = '''When I visit websites that show yahoo ads, I see a header like this (via live http header). https://syndication.streamads.yahoo.com/na_stream_brewer/brew/v2?cid=ee289520-a939-3954-a2e6-5155cf227564&amp;amp;url=http%3A%2F%2Fwww.vox.com%2F2016%2F1%2F15%2F10774204%2Fwinners-losers-republican-debate-charles...'''
date = "2016-01-15T00:33:00Z"
lastmod = "2016-01-16T19:21:00Z"
weight = 49245
keywords = [ "filter", "http", "https", "display-filter" ]
aliases = [ "/questions/49245" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to log https headers](/questions/49245/how-to-log-https-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49245-score" class="post-score" title="current number of votes">0</div><span id="post-49245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I visit websites that show yahoo ads, I see a header like this (via live http header).</p><pre><code>https://syndication.streamads.yahoo.com/na_stream_brewer/brew/v2?cid=ee289520-a939-3954-a2e6-5155cf227564&amp;url=http%3A%2F%2Fwww.vox.com%2F2016%2F1%2F15%2F10774204%2Fwinners-losers-republican-debate-charleston-fox-business%2Fin%2F10531817&amp;v=b5896bc&amp;rid=addcceb1-d5c6-47ad-9203-3bd599a15a9a&amp;pvid=1d625dc0-62a6-4a05-a440-a0fd8b913b19&amp;mode=i&amp;fill=true&amp;tti=889&amp;tts=262&amp;canonical=http%3A%2F%2Fwww.vox.com%2F2016%2F1%2F15%2F10774204%2Fwinners-losers-republican-debate-charleston-fox-business&amp;secured=true&amp;callback=YADJSONPCallbacks.receiveCallback_1452838710074

GET /na_stream_brewer/brew/v2?cid=ee289520-a939-3954-a2e6-5155cf227564&amp;url=http%3A%2F%2Fwww.vox.com%2F2016%2F1%2F15%2F10774204%2Fwinners-losers-republican-debate-charleston-fox-business%2Fin%2F10531817&amp;v=b5896bc&amp;rid=addcceb1-d5c6-47ad-9203-3bd599a15a9a&amp;pvid=1d625dc0-62a6-4a05-a440-a0fd8b913b19&amp;mode=i&amp;fill=true&amp;tti=889&amp;tts=262&amp;canonical=http%3A%2F%2Fwww.vox.com%2F2016%2F1%2F15%2F10774204%2Fwinners-losers-republican-debate-charleston-fox-business&amp;secured=true&amp;callback=YADJSONPCallbacks.receiveCallback_1452838710074 HTTP/1.1
Host: syndication.streamads.yahoo.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://s.yimg.com/uq/syndication/yad-iframe.b5896bc.html
Cookie: B=1rg7cvhb9grj9&amp;b=3&amp;s=58
Connection: keep-alive</code></pre><p>I would like to capture the above header data via wireshark but I am unable to do that. Here are my settings.</p><ol><li>Capture filter none</li><li>Display filter - http contains "yahoo", http contains "syndication" etc.</li></ol><p>However, when I use any of these filters, I don't get any results. What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '16, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/2d3358e5b4a4507b418f0f015c5377bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hvs&#39;s gravatar image" /><p><span>hvs</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hvs has no accepted answers">0%</span></p></div></div><div id="comments-container-49245" class="comments-container"></div><div id="comment-tools-49245" class="comment-tools"></div><div class="clear"></div><div id="comment-49245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49248"></span>

<div id="answer-container-49248" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49248-score" class="post-score" title="current number of votes">1</div><span id="post-49248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While <code>http contains "text"</code> is a valid filter, I'm afraid you have to feed Wireshark with the information it needs to be able to decrypt the http<strong>s</strong>, in order to get to the plaintext http contents. You should find all what you need to do that <a href="https://wiki.wireshark.org/SSL">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '16, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49248" class="comments-container"><span id="49267"></span><div id="comment-49267" class="comment"><div id="post-49267-score" class="comment-score"></div><div class="comment-text"><p>But don't I need a private key for the SSL certificate for this? I don't currently have that. As you can see in my example that the server is making call to yahoo to show the advertisement. I don't have private key for the yahoo SSL certificate. Perhaps, my understanding is incorrect here.</p><p>All I want to do is capture the header that is visible in firefox via live http header plugin. I am assuming that browser is encrypting the header and when it is intercepted by wireshark, it is all encrypted. So how to decrypt without the private key?</p><p>Thanks.</p></div><div id="comment-49267-info" class="comment-info"><span class="comment-age">(16 Jan '16, 00:55)</span> <span class="comment-user userinfo">hvs</span></div></div><span id="49268"></span><div id="comment-49268" class="comment"><div id="post-49268-score" class="comment-score"></div><div class="comment-text"><p>The very idea of encryption is that a <em>third party</em> would be unable to see the contents of the communication. The complete http contents including headers is encrypted, not just the payload. Hence,</p><blockquote><p>All I want to do is capture the header</p></blockquote><p>requires use of the same tools as</p><blockquote><p>all I want to do is see the complete contents of the encrypted communication</p></blockquote><p>The plugin to firefox has access to the plaintext contents before the browser encrypts the request/after the browser decrypts the response.</p><p>When you capture the encrypted traffic, you effectively act as a third party, because this is what anyone along the path between the browser and the server can do. When you analyse traffic which you were involved to, either as the owner/administrator of the server or as the user of the browser, you possess a couple of bits of information which a real third party lacks: the keys.</p><ul><li><p>as a server administrator, you have access to the private key of the server</p></li><li><p>as an end user (or the administrator of end user's equipment), you have access to the keylog file of the browser, which contains the actual keys used to encrypt the traffic.</p></li></ul><p>If you are none of the two (i.e. you are really a third party with regard to the particular encrypted communication you are interested in), and you don't happen to work for NSA, it is time to give up.</p><p>If you want to see which of the web pages you've visited yourself (or someone else did using your PC): on the <a href="https://wiki.wireshark.org/SSL)">original link I gave</a>, you can find <a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">a link to a step-by-step procedure how to make your browser log the session keys and how to use the contents of this file by Wireshark to decrypt the captured https sessions</a>.</p></div><div id="comment-49268-info" class="comment-info"><span class="comment-age">(16 Jan '16, 01:58)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="49280"></span><div id="comment-49280" class="comment"><div id="post-49280-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks. I figured it out. I set the env variable SSLKEYLOG on my system and started collecting the keys in the text file which the variable was pointing to. After setting up the wireshark to read the file, I can see the decrypted headers.</p></div><div id="comment-49280-info" class="comment-info"><span class="comment-age">(16 Jan '16, 12:55)</span> <span class="comment-user userinfo">hvs</span></div></div><span id="49285"></span><div id="comment-49285" class="comment"><div id="post-49285-score" class="comment-score"></div><div class="comment-text"><p><span>@hvs</span>, you should have marked the answer of <span>@sindy</span> as accepted, not posting a comment as answer and accepting it. I revoked the checkmark, converted to a comment and checked the correct answer instead.</p></div><div id="comment-49285-info" class="comment-info"><span class="comment-age">(16 Jan '16, 19:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-49248" class="comment-tools"></div><div class="clear"></div><div id="comment-49248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

