+++
type = "question"
title = "texts through home router"
description = '''Is it possible to capture the content of texts (iMessage, SMS, etc.) sent through my home router?'''
date = "2013-10-23T12:15:00Z"
lastmod = "2013-11-03T12:08:00Z"
weight = 26333
keywords = [ "texts", "router", "home" ]
aliases = [ "/questions/26333" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [texts through home router](/questions/26333/texts-through-home-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26333-score" class="post-score" title="current number of votes">0</div><span id="post-26333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to capture the content of texts (iMessage, SMS, etc.) sent through my home router?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-texts" rel="tag" title="see questions tagged &#39;texts&#39;">texts</span> <span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-home" rel="tag" title="see questions tagged &#39;home&#39;">home</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/9974caa4ffee0daedf8b5fe3b160108b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ridehrd&#39;s gravatar image" /><p><span>ridehrd</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ridehrd has no accepted answers">0%</span></p></div></div><div id="comments-container-26333" class="comments-container"><span id="26336"></span><div id="comment-26336" class="comment"><div id="post-26336-score" class="comment-score"></div><div class="comment-text"><p>Idon't know what iMessage is but SMS is probably not sent trough your home router but rather trough the Mobile network.</p></div><div id="comment-26336-info" class="comment-info"><span class="comment-age">(23 Oct '13, 13:25)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="26357"></span><div id="comment-26357" class="comment"><div id="post-26357-score" class="comment-score"></div><div class="comment-text"><p>iMessage is the Apple instant messaging app which will be going over your home LAN. This Apple KB says which <a href="http://support.apple.com/kb/ht4245">ports</a> it uses, but I suspect as both 443 and 5223 are SSL connections, even if you can capture the packets the contents will be scrambled.</p></div><div id="comment-26357-info" class="comment-info"><span class="comment-age">(24 Oct '13, 04:12)</span> <span class="comment-user userinfo">Mike the TV</span></div></div></div><div id="comment-tools-26333" class="comment-tools"></div><div class="clear"></div><div id="comment-26333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26642"></span>

<div id="answer-container-26642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26642-score" class="post-score" title="current number of votes">1</div><span id="post-26642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture method would be different depending on the protocol.</p><p>SMS: These are, in almost all cases, exclusively sent to your mobile carrier network. Further, they are sent over a control/signaling channel from your device, and not over any TCP/IP data session. From the device perspective, for either LTE or previous radio access networks (UMTS, GSM) the protocol stack would be RRC/NAS/GSM_SMS, where "RRC" or "Radio Resource Control" is a logical radio channel for your device to send control/signaling messages toward the cell tower, "NAS" or "Non-Access Stratum" is any type of control or signaling message that the device wants the radio network to tunnel toward the mobile "Core" network, and within that "non-access" message an SMS message is sent. Because SMS is sent over control channels, you would need special device analysis tools to trace the traffic, and those tools would be chipset-dependent (eg: a device that uses a Qualcomm chipset could use a tool such as Qualcomm QXDM to analyse this traffic).</p><p>MMS: This type of message is sent over a TCP/IP network connection to a web proxy, and your device's MMS configuration settings should have the IP/port details of the web proxy it is connecting to to send or receive the messages. Note, the IP network you use to reach the web proxy would be an address inside your carrier's network, so it would not be possible to use traditional MMS over Wifi (over the Internet, you would not have IP connectivity to a carrier's MMS web proxy). So, you'd need to trace data sent over the radio network in user-plane data channels, and again would need special analytical tools to do that. <em>NOTE</em> also that aside from the user-plane component, when you receive an MMS the reality is that you're receiving a background SMS message (as described above), where it tells the phone to initiate an MMS data session with the web proxy to receive the new MMS.</p><p>iMessage: This can be sent over Wifi, but I don't <em>think</em> there is any case where it would be clear-text.</p><p>For reference, here are the latest whitepapers for SMS and MMS respectively from the 3GPP. They are both huge topics to walk into, but the short of it is that SMS is based on the SS7 protocol stack rather than TCP/IP, and its really a whole other world of (legacy) networking. In a sense, sending an SMS is more like making a phone call than it is like sending an IP packet to trace: <a href="http://www.etsi.org/deliver/etsi_ts/123000_123099/123040/10.00.00_60/ts_123040v100000p.pdf">http://www.etsi.org/deliver/etsi_ts/123000_123099/123040/10.00.00_60/ts_123040v100000p.pdf</a> <a href="http://www.etsi.org/deliver/etsi_ts/123100_123199/123140/06.16.00_60/ts_123140v061600p.pdf">http://www.etsi.org/deliver/etsi_ts/123100_123199/123140/06.16.00_60/ts_123140v061600p.pdf</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Nov '13, 12:09</strong> </span></p></div></div><div id="comments-container-26642" class="comments-container"></div><div id="comment-tools-26642" class="comment-tools"></div><div class="clear"></div><div id="comment-26642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26637"></span>

<div id="answer-container-26637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26637-score" class="post-score" title="current number of votes">0</div><span id="post-26637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You CAN capture the iMessage data if it is being sent over the WiFi and not over the mobile network. However, it will be encrypted, so you will not see the actual text messages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-26637" class="comments-container"></div><div id="comment-tools-26637" class="comment-tools"></div><div class="clear"></div><div id="comment-26637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

