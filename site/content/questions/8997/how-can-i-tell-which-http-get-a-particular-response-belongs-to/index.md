+++
type = "question"
title = "How can I tell which HTTP GET a particular response belongs to?"
description = '''I would like to know which HTTP GET relates to which response. Is there somewhere in the TCP packet that references the GET and is included in the response? For example, if there are five GET requests and only one response, is there a way to determine what GET it corresponds to?'''
date = "2012-02-14T10:21:00Z"
lastmod = "2012-02-15T11:20:00Z"
weight = 8997
keywords = [ "http" ]
aliases = [ "/questions/8997" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How can I tell which HTTP GET a particular response belongs to?](/questions/8997/how-can-i-tell-which-http-get-a-particular-response-belongs-to)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8997-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know which HTTP GET relates to which response. Is there somewhere in the TCP packet that references the GET and is included in the response? For example, if there are five GET requests and only one response, is there a way to determine what GET it corresponds to?</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '12, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/742ef72410cbfe5b1faa604d3a1bc44d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ezat&#39;s gravatar image" /><p>Ezat<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ezat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '12, 10:47</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8997" class="comments-container"></div><div id="comment-tools-8997" class="comment-tools"></div><div class="clear"></div><div id="comment-8997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8998"></span>

<div id="answer-container-8998" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8998-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Without HTTP pipelining, there will be only one request at a time in each TCP session, so when you look in one TCP session (same IP addresses/TCP ports combination), each response will be for the request before it.</p><p>When HTTP pipelining is used (not used much), there can be multiple requests following each other in one TCP session. The responses then correspond chronologically to the requests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '12, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-8998" class="comments-container"><span id="8999"></span><div id="comment-8999" class="comment"><div id="post-8999-score" class="comment-score"></div><div class="comment-text"><p>Very much appreciated Sake, so if I understood the order is sequential and I don't have to worry about which Response belong to which GET just following the stream downhill, do you think there is a way to see the speed of webpage loading other than using Firebug just by adding all the packets time.</p></div><div id="comment-8999-info" class="comment-info"><span class="comment-age">(14 Feb '12, 11:24)</span> Ezat</div></div></div><div id="comment-tools-8998" class="comment-tools"></div><div class="clear"></div><div id="comment-8998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9002"></span>

<div id="answer-container-9002" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9002-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To find the time taken to load a webpage, you can take the difference of first request packet and last response for that <code>HOST</code></p><pre><code>BEGIN_TIME = packet.getCaptureHeader().timestampInMillis(); for first request (source:jNetPcap library)
FINISH_TIME = packet.getCaptureHeader().timestampInMillis(); for last response packet</code></pre><p>time to load the webpage = <code>FINSIH_TIME - BEGIN_TIME</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '12, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/84da5ede7d868490afe7e099e42aeed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rhiya&#39;s gravatar image" /><p>Rhiya<br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rhiya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '12, 12:00</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-9002" class="comments-container"><span id="9005"></span><div id="comment-9005" class="comment"><div id="post-9005-score" class="comment-score"></div><div class="comment-text"><p>is this a filter, looks like methods in programmming, sorry I don't script @ the moment, where do I plugg these lines in filters.</p></div><div id="comment-9005-info" class="comment-info"><span class="comment-age">(14 Feb '12, 12:25)</span> Ezat</div></div></div><div id="comment-tools-9002" class="comment-tools"></div><div class="clear"></div><div id="comment-9002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9044"></span>

<div id="answer-container-9044" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9044-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Highlight the GET request and select analyze; Follow TCP Stream. That should help</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/b119c1795a1d51f2d7d0aa7af9c54a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dixglata&#39;s gravatar image" /><p>dixglata<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dixglata has no accepted answers">0%</span></p></div></div><div id="comments-container-9044" class="comments-container"></div><div id="comment-tools-9044" class="comment-tools"></div><div class="clear"></div><div id="comment-9044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

