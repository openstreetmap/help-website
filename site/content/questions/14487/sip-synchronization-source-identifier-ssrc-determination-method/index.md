+++
type = "question"
title = "SIP Synchronization Source Identifier (SSRC) Determination Method"
description = '''How does Wireshark determine the which RTP streams are part of a call. In a multiple stream PCAP, how does it determine who belongs to who? thanks Eric'''
date = "2012-09-24T14:31:00Z"
lastmod = "2012-09-25T06:20:00Z"
weight = 14487
keywords = [ "sip", "rtp", "voip" ]
aliases = [ "/questions/14487" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP Synchronization Source Identifier (SSRC) Determination Method](/questions/14487/sip-synchronization-source-identifier-ssrc-determination-method)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14487-score" class="post-score" title="current number of votes">0</div><span id="post-14487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Wireshark determine the which RTP streams are part of a call. In a multiple stream PCAP, how does it determine who belongs to who?</p><p>thanks</p><p>Eric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '12, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-14487" class="comments-container"></div><div id="comment-tools-14487" class="comment-tools"></div><div class="clear"></div><div id="comment-14487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14509"></span>

<div id="answer-container-14509" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14509-score" class="post-score" title="current number of votes">1</div><span id="post-14509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First of all SSRC stands for Synchronization Source Identifier in the context of RTP. It identifies the timestamping source used to, as you might have guessed, timestamp the RTP packets. Therefore it has nothing to do with SIP.</p><p>But how then does Wireshark relate RTP sessions to SIP sessions? It looks in the SIP/SDP payloads for connection identifiers (IP address and port number), and defines so called conversations for them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '12, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14509" class="comments-container"></div><div id="comment-tools-14509" class="comment-tools"></div><div class="clear"></div><div id="comment-14509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

