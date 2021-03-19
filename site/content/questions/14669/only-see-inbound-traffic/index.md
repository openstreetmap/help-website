+++
type = "question"
title = "only see inbound traffic"
description = '''Hi, On two Dell PC, with Intel 82567LM-3 network Card on a switched wired network. I only see incoming trafic, I can&#x27;t see the outgoing trafic from my interface. As exemple, I only get the ICPM reply when a do a ping from my computer Any idea?'''
date = "2012-10-03T07:31:00Z"
lastmod = "2012-10-08T12:14:00Z"
weight = 14669
keywords = [ "capture", "outgoing", "outbound", "seeing" ]
aliases = [ "/questions/14669" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [only see inbound traffic](/questions/14669/only-see-inbound-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14669-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>On two Dell PC, with Intel 82567LM-3 network Card on a switched wired network. I only see incoming trafic, I can't see the outgoing trafic from my interface. As exemple, I only get the ICPM reply when a do a ping from my computer</p><p>Any idea?</p></div><div id="question-tags" class="tags-container tags">capture outgoing outbound seeing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '12, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/72cccd4c84572f1dd8d8c270ee4ffa63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yokan&#39;s gravatar image" /><p>yokan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yokan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '14, 07:12</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-14669" class="comments-container"><span id="14670"></span><div id="comment-14670" class="comment"><div id="post-14670-score" class="comment-score"></div><div class="comment-text"><p>After test, It's not linked to the network card. With an other card I have the same problem.</p></div><div id="comment-14670-info" class="comment-info"><span class="comment-age">(03 Oct '12, 07:35)</span> yokan</div></div><span id="14671"></span><div id="comment-14671" class="comment"><div id="post-14671-score" class="comment-score"></div><div class="comment-text"><p>Can you tell us the OS and the version of Wireshark you are using?</p></div><div id="comment-14671-info" class="comment-info"><span class="comment-age">(03 Oct '12, 08:23)</span> grahamb ♦</div></div><span id="14874"></span><div id="comment-14874" class="comment"><div id="post-14874-score" class="comment-score"></div><div class="comment-text"><p>Win 7 and multiple version, same result</p></div><div id="comment-14874-info" class="comment-info"><span class="comment-age">(10 Oct '12, 04:05)</span> yokan</div></div></div><div id="comment-tools-14669" class="comment-tools"></div><div class="clear"></div><div id="comment-14669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14787"></span>

<div id="answer-container-14787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14787-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>After test, It's not linked to the network card. With an other card I have the same problem.</p></blockquote><p>I guess it's some <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> (AV, Firewall, Endpoint Security, VPN Client, etc.). Disable all of them OR boot the system with a bootable Linux CD (BackTrack, Ubuntu, Knoppix) and then try again. It should work with Linux, as I have the same NIC in my Dell Laptop and it works with Win7 and Linux (Fedora, Ubuntu, etc.).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14787" class="comments-container"><span id="14875"></span><div id="comment-14875" class="comment"><div id="post-14875-score" class="comment-score"></div><div class="comment-text"><p>Seems right, I'll try that as soon as possible. Thank you</p></div><div id="comment-14875-info" class="comment-info"><span class="comment-age">(10 Oct '12, 04:06)</span> yokan</div></div></div><div id="comment-tools-14787" class="comment-tools"></div><div class="clear"></div><div id="comment-14787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

