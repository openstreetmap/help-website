+++
type = "question"
title = "analyse traffic between the Internet Service Provider and my Firewall"
description = '''Hello  I would like to analyse traffic between the Internet Service Providen and my Firewall. Is there a way to analyse PPPoE of VDSL-lines with Wireshark? Thank you in advance for every feedback! Joe PS An other challenge will be how to capture VDSL/PPPoE-traffic.... If somebody can give me an advi...'''
date = "2015-12-17T08:20:00Z"
lastmod = "2016-03-02T03:23:00Z"
weight = 48614
keywords = [ "vdsl", "pppoe" ]
aliases = [ "/questions/48614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [analyse traffic between the Internet Service Provider and my Firewall](/questions/48614/analyse-traffic-between-the-internet-service-provider-and-my-firewall)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48614-score" class="post-score" title="current number of votes">0</div><span id="post-48614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I would like to analyse traffic between the Internet Service Providen and my Firewall. Is there a way to analyse PPPoE of VDSL-lines with Wireshark?</p><p>Thank you in advance for every feedback!</p><p>Joe</p><p>PS An other challenge will be how to capture VDSL/PPPoE-traffic.... If somebody can give me an advice.. i would appreciate that very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vdsl" rel="tag" title="see questions tagged &#39;vdsl&#39;">vdsl</span> <span class="post-tag tag-link-pppoe" rel="tag" title="see questions tagged &#39;pppoe&#39;">pppoe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '15, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/c08acf577aad3b14e932ee8f48cf7d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph123&#39;s gravatar image" /><p><span>joseph123</span><br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph123 has no accepted answers">0%</span></p></div></div><div id="comments-container-48614" class="comments-container"></div><div id="comment-tools-48614" class="comment-tools"></div><div class="clear"></div><div id="comment-48614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48618"></span>

<div id="answer-container-48618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48618-score" class="post-score" title="current number of votes">0</div><span id="post-48618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It all depends on your goal and budget.</p><p>From what you write I suppose that your device is an all-in-one, with VDSL uplink and LAN ports on the other end, with a firewall in between.</p><p>Any hardware allowing you to connect to the VDSL line to feed <a href="http://gnuradio.org">GNU radio</a> with raw data will be much more expensive than a replacement of that box if you suspect the box to be faulty, and you'd probably need a really powerful hardware to do the demodulation in real time.</p><p>If you need to prove something to your ISP, your best bet might be an all-in-one VDSL box which can be flashed with <a href="https://openwrt.org/">OpenWRT</a>. If you are really lucky, your existing box is supported. In an OpenWRT device you <em>might</em> be able to reach the PPPoE without the VDSL (with no hands-on experience I cannot be sure about it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48618" class="comments-container"><span id="50611"></span><div id="comment-50611" class="comment"><div id="post-50611-score" class="comment-score"></div><div class="comment-text"><p>Hello</p><p>Thank you very much for that interesting feedback about GNU Radio. I do have some additional questions:</p><ul><li><p>what throughput can be expected with such an approach (e.g. with an Ettus Research USRP)?</p></li><li><p>is a single board able to support/convert all protocols like ADSL, ADSL2, VDSL and VDSL2?</p></li><li><p>does such a solution not drop any packets, i really need to be able to capurte infos of all 7 OSI-layers?</p></li></ul><p>Any feedback is appreciated very much! Thank you!</p><p>Joe</p></div><div id="comment-50611-info" class="comment-info"><span class="comment-age">(01 Mar '16, 08:52)</span> <span class="comment-user userinfo">joseph123</span></div></div><span id="50616"></span><div id="comment-50616" class="comment"><div id="post-50616-score" class="comment-score"></div><div class="comment-text"><p>We are getting quite far from the scope of this site. Also, I never did anything with GNU radio myself, so I cannot tell you much about the details. You would need to be able to demodulate OFDM. VDSL2 can use maximum frequency band of 30 MHz for a 200 Mbit/s downlink speed, that would require 60 MS/s flow between the USRP and your host. The board description says you can send up to 50 MS/s over a GigE, so we have the first bottleneck. For the 18 MHz band used for 100 Mbit/s downlink speed, 26 MS/s should be enough. Your CPU might be capable of doing the OFDM demodulation of these samples, but I have no idea about the algorithm complexity. Through arranging the demodulated slow bit streams the proper way, you should directly get two aggregated bit streams carrying the PPPoE frames.</p><p>As for the various xDSL protocols, it depends on you how many demodulation algorithms you decide to implement. The board will give you a stream of samples and the rest depends on your software.</p><p>Regarding "no packets dropped" - you'll see how much reserve your PC has while demodulating, and that should tell you whether you are surfing the edge or whether you have some reserve and so it should be able to capture continuously, i.e. with no losses.</p></div><div id="comment-50616-info" class="comment-info"><span class="comment-age">(01 Mar '16, 10:14)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50650"></span><div id="comment-50650" class="comment"><div id="post-50650-score" class="comment-score"></div><div class="comment-text"><p>36 MS/s for 18 MHz bandwidth of course, excuse my typo.</p><p>The E110 has an on-board DSP but its Ethernet interface is only a 100 Mbit/s one so you would be unable to capture above 100 Mbit of summary downlink + uplink traffic even if you would use the board's CPU and DSP for the complete VDSL demodulation and send out only the recovered packets.</p></div><div id="comment-50650-info" class="comment-info"><span class="comment-age">(02 Mar '16, 03:23)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48618" class="comment-tools"></div><div class="clear"></div><div id="comment-48618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

