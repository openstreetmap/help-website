+++
type = "question"
title = "How can I follow one conversation/session in a wireshark trace?"
description = '''Hi guys I have trace that I am trying to analyze. It is a bit difficult because we open two connections to the same IP and Port within the same application. So there are two different sockets opening connections on two different threads. We have application logs but they are huge and to try and matc...'''
date = "2012-08-10T03:56:00Z"
lastmod = "2012-08-10T12:22:00Z"
weight = 13536
keywords = [ "tcp", "socket", "trace" ]
aliases = [ "/questions/13536" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How can I follow one conversation/session in a wireshark trace?](/questions/13536/how-can-i-follow-one-conversationsession-in-a-wireshark-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13536-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys</p><p>I have trace that I am trying to analyze. It is a bit difficult because we open two connections to the same IP and Port within the same application. So there are two different sockets opening connections on two different threads. We have application logs but they are huge and to try and match up what was sent from the app logs with wireshark trace is quite difficult from each thread is quite difficult.</p><p>I don't know that much about the TCP/IP stack but I assume that there must be some sort of ID that is associated with each socket otherwise the OS wouldn't know which bytes to forward to which socket in the same application.</p><p>Does this ID show up in the wireshark trace? Is there a way to filter the view so that I can follow a single socket's conversation? If this is true what ID should I use and where can I find it in the trace?</p></div><div id="question-tags" class="tags-container tags">tcp socket trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '12, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/b7760b5831b2deaeaee8daa8aa62a39e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="uriDium&#39;s gravatar image" /><p>uriDium<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="uriDium has no accepted answers">0%</span></p></div></div><div id="comments-container-13536" class="comments-container"></div><div id="comment-tools-13536" class="comment-tools"></div><div class="clear"></div><div id="comment-13536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="13537"></span>

<div id="answer-container-13537" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13537-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Right click a packet of interest and choose "Follow TCP Stream". This will show the stream contents in another window which you can dismiss, and the main display will be filtered to only show packets for the stream you chose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '12, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13537" class="comments-container"></div><div id="comment-tools-13537" class="comment-tools"></div><div class="clear"></div><div id="comment-13537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13544"></span>

<div id="answer-container-13544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13544-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you open the TCP tree in the packet-tree pane, you'll find a field called [Stream index: N] where N is some integer. Wireshark gives each TCP connection its own stream index (the number is incremented each time Wireshark sees a new connection). This field is useful if you want to, for example, filter on only messages for this particular stream.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '12, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-13544" class="comments-container"></div><div id="comment-tools-13544" class="comment-tools"></div><div class="clear"></div><div id="comment-13544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13548"></span>

<div id="answer-container-13548" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13548-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As grahamb said, Follow TCP Stream will give what you want. No, there is no ID that is associated with each socket. The Stream Index is a Wireshark-generated value; it is not actually present in the packet. The OS differentiates between TCP connections solely on the basis of IP addresses and ports. A connection is defined by the IP addresses and port numbers at <em>both ends</em>. You said "...we open two connections to the same IP and port within the same application."</p><p>Ok, both connections may be TO the same IP address and port, but if you examine the captured traffic you will find that they are not both FROM the same port. The system that opens the connections will choose a different dynamic port for each connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '12, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-13548" class="comments-container"><span id="13562"></span><div id="comment-13562" class="comment"><div id="post-13562-score" class="comment-score"></div><div class="comment-text"><p>@Jim. Does this have anything to do with ephemeral ports?</p></div><div id="comment-13562-info" class="comment-info"><span class="comment-age">(12 Aug '12, 01:10)</span> uriDium</div></div><span id="13563"></span><div id="comment-13563" class="comment"><div id="post-13563-score" class="comment-score"></div><div class="comment-text"><p>yes, that is what Jim meant by "dynamic".</p></div><div id="comment-13563-info" class="comment-info"><span class="comment-age">(12 Aug '12, 03:18)</span> Jasper ♦♦</div></div><span id="13567"></span><div id="comment-13567" class="comment"><div id="post-13567-score" class="comment-score"></div><div class="comment-text"><p>Indeed. I first typed "ephemeral" and then changed it to "dynamic" because I find that a lot of people who are new to TCP analysis aren't familiar with the term.</p></div><div id="comment-13567-info" class="comment-info"><span class="comment-age">(12 Aug '12, 10:14)</span> Jim Aragon</div></div></div><div id="comment-tools-13548" class="comment-tools"></div><div class="clear"></div><div id="comment-13548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

