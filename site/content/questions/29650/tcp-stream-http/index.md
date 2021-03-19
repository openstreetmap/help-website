+++
type = "question"
title = "TCP Stream HTTP"
description = '''In &quot;Follow TCP Stream&quot; for http what is the numeric identifier after the 1.1.1.1 as shown below. The destination port I am using is 9999 not 96. GET / HTTP/1.1 Host: 1.1.1.1:96 User-Agent: Mozilla/5.0 Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4 Accept: text/xml,appl...'''
date = "2014-02-10T12:47:00Z"
lastmod = "2014-02-11T01:47:00Z"
weight = 29650
keywords = [ "follow", "follow.tcp.stream", "tcp" ]
aliases = [ "/questions/29650" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Stream HTTP](/questions/29650/tcp-stream-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29650-score" class="post-score" title="current number of votes">0</div><span id="post-29650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In "Follow TCP Stream" for http what is the numeric identifier after the 1.1.1.1 as shown below. The destination port I am using is 9999 not 96.</p><pre><code>GET / HTTP/1.1
Host: 1.1.1.1:96
User-Agent: Mozilla/5.0 Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Language: en-us,en;q=0.5
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Connection: close</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/05f434a9a56c4e1c748a387193e789a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r24481&#39;s gravatar image" /><p><span>r24481</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r24481 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 00:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-29650" class="comments-container"></div><div id="comment-tools-29650" class="comment-tools"></div><div class="clear"></div><div id="comment-29650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29652"></span>

<div id="answer-container-29652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29652-score" class="post-score" title="current number of votes">0</div><span id="post-29652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In "Follow TCP Stream" for http what is the numeric identifier after the 1.1.1.1</p></blockquote><p>That's the port you entered in the URL, like <a href="http://1.1.1.1:9000/,">http://1.1.1.1:9000/,</a> at least it <strong>should</strong> be the port.</p><p>What is the port in the TCP header?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29652" class="comments-container"><span id="29653"></span><div id="comment-29653" class="comment"><div id="post-29653-score" class="comment-score"></div><div class="comment-text"><p>The URL I am using is <a href="http://1.1.1.1:9999">http://1.1.1.1:9999</a> and the trace shows I am using destination port 9999. I only see 96 when looking at the stream and it appears to remain as 96 on subsequent captures.</p></div><div id="comment-29653-info" class="comment-info"><span class="comment-age">(10 Feb '14, 13:25)</span> <span class="comment-user userinfo">r24481</span></div></div><span id="29654"></span><div id="comment-29654" class="comment"><div id="post-29654-score" class="comment-score"></div><div class="comment-text"><p>Can you please post a sample capture file somewhere (Google drive, dropbox, cloudshark.org)</p></div><div id="comment-29654-info" class="comment-info"><span class="comment-age">(10 Feb '14, 13:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29668"></span><div id="comment-29668" class="comment"><div id="post-29668-score" class="comment-score"></div><div class="comment-text"><p>BTW: is that a request of a real browser (old Firefox) or another tool (script) that uses that User-Agent: header?</p></div><div id="comment-29668-info" class="comment-info"><span class="comment-age">(11 Feb '14, 01:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29652" class="comment-tools"></div><div class="clear"></div><div id="comment-29652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29673"></span>

<div id="answer-container-29673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29673-score" class="post-score" title="current number of votes">0</div><span id="post-29673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The browser will split <code>http://1.1.1.1:9999</code> into:</p><pre><code>GET / HTTP/1.1
Host: 1.1.1.1:9999</code></pre><p>Where did you capture the traffic? On the client with the browser? At the server? Or somewhere in between?</p><p>Some devices might alter the headers on purpose, think of load-balancers, reverse-proxies, etc. Are there any such devices in your network between the client and the server? Move your capture point from client to server and see where the request has been altered (assuming it leaves the client with the header <code>Host: 1.1.1.1:9999</code>, otherwise it is a problem om the client itself).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-29673" class="comments-container"></div><div id="comment-tools-29673" class="comment-tools"></div><div class="clear"></div><div id="comment-29673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

