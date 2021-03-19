+++
type = "question"
title = "Filter for detecting the third packet in a 3-way handshake"
description = '''Hello, I am working on putting together a training for my team on recognizing a SYN flood attack.  There are many ways to recognize one, for sure. The high volume of SYNs, sessions in SYN_SENT, etc.  What I would like to do, however, is provide three filters for use with the I/O graphs to show, with...'''
date = "2013-10-18T09:29:00Z"
lastmod = "2014-09-09T11:09:00Z"
weight = 26174
keywords = [ "handshake", "syn" ]
aliases = [ "/questions/26174" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filter for detecting the third packet in a 3-way handshake](/questions/26174/filter-for-detecting-the-third-packet-in-a-3-way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26174-score" class="post-score" title="current number of votes">0</div><span id="post-26174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am working on putting together a training for my team on recognizing a SYN flood attack.<br />
</p><p>There are many ways to recognize one, for sure. The high volume of SYNs, sessions in SYN_SENT, etc.</p><p>What I would like to do, however, is provide three filters for use with the I/O graphs to show, without question, that the SYN,ACK is not being honored.</p><p>I have this, so far ..</p><p>Filter 1: tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 0 Filter 2: tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 1 Filter 3: tcp.seq == 1 &amp;&amp; tcp.ack == 1 &amp;&amp; tcp.len == 0 &amp;&amp; !(tcp.flags.push == 1)</p><p>I am pretty sure I am missing something here.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/ad02d2c94bb362339b32ac9e2ca8468e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qwert&#39;s gravatar image" /><p><span>Qwert</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qwert has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-26174" class="comments-container"><span id="26175"></span><div id="comment-26175" class="comment"><div id="post-26175-score" class="comment-score"></div><div class="comment-text"><p>Looks like the formatting got lost</p><p>Filter 1: tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 0</p><p>Filter 2: tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 1</p><p>Filter 3: tcp.seq == 1 &amp;&amp; tcp.ack == 1 &amp;&amp; tcp.len == 0 &amp;&amp; !(tcp.flags.push == 1)</p></div><div id="comment-26175-info" class="comment-info"><span class="comment-age">(18 Oct '13, 09:30)</span> <span class="comment-user userinfo">Qwert</span></div></div></div><div id="comment-tools-26174" class="comment-tools"></div><div class="clear"></div><div id="comment-26174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26181"></span>

<div id="answer-container-26181" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26181-score" class="post-score" title="current number of votes">3</div><span id="post-26181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Qwert has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think this should get you what you want...</p><p>SYN packet from Clients: tcp[13]==02</p><p>SYN_ACK packets from Server: tcp[13]==12</p><p>ACK 3-way handshake: tcp.seq==1 &amp;&amp; tcp.ack==1 &amp;&amp; tcp.len==0 &amp;&amp; tcp.window_size_scalefactor ge 0</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-26181" class="comments-container"><span id="26189"></span><div id="comment-26189" class="comment"><div id="post-26189-score" class="comment-score"></div><div class="comment-text"><p>That did the trick. Thank you for the answer.</p></div><div id="comment-26189-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:32)</span> <span class="comment-user userinfo">Qwert</span></div></div><span id="26194"></span><div id="comment-26194" class="comment"><div id="post-26194-score" class="comment-score"></div><div class="comment-text"><p>Improvement on the third (assuming you're looking for a filter that shows all final acks that are part of the handshake), with the additional warning that both will fail when sequence numbers are not set to relative:</p><p><code>tcp.seq==1 &amp;&amp; tcp.ack==1 &amp;&amp; tcp.len==0 &amp;&amp; (tcp.window_size_scalefactor ge 0 or tcp.window_size_scalefactor eq -2)</code></p><p>Advantage is that with the filter of <span></span><span>@mrEEde</span> you'd miss sessions that do not use window scaling, but have a full handshake.</p><p>By the way, I think I'm probably too tired by now, but why did you accept the answer if you're looking for a filter to find SYN/ACKs that are not answered by a final ACK to complete the handshake? With the filter you accepted you'll find all ACKs that are completing the handshake.</p><p>I have to admit that, as far as I can tell, there is no way to find SYN - SYN/ACK sequences that have now final ACK with Wireshark. So maybe your way is to find all connections that have a full handshake, and substract the number from the count of all SYN/ACKs you see?</p><p>Anyway, all real SYN floods I have seen so far are pretty obvious (to put it mildly) - I'd have to be completely blind not to see the attack in 5 seconds flat, and without any filter :-)</p></div><div id="comment-26194-info" class="comment-info"><span class="comment-age">(18 Oct '13, 11:04)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26201"></span><div id="comment-26201" class="comment"><div id="post-26201-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for your response. I'm still very much a packet-analysis novice, so I appreciate the comment on window scaling. It didn't occur to me that some sessions would not use it until after you mentioned it.</p><p>My thought is that by using a filter that will reliably capture the third packet in the 3-way, the absence of matches will provide categorical proof that the SYN.ACK is not being answered (given that there should be thousands(+) SYNs).<br />
</p><p>And yes .. I absolutely agree that there are plenty of indicators when a real SYN flood is occurring, and really .. these are not a problem in most large scale networks with a robust IPS implementation.<br />
</p><p>This is for a training doc to give the TCP-novice a clear way to determine whether a SYN flood is occurring (thus .. hopefully .. mitigating the need to reach out to an oncall at OMGam).<br />
</p><p>Thanks, Kevin</p></div><div id="comment-26201-info" class="comment-info"><span class="comment-age">(18 Oct '13, 14:59)</span> <span class="comment-user userinfo">Qwert</span></div></div><span id="26202"></span><div id="comment-26202" class="comment"><div id="post-26202-score" class="comment-score"></div><div class="comment-text"><p>Okay, as long as you got an answer that helps I'm fine with it ;-)</p><p>Just a final comment: I agree, even robust IPS implementations do not always help. I've been involved in cases where the SYN flood was so big that it took down two upstream providers that provided the data connections to the customer. 70Gbit/s is just too much... :-)</p></div><div id="comment-26202-info" class="comment-info"><span class="comment-age">(18 Oct '13, 15:17)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-26181" class="comment-tools"></div><div class="clear"></div><div id="comment-26181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36117"></span>

<div id="answer-container-36117" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36117-score" class="post-score" title="current number of votes">0</div><span id="post-36117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this (must use relative SEQ #s):</p><p>(tcp.seq == 1 &amp;&amp; tcp.ack == 1&amp;&amp;tcp.len==0 &amp;&amp; !tcp.flags.fin == 1)||tcp.flags.syn==1</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '14, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/8919ee3cfc855dc549409d5a02c2c161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="akaplan&#39;s gravatar image" /><p><span>akaplan</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="akaplan has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-36117" class="comments-container"></div><div id="comment-tools-36117" class="comment-tools"></div><div class="clear"></div><div id="comment-36117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

