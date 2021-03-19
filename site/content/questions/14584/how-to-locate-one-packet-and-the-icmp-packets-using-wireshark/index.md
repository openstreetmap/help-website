+++
type = "question"
title = "How to locate one packet and the icmp packets using wireshark?"
description = '''When I found a icmp(example: icmp need to fragmented..) packet using wireshark,how can I easily locate the unique packet generating the icmp ?'''
date = "2012-09-28T01:20:00Z"
lastmod = "2012-09-28T01:32:00Z"
weight = 14584
keywords = [ "locate", "icmp" ]
aliases = [ "/questions/14584" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to locate one packet and the icmp packets using wireshark?](/questions/14584/how-to-locate-one-packet-and-the-icmp-packets-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14584-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I found a icmp(example: icmp need to fragmented..) packet using wireshark,how can I easily locate the unique packet generating the icmp ?</p></div><div id="question-tags" class="tags-container tags">locate icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/7fdbac8aac2e38813e1fc1da4c6efdf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chinasan&#39;s gravatar image" /><p>chinasan<br />
<span class="score" title="0 reputation points">0</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chinasan has no accepted answers">0%</span></p></div></div><div id="comments-container-14584" class="comments-container"></div><div id="comment-tools-14584" class="comment-tools"></div><div class="clear"></div><div id="comment-14584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14585"></span>

<div id="answer-container-14585" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14585-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's the nice thing about ICMP, it includes part of the packet that generated the ICMP message. If you look into the packet details pane you will see a second IP layer below the ICMP layer. Open it up and look for the Identification field (<a href="http://ip.id">ip.id</a>).</p><p>You can then right-click on it and choose "Copy -&gt; As filter". Then press CTRL+F to open the search dialog and paste the copied filter in the filter text-box. Choose "UP" for direction and click on "find".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '12, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14585" class="comments-container"><span id="14609"></span><div id="comment-14609" class="comment"><div id="post-14609-score" class="comment-score"></div><div class="comment-text"><p>Assume your two hosts are 1.1.1.1 and 2.2.2.2. Someone in the middle generates an ICMP telling 1.1.1.1 or 2.2.2.2 to make the packets smaller (icmp 3/4 message). Beauty of Wireshark is that "ip.addr==1.1.1.1" filter will <em>also</em> include the ICMP message from some router in the middel (who sent the type3/4 message). To make it even easier, you can use "icmp and ip.addr==1.1.1.1" to find it. good luck. By the way, it doesn't matter if you choose 1.1.1.1 or 2.2.2.2. Since the ICMP will have both addresses in the ICMP header (as Sake pointed out)</p></div><div id="comment-14609-info" class="comment-info"><span class="comment-age">(28 Sep '12, 14:15)</span> hansangb</div></div></div><div id="comment-tools-14585" class="comment-tools"></div><div class="clear"></div><div id="comment-14585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

