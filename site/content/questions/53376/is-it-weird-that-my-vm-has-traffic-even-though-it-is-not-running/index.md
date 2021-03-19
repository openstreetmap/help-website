+++
type = "question"
title = "Is it weird that my VM has traffic even though it is not running"
description = '''When I boot up Wireshark I notice that VMWare Network Adapter 1 and 8 have traffic on them (very little, such as: UDP,NBNS, LLMNR, ICMP, MDNS, BROWSER&amp;amp; DHCPv6, only around 60 packets in a minute though.)'''
date = "2016-06-12T10:44:00Z"
lastmod = "2016-06-12T10:44:00Z"
weight = 53376
keywords = [ "wireshark" ]
aliases = [ "/questions/53376" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it weird that my VM has traffic even though it is not running](/questions/53376/is-it-weird-that-my-vm-has-traffic-even-though-it-is-not-running)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53376-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I boot up Wireshark I notice that VMWare Network Adapter 1 and 8 have traffic on them (very little, such as: UDP,NBNS, LLMNR, ICMP, MDNS, BROWSER&amp; DHCPv6, only around 60 packets in a minute though.)</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '16, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/f26765f76e7477c3c88f134085f9fc4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RvBVakama&#39;s gravatar image" /><p>RvBVakama<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RvBVakama has no accepted answers">0%</span></p></div></div><div id="comments-container-53376" class="comments-container"><span id="53395"></span><div id="comment-53395" class="comment"><div id="post-53395-score" class="comment-score">1</div><div class="comment-text"><p>Each post should have a clear, specific question in the title field. Please rephrase the title as a proper question.</p><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-53395-info" class="comment-info"><span class="comment-age">(13 Jun '16, 04:43)</span> Jaap ♦</div></div><span id="53399"></span><div id="comment-53399" class="comment"><div id="post-53399-score" class="comment-score"></div><div class="comment-text"><p>Won't people be able to hack me if I share sensitive data such as the capture? I'm very worried about hacking since I have experienced it way too many times and lost too much data when my PC died many times before :(</p></div><div id="comment-53399-info" class="comment-info"><span class="comment-age">(13 Jun '16, 06:52)</span> RvBVakama</div></div><span id="53401"></span><div id="comment-53401" class="comment"><div id="post-53401-score" class="comment-score">1</div><div class="comment-text"><p>Have a look at <a href="https://www.tracewrangler.com/">TraceWrangler</a>. It allows to scramble the IP addresses and ports and to strip the payload of packets in a capture file. In this particular case (VM off), I would expect no sensitive contents of the payload, so you only need to obfuscate the IP addresses if any of them are public. If all IP addresses in the capture are private ones, it should be safe to publish it as it is.</p></div><div id="comment-53401-info" class="comment-info"><span class="comment-age">(13 Jun '16, 08:29)</span> sindy</div></div><span id="53403"></span><div id="comment-53403" class="comment"><div id="post-53403-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy</p></div><div id="comment-53403-info" class="comment-info"><span class="comment-age">(13 Jun '16, 08:39)</span> RvBVakama</div></div></div><div id="comment-tools-53376" class="comment-tools"></div><div class="clear"></div><div id="comment-53376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

