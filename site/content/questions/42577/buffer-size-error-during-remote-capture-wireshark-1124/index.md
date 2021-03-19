+++
type = "question"
title = "Buffer size error during remote capture (wireshark-1.12.4)"
description = '''I am performing remote capture between Linux and Windows machine. Remote machine is Linux and local machine is Windows. While doing this i came across a warning saying &quot;Couldn&#x27;t Set the capture buffer size!&quot; (attached the snapshot).  I am using Wireshark-1.12.4 version. Verified the same with Wiresh...'''
date = "2015-05-20T06:26:00Z"
lastmod = "2015-05-28T06:13:00Z"
weight = 42577
keywords = [ "remote-capture", "buffer-size" ]
aliases = [ "/questions/42577" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Buffer size error during remote capture (wireshark-1.12.4)](/questions/42577/buffer-size-error-during-remote-capture-wireshark-1124)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42577-score" class="post-score" title="current number of votes">0</div><span id="post-42577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am performing remote capture between Linux and Windows machine. Remote machine is Linux and local machine is Windows. While doing this i came across a warning saying "Couldn't Set the capture buffer size!" (attached the snapshot). <img src="https://osqa-ask.wireshark.org/upfiles/Buffer-Size-Error_xyPJZrv.jpg" alt="alt text" /> I am using Wireshark-1.12.4 version. Verified the same with Wireshark-1.6.1 and 1.10.8 it worked fine. Please let me know what could be the issue.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span> <span class="post-tag tag-link-buffer-size" rel="tag" title="see questions tagged &#39;buffer-size&#39;">buffer-size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '15, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/038e2af64c1850fba0f6a8274f316b47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sainath&#39;s gravatar image" /><p><span>Sainath</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sainath has no accepted answers">0%</span></p></img></div></div><div id="comments-container-42577" class="comments-container"></div><div id="comment-tools-42577" class="comment-tools"></div><div class="clear"></div><div id="comment-42577-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42582"></span>

<div id="answer-container-42582" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42582-score" class="post-score" title="current number of votes">1</div><span id="post-42582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sainath has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're basically running into a combination of problems:</p><ol><li>Bug 9067: Wireshark tries (and fails) to set the buffer size on remote capture devices (only if the buffer size is &gt; 1 Mbyte). It shouldn't even try.</li><li>(and) in 1.12 the default buffer size was increased to 2 Mb (which means you always run into (1)).</li></ol><p>For now you can ignore the annoying popup. Or change the buffer size of the capture device to 1 before starting the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '15, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-42582" class="comments-container"><span id="42614"></span><div id="comment-42614" class="comment"><div id="post-42614-score" class="comment-score"></div><div class="comment-text"><p>Hi Jeff,</p><p>This worked for me, i changed the buffer size to 1 Mb, the popup is not showing now. Thank you for your answer.</p><p>Sainath</p></div><div id="comment-42614-info" class="comment-info"><span class="comment-age">(22 May '15, 07:44)</span> <span class="comment-user userinfo">Sainath</span></div></div><span id="42730"></span><div id="comment-42730" class="comment"><div id="post-42730-score" class="comment-score"></div><div class="comment-text"><p>I merged a change which should fix this error, you can try an <a href="https://www.wireshark.org/download/automated/">automated build</a> with a sequence number of 707 or greater to see if it fixes the problem.</p></div><div id="comment-42730-info" class="comment-info"><span class="comment-age">(28 May '15, 06:13)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-42582" class="comment-tools"></div><div class="clear"></div><div id="comment-42582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

