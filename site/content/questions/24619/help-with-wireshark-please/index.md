+++
type = "question"
title = "Help with wireshark please"
description = '''Hello, I am new to Wireshark and need some help. I have been looking for a tool that can track my network internet usage.. (I.e. what each device is doing and how much data its using)  I was told about wireshark and they it does what I am after, but I am having trouble with working out how to view w...'''
date = "2013-09-12T18:51:00Z"
lastmod = "2013-09-13T01:57:00Z"
weight = 24619
keywords = [ "traffic", "data", "wireshark" ]
aliases = [ "/questions/24619" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help with wireshark please](/questions/24619/help-with-wireshark-please)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24619-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am new to Wireshark and need some help.</p><p>I have been looking for a tool that can track my network internet usage.. (I.e. what each device is doing and how much data its using)</p><p>I was told about wireshark and they it does what I am after, but I am having trouble with working out how to view what I need to.</p><p>I just want to list the device ip (and name if possible) and what its doing and how much data its using so I can see what device is using the most of my monthly data usage and then go to it and find out what its using it on..</p><p>please help, I need to be able to find out how much data each device is using :(</p><p>Thank you in advance</p></div><div id="question-tags" class="tags-container tags">traffic data wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '13, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/51bda9d68859f9b597db0237613187dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zousug&#39;s gravatar image" /><p>zousug<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zousug has no accepted answers">0%</span></p></div></div><div id="comments-container-24619" class="comments-container"></div><div id="comment-tools-24619" class="comment-tools"></div><div class="clear"></div><div id="comment-24619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24627"></span>

<div id="answer-container-24627" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24627-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark isn't really the right tool for this task. Wireshark is designed for packet analysis, i.e. the content of packets, not really for counting all packets and data, although it can do that to some extent.</p><p>Apart from the issues of running Wireshark for long term captures (it will run out of memory sooner or later) you would also need to arrange a suitable capture setup so that Wireshark would be able to observe all internet traffic on your network.</p><p>If you provide some more details about your setup then the folks here may be able to offer more suitable advice.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24627" class="comments-container"><span id="24723"></span><div id="comment-24723" class="comment"><div id="post-24723-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Sorry for the late reply..</p><p>I have about 8 devices on my network, I installed Wireshark and it seems to pick them all up (even my xbox) I just cant see the bandwidth each is using.</p><p>Do you know of some software that will do what I need? even some commercial one?</p><p>I just need to find some solution :(</p><p>Thanks again for your reply.</p></div><div id="comment-24723-info" class="comment-info"><span class="comment-age">(15 Sep '13, 13:42)</span> zousug</div></div><span id="24739"></span><div id="comment-24739" class="comment"><div id="post-24739-score" class="comment-score"></div><div class="comment-text"><p>If you are really able to capture <em>all</em> the traffic for <em>all</em> your devices (I doubt that is really happening unless you have no wireless and\or have a real hub between your "LAN" and the internet) then you can use the Statistics | Endpoints table, selecting the appropriate tabs, e.g. IPv4 or possibly IPv6, to see the traffic transmitted by each endpoint. You only need look at endpoint addresses that are within your "LAN" as all external hosts that your devices access will also be listed.</p></div><div id="comment-24739-info" class="comment-info"><span class="comment-age">(16 Sep '13, 01:40)</span> grahamb ♦</div></div></div><div id="comment-tools-24627" class="comment-tools"></div><div class="clear"></div><div id="comment-24627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

