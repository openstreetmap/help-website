+++
type = "question"
title = "libpcap Timestamp"
description = '''Hi, We are working on a project where we need to know precise details about the generation of the timestamp when capturing with tcpdump. We&#x27;ve struggled a bit to find the information we need, but trawling around the web we have pulled together what we think are the correct details - see https://comm...'''
date = "2017-03-29T00:02:00Z"
lastmod = "2017-03-29T20:11:00Z"
weight = 60395
keywords = [ "libpcap" ]
aliases = [ "/questions/60395" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [libpcap Timestamp](/questions/60395/libpcap-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60395-score" class="post-score" title="current number of votes">0</div><span id="post-60395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are working on a project where we need to know precise details about the generation of the timestamp when capturing with tcpdump. We've struggled a bit to find the information we need, but trawling around the web we have pulled together what we think are the correct details - see <a href="https://community.tribelab.com/mod/page/view.php?id=647">https://community.tribelab.com/mod/page/view.php?id=647</a></p><p>Is the detail on this page correct?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '17, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-60395" class="comments-container"><span id="60430"></span><div id="comment-60430" class="comment"><div id="post-60430-score" class="comment-score"></div><div class="comment-text"><p>Thanks Anders. I think that answers my questions.</p><p>Could someone change Anders comment to and answer and I'll mark it as accepted?</p></div><div id="comment-60430-info" class="comment-info"><span class="comment-age">(29 Mar '17, 14:10)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-60395" class="comment-tools"></div><div class="clear"></div><div id="comment-60395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="60433"></span>

<div id="answer-container-60433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60433-score" class="post-score" title="current number of votes">1</div><span id="post-60433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's the Wireshark Wiki <a href="https://wiki.wireshark.org/Timestamps">Timestamps</a> page.</p><p>There's a tcpdump FAQ: <a href="http://www.tcpdump.org/faq.html#q8">When is a packet time-stamped? How accurate are the time stamps?</a>.</p><p>For WinPcap\npcap I believe the packet is timestamped by the npf driver on receipt of the callback from the NIC driver handing off a buffer of data, so this is in the npf kernel driver. The timestamp itself is derived from several sources depending on whether the system is x86 or x64 and the timestamp mode. For info about the mode see <a href="https://www.wireshark.org/lists/wireshark-users/201008/msg00171.html">this</a> email.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '17, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60433" class="comments-container"></div><div id="comment-tools-60433" class="comment-tools"></div><div class="clear"></div><div id="comment-60433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60435"></span>

<div id="answer-container-60435" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60435-score" class="post-score" title="current number of votes">1</div><span id="post-60435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is the detail on this page correct?</p></blockquote><p>No. The time stamping is, in most OSes supported by libpcap, done in the kernel. The only exception is HP-UX.</p><p>However, that doesn't mean that the time stamping is done the instant the packet arrives on the adapter. There can be a delay between the point at which the first octet of the packet arrives and the point at which the last octet of the packet arrives, and a delay between the point at which the last octet of the packet is given to the host and the point at which the host is notified of the packet's arrival (by an interrupt, or by the host doing polling), and a delay between the point at which the host is notified of the packet's arrival and the point at which the host networking stack time-stamps the packet.</p><p>As Anders noted, newer versions of libpcap support hardware time stamping; that's supported only on Linux, with newer versions of the Linux kernel, and with adapters that support it. Note, however, that those time stamps might not be synchronized with the host's clock, and might be based on <a href="https://en.wikipedia.org/wiki/Precision_Time_Protocol">Precision Time Protocol</a> time stamps, which are based on International Atomic Time and might have, as their time origin, January 1, 1970, 00:00:00 TAI, rather than the UN*X origin of January 1, 1970, 00:00:00 UTC, and thus might be a few seconds different from UN*X time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '17, 20:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Mar '17, 20:17</strong> </span></p></div></div><div id="comments-container-60435" class="comments-container"></div><div id="comment-tools-60435" class="comment-tools"></div><div class="clear"></div><div id="comment-60435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60398"></span>

<div id="answer-container-60398" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60398-score" class="post-score" title="current number of votes">0</div><span id="post-60398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think newer libcap offers HW timestamps, not sure how well it works. <a href="http://www.tcpdump.org/manpages/pcap-tstamp.7.html">http://www.tcpdump.org/manpages/pcap-tstamp.7.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '17, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-60398" class="comments-container"></div><div id="comment-tools-60398" class="comment-tools"></div><div class="clear"></div><div id="comment-60398-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

