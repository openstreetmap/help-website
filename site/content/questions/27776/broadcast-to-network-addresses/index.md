+++
type = "question"
title = "broadcast to network addresses"
description = '''appology for my previous mail..the pad got messed up here is the trace.  Can someone explain it to me please??  I dont undrestand why the reply from the server is an ip broadcast and at the same time as hardware broadcast 255.255.255.255 Many thanks '''
date = "2013-12-04T14:06:00Z"
lastmod = "2013-12-04T14:19:00Z"
weight = 27776
keywords = [ "udp" ]
aliases = [ "/questions/27776" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [broadcast to network addresses](/questions/27776/broadcast-to-network-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27776-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>appology for my previous mail..the pad got messed up here is the trace. Can someone explain it to me please?? I dont undrestand why the reply from the server is an ip broadcast and at the same time as hardware broadcast 255.255.255.255</p><p>Many thanks</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled_2.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '13, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/4518ebe112bd749fa7a1deb5b50db9b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehran&#39;s gravatar image" /><p>Mehran<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehran has no accepted answers">0%</span></p></img></div></div><div id="comments-container-27776" class="comments-container"></div><div id="comment-tools-27776" class="comment-tools"></div><div class="clear"></div><div id="comment-27776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27779"></span>

<div id="answer-container-27779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27779-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>a quick google search (I'm sure you did that too!!) reveals, that the ports 6666 and 6667 with multicast traffic are related to the <a href="http://www.symantec.com/business/support/index?page=content&amp;id=TECH110226">Symantec Ghostcast server</a> (system imaging/backup). So, if you are using that software in your company, don't care about those packets, as they are 'normal'.</p><blockquote><p>I dont undrestand why the reply from the server is an ip broadcast</p></blockquote><p>I don't understand it either, but that's also normal, as I don't know the product and hence I have no idea what they (Symantec) are doing in their protocol. I think this would be a perfect question for their support people ;-))</p><blockquote><p>appology for my previous mail..</p></blockquote><p>No problem. I deleted your other question.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27779" class="comments-container"><span id="27780"></span><div id="comment-27780" class="comment"><div id="post-27780-score" class="comment-score"></div><div class="comment-text"><p>Port 6666 and 6667 is used by an application where devices find each other. Basically the client hook up to the device which is operates in two parts. A WEB server and streamer.</p></div><div id="comment-27780-info" class="comment-info"><span class="comment-age">(04 Dec '13, 14:21)</span> Mehran</div></div><span id="27781"></span><div id="comment-27781" class="comment"><div id="post-27781-score" class="comment-score"></div><div class="comment-text"><p>So, this is not Symantec Ghostcast?</p><blockquote><p>used by an application where devices find each other.</p></blockquote><p>Is it your product, did you develop it?</p><blockquote><p>A WEB server and streamer.</p></blockquote><p>why did they (whoever developed the application) choose <strong>UDP</strong> for a <strong>web</strong> server?</p><blockquote><p>I dont undrestand why the reply from the server is an ip broadcast and at the same time as hardware broadcast 255.255.255.255</p></blockquote><p>That's a question, only the developer of that software/application/device can answer, as there is nothing network related (I know of) that would cause such a behavior.</p><p>If you have <strong>any</strong> information about the products/software used, please post it here, otherwise we can only speculate.</p></div><div id="comment-27781-info" class="comment-info"><span class="comment-age">(04 Dec '13, 14:23)</span> Kurt Knochner ♦</div></div><span id="27782"></span><div id="comment-27782" class="comment"><div id="post-27782-score" class="comment-score"></div><div class="comment-text"><p>Well guys I think I figured it out!!! This part of the program dicover all embedded devices on the network even if they have a different IP address than 192.168.1.xx<br />
The 192.168.1.255 get the respond from 192.168.1.xx while 255.255.255.255 gets all others. remember the client application is listenning to the port 6666 while all other devices are on 6667.</p><p>Kurt thanks for your attempt mate.</p></div><div id="comment-27782-info" class="comment-info"><span class="comment-age">(04 Dec '13, 14:40)</span> Mehran</div></div></div><div id="comment-tools-27779" class="comment-tools"></div><div class="clear"></div><div id="comment-27779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

