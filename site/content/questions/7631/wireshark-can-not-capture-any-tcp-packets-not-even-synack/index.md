+++
type = "question"
title = "Wireshark can not capture any TCP packets (not even SYN/ACk )"
description = '''I was trying to capture traffci by port spanning on Cisco WS-C3750-48P. Cisco IOS Software, C3750 Software (C3750-IPBASEK9-M), Version 12.2(44)SE2, RELEASE SOFTWARE (fc2) I can see UDP, ICMP, ARP, DHCP and microsoft stuff.However, I did not see any TCP packets captured, not even TCP SYN/ACK. Is it C...'''
date = "2011-11-25T07:50:00Z"
lastmod = "2011-11-27T05:46:00Z"
weight = 7631
keywords = [ "packets", "span", "port", "tcp" ]
aliases = [ "/questions/7631" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark can not capture any TCP packets (not even SYN/ACk )](/questions/7631/wireshark-can-not-capture-any-tcp-packets-not-even-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7631-score" class="post-score" title="current number of votes">0</div><span id="post-7631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to capture traffci by port spanning on Cisco WS-C3750-48P. Cisco IOS Software, C3750 Software (C3750-IPBASEK9-M), Version 12.2(44)SE2, RELEASE SOFTWARE (fc2)</p><p>I can see UDP, ICMP, ARP, DHCP and microsoft stuff.However, I did not see any TCP packets captured, not even TCP SYN/ACK. Is it CIsco port SPAN problem?/IOS Version/ or Wireshark problem? Any ideas? BTW, I'm using promiscurous mode. The wireshark can see the tcp traffic when sniffing the PC interface it's running on.</p><p>appreciate it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-span" rel="tag" title="see questions tagged &#39;span&#39;">span</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '11, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/c8899bf7ff079454120f8340b71568a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Buddy&#39;s gravatar image" /><p><span>Buddy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Buddy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '11, 07:52</strong> </span></p></div></div><div id="comments-container-7631" class="comments-container"></div><div id="comment-tools-7631" class="comment-tools"></div><div class="clear"></div><div id="comment-7631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7662"></span>

<div id="answer-container-7662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7662-score" class="post-score" title="current number of votes">0</div><span id="post-7662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could verify if all the frames you see are broadcast/multicast frames (from the range of protocols you mentioned I guess they are). If you're sure that the device you want to span is actually using TCP and you do not see it in the SPAN session you probably got the SPAN session wrong. Monitoring the wrong port is by far the most common mistake when setting up SPAN ports in my experience.</p><p>On the other hand you might have a VLAN tagging problem. If the TCP packets are VLAN-tagged your PC Interface might drop them if the card doesn't like them, and so you will not see them in Wireshark either. Try a different card if you think the SPAN port is correct and you should receive packets; I usually go for Realtek cards - they do not exactly have a good reputation but they usually capture anything, not knowing friend or foe.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '11, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7662" class="comments-container"></div><div id="comment-tools-7662" class="comment-tools"></div><div class="clear"></div><div id="comment-7662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

