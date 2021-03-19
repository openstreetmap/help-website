+++
type = "question"
title = "Wireshark position in stack versus local firewall"
description = '''On Windows2008R2, 64 bit with HP Teaming interfaces I watch the UDP requests for my application coming to the interface, but the aplication never responds although correctly configured. There is a local firewall running on the server which is controlled by ActiveDirectory profile Administrators, I c...'''
date = "2014-01-20T08:54:00Z"
lastmod = "2014-01-21T04:16:00Z"
weight = 29031
keywords = [ "raidmanagercci", "windows2008" ]
aliases = [ "/questions/29031" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark position in stack versus local firewall](/questions/29031/wireshark-position-in-stack-versus-local-firewall)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On Windows2008R2, 64 bit with HP Teaming interfaces I watch the UDP requests for my application coming to the interface, but the aplication never responds although correctly configured. There is a local firewall running on the server which is controlled by ActiveDirectory profile Administrators, I cannot disable it (temporarily), I only have local admin rights. I'm running Wireshark in Portable mode. The question is, if I see the datagram in Wireshark on the local machine, can I be confident it is passed up all the way the IP stack to the application ? In other words where sits the local, software firewall in the stack versus the Wireshark ? Could be the local firewall at fault ?</p></div><div id="question-tags" class="tags-container tags">raidmanagercci windows2008</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '14, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/2895936f373a4f3f3503fb056b220196?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georgedone&#39;s gravatar image" /><p>georgedone<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georgedone has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '14, 00:58</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29031" class="comments-container"></div><div id="comment-tools-29031" class="comment-tools"></div><div class="clear"></div><div id="comment-29031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29032"></span>

<div id="answer-container-29032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29032-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To be totally accurate Wireshark doesn't figure in the networking stack, the component that does that is <a href="http://www.winpcap.org/docs/default.htm">WinPCap</a>. There are some architecture diagrams on their site, but they don't really show where the drivers fit into the stack, and besides that they are woefully out of date (they list Win 95 through to Win XP as supported OS's).</p><p>WinPCap is an NDIS 5 driver so if you can find other documentation (from MS ??) showing where NDIS 5 fits in that might also help.</p><p>Other than that you might try the WinPCap <a href="http://www.winpcap.org/contact.htm">support</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '14, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29032" class="comments-container"></div><div id="comment-tools-29032" class="comment-tools"></div><div class="clear"></div><div id="comment-29032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29052"></span>

<div id="answer-container-29052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29052-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>if I see the datagram in Wireshark on the local machine, <strong>can I be confident it is passed up all the way the IP stack</strong> to the application ?</p></blockquote><p><strong>No</strong>, because the packet could</p><ul><li>have the wrong destination MAC address and you see it only because the interface was put in promiscuous mode by Wireshark</li><li>a wrong IP checksum and the OS would discard it</li><li>be 'broken' in another way, and thus the OS drops it</li><li>be dropped by the firewall (your assumption)</li></ul><p>In the first three cases, you would see the frame in Wireshark, although the application never gets the UDP packet (we have had several similar issues in other questions). Please check if the OS shows an increasing number of dropped frames (netstat -s).</p><p>Regarding the firewall problem, see the answer of @grahamb.</p><blockquote><p>There is a local firewall running on the server which is controlled by ActiveDirectory profile Administrators, I cannot disable it (temporarily),</p></blockquote><p>Well, checking the firewall (config and logs) would have been the first thing I would have done ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '14, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-29052" class="comments-container"></div><div id="comment-tools-29052" class="comment-tools"></div><div class="clear"></div><div id="comment-29052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

