+++
type = "question"
title = "TCP payload begins"
description = '''How Wireshark knows where TCP header ends and TCP payload begins. In the IP header, there are two values that indicate the length of the TCP/IP in a specific packet. If you subscribe &quot;Header Length&quot; from &quot;Total Length&quot; (Total Length - Header Length = TCP header and data) in IP header you will get a ...'''
date = "2015-05-17T00:55:00Z"
lastmod = "2015-05-17T06:09:00Z"
weight = 42445
keywords = [ "tcp" ]
aliases = [ "/questions/42445" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [TCP payload begins](/questions/42445/tcp-payload-begins)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42445-score" class="post-score" title="current number of votes">0</div><span id="post-42445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How Wireshark knows where TCP header ends and TCP payload begins. In the IP header, there are two values that indicate the length of the TCP/IP in a specific packet. If you subscribe "Header Length" from "Total Length" (Total Length - Header Length = TCP header and data) in IP header you will get a total length of TCP Header and data. I'm looking a method to get a length of TCP data only.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '15, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/8f40b62905779492fd0617eb289cd795?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Namik&#39;s gravatar image" /><p><span>Namik</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Namik has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-42445" class="comments-container"></div><div id="comment-tools-42445" class="comment-tools"></div><div class="clear"></div><div id="comment-42445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42448"></span>

<div id="answer-container-42448" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42448-score" class="post-score" title="current number of votes">0</div><span id="post-42448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>IP has two values: IP header length, and IP total length.</p><p><strong>TCP size</strong> (header plus payload) is IP total length minus IP header length.</p><p>TCP payload size is <strong>TCP size</strong> minus TCP header length.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42448" class="comments-container"></div><div id="comment-tools-42448" class="comment-tools"></div><div class="clear"></div><div id="comment-42448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42449"></span>

<div id="answer-container-42449" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42449-score" class="post-score" title="current number of votes">0</div><span id="post-42449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://tcpipguide.com/free/t_TCPMessageSegmentFormat-3.htm">TCP/IP Guide</a>: "Data Offset: Specifies the number of 32-bit words of data in the TCP header. In other words, this value times four equals the number of bytes in the header, which must always be a multiple of four. It is called a “data offset” since it indicates by how many 32-bit words the start of the data is offset from the beginning of the TCP segment."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42449" class="comments-container"></div><div id="comment-tools-42449" class="comment-tools"></div><div class="clear"></div><div id="comment-42449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42453"></span>

<div id="answer-container-42453" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42453-score" class="post-score" title="current number of votes">0</div><span id="post-42453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm looking a method to get a length of TCP data only.</p></blockquote><p>what about the display filter, <strong>tcp.len</strong> which can be added as a column.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/42445_screen1.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-42453" class="comments-container"></div><div id="comment-tools-42453" class="comment-tools"></div><div class="clear"></div><div id="comment-42453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

