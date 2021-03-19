+++
type = "question"
title = "Wireshark and PXE Server"
description = '''Hello We are sending a UDP Request to the PXE Server but for some reason the PXE Server is not receiving this UDP request. Then we put wireshark on the PXE server and now we see that the PXE Server does receive our UDP Request.  Any thoughts on why this might be happening? Thanks,'''
date = "2013-07-25T16:25:00Z"
lastmod = "2013-07-25T16:25:00Z"
weight = 23370
keywords = [ "nelsme", "recognized" ]
aliases = [ "/questions/23370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and PXE Server](/questions/23370/wireshark-and-pxe-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>We are sending a UDP Request to the PXE Server but for some reason the PXE Server is not receiving this UDP request. Then we put wireshark on the PXE server and now we see that the PXE Server does receive our UDP Request.</p><p>Any thoughts on why this might be happening?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">nelsme recognized</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '13, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/36b03db527cc675fe39499fa97c33700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisPXE&#39;s gravatar image" /><p>ChrisPXE<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisPXE has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '13, 16:53</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23370" class="comments-container"><span id="23371"></span><div id="comment-23371" class="comment"><div id="post-23371-score" class="comment-score"></div><div class="comment-text"><p>What happens if, for example, you run tcpdump or WinDump (depending on whether the PXE server is running Un*x or Windows), or tshark, capturing on the interface on which the PXE server would receive packets from the host that's sending them? Does that also cause the PXE server to see the UDP request?</p><p>To what MAC address (not IP address, MAC address) is the UDP packet being sent? Is it the same as the MAC address of the interface on which the PXE server would receive packets from the host that's sending them?</p></div><div id="comment-23371-info" class="comment-info"><span class="comment-age">(25 Jul '13, 16:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-23370" class="comment-tools"></div><div class="clear"></div><div id="comment-23370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

