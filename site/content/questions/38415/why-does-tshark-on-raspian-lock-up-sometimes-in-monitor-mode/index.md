+++
type = "question"
title = "Why does tshark on Raspian lock up sometimes in monitor mode ?"
description = '''I have multiple identical Raspberry Pi B+ side by side. All use a Ralink RT5370 wireless usb dongle that is running in monitor mode. The problem is, tshark in only some of the machines dies at the same instant, presumably when the machines process the same packet. The capture file of the WiFi stream...'''
date = "2014-12-07T08:11:00Z"
lastmod = "2014-12-13T08:40:00Z"
weight = 38415
keywords = [ "tshark", "monitor-mode", "freeze" ]
aliases = [ "/questions/38415" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does tshark on Raspian lock up sometimes in monitor mode ?](/questions/38415/why-does-tshark-on-raspian-lock-up-sometimes-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38415-score" class="post-score" title="current number of votes">0</div><span id="post-38415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have multiple identical Raspberry Pi B+ side by side. All use a Ralink RT5370 wireless usb dongle that is running in monitor mode. The problem is, tshark in <strong>only some</strong> of the machines dies at the same instant, presumably when the machines process the same packet. The capture file of the WiFi stream being fed to tshark keeps growing, so the input does not freeze. WiFi traffic is low, the total cpu usage is only a few percent, and there's plenty of memory available. I'm running the latest everything (Dec 2014).</p><p>How do I fix this ?</p><p>Also, is monitor mode able to receive all WiFi channels simultaneously ?</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-monitor-mode" rel="tag" title="see questions tagged &#39;monitor-mode&#39;">monitor-mode</span> <span class="post-tag tag-link-freeze" rel="tag" title="see questions tagged &#39;freeze&#39;">freeze</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '14, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/a07a2459f82b7e0994552a4088be7857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewtownGuy&#39;s gravatar image" /><p><span>NewtownGuy</span><br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewtownGuy has no accepted answers">0%</span></p></div></div><div id="comments-container-38415" class="comments-container"></div><div id="comment-tools-38415" class="comment-tools"></div><div class="clear"></div><div id="comment-38415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38430"></span>

<div id="answer-container-38430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38430-score" class="post-score" title="current number of votes">0</div><span id="post-38430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/37538/bridging-on-a-raspberry-pi-previous-not-seen-and-freezing-after-a-while">https://ask.wireshark.org/questions/37538/bridging-on-a-raspberry-pi-previous-not-seen-and-freezing-after-a-while</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '14, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38430" class="comments-container"><span id="38432"></span><div id="comment-38432" class="comment"><div id="post-38432-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. However, in my case, it's only my script's processing of packets captured by tshark (apparently using dumpcap) and piped to it that freezes. The machine continues to run fine otherwise. Packet capture from the wlan0 interface continues to run as evidenced by the continually growing size of the capture file. I have also seen this on the older Model B. All of my tests use WiFi dongles with the Ralink RT5370 chipset since I need to use monitor mode. I will see if I can get another make of dongle that supports monitormode, but the fact that the packet capture continues to run makes me think the driver is OK. It acts like the pipe breaks, or tshark freezes, but I don't know how to confirm this. Any suggestions ?</p></div><div id="comment-38432-info" class="comment-info"><span class="comment-age">(08 Dec '14, 05:56)</span> <span class="comment-user userinfo">NewtownGuy</span></div></div><span id="38434"></span><div id="comment-38434" class="comment"><div id="post-38434-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any suggestions ?</p></blockquote><p>well, how does your script look like and how are you calling what?</p></div><div id="comment-38434-info" class="comment-info"><span class="comment-age">(08 Dec '14, 06:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="38435"></span><div id="comment-38435" class="comment"><div id="post-38435-score" class="comment-score"></div><div class="comment-text"><p>dumpcap is the process used by tshark (and Wireshark) to do the actual capture, it does sound as though something in tshark is hitting an issue. I suspect that you'll have to debug this yourself on the target machines.</p><p>Note that neither tshark or Wireshark can be used for continuous capturing as they retain state as the traffic is dissected and will eventually run out of memory, have you checked for this?</p></div><div id="comment-38435-info" class="comment-info"><span class="comment-age">(08 Dec '14, 06:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38549"></span><div id="comment-38549" class="comment"><div id="post-38549-score" class="comment-score"></div><div class="comment-text"><p>The capture file is stored in /tmp, the default. I delete it periodically and restart the process so I don't fill up the disk with capture data.</p><p>I now have TEN different but identical machines running side by side. I have seen as many as FIVE of them all fault at the same time. What I mean by fault is, tshark stops pipeing the output file to my app. The capture process continues, so the network interface is still running. I can't find any error messages or warnings, the pipe just stops. I have a script that detects the fault and restarts it, creating a new capture file and sending me an alert so I know to check it. My processing script is the same on all ten machines, and all machines are monitoring the same WiFi channel, so my script is ok.</p><p>Why does tshark stop pipeing its output to my script ??????</p><p>I doubt it matters, but I'm trying to configure tshark to configure dumpcap to write the raw capture data to a circular buffer (10 files, each 15 MB) in /var/tmp, which is a RAM disk, but I can't make it work. I made a separate post on this one question. tshark does not like the specification of capture files for dumpcap, it confuses them with writing its output.</p><p>Any suggestions on either the pipe problem or the buffer problem ?</p></div><div id="comment-38549-info" class="comment-info"><span class="comment-age">(13 Dec '14, 08:40)</span> <span class="comment-user userinfo">NewtownGuy</span></div></div></div><div id="comment-tools-38430" class="comment-tools"></div><div class="clear"></div><div id="comment-38430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

