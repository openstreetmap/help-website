+++
type = "question"
title = "Ethernet frame check sequence incorrect"
description = '''I am using Wireshark to debug an obscure problem, but on the way I have started seeing an unrelated issue: every packet sent to the monitoring PC is being flagged as having an incorrect frame check sequence (reported as being 0). This has started happening from the time I reinstalled Wiresharc, befo...'''
date = "2013-06-30T02:41:00Z"
lastmod = "2013-06-30T17:17:00Z"
weight = 22483
keywords = [ "frame", "badchecksum" ]
aliases = [ "/questions/22483" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet frame check sequence incorrect](/questions/22483/ethernet-frame-check-sequence-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22483-score" class="post-score" title="current number of votes">1</div><span id="post-22483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark to debug an obscure problem, but on the way I have started seeing an unrelated issue: every packet sent to the monitoring PC is being flagged as having an incorrect frame check sequence (reported as being 0).</p><p>This has started happening from the time I reinstalled Wiresharc, before which no such problems were being reported. I am assuming that the reinstallation gave me a newer version of Wireshark; I am currently running Version 1.10.0 (SVN Rev 49790 from /trunk-1.10).</p><p>As Windows XP is happily processing all these packets and giving the correct results, it seems that XP is seeing correct checksums in the packets.</p><p>Is there a problem with Wireshark or are the packets really wrong and XP is ignoring the frame check?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame" rel="tag" title="see questions tagged &#39;frame&#39;">frame</span> <span class="post-tag tag-link-badchecksum" rel="tag" title="see questions tagged &#39;badchecksum&#39;">badchecksum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '13, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/ef7626f540002d6403180aa20be73c9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Robertson&#39;s gravatar image" /><p><span>Peter Robertson</span><br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Robertson has no accepted answers">0%</span></p></div></div><div id="comments-container-22483" class="comments-container"><span id="22492"></span><div id="comment-22492" class="comment"><div id="post-22492-score" class="comment-score"></div><div class="comment-text"><p>Wireshark uses a hack^Wheuristic to determine whether the packet capture includes the checksum - some adapters/drivers/OS capture mechanisms supply checksums, some don't. Perhaps the code that implemented the heuristic changed between the previous version of Wireshark and the one you're now running, and it's now thinking the zero bytes at the end are an FCS.</p><p>What type of packets are they? Does the Ethernet header have a type or length field? If it's a length field, does it equal {the length as reported in the "Frame" section, minus 14}? If it's a type field, what protocol type are they? If some are IPv4 packets, does the "total length" in those packets equal {the length as reported in the "Frame" section, minus 14}? If some are IPv6 packets, does the "payload length" of those packets equal {the length as reported in the "Frame" section, minus 54}?</p></div><div id="comment-22492-info" class="comment-info"><span class="comment-age">(30 Jun '13, 17:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22483" class="comment-tools"></div><div class="clear"></div><div id="comment-22483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22484"></span>

<div id="answer-container-22484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22484-score" class="post-score" title="current number of votes">0</div><span id="post-22484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can disable the checksum validation in the ethernet protocol preferences. In most cases it's because the frame has some residual data appended to the real packet that was flowing over the ethernet. So it is not really something to be worried about. if the FCS was indeed incorrect you wouldn't have seen it in your trace.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '13, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/d6607c3aca20db751d019d8bbd2da893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde2&#39;s gravatar image" /><p><span>mrEEde2</span><br />
<span class="score" title="336 reputation points">336</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde2 has 5 accepted answers">20%</span></p></div></div><div id="comments-container-22484" class="comments-container"></div><div id="comment-tools-22484" class="comment-tools"></div><div class="clear"></div><div id="comment-22484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

