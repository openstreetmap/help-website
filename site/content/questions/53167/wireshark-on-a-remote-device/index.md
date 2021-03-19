+++
type = "question"
title = "Wireshark on a remote device"
description = '''Hi everyone, i want to use wireshark on my router, to see the traffic on the gateway of my network. So i&#x27;m trying to add as new interface my gateway but it doesn&#x27;t find it, even when is try with the login and password of my router...  I&#x27;m on W10, my wireshark version is 2.0.3, and i&#x27;m wired conneted...'''
date = "2016-06-03T02:00:00Z"
lastmod = "2016-06-03T02:58:00Z"
weight = 53167
keywords = [ "remote-capture" ]
aliases = [ "/questions/53167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on a remote device](/questions/53167/wireshark-on-a-remote-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53167-score" class="post-score" title="current number of votes">0</div><span id="post-53167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, i want to use wireshark on my router, to see the traffic on the gateway of my network. So i'm trying to add as new interface my gateway but it doesn't find it, even when is try with the login and password of my router... I'm on W10, my wireshark version is 2.0.3, and i'm wired conneted to ny router. Any help'll be very appreciated. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/cb0b7291f3b5ce37e2d51486150b8b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lyess2b&#39;s gravatar image" /><p><span>lyess2b</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lyess2b has no accepted answers">0%</span></p></div></div><div id="comments-container-53167" class="comments-container"></div><div id="comment-tools-53167" class="comment-tools"></div><div class="clear"></div><div id="comment-53167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53169"></span>

<div id="answer-container-53169" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53169-score" class="post-score" title="current number of votes">1</div><span id="post-53169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your router would need to support capture itself, and then Wireshark on your PC could use several methods to connect to, and control the remote capture.</p><p>The choices (currently) that I know of for remote capture are:</p><ul><li>Via pipes over ssh</li><li>Using the remote capture protocol rpcapd</li><li>Using the Wireshark extcap plugin sshdump</li></ul><p>However, all the above require your router to be able to run a capturing process, usually tcpdump. You need to ascertain if your router can do that, most unmodified home routers can't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53169" class="comments-container"></div><div id="comment-tools-53169" class="comment-tools"></div><div class="clear"></div><div id="comment-53169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

