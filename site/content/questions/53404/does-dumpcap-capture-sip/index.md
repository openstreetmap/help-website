+++
type = "question"
title = "Does dumpcap capture SIP"
description = '''I have been using dumpcap to capture and i was wondering if it captures SIP and RTP and if i open the trace in wireshark will it be shown as a SIP packer or an RTP packet'''
date = "2016-06-13T09:13:00Z"
lastmod = "2016-06-13T10:13:00Z"
weight = 53404
keywords = [ "sip", "dumpcap", "rtp" ]
aliases = [ "/questions/53404" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does dumpcap capture SIP](/questions/53404/does-dumpcap-capture-sip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53404-score" class="post-score" title="current number of votes">0</div><span id="post-53404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been using dumpcap to capture and i was wondering if it captures SIP and RTP and if i open the trace in wireshark will it be shown as a SIP packer or an RTP packet</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '16, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/0bfabb44c662192bed32f1818643c715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattG&#39;s gravatar image" /><p><span>MattG</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattG has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '16, 09:25</strong> </span></p></div></div><div id="comments-container-53404" class="comments-container"></div><div id="comment-tools-53404" class="comment-tools"></div><div class="clear"></div><div id="comment-53404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53406"></span>

<div id="answer-container-53406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53406-score" class="post-score" title="current number of votes">0</div><span id="post-53406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Dumpcap captures everything that comes to the NIC and that the NIC's hardware filter or dumpcap's capture filter doesn't filter out, unless the drivers installed by some security software interfere with WinPcap/NPcap operation (this is a concern on Windows). So if</p><ul><li><p>you use promiscuous mode (dumpcap's default setting of the NIC) and no capture filter at all,</p></li><li><p>we talk about wired NIC (wireless is a much more colourful story),</p></li><li><p>the SIP and RTP traffic is really present at the NIC,</p></li></ul><p>dumpcap will capture it.</p><p>What may be a bit of a trouble is whether Wireshark (or tshark) would recognize the two in the resulting capture automatically, but you should always be able to help it using <code>Decode as...</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '16, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53406" class="comments-container"><span id="53407"></span><div id="comment-53407" class="comment"><div id="post-53407-score" class="comment-score"></div><div class="comment-text"><p>Hi thanks for the reply so will the SIP show or will I have to decde it</p></div><div id="comment-53407-info" class="comment-info"><span class="comment-age">(13 Jun '16, 09:45)</span> <span class="comment-user userinfo">MattG</span></div></div><span id="53410"></span><div id="comment-53410" class="comment"><div id="post-53410-score" class="comment-score"></div><div class="comment-text"><p>Try it and find out :-)</p></div><div id="comment-53410-info" class="comment-info"><span class="comment-age">(13 Jun '16, 10:13)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-53406" class="comment-tools"></div><div class="clear"></div><div id="comment-53406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

