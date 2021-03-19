+++
type = "question"
title = "capture traffic of all devices that connected to a broadband modem"
description = '''how to capture traffic of all devices that connected to a broadband modem with wireshark? or how to capture a adsl broadband modem?'''
date = "2015-12-02T03:38:00Z"
lastmod = "2015-12-03T08:34:00Z"
weight = 48184
keywords = [ "broadband", "modem" ]
aliases = [ "/questions/48184" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture traffic of all devices that connected to a broadband modem](/questions/48184/capture-traffic-of-all-devices-that-connected-to-a-broadband-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48184-score" class="post-score" title="current number of votes">0</div><span id="post-48184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to capture traffic of all devices that connected to a broadband modem with wireshark? or how to capture a adsl broadband modem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadband" rel="tag" title="see questions tagged &#39;broadband&#39;">broadband</span> <span class="post-tag tag-link-modem" rel="tag" title="see questions tagged &#39;modem&#39;">modem</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/c1162b9898f26cde7a9774225e2078db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kj_saeid&#39;s gravatar image" /><p><span>kj_saeid</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kj_saeid has no accepted answers">0%</span></p></div></div><div id="comments-container-48184" class="comments-container"></div><div id="comment-tools-48184" class="comment-tools"></div><div class="clear"></div><div id="comment-48184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48191"></span>

<div id="answer-container-48191" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48191-score" class="post-score" title="current number of votes">1</div><span id="post-48191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the devices are connected to the broadband modem using Ethernet ports of the modem, try to use <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_machine-in-the-middle">these instructions</a>. It is very likely that you will need additional hardware, unless your modem is running OpenWrt or some similar linux-based firmware allowing you to run tcpdump directly on it.</p><p>If some questions still remain after reading the instructions, come back here and press "add a comment" to this answer to enter your additional questions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48191" class="comments-container"><span id="48219"></span><div id="comment-48219" class="comment"><div id="post-48219-score" class="comment-score"></div><div class="comment-text"><p>thans for your answer, but please see this picture's link and answer how to capture traffic between wireless modem and ISP and between client and wireless modem with system that wireshark installed on?</p><p><a href="https://osqa-ask.wireshark.org/upfiles/pic_mYkGwoC.jpg">https://osqa-ask.wireshark.org/upfiles/pic_mYkGwoC.jpg</a></p><p>thank you</p></div><div id="comment-48219-info" class="comment-info"><span class="comment-age">(03 Dec '15, 03:01)</span> <span class="comment-user userinfo">kj_saeid</span></div></div><span id="48224"></span><div id="comment-48224" class="comment"><div id="post-48224-score" class="comment-score"></div><div class="comment-text"><p>First of all, "wireless something" can be quite confusing.</p><p>A "wireless access point" normally describes an equipment to which "wireless clients" talk using IEEE 802.11 family of protocols, popularly known as "WiFi".</p><p>On the contrary, a "wireless modem" typically means an equipment which allows to connect your PC to the internet using a public mobile network and its air interface (the 2G/3G/4G, EDGE, HSPA, LTE etc. acronyms are relevant here).</p><p>Your picture suggests that when using the term "wireless", you are talking solely about WiFi and do not have in mind the 2G/3G/4G mobile network.</p><p>Supposing this is true, you can use a WiFi card capable of "monitoring mode" to analyse communication between the PCs and the access point. Everything what could ever be said about the subject has already been said <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">here</a>.</p><p>When it comes to capturing the communication between the ISP and your box in the middle of your picture, it becomes much harder. Basically, no interfaces capable of receiving the signal which is used on the cable towards the ISP are available at an ordinary PC (regardless whether it is a "cable modem", which is a name usually used for modems connected to coaxial network used for Cable TV distribution, or an "xDSL modem", which is a name usually used for modems connected to twisted pair network used for telephony service). So if your cable modem and your WiFi access point are actually two separate boxes, you could capture on the Ethernet cable connecting them, using the methods described in the link in my initial answer. If it is an "all-in-one" box, you may still be able to capture "almost at the cable" if the box can be flashed with OpenWrt. Or replacement of the all-in-one box with two separate ones may be an option.</p><p>And if you really feel brave, you may try <a href="http://gnuradio.org">the GNU radio project</a> to connect to the cable and demodulate and decode the signal running there. But such approach requires a specific hardware (typically, a USB TV tuner) and basic skills in electronics allowing you to connect this hardware in parallel to the cable.</p></div><div id="comment-48224-info" class="comment-info"><span class="comment-age">(03 Dec '15, 05:36)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48236"></span><div id="comment-48236" class="comment"><div id="post-48236-score" class="comment-score"></div><div class="comment-text"><p>thank you very much :))</p></div><div id="comment-48236-info" class="comment-info"><span class="comment-age">(03 Dec '15, 08:34)</span> <span class="comment-user userinfo">kj_saeid</span></div></div></div><div id="comment-tools-48191" class="comment-tools"></div><div class="clear"></div><div id="comment-48191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

