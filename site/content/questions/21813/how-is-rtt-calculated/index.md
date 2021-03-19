+++
type = "question"
title = "How is RTT calculated"
description = '''i would like to know how wireshark is calculating rtt? is it cosidering delayed ack&#x27;s, piggybacked acks and retransmitted packets.If it is not considered how do i incoorporate/filter these in calcuting rtt'''
date = "2013-06-07T00:49:00Z"
lastmod = "2016-11-08T09:57:00Z"
weight = 21813
keywords = [ "calculation", "rtt" ]
aliases = [ "/questions/21813" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How is RTT calculated](/questions/21813/how-is-rtt-calculated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21813-score" class="post-score" title="current number of votes">0</div><span id="post-21813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i would like to know how wireshark is calculating rtt? is it cosidering delayed ack's, piggybacked acks and retransmitted packets.If it is not considered how do i incoorporate/filter these in calcuting rtt</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-calculation" rel="tag" title="see questions tagged &#39;calculation&#39;">calculation</span> <span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '13, 00:49</strong></p><img src="https://secure.gravatar.com/avatar/1bfd7c73ffe5eef5c45238e0e0f548a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SThomas&#39;s gravatar image" /><p><span>SThomas</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SThomas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted <strong>07 Jun '13, 01:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21813" class="comments-container"></div><div id="comment-tools-21813" class="comment-tools"></div><div class="clear"></div><div id="comment-21813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57178"></span>

<div id="answer-container-57178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57178-score" class="post-score" title="current number of votes">1</div><span id="post-57178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark initial Round Trip Time (iRTT) value is calculated when the first two packets of a TCP handshake are seen {SYN, SYN/ACK}. This value will remain the same for the entire TCP conversation. {tcp.analysis.initial_rtt}</p><p>When you graph RTT in an IO graph, latency times are depicted between a data packet and the subsequent acknowledgment packet.</p><p>You can always do your own handshake analysis and filter on {tcp.flags.syn==1} to find the start of the conversation and then set time deltas to calculate individual session RTTs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '16, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/bfccba6dc51febee5ca1641be7df63ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BruteForce&#39;s gravatar image" /><p><span>BruteForce</span><br />
<span class="score" title="120 reputation points">120</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BruteForce has one accepted answer">9%</span></p></div></div><div id="comments-container-57178" class="comments-container"></div><div id="comment-tools-57178" class="comment-tools"></div><div class="clear"></div><div id="comment-57178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57075"></span>

<div id="answer-container-57075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57075-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57075-score" class="post-score" title="current number of votes">0</div><span id="post-57075-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It takes the send time (ack) - send time (packet, that is, tcp)</p><p>k?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/2b54f6631869b2e7b13cb746742ea8cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Josh123456789&#39;s gravatar image" /><p><span>Josh123456789</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Josh123456789 has no accepted answers">0%</span></p></div></div><div id="comments-container-57075" class="comments-container"></div><div id="comment-tools-57075" class="comment-tools"></div><div class="clear"></div><div id="comment-57075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

