+++
type = "question"
title = "wireshark only shows one protocol in capture"
description = '''how come i only get one protocol in wireshark capture. the protocols i got first time was only &quot;802.11&quot; the protocols i got 2nd time was only &quot;usb&quot; i want to capture everything. i am using alfa wifi device to capture how do i capture everything, smtp, tcp, dns, ...???????????'''
date = "2013-07-15T15:44:00Z"
lastmod = "2013-07-15T16:56:00Z"
weight = 22980
keywords = [ "capture", "802.11-only", "protocol", "usb-only" ]
aliases = [ "/questions/22980" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark only shows one protocol in capture](/questions/22980/wireshark-only-shows-one-protocol-in-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22980-score" class="post-score" title="current number of votes">0</div><span id="post-22980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how come i only get one protocol in wireshark capture.</p><p>the protocols i got first time was only "802.11"</p><p>the protocols i got 2nd time was only "usb"</p><p>i want to capture everything.</p><p>i am using alfa wifi device to capture</p><p>how do i capture everything, smtp, tcp, dns, ...???????????</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-802.11-only" rel="tag" title="see questions tagged &#39;802.11-only&#39;">802.11-only</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-usb-only" rel="tag" title="see questions tagged &#39;usb-only&#39;">usb-only</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '13, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/60adade2f3b312a3ef7a29ad1c416390?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Freddy%20Krueger&#39;s gravatar image" /><p><span>Freddy Krueger</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Freddy Krueger has no accepted answers">0%</span></p></div></div><div id="comments-container-22980" class="comments-container"><span id="22981"></span><div id="comment-22981" class="comment"><div id="post-22981-score" class="comment-score"></div><div class="comment-text"><p>On what interfaces are you capturing on? You can check by going to "Capture -&gt; Interfaces" or directly to "Interfaces List" from the home wireshark program.</p></div><div id="comment-22981-info" class="comment-info"><span class="comment-age">(15 Jul '13, 16:09)</span> <span class="comment-user userinfo">Edmond</span></div></div></div><div id="comment-tools-22980" class="comment-tools"></div><div class="clear"></div><div id="comment-22980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22982"></span>

<div id="answer-container-22982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22982-score" class="post-score" title="current number of votes">0</div><span id="post-22982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since when capturing wireless data everything is encapsulated withing 802.11 headers, you shouldn't wonder about seeing lots of these as protocol marks. The other mentioned high layer procotols are within 802.11 encapsulation and can be interpreted as such given either capturing on non-encrypted networks or supplying the respective WEP/WPA key to wireshark.</p><p>For more information on how to configure use the search function inside this QA site or see <a href="http://wiki.wireshark.org/HowToDecrypt802.11">here</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-22982" class="comments-container"></div><div id="comment-tools-22982" class="comment-tools"></div><div class="clear"></div><div id="comment-22982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22983"></span>

<div id="answer-container-22983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22983-score" class="post-score" title="current number of votes">0</div><span id="post-22983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>the protocols i got first time was only "802.11"</p></blockquote><p>You're probably capturing in monitor mode on a protected network (WEP or WPA/WPA2). You will either have to capture without monitor mode (meaning you will only see traffic to and from your machine) or tell Wireshark the password for your network and, for WPA/WPA2, make sure you capture the initial "EAPOL handshake" for each device whose traffic you want to see. (The whole <em>point</em> of WEP and WPA/WPA2 is to make it hard to sniff traffic!) See <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki's page on "How to Decrypt 802.11"</a> for details.</p><blockquote><p>the protocols i got 2nd time was only "usb"</p></blockquote><p>Are you sure you were capturing on your 802.11 device when that happened? I suspect you were capturing on a "usbmon" device; those devices have names such as <code>usbmon0</code>, <code>usbmon1</code>, etc., and allow you to capture raw USB traffic (<em>NOT</em> "networking traffic on a USB device", but raw USB commands and data). Don't capture on "usbmon" devices if you want to capture networking traffic, <em>even if your networking device is a USB device</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '13, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22983" class="comments-container"></div><div id="comment-tools-22983" class="comment-tools"></div><div class="clear"></div><div id="comment-22983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

