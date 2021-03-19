+++
type = "question"
title = "Wireshark format error when capturing on multiple USB interfaces on the same machine"
description = '''Hi, I am trying to run tshark on mutliple USB interfaces using the below command. Note that, in both HUBs multiple USB devices are connected. Also, when I am running on both interfaces separately, it runs perfectly. tshark.exe -i 5 -i 6 Error:  Can anyone please help me on this. Thanks in advance!!'''
date = "2017-05-30T08:26:00Z"
lastmod = "2017-05-30T22:08:00Z"
weight = 61701
keywords = [ "multiple-interfaces" ]
aliases = [ "/questions/61701" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark format error when capturing on multiple USB interfaces on the same machine](/questions/61701/wireshark-format-error-when-capturing-on-multiple-usb-interfaces-on-the-same-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61701-score" class="post-score" title="current number of votes">0</div><span id="post-61701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to run tshark on mutliple USB interfaces using the below command. Note that, in both HUBs multiple USB devices are connected. Also, when I am running on both interfaces separately, it runs perfectly.</p><p><em>tshark.exe -i 5 -i 6</em></p><p><strong>Error:</strong></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled_ew0tB2g.png" alt="alt text" /></p><p>Can anyone please help me on this.</p><p>Thanks in advance!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multiple-interfaces" rel="tag" title="see questions tagged &#39;multiple-interfaces&#39;">multiple-interfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '17, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/3e1c00d8a265b252f8c00be1f4570801?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ganesan&#39;s gravatar image" /><p><span>Ganesan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ganesan has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 May '17, 08:26</strong> </span></p></div></div><div id="comments-container-61701" class="comments-container"></div><div id="comment-tools-61701" class="comment-tools"></div><div class="clear"></div><div id="comment-61701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61702"></span>

<div id="answer-container-61702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61702-score" class="post-score" title="current number of votes">0</div><span id="post-61702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For some reason, dumpcap (which is what tshark is running to capture the traffic) thinks it's reading something from a pipe.</p><p>This appears to be a bug. Please file a bug about this at <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '17, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61702" class="comments-container"><span id="61705"></span><div id="comment-61705" class="comment"><div id="post-61705-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Guy Harris. Created Bug 13742. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13742">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13742</a></p></div><div id="comment-61705-info" class="comment-info"><span class="comment-age">(30 May '17, 22:08)</span> <span class="comment-user userinfo">Ganesan</span></div></div></div><div id="comment-tools-61702" class="comment-tools"></div><div class="clear"></div><div id="comment-61702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

