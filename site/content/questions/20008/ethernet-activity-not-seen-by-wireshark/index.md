+++
type = "question"
title = "Ethernet activity not seen by Wireshark"
description = '''I have a USB-Ethernet adaptor connecting my Windows XP PC to an external device. Wiresharc (running on the same PC) sees all the activity I expect between the PC and the device. When both the PC and the device are idle (sending no Ethernet packets on that interface) I usually (but not always) see fr...'''
date = "2013-04-02T01:41:00Z"
lastmod = "2013-04-02T09:30:00Z"
weight = 20008
keywords = [ "ignored", "ethernet", "activity" ]
aliases = [ "/questions/20008" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet activity not seen by Wireshark](/questions/20008/ethernet-activity-not-seen-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20008-score" class="post-score" title="current number of votes">0</div><span id="post-20008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a USB-Ethernet adaptor connecting my Windows XP PC to an external device. Wiresharc (running on the same PC) sees all the activity I expect between the PC and the device. When both the PC and the device are idle (sending no Ethernet packets on that interface) I usually (but not always) see frantic, continuous activity on the adaptor (its lights are flashing), but Wireshark detects nothing.</p><p>Is there any way I can discover what's causing this activity?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ignored" rel="tag" title="see questions tagged &#39;ignored&#39;">ignored</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-activity" rel="tag" title="see questions tagged &#39;activity&#39;">activity</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '13, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/ef7626f540002d6403180aa20be73c9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Robertson&#39;s gravatar image" /><p><span>Peter Robertson</span><br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Robertson has no accepted answers">0%</span></p></div></div><div id="comments-container-20008" class="comments-container"></div><div id="comment-tools-20008" class="comment-tools"></div><div class="clear"></div><div id="comment-20008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20011"></span>

<div id="answer-container-20011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20011-score" class="post-score" title="current number of votes">0</div><span id="post-20011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is the external device a networking device (like a switch/router) etc? Does it have statistics for the interface? That help you determine if it is real traffic and not just a flashing LED. Wireshark must be in "promiscuous" mode (in the interface options) to be able to see traffic that is not orignated or a destination for the monitoring interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-20011" class="comments-container"><span id="20013"></span><div id="comment-20013" class="comment"><div id="post-20013-score" class="comment-score"></div><div class="comment-text"><p>It's a DSP that is idle; it is not a networking device. It's doing nothing, so there are no statistics. Wireshark is in promiscuous mode.</p></div><div id="comment-20013-info" class="comment-info"><span class="comment-age">(02 Apr '13, 03:42)</span> <span class="comment-user userinfo">Peter Robertson</span></div></div><span id="20014"></span><div id="comment-20014" class="comment"><div id="post-20014-score" class="comment-score"></div><div class="comment-text"><p>Wireshark (actually the pcap library) only will see packets that pass the physical layer. So there is "nothing to see" I expect.</p></div><div id="comment-20014-info" class="comment-info"><span class="comment-age">(02 Apr '13, 03:51)</span> <span class="comment-user userinfo">martyvis</span></div></div></div><div id="comment-tools-20011" class="comment-tools"></div><div class="clear"></div><div id="comment-20011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20021"></span>

<div id="answer-container-20021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20021-score" class="post-score" title="current number of votes">0</div><span id="post-20021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>When both the PC and the device are idle (sending no Ethernet packets on that interface) I usually (but not always) see frantic, continuous activity on the adaptor (its lights are flashing), but Wireshark detects nothing.</p></blockquote><p>That <strong>activity</strong> could be data on the USB bus that are not related to your networking traffic. To verify this scenario, add a switch between the DSP and the USB adapter. Then check if the activity LED of the switch blinks whenever the LED of the USB adapter does.</p><ul><li>If yes: There is network traffic, and there is a reason why you don't see those packets in Wireshark (see below).</li><li>If no: There is no network traffic and the USB adapter LED might just indicate data on the USB bus.</li></ul><p>If there is network traffic (switch LED) it could also 'damaged' network packets that are dropped by the USB adapter and thus don't make it to Wireshark. To verify this scenario, you could use a second laptop (<a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">plus a HUB, TAP or Switch mirror port</a>) and monitor the traffic between the DSP and the USB adapter. If you see traffic on the line, but not on the USB adapter, you can check if the packets are possibly 'damaged' (however, the NIC of your second PC might also drop damaged packets).<br />
</p><blockquote><p>Is there any way I can discover what's causing this activity?</p></blockquote><p>Without knowledge about the internals of the USB adapter (what exactly triggers the LED), you can only guess. I think you can get that kind of information only from the vendor of the USB adapter.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20021" class="comments-container"></div><div id="comment-tools-20021" class="comment-tools"></div><div class="clear"></div><div id="comment-20021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

