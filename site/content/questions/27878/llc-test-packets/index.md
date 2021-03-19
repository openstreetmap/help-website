+++
type = "question"
title = "LLC TEST packets?"
description = '''So I noticed in my packet captures that something on the lan is broadcasting LLC TEST packets. I read the 802.2 standard and it sounds like it is essentially a layer 2 PING function and it is required. I thought this is great! I can broadcast an L2 ping and get a reply from every node on the lan, wh...'''
date = "2013-12-06T12:02:00Z"
lastmod = "2013-12-09T07:42:00Z"
weight = 27878
keywords = [ "llc" ]
aliases = [ "/questions/27878" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [LLC TEST packets?](/questions/27878/llc-test-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27878-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I noticed in my packet captures that something on the lan is broadcasting LLC TEST packets. I read the 802.2 standard and it sounds like it is essentially a layer 2 PING function and it is required. I thought this is great! I can broadcast an L2 ping and get a reply from every node on the lan, whether it is running IP or not. Alas, after using scapy to craft and send one, I get no replies.</p><p>So my question is, why am I not getting a reply? Am I misunderstanding the standard or does nobody bother to comply with it? Bonus points if you have any idea why something on the lan is broadcasting these packets that don't seem to work.</p><p>The LLC header decode is:</p><pre><code>DSAP: NULL SSAP: LLC Sub-Layer Management (0x02)
CR Bit: Command
Control Field: U, func=TEST (0xE3)</code></pre><p>Full packet capture <a href="https://drive.google.com/file/d/0ByOQJBpP4bDXWW9QWlZ1SVl0TTA/edit?usp=sharing">here</a></p></div><div id="question-tags" class="tags-container tags">llc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/f8c3cfd457dc8c60b71f0b0e5f7b90b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="psusi&#39;s gravatar image" /><p>psusi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="psusi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '13, 06:58</p></div></div><div id="comments-container-27878" class="comments-container"><span id="27898"></span><div id="comment-27898" class="comment"><div id="post-27898-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to post the full frame in a capture file (Google drive,dropbox, cloudshark.org vor mega.co.nz)?</p></div><div id="comment-27898-info" class="comment-info"><span class="comment-age">(07 Dec '13, 13:24)</span> Kurt Knochner ♦</div></div><span id="27949"></span><div id="comment-27949" class="comment"><div id="post-27949-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner, done.</p></div><div id="comment-27949-info" class="comment-info"><span class="comment-age">(09 Dec '13, 06:59)</span> psusi</div></div></div><div id="comment-tools-27878" class="comment-tools"></div><div class="clear"></div><div id="comment-27878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27951"></span>

<div id="answer-container-27951" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27951-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So my question is, why am I not getting a reply?</p></blockquote><p>Because that feature is (apparently) not widely implemented.</p><blockquote><p>Bonus points if you have any idea why something on the lan is broadcasting these packets</p></blockquote><p>According to the MAC address in the frame, it comes from a device of "<a href="http://www.senao.com/English/">Senao International Co., Ltd.</a>", which builds all kinds of networking devices. Maybe they use LLC TEST for internal purposes (finding other Senao devices or similar).</p><p>You should be able to find the port of that devices by looking at the <a href="http://en.wikipedia.org/wiki/CAM_Table">CAM table</a> of your switch. It will show you the port that device is connected to and then you can 'follow the cables', unless your switch documentation already contains some information about that device ;-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '13, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Dec '13, 07:46</p></div></div><div id="comments-container-27951" class="comments-container"><span id="27952"></span><div id="comment-27952" class="comment"><div id="post-27952-score" class="comment-score"></div><div class="comment-text"><p>Am I misinterpreting the standard though, which seems to say that support for this packet is <em>REQUIRED</em>. I find it hard to believe that nobody bothers to follow a mandatory part of the standard, and what's more, even this Senao device that is sending them doesn't reply to them, which is really weird.</p></div><div id="comment-27952-info" class="comment-info"><span class="comment-age">(09 Dec '13, 08:02)</span> psusi</div></div><span id="27953"></span><div id="comment-27953" class="comment"><div id="post-27953-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Am I misinterpreting the standard though, which seems to say that support for this packet is REQUIRED.</p></blockquote><p>well, I guess it's as always. Some people read the docs differently than others.</p><p>Here is the text from the standard</p><blockquote><p><a href="http://standards.ieee.org/getieee802/download/802.2-1998.pdf">http://standards.ieee.org/getieee802/download/802.2-1998.pdf</a></p></blockquote><p>Cite:</p><pre><code>6.7 Uses of the TEST command PDU and response PDU
....

Implementation of the TEST command PDU is optional but every LLC must be able to respond to a received TEST command PDU with a TEST response PDU. </code></pre><p>To <strong>be able</strong> to respond does not mean it is mandatory to actually respond ;-)) Some devices might <strong>be able to respond</strong> but that feature is disabled by default. Another possibilty: (most) developers stopped reading after the word <strong>optional</strong>.</p><blockquote><p>I find it hard to believe that nobody bothers to follow a mandatory part of the standard,</p></blockquote><p>well, if you look at the history of standards and the rate of fulfillment in the field, you will believe it ;-))</p><blockquote><p>and what's more, even this Senao device that is sending them doesn't reply to them, which is really weird.</p></blockquote><p>There you have it. Even those who use that feature don't implement it fully ;-)) But that's something only the vendor of that device can answer.</p><p>Another possibility would be, that your hand crafted frame (scapy) was bogus. Can you post that as a capture file?</p></div><div id="comment-27953-info" class="comment-info"><span class="comment-age">(09 Dec '13, 08:18)</span> Kurt Knochner ♦</div></div><span id="27971"></span><div id="comment-27971" class="comment"><div id="post-27971-score" class="comment-score"></div><div class="comment-text"><p>@Kurt Knochner, it was identical to the one sent by the Senao device, save for the source MAC address, which I switched to my own.</p></div><div id="comment-27971-info" class="comment-info"><span class="comment-age">(10 Dec '13, 06:42)</span> psusi</div></div><span id="27972"></span><div id="comment-27972" class="comment"><div id="post-27972-score" class="comment-score"></div><div class="comment-text"><p>So, do you get a TEST <strong>answer</strong> now?</p><p>EDIT: I misunderstood your answer. Never mind...</p></div><div id="comment-27972-info" class="comment-info"><span class="comment-age">(10 Dec '13, 06:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27951" class="comment-tools"></div><div class="clear"></div><div id="comment-27951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

