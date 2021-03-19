+++
type = "question"
title = "Wireshark Win 7 x64 not showing incoming frames over 1518 bytes size despite of big MTU"
description = '''I have changed the MTU to 1600 and do several tests with different setups. I get to capture and see in Wireshark &quot;big&quot; outgoing frames (i.e. 1600 bytes) but fail to see incoming &quot;big&quot; frames, despite I am totally certain those frames get the network adapter. Any help would be very much appreciated. '''
date = "2013-04-11T02:25:00Z"
lastmod = "2013-04-11T05:49:00Z"
weight = 20310
keywords = [ "jumbo", "windows7", "jumboframes", "mtu" ]
aliases = [ "/questions/20310" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Win 7 x64 not showing incoming frames over 1518 bytes size despite of big MTU](/questions/20310/wireshark-win-7-x64-not-showing-incoming-frames-over-1518-bytes-size-despite-of-big-mtu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have changed the MTU to 1600 and do several tests with different setups. I get to capture and see in Wireshark "big" outgoing frames (i.e. 1600 bytes) but fail to see incoming "big" frames, despite I am totally certain those frames get the network adapter.</p><p>Any help would be very much appreciated.</p></div><div id="question-tags" class="tags-container tags">jumbo windows7 jumboframes mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/479b7e7979023e976f3429d7b5d7f735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JAVIER&#39;s gravatar image" /><p>JAVIER<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JAVIER has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '13, 07:27</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-20310" class="comments-container"><span id="20323"></span><div id="comment-20323" class="comment"><div id="post-20323-score" class="comment-score"></div><div class="comment-text"><p>What is your NIC brand and modell?</p></div><div id="comment-20323-info" class="comment-info"><span class="comment-age">(11 Apr '13, 03:37)</span> Kurt Knochner ♦</div></div><span id="20327"></span><div id="comment-20327" class="comment"><div id="post-20327-score" class="comment-score"></div><div class="comment-text"><p>Intel 82577LC Gigabit Network Connection</p></div><div id="comment-20327-info" class="comment-info"><span class="comment-age">(11 Apr '13, 04:18)</span> JAVIER</div></div></div><div id="comment-tools-20310" class="comment-tools"></div><div class="clear"></div><div id="comment-20310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20332"></span>

<div id="answer-container-20332" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20332-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Intel 82577LC Gigabit Network Connection</p></blockquote><p>Can you please follow the instructions of a guy who also had problems with same NIC and with Jumbo frames.</p><blockquote><p><code>http://forum.notebookreview.com/sony/565138-vpc-z1-jumbo-frames.html</code><br />
</p></blockquote><p>First: Please change (or check) the registry value mentioned in the post (then reboot).<br />
Second: Don't use a docking station (if you do now)! That solved the problem for the other guy.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20332" class="comments-container"><span id="20335"></span><div id="comment-20335" class="comment"><div id="post-20335-score" class="comment-score"></div><div class="comment-text"><p>Eureka!</p><p>Just follow the instructions and finally get Jumbo Frames incoming !!</p><p>To summarize my conclusions and experience:</p><p>1) By changing mtu at Win7 "netsh" context level ("netsh int ipv4 set subint &lt;interface name=""&gt; mtu=xxxx") I got just only Jumbo Frames outgoing capability, the laptop was able to send large frames, but not large incoming frames were displayed.</p><p>2) By changing the NIC Jumbo Frames capability at Win 7registry level (according to your instructions), the laptop finally got Jumbo frames incoming capability, I just got to display incoming large frames!. Notice that "*JumboPacket" entry was not present and I had to create it in the registry.</p><p>Thanks a lot</p><p>Kind regards</p></div><div id="comment-20335-info" class="comment-info"><span class="comment-age">(11 Apr '13, 06:42)</span> JAVIER</div></div><span id="20336"></span><div id="comment-20336" class="comment"><div id="post-20336-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thanks a lot</p></blockquote><p>You're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-20336-info" class="comment-info"><span class="comment-age">(11 Apr '13, 07:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-20332" class="comment-tools"></div><div class="clear"></div><div id="comment-20332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20311"></span>

<div id="answer-container-20311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20311-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where are you capturing? On the device that is sending the packets? Have you disabled offloading capabilities in your NIC? Otherwise you might just see large chunks of data that gets segmented on the card.</p><p>Also, your switch may drop "oversized" packets unless it is configured to work with Jumbo frames, which means that your packets may leave your PC but they will not get to the destination, and there will not be any reply. Even IF there would be a reply, the switch could drop the frames again for being "oversized".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '13, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-20311" class="comments-container"><span id="20322"></span><div id="comment-20322" class="comment"><div id="post-20322-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jasper for your promptly answer.</p><p>I have tried lot of setups and different options.</p><p>In order to discard some dropping in the intermediate path, finally I tested two Win7 1600 mtu laptops directly connected, with the same results. Both laptops send "big frames" and display it perfectly in Wireshark (I am certain they send big frames as I got to trace them in a intermediate router in a different setup), but fail to ¿capture? and display in Wireshark incoming big frames that get their network adapters.</p><p>I have disable all offloading related options in NIC capabilites with the same result.</p></div><div id="comment-20322-info" class="comment-info"><span class="comment-age">(11 Apr '13, 03:27)</span> JAVIER</div></div></div><div id="comment-tools-20311" class="comment-tools"></div><div class="clear"></div><div id="comment-20311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

