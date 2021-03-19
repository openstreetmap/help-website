+++
type = "question"
title = "Wireshark with Atheros wireless in Monitor mode."
description = '''Is working but I am only seeing 802.11 management packets, Beacons, Probe Requests etc. Proof that monitor mode is working or partly working.  But I am not getting anything else, no data packets. This is a wireless nic that supports monitor mode and I am properly putting it in monitor mode setting t...'''
date = "2016-09-18T18:11:00Z"
lastmod = "2016-09-19T03:36:00Z"
weight = 55637
keywords = [ "802.11", "monitor", "mode" ]
aliases = [ "/questions/55637" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with Atheros wireless in Monitor mode.](/questions/55637/wireshark-with-atheros-wireless-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55637-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is working but I am only seeing 802.11 management packets, Beacons, Probe Requests etc.<br />
Proof that monitor mode is working or partly working.<br />
But I am not getting anything else, no data packets.<br />
This is a wireless nic that supports monitor mode and I am properly putting it in monitor mode setting the channel and such.<br />
I have tried this with a number of cards and systems same issue.</p><p>What do I need to do to see/capture ALL of the activity on the channel and not just the 802.11 management?<br />
</p><p>Thanks!<br />
Steve</p></div><div id="question-tags" class="tags-container tags">802.11 monitor mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '16, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/c7d876f10c612df0732c5cb6dcbb901f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="N8lbv&#39;s gravatar image" /><p>N8lbv<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="N8lbv has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-55637" class="comments-container"><span id="55642"></span><div id="comment-55642" class="comment"><div id="post-55642-score" class="comment-score"></div><div class="comment-text"><p>First look at the questions suggested at the bottom of the right hand column on this page (Related questions). Then, if possible, disable ac and n modes on your access point, as it is quite likely that your Atheros doesn't support them so if the other devices use them, the Atheros cannot capture them. The management frames are sent using widely supported modes so that all devices could handle them.</p></div><div id="comment-55642-info" class="comment-info"><span class="comment-age">(19 Sep '16, 02:57)</span> sindy</div></div><span id="55665"></span><div id="comment-55665" class="comment"><div id="post-55665-score" class="comment-score"></div><div class="comment-text"><p>Excellent suggestion.<br />
I do indeed already have the AP set to only 2.4Ghz and BG. (mixed). Oddly I found that in my linux distribution that various wireless utilities when ran create a virtual wireless interface (wlan0mon) And leave it in place after running. Kismet in particular does this even though I am specifying "wlan0" as the capture device.<br />
Now when I run wireshark and choose wlan0mon instead of wlan0 it works. I am getting all the packets. I captured a SIP/VOIP phone call between two other nodes and all the RTP.<br />
So I at least have a work around that works now.<br />
But I don;t for the life of me know why it matters that I use a virtual interface and why it doesn't work simply with wlan0 after putting it in monitor mode.<br />
:)</p></div><div id="comment-55665-info" class="comment-info"><span class="comment-age">(19 Sep '16, 09:44)</span> N8lbv</div></div><span id="55668"></span><div id="comment-55668" class="comment"><div id="post-55668-score" class="comment-score"></div><div class="comment-text"><p>Maybe the tool reverts to managed mode after you stop using the tool? But the secondary interface is still in monitor mode. You should be able to see them with commands:</p><p>iw dev or iwconfig</p><p>The iw command is the most useful - plenty of options. Also shut down any network managers you may have - they like to move your interfaces back to managed mode at every opportunity.</p></div><div id="comment-55668-info" class="comment-info"><span class="comment-age">(19 Sep '16, 11:28)</span> Bob Jones</div></div></div><div id="comment-tools-55637" class="comment-tools"></div><div class="clear"></div><div id="comment-55637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55643"></span>

<div id="answer-container-55643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55643-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two likely scenarios you are running into that can cause this:</p><ol><li>The device supports monitor mode, but not promiscuous mode. You need both. The way to tell is to identify unicast traffic in the data stream. If you have it, then this is not the issue.</li><li>Per @Sindy's comment, it may be that you support monitor and promiscuous mode, but your capture adapter can not decode the data packets due to modulation differences. Just because the device says it is capable of x/y/z (i.e. maybe 802.11ac 2x2:2 or whatever), does not mean it will capture that traffic in monitor mode. There is a good chance it will, but we need to know how you are configuring the device for capture.<br />
</li></ol><p>Degrade a test platform to 802.11a/b/g only (probably does not matter, but you would need to know so you can setup your capture accordingly) and pass traffic. Do you pick it all up? If so, start adding back in the advanced features like 802.11n/ac, 40/80MHz channels, LDPC encoding, etc. And see when it starts to break.<br />
</p><p>Of course there is the obvious root cause just to be sure: are you capturing on a channel that has known data flowing? I know it's a stupid question, but you should be able to identify your BSSID and any devices you are using to test, like your laptop, tablet, smartphone, etc. As you are connected and, for instance, accessing webpages, you should at least see some traffic from this device even if either of the two cases are true above.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '16, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-55643" class="comments-container"><span id="55666"></span><div id="comment-55666" class="comment"><div id="post-55666-score" class="comment-score"></div><div class="comment-text"><p>Yep, as commented above I have it working if I use a virtual interface that gets created when I run Kismet instead of the actual wireless interface in monitor mode.<br />
Might be a driver quirk.<br />
Or it's just written that way and expected to be used this 'new_way'</p><p>But yes I had already simplified the test scenario about as much as possible, no encryption 2.4BG only (open network) two known test nodes passing known traffic during test etc. :) All good suggestions.<br />
Yep had a VoIP/RTP call in the clear going on during all testing.</p></div><div id="comment-55666-info" class="comment-info"><span class="comment-age">(19 Sep '16, 09:49)</span> N8lbv</div></div></div><div id="comment-tools-55643" class="comment-tools"></div><div class="clear"></div><div id="comment-55643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

