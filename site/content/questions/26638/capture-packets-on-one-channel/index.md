+++
type = "question"
title = "capture packets on one channel"
description = '''Hi, how can I configure Wireshark to capture packets on only one channel? I can&#x27;t seem to find that option.'''
date = "2013-11-03T05:31:00Z"
lastmod = "2013-12-13T08:34:00Z"
weight = 26638
keywords = [ "capture", "packets", "channel", "one" ]
aliases = [ "/questions/26638" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture packets on one channel](/questions/26638/capture-packets-on-one-channel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26638-score" class="post-score" title="current number of votes">0</div><span id="post-26638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, how can I configure Wireshark to capture packets on only one channel? I can't seem to find that option.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-channel" rel="tag" title="see questions tagged &#39;channel&#39;">channel</span> <span class="post-tag tag-link-one" rel="tag" title="see questions tagged &#39;one&#39;">one</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '13, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/412b10652e55b9c4d3cc5243b7b58d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myrddin&#39;s gravatar image" /><p><span>myrddin</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myrddin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Nov '13, 08:57</strong> </span></p></div></div><div id="comments-container-26638" class="comments-container"><span id="26643"></span><div id="comment-26643" class="comment"><div id="post-26643-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "channel"? Network card? Transmit/Receive?</p></div><div id="comment-26643-info" class="comment-info"><span class="comment-age">(03 Nov '13, 12:15)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="26646"></span><div id="comment-26646" class="comment"><div id="post-26646-score" class="comment-score"></div><div class="comment-text"><p>Wi-Fi channel?</p></div><div id="comment-26646-info" class="comment-info"><span class="comment-age">(03 Nov '13, 14:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="26655"></span><div id="comment-26655" class="comment"><div id="post-26655-score" class="comment-score"></div><div class="comment-text"><p>Yes, I wanted to use only one Wi-Fi channel because there are some open networks that interfere with my own, so I wanted to avoid them, but then I found out how to filter out what I need, so i don't need it any more</p></div><div id="comment-26655-info" class="comment-info"><span class="comment-age">(04 Nov '13, 04:53)</span> <span class="comment-user userinfo">myrddin</span></div></div><span id="26660"></span><div id="comment-26660" class="comment"><div id="post-26660-score" class="comment-score"></div><div class="comment-text"><p>It would have been easier to help you, if you had been (much) more precise in the question ;-)</p></div><div id="comment-26660-info" class="comment-info"><span class="comment-age">(04 Nov '13, 05:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26638" class="comment-tools"></div><div class="clear"></div><div id="comment-26638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28081"></span>

<div id="answer-container-28081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28081-score" class="post-score" title="current number of votes">0</div><span id="post-28081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just in case someone finds this old thread and isn't helped by the snarky comments:</p><p>I'm using Kali 1.0, an old Dell Laptop, and a TPE-N150USBL radio. Before I fired-up Wireshark I forced the radio to my desired channel (4 in my case) with this command:</p><p>iwconfig wlan1 channel 4</p><p>My network interface was wlan1 but make sure to set yours appropriately.</p><p>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 08:34</strong></p><img src="https://secure.gravatar.com/avatar/ad883964cc6044648ecaf083e3ae5991?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fervor&#39;s gravatar image" /><p><span>fervor</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fervor has no accepted answers">0%</span></p></div></div><div id="comments-container-28081" class="comments-container"></div><div id="comment-tools-28081" class="comment-tools"></div><div class="clear"></div><div id="comment-28081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

