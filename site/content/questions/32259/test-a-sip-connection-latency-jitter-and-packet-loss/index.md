+++
type = "question"
title = "Test a SIP connection: latency, jitter and Packet Loss"
description = '''Is there anyway to test, by means Wireshark, a SIP connection calls quality in terms of: latency, jitter and Packet Loss? Thanks in advance'''
date = "2014-04-28T08:20:00Z"
lastmod = "2014-04-28T08:53:00Z"
weight = 32259
keywords = [ "sip", "calls" ]
aliases = [ "/questions/32259" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Test a SIP connection: latency, jitter and Packet Loss](/questions/32259/test-a-sip-connection-latency-jitter-and-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32259-score" class="post-score" title="current number of votes">0</div><span id="post-32259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyway to test, by means Wireshark, a SIP connection calls quality in terms of: latency, jitter and Packet Loss? Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-calls" rel="tag" title="see questions tagged &#39;calls&#39;">calls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '14, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/d51704b8a42befd4e65f1b85743233d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m4biz&#39;s gravatar image" /><p><span>m4biz</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m4biz has no accepted answers">0%</span></p></div></div><div id="comments-container-32259" class="comments-container"></div><div id="comment-tools-32259" class="comment-tools"></div><div class="clear"></div><div id="comment-32259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32262"></span>

<div id="answer-container-32262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32262-score" class="post-score" title="current number of votes">0</div><span id="post-32262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there anyway to test,</p></blockquote><p>If <strong>to test</strong> means that Wireshark actively sends test traffic, then the answer is: No, because Wireshark is a passive network analysis/troubleshooting tool, thus it cannot send simulated traffic.</p><p>If <strong>to test</strong> means that you want to analyze the quality of a recorded RTP session, then the answer is: Yes</p><blockquote><p>Telephony -&gt; RTP -&gt; Show all Streams</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32262" class="comments-container"><span id="32263"></span><div id="comment-32263" class="comment"><div id="post-32263-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt. Thanks for your reply. I'd like to test a QoS solution (<em>Untangle</em>). For this, I'd like to see - during a SIP call placed by means an IP phone connected via Internet to an external SIP server (<em>VoIP provider</em>) - wich is the actual latency, jitter and packet loss. In particular I'd like to see if the VoIP call latency, jitter and packet loss increase when on the internal LAN there are download and uploads from other PCs (<em>all connected to the same router/ADSL modem than IP phone</em>). In other words I'd like to evaluate the effective "quality" of my QoS solution. I don't need that Wireshark generate any SIP/RTP traffic because the IP phone generate all traffic needed. I hope my question, now, is more understandable</p></div><div id="comment-32263-info" class="comment-info"><span class="comment-age">(28 Apr '14, 08:53)</span> <span class="comment-user userinfo">m4biz</span></div></div></div><div id="comment-tools-32262" class="comment-tools"></div><div class="clear"></div><div id="comment-32262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

