+++
type = "question"
title = "wireshark is not capturing ping/ICMP packets. Why?"
description = '''I an running wireshark on two different computers, one is a Linux (Lucid Lynx), and the other is running BackTrack4. Both computers are on the same network. Wireshark is listening on eth0 of both computers. No filters are set, and all traffic is visible. Browser requests show up, secure shell connec...'''
date = "2011-09-14T07:20:00Z"
lastmod = "2011-09-14T17:56:00Z"
weight = 6362
keywords = [ "icmp", "ping" ]
aliases = [ "/questions/6362" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark is not capturing ping/ICMP packets. Why?](/questions/6362/wireshark-is-not-capturing-pingicmp-packets-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6362-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I an running wireshark on two different computers, one is a Linux (Lucid Lynx), and the other is running BackTrack4. Both computers are on the same network. Wireshark is listening on eth0 of both computers. No filters are set, and all traffic is visible. Browser requests show up, secure shell connections show up, and all sorts of assorted network traffic between the other computers on the network are also visible. HOWEVER, when I ping my DNS (OpenDNS, 208.67.222.222) or other computers on my own network, NO ICMP traffic shows up in Wireshark. I ping from the exact same command shell that I am using for SSH connections, and while the SSH connection traffic is detected by wireshark, ping traffic from that same shell is NOT detected. This is happening on TWO different computers running wireshark. No ping traffic whatsoever is detected by either instance of Wireshark. What the hell is going on?</p></div><div id="question-tags" class="tags-container tags">icmp ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '11, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/b7abac5d0aeb4ac5342b12d4f1be70e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KatmanDu&#39;s gravatar image" /><p>KatmanDu<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KatmanDu has no accepted answers">0%</span></p></div></div><div id="comments-container-6362" class="comments-container"><span id="6363"></span><div id="comment-6363" class="comment"><div id="post-6363-score" class="comment-score"></div><div class="comment-text"><p>Okay, things just got a little weirder. I tried Wireshark on a CentOS 6 machine, and the ICMP packets were shown by Wireshark. It must be an Ubuntu issue, as BT4 is based on Ubuntu. I would still like to know why Ubuntu-based ICMP traffic is not detected by Wireshark...........</p></div><div id="comment-6363-info" class="comment-info"><span class="comment-age">(14 Sep '11, 07:34)</span> KatmanDu</div></div></div><div id="comment-tools-6362" class="comment-tools"></div><div class="clear"></div><div id="comment-6362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6378"></span>

<div id="answer-container-6378" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6378-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>NEVER MIND! I had a dumbass attack. My laptops were connected wirelessly, not on eth0. <em>slinks off in shame</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/b7abac5d0aeb4ac5342b12d4f1be70e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KatmanDu&#39;s gravatar image" /><p>KatmanDu<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KatmanDu has no accepted answers">0%</span></p></div></div><div id="comments-container-6378" class="comments-container"></div><div id="comment-tools-6378" class="comment-tools"></div><div class="clear"></div><div id="comment-6378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

