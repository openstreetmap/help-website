+++
type = "question"
title = "How to interpret IPv4 header"
description = '''I need guides on how to read following hexadecimal value. I got the following example, but still don&#x27;t really get it on how to read them. 45 00 00 30 44 22 40 00 8 006 00 00 8c 7c 19 ac ae 24 1e 2b As you can see above..there are 20 bytes/bits (still not really sure how to call them) How do i determ...'''
date = "2014-04-23T06:19:00Z"
lastmod = "2014-04-23T12:54:00Z"
weight = 32097
keywords = [ "ipv4", "homework" ]
aliases = [ "/questions/32097" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to interpret IPv4 header](/questions/32097/how-to-interpret-ipv4-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32097-score" class="post-score" title="current number of votes">0</div><span id="post-32097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need guides on how to read following hexadecimal value.</p><p>I got the following example, but still don't really get it on how to read them.</p><p>45 00 00 30 44 22 40 00 8 006 00 00 8c 7c 19 ac ae 24 1e 2b</p><p>As you can see above..there are 20 bytes/bits (still not really sure how to call them)</p><p>How do i determine following.</p><p>1)Version 2)Header length 3)Type of service 4)Total length 5)Identification 6)Flags 7)Fragment offset 8)TTL 9)Protocol 10)Header checksum 11)Source IP 12)Destination IP</p><p>I hope there will be anyone kind enough to guide me on how to get the data.</p><p>TQVM.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span> <span class="post-tag tag-link-homework" rel="tag" title="see questions tagged &#39;homework&#39;">homework</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/0bf536acfbac2573db27cb3c61722011?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Titanfall&#39;s gravatar image" /><p><span>Titanfall</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Titanfall has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '14, 06:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32097" class="comments-container"></div><div id="comment-tools-32097" class="comment-tools"></div><div class="clear"></div><div id="comment-32097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32098"></span>

<div id="answer-container-32098" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32098-score" class="post-score" title="current number of votes">2</div><span id="post-32098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe you want <a href="http://tools.ietf.org/html/rfc791">RFC 791</a>, in particular <a href="http://tools.ietf.org/html/rfc791#section-3.1">Sect 3.1 Internet Header Format</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-32098" class="comments-container"><span id="32102"></span><div id="comment-32102" class="comment"><div id="post-32102-score" class="comment-score"></div><div class="comment-text"><p>Hello sir, thx for replying.</p><p>I have gone through those notes.Unfortunately I still don't get it on how thing works.</p><p>Therefore,my purpose of above question was to look for ppl who might be free to provide me the way they get the answer.</p><p>I hope you could help me out.</p></div><div id="comment-32102-info" class="comment-info"><span class="comment-age">(23 Apr '14, 07:54)</span> <span class="comment-user userinfo">Titanfall</span></div></div><span id="32106"></span><div id="comment-32106" class="comment"><div id="post-32106-score" class="comment-score"></div><div class="comment-text"><pre><code>0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+</code></pre><p>45 00 00 30 44 ...<br />
First for bits is 4 (out of Hexadecimal 45) Version = 4<br />
IHL = next for bits = 5<br />
and so on ( Total lenght = #00 30)</p></div><div id="comment-32106-info" class="comment-info"><span class="comment-age">(23 Apr '14, 08:18)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-32098" class="comment-tools"></div><div class="clear"></div><div id="comment-32098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32123"></span>

<div id="answer-container-32123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32123-score" class="post-score" title="current number of votes">2</div><span id="post-32123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><img src="http://foren6.files.wordpress.com/2011/04/ip-header-v41.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span> </br></br></p></img></div></div><div id="comments-container-32123" class="comments-container"></div><div id="comment-tools-32123" class="comment-tools"></div><div class="clear"></div><div id="comment-32123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

