+++
type = "question"
title = "Capturing Omron FINS protocol: only responses are captured"
description = '''I want to look at the communication between a Win7 box and a PLC device. They speak the Omron FINS protocol over ethernet. However, Wireshark 1.8.3 is only able to capture the responses of the PLC, not my requests. There aren&#x27;t any problems with other protocols - they got captured correctly. The sou...'''
date = "2012-11-02T03:36:00Z"
lastmod = "2012-11-02T13:08:00Z"
weight = 15489
keywords = [ "omron", "capture", "fins" ]
aliases = [ "/questions/15489" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Omron FINS protocol: only responses are captured](/questions/15489/capturing-omron-fins-protocol-only-responses-are-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15489-score" class="post-score" title="current number of votes">0</div><span id="post-15489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to look at the communication between a Win7 box and a PLC device. They speak the <a href="http://wiki.wireshark.org/OMRON-FINS">Omron FINS protocol</a> over ethernet. However, Wireshark 1.8.3 is only able to capture the responses of the PLC, not my requests. There aren't any problems with other protocols - they got captured correctly.</p><p>The source PC is running Win7 x64 with Wireshark 1.8.3 64 bit and has a Broadcom 57xx Gbit NIC. Wireshark is started in promiscious mode without any filters. This PC is connected to an switch. The PLC device is also connected to this switch. We also tried to directly connect the PC to the PLC device with an ethernet cable - no change here.</p><p>What may be the problem here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-omron" rel="tag" title="see questions tagged &#39;omron&#39;">omron</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-fins" rel="tag" title="see questions tagged &#39;fins&#39;">fins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '12, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/9cd96b7e36437e7a66ac577656ca3814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abachmann&#39;s gravatar image" /><p><span>abachmann</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abachmann has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Nov '12, 07:01</strong> </span></p></div></div><div id="comments-container-15489" class="comments-container"><span id="15496"></span><div id="comment-15496" class="comment"><div id="post-15496-score" class="comment-score"></div><div class="comment-text"><p>Please edit your question to describe your capture setup, i.e. where are you capturing etc.</p></div><div id="comment-15496-info" class="comment-info"><span class="comment-age">(02 Nov '12, 05:53)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-15489" class="comment-tools"></div><div class="clear"></div><div id="comment-15489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15508"></span>

<div id="answer-container-15508" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15508-score" class="post-score" title="current number of votes">0</div><span id="post-15508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sometime software firewalls can cause these symptoms, especially 3rd party ones, e.g. Norton. The standard Windows one has never caused me issues.</p><p>If you do have 3rd party firewalls/anti-virus try disabling it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '12, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15508" class="comments-container"><span id="15511"></span><div id="comment-15511" class="comment"><div id="post-15511-score" class="comment-score"></div><div class="comment-text"><p>There is no 3rd party firewall installed and the Windows firewall is turned off. But there is Mcafee Antivirus installed, I will try disabling it. But why should it block only this traffic and no other packets like ARP or SMB?</p></div><div id="comment-15511-info" class="comment-info"><span class="comment-age">(02 Nov '12, 12:12)</span> <span class="comment-user userinfo">abachmann</span></div></div><span id="15515"></span><div id="comment-15515" class="comment"><div id="post-15515-score" class="comment-score"></div><div class="comment-text"><p>I have no idea, and this is purely anecdotal, but every machine I've ever had to look at for "issues" was improved by removing Mcafee or Norton if they were found to be infesting the machine.</p></div><div id="comment-15515-info" class="comment-info"><span class="comment-age">(02 Nov '12, 13:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-15508" class="comment-tools"></div><div class="clear"></div><div id="comment-15508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

