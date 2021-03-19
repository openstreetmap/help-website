+++
type = "question"
title = "Wireshark suddenly stops"
description = '''When I run wireshark it stops at random times telling me: The network adapter on which the capture was being done is no longer running; the capture has stopped. tshark just exists without any message. Some more context:  I am running linux. I am trying to capture wifi in monitor mode with a usb wifi...'''
date = "2017-07-02T07:20:00Z"
lastmod = "2017-07-05T00:11:00Z"
weight = 62466
keywords = [ "capture-setup" ]
aliases = [ "/questions/62466" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark suddenly stops](/questions/62466/wireshark-suddenly-stops)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62466-score" class="post-score" title="current number of votes">0</div><span id="post-62466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run wireshark it stops at random times telling me: The network adapter on which the capture was being done is no longer running; the capture has stopped.</p><p>tshark just exists without any message.</p><p>Some more context:</p><ul><li>I am running linux.</li><li>I am trying to capture wifi in monitor mode with a usb wifi dongle.</li><li>I have checked dmesg and syslog and kern.log but couldn't find anything except information that the device was entering and leaving promiscuous mode.</li></ul><p>Does anybody have an idea what the problem might be or how to debug?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '17, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/fe16a31076f182a20808a52cc4b76217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monkeybusiness&#39;s gravatar image" /><p><span>Monkeybusiness</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monkeybusiness has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Jul '17, 02:19</strong> </span></p></div></div><div id="comments-container-62466" class="comments-container"><span id="62467"></span><div id="comment-62467" class="comment"><div id="post-62467-score" class="comment-score"></div><div class="comment-text"><p>This usually happens when the network card loses its link. Can you check if that was the case? And if not, try to capture with dumpcap instead of tshark to check if it's related to packet decodings?</p></div><div id="comment-62467-info" class="comment-info"><span class="comment-age">(02 Jul '17, 08:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="62468"></span><div id="comment-62468" class="comment"><div id="post-62468-score" class="comment-score"></div><div class="comment-text"><p>Ah, maybe I should have mentioned: I'm capping wifi!</p></div><div id="comment-62468-info" class="comment-info"><span class="comment-age">(02 Jul '17, 09:43)</span> <span class="comment-user userinfo">Monkeybusiness</span></div></div><span id="62469"></span><div id="comment-62469" class="comment"><div id="post-62469-score" class="comment-score"></div><div class="comment-text"><p>If you are not capturing in monitoring mode, it could well be that the network card loses association with the AP for a while, which has similar consequences like cable disconnection for wired interfaces, but it is just a wild guess.</p></div><div id="comment-62469-info" class="comment-info"><span class="comment-age">(02 Jul '17, 09:54)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62470"></span><div id="comment-62470" class="comment"><div id="post-62470-score" class="comment-score"></div><div class="comment-text"><p>I am capturing in monitor mode.</p></div><div id="comment-62470-info" class="comment-info"><span class="comment-age">(02 Jul '17, 15:06)</span> <span class="comment-user userinfo">Monkeybusiness</span></div></div><span id="62471"></span><div id="comment-62471" class="comment"><div id="post-62471-score" class="comment-score"></div><div class="comment-text"><p>Assuming your on Linux, use dmesg and other system logs. You can get the status of the interface with iw dev, iwconfig, and ifconfig.</p><p>With no logs, no OS noted, and no hardware description, it's very difficult to help you.</p></div><div id="comment-62471-info" class="comment-info"><span class="comment-age">(02 Jul '17, 17:05)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="62487"></span><div id="comment-62487" class="comment not_top_scorer"><div id="post-62487-score" class="comment-score"></div><div class="comment-text"><p>@bobjones I added some more context</p></div><div id="comment-62487-info" class="comment-info"><span class="comment-age">(03 Jul '17, 23:54)</span> <span class="comment-user userinfo">Monkeybusiness</span></div></div></div><div id="comment-tools-62466" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-62466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62513"></span>

<div id="answer-container-62513" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62513-score" class="post-score" title="current number of votes">0</div><span id="post-62513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The extremely lame result of trying further is that I think some network manager or similar was interfering.</p><p>If you have the same problem:</p><ul><li>The guide at <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a> has a section on how to set the interface to manual mode which, I assume, means that the network manager will leave it alone.</li><li>Also note that airmon-ng will tell you which running processes might be problematic so at least for debugging you could try killing them all and see if that solves the problem.</li></ul><p>Somebody also warned me that for USB devices it might be a power problem and it might help to try with an externally powered hub. Not relevant for me, but maybe for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '17, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/fe16a31076f182a20808a52cc4b76217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monkeybusiness&#39;s gravatar image" /><p><span>Monkeybusiness</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monkeybusiness has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jul '17, 00:12</strong> </span></p></div></div><div id="comments-container-62513" class="comments-container"></div><div id="comment-tools-62513" class="comment-tools"></div><div class="clear"></div><div id="comment-62513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

