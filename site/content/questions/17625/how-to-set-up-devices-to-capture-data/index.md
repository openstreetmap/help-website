+++
type = "question"
title = "How to set up devices to capture data"
description = '''I have a device that runs an embedded web server that I would like to capture packets from.  Since I can&#x27;t run Wireshark from the device, I am guessing that I will need to setup a PC (that&#x27;s running Wireshark) in front of the server. If my guess is correct, then I&#x27;m stuck on how to setup the PC to c...'''
date = "2013-01-11T13:33:00Z"
lastmod = "2013-01-12T07:27:00Z"
weight = 17625
keywords = [ "capture-setup" ]
aliases = [ "/questions/17625" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to set up devices to capture data](/questions/17625/how-to-set-up-devices-to-capture-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17625-score" class="post-score" title="current number of votes">0</div><span id="post-17625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device that runs an embedded web server that I would like to capture packets from.</p><p>Since I can't run Wireshark from the device, I am guessing that I will need to setup a PC (that's running Wireshark) in front of the server. If my guess is correct, then I'm stuck on how to setup the PC to capture packets going in/out of the server - (I searched this forum, but couldn't find any info on how to do this).</p><p>If I have the wrong idea on how to go about capturing data for a device that is unable to run Wireshark, please set me straight on what I need to do.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '13, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/1259897b9b42059302967b55c0dc2228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KTM&#39;s gravatar image" /><p><span>KTM</span><br />
<span class="score" title="76 reputation points">76</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KTM has one accepted answer">100%</span></p></div></div><div id="comments-container-17625" class="comments-container"></div><div id="comment-tools-17625" class="comment-tools"></div><div class="clear"></div><div id="comment-17625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17626"></span>

<div id="answer-container-17626" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17626-score" class="post-score" title="current number of votes">0</div><span id="post-17626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="KTM has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Obviously, the answer depends upon how the device is connected to a network; If ethernet then</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet capture setup</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jan '13, 14:14</strong> </span></p></div></div><div id="comments-container-17626" class="comments-container"><span id="17639"></span><div id="comment-17639" class="comment"><div id="post-17639-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link - I now need to find an "old" hub. I never realized that when devices are attached to an old hub, that the packets are sent to all ports of the old hub (as opposed to a specific port)... this inefficient way of sending packets over the hubbed network makes it possible for a Wireshark'd PC to see all packets that are going over the network.</p></div><div id="comment-17639-info" class="comment-info"><span class="comment-age">(12 Jan '13, 07:27)</span> <span class="comment-user userinfo">KTM</span></div></div></div><div id="comment-tools-17626" class="comment-tools"></div><div class="clear"></div><div id="comment-17626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

