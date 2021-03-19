+++
type = "question"
title = "Unable to capture DICOM packets with USB-Ethernet adapter"
description = '''Hello - I&#x27;ve been using my laptop with built in ethernet card to capture DICOM packets for a long time now. I recently purchased a new laptop that doesn&#x27;t have a built in Ethernet card but has a USB-Ethernet adapter. I&#x27;m now unable to capture DICOM packets with the new USB-Ethernet adapter. I have s...'''
date = "2013-02-09T18:31:00Z"
lastmod = "2013-02-12T02:45:00Z"
weight = 18472
keywords = [ "dicom", "usb", "ethernet" ]
aliases = [ "/questions/18472" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture DICOM packets with USB-Ethernet adapter](/questions/18472/unable-to-capture-dicom-packets-with-usb-ethernet-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18472-score" class="post-score" title="current number of votes">0</div><span id="post-18472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello - I've been using my laptop with built in ethernet card to capture DICOM packets for a long time now. I recently purchased a new laptop that doesn't have a built in Ethernet card but has a USB-Ethernet adapter. I'm now unable to capture DICOM packets with the new USB-Ethernet adapter. I have searched everywhere on the internet and can't seem to find any answers. Does anyone know how to fix this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dicom" rel="tag" title="see questions tagged &#39;dicom&#39;">dicom</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '13, 18:31</strong></p><img src="https://secure.gravatar.com/avatar/c3c5ecd9e81455894ca7ae85656ceea4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bca&#39;s gravatar image" /><p><span>bca</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bca has no accepted answers">0%</span></p></div></div><div id="comments-container-18472" class="comments-container"><span id="18473"></span><div id="comment-18473" class="comment"><div id="post-18473-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "unable to capture DICOM packets"? Do you mean that, on an Ethernet segment that has DICOM traffic on it, you can, for example, plug both your old laptop and your new laptop into that segment at the same time, and the old laptop will see DICOM packets but the new one won't?</p><p>Is the DICOM traffic being sent to or from the laptop in question, or is it "third-party" traffic that must be sniffed promiscuously?</p><p>Does the laptop with the USB Ethernet adapter see any "third-party" traffic other than broadcasts and multicasts?</p><p>What operating system is are the machines running?</p></div><div id="comment-18473-info" class="comment-info"><span class="comment-age">(09 Feb '13, 19:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18488"></span><div id="comment-18488" class="comment"><div id="post-18488-score" class="comment-score"></div><div class="comment-text"><p>Yes that is correct, I am unable to capture DICOM traffic on an ethernet segmnet.<br />
</p><p>My setup is as follows:</p><p>I have my: a. "DICOM System" sending/receiving DICOM traffic b. "DICOM Server" sending/recieving DICOM traffic c. New laptop with "USB-ethernet adapter" d. Port for company network<br />
e. Dumb hub</p><p>I connect a, b, c, and d into e (Dumb hub).</p><p>I can now monitor all ethernet traffic on my new laptop(c) between a and b, but can't see the DICOM traffic.</p><p>I then take my old laptop with "built in ethernet adapter" and replace it with "c". I can now see the DICOM traffic.</p></div><div id="comment-18488-info" class="comment-info"><span class="comment-age">(11 Feb '13, 09:19)</span> <span class="comment-user userinfo">bca</span></div></div><span id="18489"></span><div id="comment-18489" class="comment"><div id="post-18489-score" class="comment-score"></div><div class="comment-text"><p>My new laptop with "USB-ethernet adapter" is running Windows 7 64-bit.</p><p>My old laptop with "built in ethernet adapter" is running Windows XP 32-bit.</p></div><div id="comment-18489-info" class="comment-info"><span class="comment-age">(11 Feb '13, 09:19)</span> <span class="comment-user userinfo">bca</span></div></div><span id="18492"></span><div id="comment-18492" class="comment"><div id="post-18492-score" class="comment-score"></div><div class="comment-text"><p>Is the "dumb hub" a dual-speed hub?</p><p>If you "can now monitor all ethernet traffic on my new laptop(c) between a and b", that means you can monitor DICOM traffic between a and b, as it's Ethernet traffic, so presumably you mean something like "I <em>should</em> now be able to monitor all Ethernet traffic on my new laptop(c) between a and b, but I'm not seeing all the traffic". Are you seeing any unicast Ethernet traffic between a and b <em>at all</em>? Are you, for example, seeing non-DICOM TCP traffic, of any sort, between a and b?</p></div><div id="comment-18492-info" class="comment-info"><span class="comment-age">(11 Feb '13, 10:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18518"></span><div id="comment-18518" class="comment"><div id="post-18518-score" class="comment-score"></div><div class="comment-text"><p>Yes, the "dumb hub" is a dual speed hub.</p><p>What you stated is correct, "I should now be able to monitor all Ethernet traffic on my new laptop(c) between a and b, but I'm not seeing all the traffic".</p><p>And yes, I am seeing unicast (non-DICOM) Ethernet traffic between a and b with the new laptop.</p><p>The only two things I can see as being the root cause are: a. the difference in operating system b. the difference in the ethernet adapter</p><p>Thanks again for your help.</p></div><div id="comment-18518-info" class="comment-info"><span class="comment-age">(11 Feb '13, 16:17)</span> <span class="comment-user userinfo">bca</span></div></div><span id="18519"></span><div id="comment-18519" class="comment not_top_scorer"><div id="post-18519-score" class="comment-score"></div><div class="comment-text"><p>So:</p><p>1) what speed is the DICOM traffic - 10Mb/s or 100Mb/s?</p><p>2) what speed is the adapter on the old laptop running - 10Mb/s or 100Mb/s?</p><p>3) what speed is the USB adapter on the new laptop running - 10Mb/s or 100Mb/s?</p></div><div id="comment-18519-info" class="comment-info"><span class="comment-age">(11 Feb '13, 16:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="18520"></span><div id="comment-18520" class="comment not_top_scorer"><div id="post-18520-score" class="comment-score"></div><div class="comment-text"><p>100 for all</p></div><div id="comment-18520-info" class="comment-info"><span class="comment-age">(11 Feb '13, 17:47)</span> <span class="comment-user userinfo">bca</span></div></div><span id="18521"></span><div id="comment-18521" class="comment not_top_scorer"><div id="post-18521-score" class="comment-score"></div><div class="comment-text"><p>I.e., you could replace the hub with a 100Mb/s-only hub and it would still work?</p><p>If you're seeing other TCP traffic, but not DICOM traffic, with the new machine, and Wireshark is configured the same on both machines so that it <em>recognizes</em> DICOM traffic and dissects it as DICOM traffic in both cases, there's probably something really weird about the adapter driver or adapter on the new laptop.</p><p>If you're not seeing <em>any</em> TCP traffic with the new machine, that would be much less weird, as the adapter wouldn't know what's DICOM traffic and what's other TCP traffic.</p></div><div id="comment-18521-info" class="comment-info"><span class="comment-age">(11 Feb '13, 17:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-18472" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-18472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18535"></span>

<div id="answer-container-18535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18535-score" class="post-score" title="current number of votes">0</div><span id="post-18535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The only two things I can see as being the root cause are: a. the difference in operating system b. the difference in the ethernet adapter</p></blockquote><p>Or a difference in the Wireshark preferences? Did you change anything in the default settings on your old laptop to see DICOM traffic (maybe it's not using the standard ports in your environment)?</p><p>Please compare the following settings on the old/new laptop:</p><blockquote><p><code>Edit -&gt; Preferences -&gt; DICOM</code><br />
<code>Analyze -&gt; Decode As -&gt; Show Current</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '13, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18535" class="comments-container"></div><div id="comment-tools-18535" class="comment-tools"></div><div class="clear"></div><div id="comment-18535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

