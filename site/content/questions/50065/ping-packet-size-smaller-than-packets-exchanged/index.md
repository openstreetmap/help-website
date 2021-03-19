+++
type = "question"
title = "ping packet size smaller than packets exchanged"
description = '''hello, I&#x27;m wondering why I&#x27;m not able to ping a remote host with a larger packet size than the MTU allowed on the link (ping remote_host -l 1500 -f). The &quot;f&quot; flag is not allowing fragmentation. So when running the ping command I&#x27;m receiving msg that packets need to be fragmented and this is ok for m...'''
date = "2016-02-10T10:31:00Z"
lastmod = "2016-02-10T10:51:00Z"
weight = 50065
keywords = [ "ping" ]
aliases = [ "/questions/50065" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ping packet size smaller than packets exchanged](/questions/50065/ping-packet-size-smaller-than-packets-exchanged)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50065-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>I'm wondering why I'm not able to ping a remote host with a larger packet size than the MTU allowed on the link (ping remote_host -l 1500 -f). The "f" flag is not allowing fragmentation. So when running the ping command I'm receiving msg that packets need to be fragmented and this is ok for me. But I have a trace file between my laptop and the remote server and I can see both exchange packets up to 6000 bytes in size even though I can see the DF bit flag set as well ....</p><p><img src="https://osqa-ask.wireshark.org/upfiles/length.PNG" alt="alt text" /> Can anyone please explain why is that ?</p><p>BR</p><p>Adam<br />
</p></div><div id="question-tags" class="tags-container tags">ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '16, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 10 Feb '16, 10:39</p></div></div><div id="comments-container-50065" class="comments-container"></div><div id="comment-tools-50065" class="comment-tools"></div><div class="clear"></div><div id="comment-50065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50066"></span>

<div id="answer-container-50066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50066-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably because of this: <a href="https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '16, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50066" class="comments-container"><span id="50067"></span><div id="comment-50067" class="comment"><div id="post-50067-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thank you for the comment. Does it also count when I was simulating on two VMware Workstation VM's? I mean especially the Offloading stuff ?</p><p>BR</p><p>Adam</p></div><div id="comment-50067-info" class="comment-info"><span class="comment-age">(10 Feb '16, 10:58)</span> adasko</div></div><span id="50068"></span><div id="comment-50068" class="comment"><div id="post-50068-score" class="comment-score"></div><div class="comment-text"><p>Whenever you're not using a dedicated capture device you can run into symptoms like oversized packets, crc errors etc.</p></div><div id="comment-50068-info" class="comment-info"><span class="comment-age">(10 Feb '16, 11:03)</span> Jasper ♦♦</div></div><span id="50069"></span><div id="comment-50069" class="comment"><div id="post-50069-score" class="comment-score">1</div><div class="comment-text"><p>dedicated device you mean like a TAP or any device running Wireshark ?</p></div><div id="comment-50069-info" class="comment-info"><span class="comment-age">(10 Feb '16, 11:05)</span> adasko</div></div><span id="50070"></span><div id="comment-50070" class="comment"><div id="post-50070-score" class="comment-score"></div><div class="comment-text"><p>TAP, SPAN, it all works as long as you're not capturing on the device creating the packets ;-)</p></div><div id="comment-50070-info" class="comment-info"><span class="comment-age">(10 Feb '16, 11:06)</span> Jasper ♦♦</div></div><span id="50071"></span><div id="comment-50071" class="comment"><div id="post-50071-score" class="comment-score"></div><div class="comment-text"><p>so it could be even a dedicated laptop with Wireshark on it ? If yes, does the NIC have to specifically configured ?</p></div><div id="comment-50071-info" class="comment-info"><span class="comment-age">(10 Feb '16, 11:07)</span> adasko</div></div><span id="50072"></span><div id="comment-50072" class="comment not_top_scorer"><div id="post-50072-score" class="comment-score"></div><div class="comment-text"><p>yes, a dedicated laptop is enough. It's usually a good idea to disable all protocol bindings from the capture card to prevent it from adding packets to the capture.</p></div><div id="comment-50072-info" class="comment-info"><span class="comment-age">(10 Feb '16, 11:25)</span> Jasper ♦♦</div></div></div><div id="comment-tools-50066" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-50066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

