+++
type = "question"
title = "Initial tcp.window_size_value / tcp.window_size_scalefactor"
description = '''Hi, I have read RFCs 2001, 1323 + 2414 as well as a lot of other sources inc. packetlife, ask wireshark and google etc.. But I cannot figure out why a computer is sometimes giving Window size value of(i.e.) 237 and a WSS(i.e.) of 128 and other times a Window size value 16028 and a WSS of 4. I am ass...'''
date = "2014-10-05T12:01:00Z"
lastmod = "2014-12-21T23:06:00Z"
weight = 36850
keywords = [ "tcpwindowsize" ]
aliases = [ "/questions/36850" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Initial tcp.window\_size\_value / tcp.window\_size\_scalefactor](/questions/36850/initial-tcpwindow_size_value-tcpwindow_size_scalefactor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36850-score" class="post-score" title="current number of votes">0</div><span id="post-36850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have read RFCs 2001, 1323 + 2414 as well as a lot of other sources inc. packetlife, ask wireshark and google etc.. But I cannot figure out why a computer is sometimes giving Window size value of(i.e.) 237 and a WSS(i.e.) of 128 and other times a Window size value 16028 and a WSS of 4.</p><p>I am assuming / guessing / interpretting that it has to do with the bandwidth delay product as it seems small WSV and large WSS on low latency and large WSV and low WSS on high latency. I can figure out why a window is sometimes 64k to start and sometimes 4k, but I cannot find any Information up to now of how the value*scale is worked out? Would be very much appreciated if someone can point me at the right RFC or explanation somewhere.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Oct '14, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-36850" class="comments-container"></div><div id="comment-tools-36850" class="comment-tools"></div><div class="clear"></div><div id="comment-36850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38647"></span>

<div id="answer-container-38647" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38647-score" class="post-score" title="current number of votes">0</div><span id="post-38647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarrenWright has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>ahahahaha "NEVER GIVE UP, NEVER SAY DIE"</p><p>for Windows 7 missing TCP Stack selections find these KBs: KB2861819 + KB2472264</p><p><code> netsh interface tcp set global initialRto=1000 (500 to 3000*is default. 500 causes retransmissions if your RTT is high) netsh interface tcp set global timestamps=enabled netsh interface tcp set global congestionprovider=ctcp netsh int tcp set heuristics disabled </code></p><p>Now you can workout roughly what size of Windows will be used to ensure the best use of the Line: Low latency High BW = small window size * large WS multiplier High Latency Low BW = Larger window size * small WS Multiplier</p><p>If you are on WIndows 2008R2 or Windows 8 you can even manually edit the Initial CWIN Multiplier (&gt;16)</p><p><code> netsh interface tcp set supplemental template=custom minRto=20 icw=16 delayedacktimeout=10 netsh interface tcp set supplemental template=custom</code></p><p>With a little fine tuning you can rip your download speed in Windows to almost the maximum</p><p>I know the thread is old, but I couldn't believe how anoyying this information is to piece together... And Tip: Disable mscc Windows service + dependency on Audio Service. It really screws with your retransmissions...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '14, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-38647" class="comments-container"><span id="38652"></span><div id="comment-38652" class="comment"><div id="post-38652-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the formatting Graham. Still haven't quite got the hang of it :/</p><p>I have deleted my old answer as some of the information there was, following testing, found to be not 100% relevant.</p><p>I have been testing this now for a few days under windows 7(x64) SP1 with the settings above. I am seeing far fewer retransmissions and my download speed is almost always maxed out now on my dsl 16k. The window sizes are also now somewhat more predictable.</p></div><div id="comment-38652-info" class="comment-info"><span class="comment-age">(21 Dec '14, 23:06)</span> <span class="comment-user userinfo">DarrenWright</span></div></div></div><div id="comment-tools-38647" class="comment-tools"></div><div class="clear"></div><div id="comment-38647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36852"></span>

<div id="answer-container-36852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36852-score" class="post-score" title="current number of votes">0</div><span id="post-36852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The scale factor is determined by the TCP stack. Sometimes it uses specific values (e.g. Vista used a scale factor of 2^8 = 256 and set the window size value to 256), sometimes it is based on some heuristics.</p><p>The stack in Windows 7 and up even tells you that it has a "Receive Window Auto-Tuning Level". You can check the current setting with the command "netsh interface tcp show global" on a command prompt. If you check the available settings it shows</p><pre><code>autotuninglevel - One of the following values:
                         disabled: Fix the receive window at its default
                             value.
                         highlyrestricted: Allow the receive window to
                             grow beyond its default value, but do so
                             very conservatively.
                         restricted: Allow the receive window to grow
                             beyond its default value, but limit such
                             growth in some scenarios.
                         normal: Allow the receive window to grow to
                             accomodate almost all scenarios.
                         experimental: Allow the receive window to grow</code></pre><p>As far as I found out, experimental sets the scale factor to 2^14 (maximum) which allows scaling to about 1 GByte. "Disabled" does just that - no more scaling.</p><p>What the stack does is setting scale factors that allow it to set the receive window to values that are big enough for it's puposes. E.g. with Vista, it could scale the Window from 256 (actually, 0, but that's a full stop) to 16MB (256 * 65,535), but of course only in steps of 256 bytes.</p><p>BTW, the Windows stack will also tell you this: "** The above autotuninglevel setting is the result of Windows Scaling heuristics overriding any local/policy configuration on at least one profile." - and there is no documentation (AFAIK) that shows how that heuristics work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '14, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Oct '14, 12:49</strong> </span></p></div></div><div id="comments-container-36852" class="comments-container"><span id="36853"></span><div id="comment-36853" class="comment"><div id="post-36853-score" class="comment-score"></div><div class="comment-text"><p>this is why I am confused. Heuristics is disabled. Tuning (aka Scaling..) is Normal. So, why does it vary, without heuristics I would expect it to always go for 2^8 * 256? I can connect to one site and get a wss of 256, on another 4. I can get a Window size value of 128 or a window size value of 65535.. What gives? Funnily enough as I write this I realise I have never seen anything less than 4 from my client?</p></div><div id="comment-36853-info" class="comment-info"><span class="comment-age">(05 Oct '14, 13:07)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="36854"></span><div id="comment-36854" class="comment"><div id="post-36854-score" class="comment-score"></div><div class="comment-text"><p>I don't think you can actually disable the heuristics except if you set autotuning level to disabled... btw., I have even seen that turning Antivirus softwares on and off can have an effect on the scaling...</p></div><div id="comment-36854-info" class="comment-info"><span class="comment-age">(05 Oct '14, 13:09)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="36855"></span><div id="comment-36855" class="comment"><div id="post-36855-score" class="comment-score"></div><div class="comment-text"><p>netsh int tcp set heuristics disabled</p><p>Apparently (and I cant be sure. WIndows 7 stack is (with heuristics enabled) doing it's upmost to hold your rwin at 256k.</p><p>If you disable Heuristics, it can grow normally apparently. I would have to play around here to see what is happening..</p><p>BUT. My question still remains. Windows decides on an Initial Window of 66052(for ease of Maths..) Why is this windows sometimes made up as 16513 Window_Size_Value with Scalefactor 4 And other times made up of Window_Size_Value 256 and Scalefactor 256. On the same stack. Talking to the same host. Could this be a switch or other path object laughing at me?</p></div><div id="comment-36855-info" class="comment-info"><span class="comment-age">(05 Oct '14, 13:27)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="36856"></span><div id="comment-36856" class="comment"><div id="post-36856-score" class="comment-score"></div><div class="comment-text"><p>Well, you'll not get an answer, because Microsoft doesn't tell - many of us have tried :-)</p></div><div id="comment-36856-info" class="comment-info"><span class="comment-age">(05 Oct '14, 13:28)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36852" class="comment-tools"></div><div class="clear"></div><div id="comment-36852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

