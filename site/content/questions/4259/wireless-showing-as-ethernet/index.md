+++
type = "question"
title = "Wireless showing as Ethernet"
description = '''Hi, I&#x27;ve been struggling with this for days now, I have installed Backtrack 5, I have Atheros AR9287 wireless card. But whenever I open Wireshark to sniff the wireless network, I am able to see only my own traffic, or traffic targeted to the whole network *.255 only. I&#x27;ve noticed that whenever I try...'''
date = "2011-05-27T14:24:00Z"
lastmod = "2011-05-31T00:03:00Z"
weight = 4259
keywords = [ "wireless", "adapter", "atheros", "ar9287" ]
aliases = [ "/questions/4259" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless showing as Ethernet](/questions/4259/wireless-showing-as-ethernet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4259-score" class="post-score" title="current number of votes">0</div><span id="post-4259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've been struggling with this for days now, I have installed Backtrack 5, I have Atheros AR9287 wireless card. But whenever I open Wireshark to sniff the wireless network, I am able to see only my own traffic, or traffic targeted to the whole network *.255 only. I've noticed that whenever I try to select the capture interface, wlan0 (which is the wireless adapter) shows as ETHERNET, and I don't have 802.11 option in the drop down list...I've been searching for days now, and couldn't find any useful answer. I really do appreciate your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-adapter" rel="tag" title="see questions tagged &#39;adapter&#39;">adapter</span> <span class="post-tag tag-link-atheros" rel="tag" title="see questions tagged &#39;atheros&#39;">atheros</span> <span class="post-tag tag-link-ar9287" rel="tag" title="see questions tagged &#39;ar9287&#39;">ar9287</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '11, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/8cb367d2e1d9c521b798492d8c586f08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thirdium&#39;s gravatar image" /><p><span>Thirdium</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thirdium has no accepted answers">0%</span></p></div></div><div id="comments-container-4259" class="comments-container"></div><div id="comment-tools-4259" class="comment-tools"></div><div class="clear"></div><div id="comment-4259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4261"></span>

<div id="answer-container-4261" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4261-score" class="post-score" title="current number of votes">2</div><span id="post-4261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Basics things to try with that problem:</p><p>look in 'iwconfig' if your wireless card is recognized at all within BT5</p><ul><li>Use airmon-ng start wlan0 to bring your wireless NIC into monitor mode</li><li>Since BT4 there are many cards coming up with a new "virtual" interface commonly called 'mon0'</li><li>Try sniffing with the mon0 interface now</li><li>If channel hopping is a problem, add the -c &lt;channel number=""&gt; flag to airmon-ng to specify the channel you're interedsted in</li></ul><p>Apart from that, there are some issues with BT5 and wireless drivers atm - i would ask you to stick to the official BackTrack Forums for more help with that. There are several posts that might bring you forward.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '11, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4261" class="comments-container"><span id="4266"></span><div id="comment-4266" class="comment"><div id="post-4266-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply, I actually tried that before: airmon-ng start monitor wlan0 -c 6</p><p>But when I open wireshark, choose mon0 as my interface, I sniff as if I'm not on the network...everything is encrypted, no IP addresses.</p><p>Any other thoughts ?</p></div><div id="comment-4266-info" class="comment-info"><span class="comment-age">(28 May '11, 01:49)</span> <span class="comment-user userinfo">Thirdium</span></div></div><span id="4268"></span><div id="comment-4268" class="comment"><div id="post-4268-score" class="comment-score"></div><div class="comment-text"><p>Did airmon-ng respond that your chipset was successfully set into monitor mode ?</p><p>Try using airodump-ng -c 6 -w /tmp/tracefile, maybe wireshark tries enabling monitor mode as well which might interfere with airmon...</p></div><div id="comment-4268-info" class="comment-info"><span class="comment-age">(28 May '11, 03:28)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="4273"></span><div id="comment-4273" class="comment"><div id="post-4273-score" class="comment-score"></div><div class="comment-text"><p>yes it does, here is the output:</p><pre><code>Found 5 processes that could cause trouble.
If airodump-ng, aireplay-ng or airtun-ng stops working after
a short period of time, you may want to kill (some of) them!

PID Name
1263    dhclient3
1675    dhclient3
10852   wpa_supplicant
10862   dhclient
10900   dhclient
Process with PID 1675 (dhclient3) is running on interface wlan0
Process with PID 10852 (wpa_supplicant) is running on interface wlan0
Process with PID 10900 (dhclient) is running on interface wlan0

Interface   Chipset     Driver

wlan0       Atheros AR9287  ath9k - [phy0]/usr/local/sbin/airmon-ng: line 598: [: -c: integer expression expected

                (monitor mode enabled on mon0)</code></pre></div><div id="comment-4273-info" class="comment-info"><span class="comment-age">(28 May '11, 15:33)</span> <span class="comment-user userinfo">Thirdium</span></div></div><span id="4274"></span><div id="comment-4274" class="comment"><div id="post-4274-score" class="comment-score"></div><div class="comment-text"><p>Interface Chipset Driver</p><pre><code>wlan0       Atheros AR9287  ath9k - [phy0]/usr/local/sbin/airmon-ng: line 598: [: -c: integer expression expected

                (monitor mode enabled on mon0)</code></pre></div><div id="comment-4274-info" class="comment-info"><span class="comment-age">(28 May '11, 15:33)</span> <span class="comment-user userinfo">Thirdium</span></div></div><span id="4279"></span><div id="comment-4279" class="comment not_top_scorer"><div id="post-4279-score" class="comment-score"></div><div class="comment-text"><p>This output:</p><pre><code>/usr/local/sbin/airmon-ng: line 598: [: -c: integer expression expected</code></pre><p>is obviously some error, because -c is not assigned in airmon... once again, try the following syntax</p><p>'airmon-ng start wlan0 6'</p><p>Then mon0 should be your virtuel NIC on 2.4GHz channel 6, then go for</p><p>'airodump-ng -w /tmp/tracefile mon0'</p></div><div id="comment-4279-info" class="comment-info"><span class="comment-age">(29 May '11, 05:38)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="4292"></span><div id="comment-4292" class="comment"><div id="post-4292-score" class="comment-score">1</div><div class="comment-text"><p>If your network is using WEP or WPA, then, when you capture in monitor mode, you will see the raw packets on the network - which will be encrypted. To decrypt it, see the <a href="http://wiki.wireshark.org/HowToDecrypt802.11">How To Decrypt 802.11</a> page in the Wireshark wiki.</p></div><div id="comment-4292-info" class="comment-info"><span class="comment-age">(31 May '11, 00:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4261" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-4261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4260"></span>

<div id="answer-container-4260" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4260-score" class="post-score" title="current number of votes">0</div><span id="post-4260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You won't see the 802.11 layer unless you enable monitor mode on your WiFi card. Without it, you will only see the ethernet and further layers, but not the radio layer.</p><p>On backtrack you can use the airmon-ng utility to enable monitor mode if I remember correctly (has been a while I used it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '11, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4260" class="comments-container"></div><div id="comment-tools-4260" class="comment-tools"></div><div class="clear"></div><div id="comment-4260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

