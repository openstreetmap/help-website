+++
type = "question"
title = "Does Wireshark not count a Duplicate-ACK if it also contains a Receive Window change?"
description = '''In the capture included with Ask Wireshark question #60530, there were acknowledgement packets #17-#23 and #28-#31 that were Dup-ACKs but each also increased the Receive Window size. Due to the receive window increase, Wireshark reported them as a &quot;TCP Window Update&quot; but did not report them as &quot;Dupl...'''
date = "2017-04-04T03:38:00Z"
lastmod = "2017-04-04T20:52:00Z"
weight = 60562
keywords = [ "dup-ack", "rwin" ]
aliases = [ "/questions/60562" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark not count a Duplicate-ACK if it also contains a Receive Window change?](/questions/60562/does-wireshark-not-count-a-duplicate-ack-if-it-also-contains-a-receive-window-change)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60562-score" class="post-score" title="current number of votes">0</div><span id="post-60562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the capture included with Ask Wireshark <a href="https://ask.wireshark.org/questions/60530/question-regarding-tcp-traffic-capture-and-tcp-reno">question #60530</a>, there were acknowledgement packets #17-#23 and #28-#31 that were Dup-ACKs but each also increased the Receive Window size.</p><p>Due to the receive window increase, Wireshark reported them as a "TCP Window Update" but did not report them as "Duplicate ACK".</p><p>It also seems that the receiving client also didn't treat them as Dup-ACKs.</p><p>1) Can anyone confirm that the Wireshark code explicitly decides not to treat a Dup-ACK as such if it also contains an increment (or change) to the Receive Window value.</p><p>2) Does anyone know if this is a general TCP/IP rule, as suggested in the article:</p><p><a href="https://www.ietf.org/mail-archive/web/tcpm/current/msg01200.html">https://www.ietf.org/mail-archive/web/tcpm/current/msg01200.html</a></p><p>3) Can anyone comment about the way these are handled in any TCP/IP implementations they are aware of.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-rwin" rel="tag" title="see questions tagged &#39;rwin&#39;">rwin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '17, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p><span>Philst</span><br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Apr '17, 04:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-60562" class="comments-container"></div><div id="comment-tools-60562" class="comment-tools"></div><div class="clear"></div><div id="comment-60562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60576"></span>

<div id="answer-container-60576" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60576-score" class="post-score" title="current number of votes">0</div><span id="post-60576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Philst has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For my question (2), I just found RFC 5681 which does define Dup-ACKs.</p><p><em>Start Quote.</em></p><p>DUPLICATE ACKNOWLEDGMENT:</p><p>An acknowledgment is considered a "duplicate" in the following algorithms when</p><p>(a) the receiver of the ACK has outstanding data,</p><p>(b) the incoming acknowledgment carries no data,</p><p>(c) the SYN and FIN bits are both off,</p><p>(d) the acknowledgment number is equal to the greatest acknowledgment received on the given connection (TCP.UNA from [RFC793]) and</p><p><strong>(e) the advertised window in the incoming acknowledgment equals the advertised window in the last incoming acknowledgment.</strong></p><p>Alternatively, a TCP that utilizes selective acknowledgments (SACKs) [RFC2018, RFC2883] can leverage the SACK information to determine when an incoming ACK is a "duplicate" (e.g., if the ACK contains previously unknown SACK information).</p><p><em>End quote.</em></p><p>It would therefore appear that a receiver should not include Receive Window changes in any ACK packets that it wants to be treated as Dup-ACKs.</p><p>Thus, the TCP stack in the receiving client in <a href="https://ask.wireshark.org/questions/60530/question-regarding-tcp-traffic-capture-and-tcp-reno">Question #60530</a> is behaving badly.</p><p>This means that my own answers to my questions are:</p><p>(1) Yes, Wireshark is indeed treating behaving correctly in the way it handles such ACK packets.</p><p>(2) Yes, it is a rule as defined in <a href="https://tools.ietf.org/html/rfc5681#section-2">RFC 5681 Section 2</a>.</p><p>(3) Therefore, we wouldn't expect any TCP stacks to treat such ACKs as Dup-ACKs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '17, 20:52</strong></p><img src="https://secure.gravatar.com/avatar/35a0c1d0cf15b9d54d73bf54ae28abcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philst&#39;s gravatar image" /><p><span>Philst</span><br />
<span class="score" title="431 reputation points">431</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philst has 6 accepted answers">27%</span></p></div></div><div id="comments-container-60576" class="comments-container"></div><div id="comment-tools-60576" class="comment-tools"></div><div class="clear"></div><div id="comment-60576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60565"></span>

<div id="answer-container-60565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60565-score" class="post-score" title="current number of votes">1</div><span id="post-60565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li><p>I think this is the comment of the code block in question, taken from <a href="https://raw.githubusercontent.com/boundary/wireshark/master/epan/dissectors/packet-tcp.c">packet-tcp.c</a>:</p><pre><code>/* DUPLICATE ACK
 * It is a duplicate ack if window/seq/ack is the same as the previous
 * segment and if the segment length is 0
 */</code></pre></li><li><p>yes, I think it is, but stacks behavior may vary (as always) :-)</p></li><li><p>I can't remember to have seen any trace where an ACK with a receive window change was considered a duplicate ACK.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '17, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60565" class="comments-container"></div><div id="comment-tools-60565" class="comment-tools"></div><div class="clear"></div><div id="comment-60565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

