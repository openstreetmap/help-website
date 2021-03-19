+++
type = "question"
title = "Remote capture"
description = '''Does wireshark have the capability to use remote capture agents in order to get an n-tier view of network traffic? i.e Client-&amp;gt; Web Server-&amp;gt; App server-&amp;gt; DB Server -&amp;gt; Mainframe... There are a number of non-Opensource tools that do this very well (Compuwares GTTA product is particularly g...'''
date = "2013-12-04T06:02:00Z"
lastmod = "2014-04-09T13:33:00Z"
weight = 27763
keywords = [ "capture", "remote", "packet" ]
aliases = [ "/questions/27763" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capture](/questions/27763/remote-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27763-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does wireshark have the capability to use remote capture agents in order to get an n-tier view of network traffic? i.e Client-&gt; Web Server-&gt; App server-&gt; DB Server -&gt; Mainframe... There are a number of non-Opensource tools that do this very well (Compuwares GTTA product is particularly good in this area.) It would be cool if you could do similar with Wireshark.(Or maybe you already can?)</p></div><div id="question-tags" class="tags-container tags">capture remote packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '13, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/ea7b0486afca4390bad74593972a2022?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ian%20Molyneaux&#39;s gravatar image" /><p>Ian Molyneaux<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ian Molyneaux has no accepted answers">0%</span></p></div></div><div id="comments-container-27763" class="comments-container"></div><div id="comment-tools-27763" class="comment-tools"></div><div class="clear"></div><div id="comment-27763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27764"></span>

<div id="answer-container-27764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27764-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can do that, e.g. when using the rpcapd capture daemon. If you open the capture options and click on the "Manage Interfaces" button you can see that there is a tab for remote interface configuration, where you can configure the details of the remote capture PC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27764" class="comments-container"><span id="31681"></span><div id="comment-31681" class="comment"><div id="post-31681-score" class="comment-score"></div><div class="comment-text"><p>How do i capture the traffic from my client on a network that this IP range different from mine?</p><p>currently I communicate with him through the VPN network.</p><p>can help me please?</p></div><div id="comment-31681-info" class="comment-info"><span class="comment-age">(09 Apr '14, 12:35)</span> jsilva</div></div></div><div id="comment-tools-27764" class="comment-tools"></div><div class="clear"></div><div id="comment-27764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31683"></span>

<div id="answer-container-31683" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31683-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does wireshark have the capability to use remote capture agents</p></blockquote><p>yes, as @Jasper said, with rpcapd (part of WinPcap). rpcapd works on Linux as well (maybe also UNIX/*BSD), if you compile it from source. Please don't expect to get a rock stable, production quality tool, as it is not. It works, but ....</p><blockquote><p>in order to get an n-tier view of network traffic? i.e Client-&gt; Web Server-&gt; App server-&gt; DB Server -&gt; Mainframe...</p></blockquote><p>Well, Wireshark isn't necessarily the right tool for that kind of approach. Yes, you could probably build something similar with rpcapd, but I would'nt do it.</p><p>Wireshark is superior for <strong>manual capture file analysis</strong>, but there are better tools to build a whole capturing infrastructure, with capture file indexing, archiving, etc.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31683" class="comments-container"></div><div id="comment-tools-31683" class="comment-tools"></div><div class="clear"></div><div id="comment-31683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

