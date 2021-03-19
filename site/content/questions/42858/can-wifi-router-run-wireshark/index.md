+++
type = "question"
title = "Can Wifi router run Wireshark?"
description = '''Hi, New to Wireshark. I would like to capture network packets on my own home network for educational purpose. I&#x27;ve read that you could install wireshark on the Wifi router itself that powered by either DD-WRT or OpenWRT firmware. So, you don&#x27;t need another client to capture packets. However, I can&#x27;t...'''
date = "2015-06-03T13:47:00Z"
lastmod = "2015-06-05T05:47:00Z"
weight = 42858
keywords = [ "router", "wifi", "wireshark" ]
aliases = [ "/questions/42858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wifi router run Wireshark?](/questions/42858/can-wifi-router-run-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42858-score" class="post-score" title="current number of votes">0</div><span id="post-42858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, New to Wireshark.</p><p>I would like to capture network packets on my own home network for educational purpose. I've read that you could install wireshark on the Wifi router itself that powered by either DD-WRT or OpenWRT firmware. So, you don't need another client to capture packets. However, I can't find any detailed tutorial on this. If anybody can provide these info:</p><p>a) Is there any way for the router to do it's primary job (provide wifi connection to clients), and capturing packets at the same time?</p><p>b) How about promiscuous mode?</p><p>c) Are SD card and USB drive good enough for the storage?</p><p>d) If I schedule to run wireshark 6 hours a day at around 200kbps data average, will this setup put too much load to the wifi router?</p><p>e) Is there any consumer grade wifi router that is capable to do this setup? Can you recommend some?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '15, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/98b8a594eff74cfcf0be8c81d23242b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrafalgarLaw&#39;s gravatar image" /><p><span>TrafalgarLaw</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrafalgarLaw has no accepted answers">0%</span></p></div></div><div id="comments-container-42858" class="comments-container"></div><div id="comment-tools-42858" class="comment-tools"></div><div class="clear"></div><div id="comment-42858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42862"></span>

<div id="answer-container-42862" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42862-score" class="post-score" title="current number of votes">0</div><span id="post-42862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The real benefit of Wireshark is the GUI and what you can do therein. However, you won't be able to use the GUI version of Wireshark on the router, so there is no benefit for you to have Wireshark on DD-WRT or OpenWRT. I would do the capturing on the router with tcpdump and the analysis on Windows/MacOS/Linux. tcpdump is available on any Unix like system, which includes DD-WRT and OpenWRT.</p><p>To answer your questions:</p><p>a.) Sure, any multitasking OS is able to do that, which includes *WRT.<br />
b.) No problem for *WRT<br />
c.) Depends on the amount of data you'll have to write per second, as the write rate is rather low for those storage devices.<br />
d.) usually no, but it depends on the overall load and the system parameters (CPU, RAM, etc.)<br />
e.) recommend? No, but I can tell you, what I'm using: Netgear WNDR 3700/3800 plus some TP-Link routers to run DD-WRT and/or OpenWRT and/or Gargoyle (if you like the simple one).<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-42862" class="comments-container"><span id="42863"></span><div id="comment-42863" class="comment"><div id="post-42863-score" class="comment-score"></div><div class="comment-text"><blockquote><p>However, you won't be able to use the GUI version of Wireshark on the router</p></blockquote><p>(Unless you have the X11 client library, and GTK+/Qt and the libraries they depend on, installed on the router, and ensure that when you run Wireshark the DISPLAY environment is set to point to the X server on your desktop machine. Whether you will be able to fit all that software on the router is another matter, and we can't really help much with such a significant project. I'd follow Kurt's suggestions instead.)</p></div><div id="comment-42863-info" class="comment-info"><span class="comment-age">(03 Jun '15, 15:44)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="42864"></span><div id="comment-42864" class="comment"><div id="post-42864-score" class="comment-score"></div><div class="comment-text"><p>Sure X11 DISPLAY forwarding would work, but I doubt that X11 is available for DD-WRT and/or OpenWRT. Although I did not check yet, it would just not make much sense to have X11 on those devices.</p></div><div id="comment-42864-info" class="comment-info"><span class="comment-age">(03 Jun '15, 15:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42886"></span><div id="comment-42886" class="comment"><div id="post-42886-score" class="comment-score"></div><div class="comment-text"><p>Thanks, and which interface wireshark/tcpdump should listen to? I believe the router itself decodes wireless packets and sending them to dsl phone line output, can we tap at this point? Thanks again!</p></div><div id="comment-42886-info" class="comment-info"><span class="comment-age">(04 Jun '15, 07:12)</span> <span class="comment-user userinfo">TrafalgarLaw</span></div></div><span id="42887"></span><div id="comment-42887" class="comment"><div id="post-42887-score" class="comment-score"></div><div class="comment-text"><p>You have a DSL modem. DD-WRT does not work on DSL modems: <a href="http://www.flashrouters.com/blog/2015/02/03/best-options-for-using-vpn-ddwrt-with-modem-router-combo/">http://www.flashrouters.com/blog/2015/02/03/best-options-for-using-vpn-ddwrt-with-modem-router-combo/</a></p></div><div id="comment-42887-info" class="comment-info"><span class="comment-age">(04 Jun '15, 09:02)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="42926"></span><div id="comment-42926" class="comment"><div id="post-42926-score" class="comment-score"></div><div class="comment-text"><p>As <span></span><span>@Amato_C</span> said: There is no (easy) way to run a custom linux on a router with inbuilt DSL modem. So, your options are:</p><ul><li>Capture the wifi/wlan traffic: <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></li><li>Place a cheap wifi/wlan router in front of your DSL router and let it do wireless. Then you can capture everything on the router interface that's cconnected to you DSL router.</li></ul><pre><code>    client -- wlan --- cheap router with *WRT --- ethernet --- DSL Router --- Internet</code></pre><p>Regards<br />
Kurt</p></div><div id="comment-42926-info" class="comment-info"><span class="comment-age">(05 Jun '15, 05:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-42862" class="comment-tools"></div><div class="clear"></div><div id="comment-42862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

