+++
type = "question"
title = "Is wireshark suitable to debug a crashing modem?"
description = '''Hello, I&#x27;m trying to understand if Wireshark could be useful for my issue (I&#x27;m computer literate, but a newbie at diagnosing network issues). For the past year and a half, my ISP-provided modem (500Mbps/50Mbps - Cable connection in Switzerland, DOCSIS 3.0) has been crashing several times a day. It s...'''
date = "2017-06-02T13:17:00Z"
lastmod = "2017-06-07T02:52:00Z"
weight = 61753
keywords = [ "troubleshooting", "cable_modem" ]
aliases = [ "/questions/61753" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is wireshark suitable to debug a crashing modem?](/questions/61753/is-wireshark-suitable-to-debug-a-crashing-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61753-score" class="post-score" title="current number of votes">0</div><span id="post-61753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to understand if Wireshark could be useful for my issue (I'm computer literate, but a newbie at diagnosing network issues). For the past year and a half, my ISP-provided modem (500Mbps/50Mbps - Cable connection in Switzerland, DOCSIS 3.0) has been crashing several times a day. It soft resets by itself at random times and cuts the connection for three minutes, the boot-up time. Sometimes once a day, sometimes (like today) 7. Modem has been replaced twice, ISP support said that the culprit might be my router (Netgear R7000) and that I should use the router functions of the modem instead of running it as modem-only. This is a no-go because the ISP modem/router is lacking several functions. So, while being reluctant, I finally gave them the benefit of the doubt and replaced my router with a new one (Synology rt2600ac). As I suspected, the problem still occurs. So I imagine there could be a device on my network that somehow triggers the issue on the modem (which by the way happens also in the middle of the night, when no-one in the family is active)</p><p>Therefore, I wonder if Wireshark is ok to diagnose this kind of problem. My idea is to cross-check the times when the outage occurs with a wireshark log and maybe find some common denominator to isolate the faulty device, if any (I still believe it's a signal problem of the cable connection, but good luck in convincing my ISP). But I honestly have no idea what to look for since I understand the the Wireshark monitoring is cumbersome.</p><p>Any pointers would be greatly appreciated.</p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-cable_modem" rel="tag" title="see questions tagged &#39;cable_modem&#39;">cable_modem</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '17, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/1dc0ae99534b2c0b5e47f40d62eb0e0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Netch&#39;s gravatar image" /><p><span>Netch</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Netch has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '17, 14:10</strong> </span></p></div></div><div id="comments-container-61753" class="comments-container"></div><div id="comment-tools-61753" class="comment-tools"></div><div class="clear"></div><div id="comment-61753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61821"></span>

<div id="answer-container-61821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61821-score" class="post-score" title="current number of votes">0</div><span id="post-61821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you suspect that something on "your" side of the modem is causing the crash you can probably diagnose that with Wireshark. If it's something on the ISP side of the modem it is not very likely. The reason for that is that "your" side has Ethernet (or WiFi, or both), which can be captured with an appropriate capture setup. The ISP side is cable, which you cannot capture unless you have access to special diagnostic devices that can, which I doubt.</p><p>So what you can do is to setup a SPAN or TAP for the link of the Ethernet side of the modem, and do a long term capture using a ring buffer. That way you can record all the traffic of the modem on your side and check what happens just before it crashes. Maybe you can spot something that causes the crash.</p><p>I just checked the manual for your router and it doesn't seems to support packet captures on the device itself (neither local capture, nor SPAN), so if you want to do this you'll probably have to work with extra hardware - unless all connectivity is Wireless, in which case you might be able to work with a laptop you already have. You might want to check the Wiki for various ways of tapping into the Ethernet cable:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '17, 02:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61821" class="comments-container"></div><div id="comment-tools-61821" class="comment-tools"></div><div class="clear"></div><div id="comment-61821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

