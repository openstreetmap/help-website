+++
type = "question"
title = "Capture packets from my Broadband Modem"
description = '''Hi Experts, I have an UTStarCom ADSL2+ modem in my home for Braodband internet connection.  Is it possbile to capture packets flowing in/out of my modem. Cheers, Arun'''
date = "2013-08-02T23:37:00Z"
lastmod = "2014-07-02T16:11:00Z"
weight = 23522
keywords = [ "broadband", "capture", "broadcast", "packet", "in" ]
aliases = [ "/questions/23522" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packets from my Broadband Modem](/questions/23522/capture-packets-from-my-broadband-modem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23522-score" class="post-score" title="current number of votes">0</div><span id="post-23522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>I have an UTStarCom ADSL2+ modem in my home for Braodband internet connection.</p><p>Is it possbile to capture packets flowing in/out of my modem.</p><p>Cheers, Arun</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadband" rel="tag" title="see questions tagged &#39;broadband&#39;">broadband</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '13, 23:37</strong></p><img src="https://secure.gravatar.com/avatar/b789dd708d1d221f00d970bb10a0758a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20N&#39;s gravatar image" /><p><span>Arun N</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun N has no accepted answers">0%</span></p></div></div><div id="comments-container-23522" class="comments-container"></div><div id="comment-tools-23522" class="comment-tools"></div><div class="clear"></div><div id="comment-23522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23650"></span>

<div id="answer-container-23650" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23650-score" class="post-score" title="current number of votes">2</div><span id="post-23650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possbile to capture packets flowing in/out of my modem.</p></blockquote><p>at the DSL (WAN) side: <strong>No</strong>. Only with special (expensive) hardware.</p><p>at the ethernet (LAN) side: <strong>Yes</strong>. Please read the following wiki article:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>Basically you need a way to capture the whole traffic at the ethernet level. The easiest way is to use an ethernet hub (hard to get one these days) or a small switch with port mirroring capabilities (very cheap these days). See the answers to the following question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/13892/port-mirror-switch">http://ask.wireshark.org/questions/13892/port-mirror-switch</a><br />
</p></blockquote><p>or the Wiki</p><blockquote><p><a href="http://wiki.wireshark.org/SwitchReference">http://wiki.wireshark.org/SwitchReference</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23650" class="comments-container"></div><div id="comment-tools-23650" class="comment-tools"></div><div class="clear"></div><div id="comment-23650-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34370"></span>

<div id="answer-container-34370" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34370-score" class="post-score" title="current number of votes">0</div><span id="post-34370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Would you really need to see the dsl or atm layer? That's what the error stats are for. FEC/HEC/CRC's etc..</p><p>I work for a UK ISP and need to capture/record all incoming/outgoing web traffic (due to weird issue) and suspect the best solution would be a packet sniffer on a PC. Auth on PC via router in 'modem only' mode. Critical to ensure the only MAC presented on the WAN is that of your ethernet NIC - then sniff away! :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '14, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/0faa51a5447a43474874167bd2b86645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsporsche&#39;s gravatar image" /><p><span>jsporsche</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsporsche has no accepted answers">0%</span></p></div></div><div id="comments-container-34370" class="comments-container"></div><div id="comment-tools-34370" class="comment-tools"></div><div class="clear"></div><div id="comment-34370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

