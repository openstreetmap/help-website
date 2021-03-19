+++
type = "question"
title = "How to do capture activity on others PCs in the same network."
description = '''Dear Guys Good Day. The first time use WireShark for testing purpose. I tried setup one of my PC as the Wireshark host which attach to a planet core switch, then other PCs will connect to the core switch as well. I tried to start capture and I can see my host IP address activity like destination IP ...'''
date = "2014-09-30T18:35:00Z"
lastmod = "2014-10-01T01:55:00Z"
weight = 36737
keywords = [ "spying", "pc", "activity" ]
aliases = [ "/questions/36737" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to do capture activity on others PCs in the same network.](/questions/36737/how-to-do-capture-activity-on-others-pcs-in-the-same-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36737-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Guys</p><p>Good Day. The first time use WireShark for testing purpose. I tried setup one of my PC as the Wireshark host which attach to a planet core switch, then other PCs will connect to the core switch as well. I tried to start capture and I can see my host IP address activity like destination IP is where and what is the protocol. However, others PC destination only show the last IP address (192.168.0.255), it won't show where is the actual destination like google IP. Anyone can help me on this? Thanks.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/WireShark_Test.jpg" alt="alt text" /></p><p>JACK</p></div><div id="question-tags" class="tags-container tags">spying pc activity</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '14, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/bcdd814ab092f858cca8e10f5d7763e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JACKJACK&#39;s gravatar image" /><p>JACKJACK<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JACKJACK has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 30 Sep '14, 18:56</p></div></div><div id="comments-container-36737" class="comments-container"></div><div id="comment-tools-36737" class="comment-tools"></div><div class="clear"></div><div id="comment-36737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36748"></span>

<div id="answer-container-36748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36748-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the Wiki page on capturing in a <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">switched</a> network?</p><p>A tap is only necessary if your switches aren't able to span or mirror ports, most managed switches can do this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '14, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36748" class="comments-container"><span id="36768"></span><div id="comment-36768" class="comment"><div id="post-36768-score" class="comment-score"></div><div class="comment-text"><p>Dear Beldum and Grahamb</p><p>Good Day. Thanks for the guide and comment. I configure the morroring in the switched and now work perfectly as I planned. Thanks for the share, I think most of the new WireShark user may face problem like me as have no idea how to setup.</p></div><div id="comment-36768-info" class="comment-info"><span class="comment-age">(01 Oct '14, 20:44)</span> JACKJACK</div></div><span id="36774"></span><div id="comment-36774" class="comment"><div id="post-36774-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb</p><p>Good Day. As per my answer, I successful trace what I want, but I would like to know how to make WireShark show the actual http location and page in the destination rather than display the host? Thanks.</p></div><div id="comment-36774-info" class="comment-info"><span class="comment-age">(01 Oct '14, 23:52)</span> JACKJACK</div></div><span id="36778"></span><div id="comment-36778" class="comment"><div id="post-36778-score" class="comment-score"></div><div class="comment-text"><p>@JACKJACK</p><p>It's not entirely clear to me what your issue is (what is "last address"), but I think you're still having issues with switched capture. As you are now hopefully capturing from a mirrored port on the switch that's connected to your internet access device, and the mirrored port should be the port used for internet access. Then, every packet transmitted to and from the internet will be mirrored onto the capture port. You can simply test this by running ping 8.8.8.8 (Google DNS) on one of the other machines and ensuring you can capture both the ping request and reply. Once you have this working, then you can test accessing a web site.</p></div><div id="comment-36778-info" class="comment-info"><span class="comment-age">(02 Oct '14, 02:07)</span> grahamb ♦</div></div><span id="36780"></span><div id="comment-36780" class="comment"><div id="post-36780-score" class="comment-score"></div><div class="comment-text"><p>grahamb</p><p>Thanks for reply. Yes, I successful setup the device and I can capture all my network point in the network. What I ask is I can see my source IP (Example 192.168.0.100 is one of my network PC) and destination IP (Example 72.52.228.152). On this point, I only can see the destination IP and this IP belong to www.cfwebserver.com. This site host a lot of website domain and mail server. How may I know that my 192.168.0.100 actually visit to which website? Thanks.</p></div><div id="comment-36780-info" class="comment-info"><span class="comment-age">(02 Oct '14, 02:34)</span> JACKJACK</div></div><span id="36781"></span><div id="comment-36781" class="comment"><div id="post-36781-score" class="comment-score"></div><div class="comment-text"><p>As the mirror of the internet port will be showing traffic from all the network PC's, you can add a capture filter to limit the capture to just the PC you're interested in. In the capture options dialog add a capture filter of the form <code>host 192.168.0.100</code> adjusting the ip address as required. If you then only need to see traffic between that network PC and a single website you can extend the filter to include the website address, e.g. <code>host 192.168.0.100 &amp; host 72.52.228.152</code>.</p></div><div id="comment-36781-info" class="comment-info"><span class="comment-age">(02 Oct '14, 02:54)</span> grahamb ♦</div></div></div><div id="comment-tools-36748" class="comment-tools"></div><div class="clear"></div><div id="comment-36748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36738"></span>

<div id="answer-container-36738" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36738-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to have a Tap for your switch to capture traffic of other hosts.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '14, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/4784c5fb1a0142030d51a339706a456c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beldum&#39;s gravatar image" /><p>Beldum<br />
<span class="score" title="49 reputation points">49</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beldum has no accepted answers">0%</span></p></div></div><div id="comments-container-36738" class="comments-container"><span id="36741"></span><div id="comment-36741" class="comment"><div id="post-36741-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. My wireshark version is 1.12.1. Do you mean that I need to add in a script into my core switch?</p></div><div id="comment-36741-info" class="comment-info"><span class="comment-age">(30 Sep '14, 19:39)</span> JACKJACK</div></div><span id="36743"></span><div id="comment-36743" class="comment"><div id="post-36743-score" class="comment-score"></div><div class="comment-text"><p>What I mean is that you would need a full-duplex tap to analyze more than one port on a switch or.....or you can SPAN a port on a switch. The best thing to do would be to just obtain a full-duplex tap.</p></div><div id="comment-36743-info" class="comment-info"><span class="comment-age">(30 Sep '14, 22:23)</span> Beldum</div></div></div><div id="comment-tools-36738" class="comment-tools"></div><div class="clear"></div><div id="comment-36738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

