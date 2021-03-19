+++
type = "question"
title = "TCP data size &lt; size(IP Packet) - size(IP Header) - size(TCP Header) ???"
description = '''I use a java socket API to send data over TCP network. Recently I&#x27;ve got a strange bug: I&#x27;m sending 45 bytes into socket stream, but reciver gots only 42 of them. Looking through a tcpdump I see that the data section 42 bytes, although IP Packet size - IP Header size - TCP Header = 45! (see the imag...'''
date = "2014-03-19T09:01:00Z"
lastmod = "2014-03-19T13:12:00Z"
weight = 30957
keywords = [ "data", "tcp", "size" ]
aliases = [ "/questions/30957" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP data size &lt; size(IP Packet) - size(IP Header) - size(TCP Header) ???](/questions/30957/tcp-data-size-sizeip-packet-sizeip-header-sizetcp-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30957-score" class="post-score" title="current number of votes">0</div><span id="post-30957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use a java socket API to send data over TCP network. Recently I've got a strange bug: I'm sending 45 bytes into socket stream, but reciver gots only 42 of them. Looking through a tcpdump I see that the data section 42 bytes, although IP Packet size - IP Header size - TCP Header = 45! (see the image <img src="https://osqa-ask.wireshark.org/upfiles/2014-03-19_195308.png" alt="alt text" />) How it's possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '14, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/6a41079900d69edd24b32baaf7cf7f6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey%20Tolmachev&#39;s gravatar image" /><p><span>Andrey Tolma...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey Tolmachev has no accepted answers">0%</span></p></img></div></div><div id="comments-container-30957" class="comments-container"></div><div id="comment-tools-30957" class="comment-tools"></div><div class="clear"></div><div id="comment-30957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30958"></span>

<div id="answer-container-30958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30958-score" class="post-score" title="current number of votes">4</div><span id="post-30958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look at the line for the frame in the packet details:</p><p><code>Frame 1: 99 bytes on wire (792 bits), 96 bytes captured (768 bits)</code></p><p>Your capture is probably set to only grab 96 bytes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '14, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-30958" class="comments-container"><span id="30962"></span><div id="comment-30962" class="comment"><div id="post-30962-score" class="comment-score"></div><div class="comment-text"><p>and it's a good thing the IP total length is not adjusted accordingly, or the TCP expert would go crazy over missing sequence numbers :-)</p></div><div id="comment-30962-info" class="comment-info"><span class="comment-age">(19 Mar '14, 12:24)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="30970"></span><div id="comment-30970" class="comment"><div id="post-30970-score" class="comment-score"></div><div class="comment-text"><p><span>@Andrey</span> If you want to capture the entire packet with tcpdump use the -s 0 option.</p></div><div id="comment-30970-info" class="comment-info"><span class="comment-age">(19 Mar '14, 13:12)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-30958" class="comment-tools"></div><div class="clear"></div><div id="comment-30958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

