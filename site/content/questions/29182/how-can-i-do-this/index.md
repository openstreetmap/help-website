+++
type = "question"
title = "How can i do this?"
description = '''How do i connect wireshark to a router, so that i can view the packets that are flowing through the router? Maybe if there is something like this: dst host xxx.xxx.xxx.xxx . Am I on the right way?'''
date = "2014-01-27T08:01:00Z"
lastmod = "2014-01-27T08:10:00Z"
weight = 29182
keywords = [ "router" ]
aliases = [ "/questions/29182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can i do this?](/questions/29182/how-can-i-do-this)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do i connect wireshark to a router, so that i can view the packets that are flowing through the router? Maybe if there is something like this: dst host xxx.xxx.xxx.xxx . Am I on the right way?</p></div><div id="question-tags" class="tags-container tags">router</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/02bfcf9ef119a526e187ef0550113711?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beginer&#39;s gravatar image" /><p>Beginer<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beginer has no accepted answers">0%</span></p></div></div><div id="comments-container-29182" class="comments-container"></div><div id="comment-tools-29182" class="comment-tools"></div><div class="clear"></div><div id="comment-29182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29184"></span>

<div id="answer-container-29184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29184-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't "connect" Wireshark to a router. You can only capture packets on a system that Wireshark runs on, or open a capture file that was already saved to disk by TCPdump or similar tools. So no, unfortunately you're not on the right way. You need to find out if your router has a feature to write packets to disk/sdcard/usb key, otherwise you're out of luck. Maybe it has a port mirroring feature ("SPAN") that allows you to copy packets to an interface Wireshark listens on though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29184" class="comments-container"><span id="29186"></span><div id="comment-29186" class="comment"><div id="post-29186-score" class="comment-score"></div><div class="comment-text"><p>ohh.. i thought if I will be able to "connect" to router, so i will be able to trace all files whitch are traveling through router. If I write a filter dst host xxx.xxx.xxx.xxx , i can see only my traffic.</p></div><div id="comment-29186-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:14)</span> Beginer</div></div><span id="29188"></span><div id="comment-29188" class="comment"><div id="post-29188-score" class="comment-score"></div><div class="comment-text"><p>yes, because only packets that the router forwards to your PC will be captured. You'd need to get to the "inner workings" of the router to capture all its packets, and you can't do that from the outside.</p></div><div id="comment-29188-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:19)</span> Jasper ♦♦</div></div><span id="29190"></span><div id="comment-29190" class="comment"><div id="post-29190-score" class="comment-score"></div><div class="comment-text"><p>So is there any option, any filter to get traffic that are traveling in whole network?</p></div><div id="comment-29190-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:30)</span> Beginer</div></div><span id="29191"></span><div id="comment-29191" class="comment"><div id="post-29191-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately not anymore. In the past, when we were using "hubs" you could do that, because the whole network was half duplex and every packet was forwarded on every port. Since we're now on full duplex networks using switches it does not longer work that way. With the only exception of WiFi, of course, because with enough antennas you can capture everything (but not read it probably, because it should be encrypted).</p></div><div id="comment-29191-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:35)</span> Jasper ♦♦</div></div><span id="29192"></span><div id="comment-29192" class="comment"><div id="post-29192-score" class="comment-score"></div><div class="comment-text"><p>So i will not be able to scan whole network. Thanks you've been helpful :)</p></div><div id="comment-29192-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:39)</span> Beginer</div></div><span id="29193"></span><div id="comment-29193" class="comment not_top_scorer"><div id="post-29193-score" class="comment-score"></div><div class="comment-text"><p>Uhm, scanning is not the same as capturing. Scanning is an active process of sending packets to all nodes, while capturing is passive, collecting packets from other nodes. If you need to scan the network for active nodes, ports, etc, you should take a look at nmap. It can scan whole networks (depending on its size, and if you have the time)</p></div><div id="comment-29193-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:43)</span> Jasper ♦♦</div></div><span id="29194"></span><div id="comment-29194" class="comment not_top_scorer"><div id="post-29194-score" class="comment-score"></div><div class="comment-text"><p>Oh so it is not over yet. I think that i expressed wrong, sorry. But i was looking for nmap filter but i didnt find it? Probably i need to create it, am i right?</p></div><div id="comment-29194-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:53)</span> Beginer</div></div><span id="29195"></span><div id="comment-29195" class="comment not_top_scorer"><div id="post-29195-score" class="comment-score"></div><div class="comment-text"><p>nmap is not a filter. It's a tool: <a href="http://nmap.org/">http://nmap.org/</a></p></div><div id="comment-29195-info" class="comment-info"><span class="comment-age">(27 Jan '14, 08:56)</span> Jasper ♦♦</div></div><span id="29196"></span><div id="comment-29196" class="comment not_top_scorer"><div id="post-29196-score" class="comment-score"></div><div class="comment-text"><p>Sorry because i am stupid. I am starting to using wireshark. Thanks for all help you gave me.</p></div><div id="comment-29196-info" class="comment-info"><span class="comment-age">(27 Jan '14, 09:06)</span> Beginer</div></div><span id="29197"></span><div id="comment-29197" class="comment not_top_scorer"><div id="post-29197-score" class="comment-score"></div><div class="comment-text"><p>No problem. Starting on a new topic is always hard. Just don't give up, and you'll get there ;-)</p></div><div id="comment-29197-info" class="comment-info"><span class="comment-age">(27 Jan '14, 09:08)</span> Jasper ♦♦</div></div><span id="29198"></span><div id="comment-29198" class="comment not_top_scorer"><div id="post-29198-score" class="comment-score"></div><div class="comment-text"><p>Thanks, i kinda like to learn more about wireshark. I hope i wont stop because it is probably amazing tool :)</p></div><div id="comment-29198-info" class="comment-info"><span class="comment-age">(27 Jan '14, 09:12)</span> Beginer</div></div></div><div id="comment-tools-29184" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-29184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

