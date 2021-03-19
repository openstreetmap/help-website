+++
type = "question"
title = "Wireshark with .NET WCF?"
description = '''Hi, I have a .NET WCF service running on my computer (in IIS7) that communicates over secured (certificate) TCP with my client (also on my computer). Now I need to clarify if my data really is secured (encrypted). When using the Microsoft tools like Service Trace Viewer it seems like it is not. I ha...'''
date = "2010-10-22T08:10:00Z"
lastmod = "2010-10-25T02:43:00Z"
weight = 585
keywords = [ "wireshark" ]
aliases = [ "/questions/585" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark with .NET WCF?](/questions/585/wireshark-with-net-wcf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-585-score" class="post-score" title="current number of votes">0</div><span id="post-585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>Hi,</strong></p><p>I have a .NET WCF service running on my computer (in IIS7) that communicates over secured (certificate) TCP with my client (also on my computer). Now I need to clarify if my data really is secured (encrypted). When using the Microsoft tools like Service Trace Viewer it seems like it is not.</p><p>I have installed Wireshark and have selected the correct interface (my network card). When starting the capture a lot of packages will be shown, so first I filter it by tcp then by src (my local ip address). This reduces the number of packages but when running my application (doing some calls to the service) I can´t see them in Wireshark? I am probably using wrong filters. Please help!</p><p><strong>BestRegards</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '10, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/796412036ad598411b1dfeecec631d37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Snowman&#39;s gravatar image" /><p><span>Snowman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Snowman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '10, 07:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-585" class="comments-container"><span id="594"></span><div id="comment-594" class="comment"><div id="post-594-score" class="comment-score"></div><div class="comment-text"><p>Can you provide the filter details? Can you recheck your filter?</p><p>Are you using capture filters or display filters?</p></div><div id="comment-594-info" class="comment-info"><span class="comment-age">(22 Oct '10, 15:39)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div><span id="600"></span><div id="comment-600" class="comment"><div id="post-600-score" class="comment-score"></div><div class="comment-text"><p>Capture filters was set to : tcp and src 192.168.0.30</p><p>Then the display filter was set to xml.</p></div><div id="comment-600-info" class="comment-info"><span class="comment-age">(23 Oct '10, 00:03)</span> <span class="comment-user userinfo">Snowman</span></div></div></div><div id="comment-tools-585" class="comment-tools"></div><div class="clear"></div><div id="comment-585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="603"></span>

<div id="answer-container-603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-603-score" class="post-score" title="current number of votes">0</div><span id="post-603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With both server and client on the same platform your packets will go through the loopback interface, not your network interface. Therefore you don't see them flowing out of your network connection, hence Wireshark doesn't see them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '10, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-603" class="comments-container"><span id="604"></span><div id="comment-604" class="comment"><div id="post-604-score" class="comment-score"></div><div class="comment-text"><p>Okay, so I must have the client and server on two separated computers? I can´t run them both from the same computer?</p></div><div id="comment-604-info" class="comment-info"><span class="comment-age">(23 Oct '10, 12:49)</span> <span class="comment-user userinfo">Snowman</span></div></div><span id="605"></span><div id="comment-605" class="comment"><div id="post-605-score" class="comment-score"></div><div class="comment-text"><p>http://wiki.wireshark.org/CaptureSetup/Loopback has information which may be of help ....</p></div><div id="comment-605-info" class="comment-info"><span class="comment-age">(23 Oct '10, 12:58)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="613"></span><div id="comment-613" class="comment"><div id="post-613-score" class="comment-score"></div><div class="comment-text"><p>Thanks! We solved it by setting up two computers (server and client) and we got the communication flow as expected.</p></div><div id="comment-613-info" class="comment-info"><span class="comment-age">(25 Oct '10, 02:43)</span> <span class="comment-user userinfo">Snowman</span></div></div></div><div id="comment-tools-603" class="comment-tools"></div><div class="clear"></div><div id="comment-603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

