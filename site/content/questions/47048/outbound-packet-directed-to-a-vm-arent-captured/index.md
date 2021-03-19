+++
type = "question"
title = "Outbound packet directed to a VM aren&#x27;t captured"
description = '''Hi, I&#x27;m running a VM on my host, its network configuration is bridged networking (virtualbox). I&#x27;m testing an application that sends packets on host and guest. It&#x27;s basically a ping and a response. I have wireshark on both host and guest, on the guest it captures properly the packets sent and receiv...'''
date = "2015-10-29T01:56:00Z"
lastmod = "2015-10-29T04:19:00Z"
weight = 47048
keywords = [ "vm", "virtualbox" ]
aliases = [ "/questions/47048" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Outbound packet directed to a VM aren't captured](/questions/47048/outbound-packet-directed-to-a-vm-arent-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47048-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47048-score" class="post-score" title="current number of votes">0</div><span id="post-47048-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm running a VM on my host, its network configuration is bridged networking (virtualbox). I'm testing an application that sends packets on host and guest. It's basically a ping and a response. I have wireshark on both host and guest, on the guest it captures properly the packets sent and received to/from the host IP, but on the host wireshark doesn't capture the packets sent to the guest IP (they exist, as they are captured as inbound packet in guest). Maybe the bridged networking configuration conflicts with winpcap? If I'm right, is there any solution? Thank you<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vm" rel="tag" title="see questions tagged &#39;vm&#39;">vm</span> <span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '15, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/065a787c1564a0f77c10c927f7f080b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rok&#39;s gravatar image" /><p><span>rok</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rok has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-47048" class="comments-container"></div><div id="comment-tools-47048" class="comment-tools"></div><div class="clear"></div><div id="comment-47048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47058"></span>

<div id="answer-container-47058" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47058-score" class="post-score" title="current number of votes">0</div><span id="post-47058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rok has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There have been other reports about problems with capturing data on <strong>bridged Virtualbox interfaces</strong>.</p><blockquote><p><a href="https://www.google.com/?q=site:ask.wireshark.org+virtualbox+bridge">https://www.google.com/?q=site:ask.wireshark.org+virtualbox+bridge</a></p></blockquote><p>Please run Wireshark in the virtual machine and capture the whole traffic there. That seems to work well.</p><p>See also my answer to similar questions:</p><blockquote><p><a href="https://ask.wireshark.org/questions/24181/unable-to-catch-websocket-traffic-both-directions">https://ask.wireshark.org/questions/24181/unable-to-catch-websocket-traffic-both-directions</a><br />
<a href="https://ask.wireshark.org/questions/41843/live-traffic-capture-of-two-vms-running-in-virtualbox">https://ask.wireshark.org/questions/41843/live-traffic-capture-of-two-vms-running-in-virtualbox</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47058" class="comments-container"></div><div id="comment-tools-47058" class="comment-tools"></div><div class="clear"></div><div id="comment-47058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

