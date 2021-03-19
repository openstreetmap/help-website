+++
type = "question"
title = "Unable to capture data that browser Chrome can get."
description = '''In order to diagnose this problem, I restarted the computer. I open browser Chrome to stream MJPEG from address: http://172.16.80.1. Everything works flawlessly. The video is smooth. Wireshark does not capture anything from address 172.16.80.1.  Address 172.16.80.1 is the address of a Windows Phone ...'''
date = "2017-03-03T07:28:00Z"
lastmod = "2017-03-08T05:29:00Z"
weight = 59830
keywords = [ "capture" ]
aliases = [ "/questions/59830" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture data that browser Chrome can get.](/questions/59830/unable-to-capture-data-that-browser-chrome-can-get)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59830-score" class="post-score" title="current number of votes">0</div><span id="post-59830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In order to diagnose this problem, I restarted the computer. I open browser Chrome to stream MJPEG from address: <a href="http://172.16.80.1">http://172.16.80.1</a>. Everything works flawlessly. The video is smooth. Wireshark does not capture anything from address 172.16.80.1.<br />
</p><p>Address 172.16.80.1 is the address of a Windows Phone emulator. The options in Wireshark are the following: <img src="https://osqa-ask.wireshark.org/upfiles/wire_shark_optionspng.png" alt="alt text" /></p><p>Could anyone shed some light on this/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '17, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/e23332dc51869f08737cc96395284e59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hong&#39;s gravatar image" /><p><span>Hong</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hong has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-59830" class="comments-container"><span id="59921"></span><div id="comment-59921" class="comment"><div id="post-59921-score" class="comment-score"></div><div class="comment-text"><p>Could you turn your comment into an answer that I can accept?</p></div><div id="comment-59921-info" class="comment-info"><span class="comment-age">(08 Mar '17, 05:21)</span> <span class="comment-user userinfo">Hong</span></div></div></div><div id="comment-tools-59830" class="comment-tools"></div><div class="clear"></div><div id="comment-59830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59867"></span>

<div id="answer-container-59867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59867-score" class="post-score" title="current number of votes">0</div><span id="post-59867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks as though the capture library you have installed (WinPcap??) is unable to capture on that interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '17, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59867" class="comments-container"><span id="59922"></span><div id="comment-59922" class="comment"><div id="post-59922-score" class="comment-score"></div><div class="comment-text"><p>Presumably then, you've done something different, maybe installed npcap?</p></div><div id="comment-59922-info" class="comment-info"><span class="comment-age">(08 Mar '17, 05:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59867" class="comment-tools"></div><div class="clear"></div><div id="comment-59867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

