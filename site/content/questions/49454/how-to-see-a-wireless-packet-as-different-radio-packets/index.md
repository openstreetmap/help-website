+++
type = "question"
title = "how to see a wireless packet as different radio packets"
description = '''Hi, I have a network setup only via wifi composed by 1 smartphone, 1 wifi router and 1 wireless device. The smartphone is sending a broadcast in the network, but sometimes doesn&#x27;t reach my wireless device. I can see the broadcast in wireshark( captured with Airpcap) but I can&#x27;t tell if my wifi route...'''
date = "2016-01-22T06:32:00Z"
lastmod = "2016-01-27T04:44:00Z"
weight = 49454
keywords = [ "packets", "airpcap", "radio" ]
aliases = [ "/questions/49454" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to see a wireless packet as different radio packets](/questions/49454/how-to-see-a-wireless-packet-as-different-radio-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49454-score" class="post-score" title="current number of votes">0</div><span id="post-49454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a network setup only via wifi composed by 1 smartphone, 1 wifi router and 1 wireless device. The smartphone is sending a broadcast in the network, but sometimes doesn't reach my wireless device. I can see the broadcast in wireshark( captured with Airpcap) but I can't tell if my wifi router firewall did allow the broadcast to pass by to my device or not. In other words, how can I see that broadcast as 2 radio transmission(from phone to wifi router and from wifi router to device) instead of 1 that I'm seeing. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-radio" rel="tag" title="see questions tagged &#39;radio&#39;">radio</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '16, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/7f54408f94ef2e44866500f3825742d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cristibalint91&#39;s gravatar image" /><p><span>cristibalint91</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cristibalint91 has no accepted answers">0%</span></p></div></div><div id="comments-container-49454" class="comments-container"></div><div id="comment-tools-49454" class="comment-tools"></div><div class="clear"></div><div id="comment-49454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49459"></span>

<div id="answer-container-49459" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49459-score" class="post-score" title="current number of votes">1</div><span id="post-49459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cristibalint91 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><del>Use <em>monitoring</em> mode at your PC's wireless network adapter, which requires some pre-requisities to exist. See <a href="https://wiki.wireshark.org/CaptureSetup/WLAN#Turning_on_monitor_mode">this link</a> for further details; don't even bother opening it if you cannot use any other than Windows-running PC, as you'd need a specialized capture hardware in such case.</del></p><p>Sorry, I haven't noticed you already do have the Airpcap. Since Airpcap always runs in monitor mode, the fact that you can see only a single occurrence of the broadcast packet should indicate that the AP has not forwarded it. Can you check the transmitter MAC address and source MAC address match in the 802.11 frame you can see? If they do (which I suppose), it is the frame sent from the phone; if they differ, it is the frame forwarded by the AP (so the source address is the one of the phone and the transmitter address is the one of the AP).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '16, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '16, 13:56</strong> </span></p></div></div><div id="comments-container-49459" class="comments-container"><span id="49538"></span><div id="comment-49538" class="comment"><div id="post-49538-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer, you are right, that is the logic I'm using too, but the problem is that there is no difference between the times it works and it doesn't work. I can see that TA and SA are the same but I can't see the same packet once with RA == router MAC and second with RA == device MAC. Is there a setting need to be done in Wireshark to do this?</p></div><div id="comment-49538-info" class="comment-info"><span class="comment-age">(27 Jan '16, 04:10)</span> <span class="comment-user userinfo">cristibalint91</span></div></div><span id="49540"></span><div id="comment-49540" class="comment"><div id="post-49540-score" class="comment-score">1</div><div class="comment-text"><p>To my best knowledge, no setting is necessary.</p><p>But in the case you've talked about, i.e. when the destination MAC address is a broadcast one, both <code>wlan.da</code> and <code>wlan.ra</code> are <code>ff:ff:ff:ff:ff:ff</code> for both frames (source device -&gt; AP as well as AP -&gt; all devices). So you have to look only at <code>wlan.sa</code> and <code>wlan.ta</code> in this case - if they match, it is the source frame (sent by the source device), if they don't match, it is the re-translated frame (re-sent by the AP).</p><p>I've just double-checked for a DHCP discover in a sample capture (no Apple, no Linux with WLAN, no AirPcap at my side).</p><p>Can you publish the capture(s) of both cases somewhere and post the link(s) to it (them) here? If you use encryption, you'll probably want to change your usual WPA passphrase before capturing and publishing the decryption information.</p><p>I would look for Rx level etc. as seen by the AirPcap for packets from different sources. I mean, are you sure you can see both frames, i.e. that the device or the AP are not so weak that the AirPcap would fail to demodulate one of the frames?</p></div><div id="comment-49540-info" class="comment-info"><span class="comment-age">(27 Jan '16, 04:44)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49459" class="comment-tools"></div><div class="clear"></div><div id="comment-49459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

