+++
type = "question"
title = "What is  meaning and effect FCS checksum error in MODBUS Communication ?"
description = '''Hi, I have one Device from SCHNEIDER ( 192.168.0.41) send modbus request to Prosoft device ( 192.168.0.154/155). In this Modbus Communication I am getting one error response. After Query and Respond communication Schneider Unit send error message to Prosoft device. Frame Check Sequence 0xf6e37764 Me...'''
date = "2014-04-16T02:51:00Z"
lastmod = "2014-04-17T02:24:00Z"
weight = 31872
keywords = [ "modbus" ]
aliases = [ "/questions/31872" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is meaning and effect FCS checksum error in MODBUS Communication ?](/questions/31872/what-is-meaning-and-effect-fcs-checksum-error-in-modbus-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31872-score" class="post-score" title="current number of votes">0</div><span id="post-31872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have one Device from SCHNEIDER ( 192.168.0.41) send modbus request to Prosoft device ( 192.168.0.154/155). In this Modbus Communication I am getting one error response.</p><p>After Query and Respond communication Schneider Unit send error message to Prosoft device.</p><p>Frame Check Sequence 0xf6e37764 Message : Bad CheckSum</p><p>I want to understand meaning of this message.</p><p>Thanmks!</p><p>Log photo <a href="http://www.sendspace.com/filegroup/7HhNqafkEw0aGnxHfqsNNg">alt text</a></p><p>Wireshark Log</p><p><img src="http://www.sendspace.com/file/g5bwfb" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/066244a23b152aaa862f5b198500f2d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lalitvedak&#39;s gravatar image" /><p><span>lalitvedak</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lalitvedak has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '14, 05:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-31872" class="comments-container"></div><div id="comment-tools-31872" class="comment-tools"></div><div class="clear"></div><div id="comment-31872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31878"></span>

<div id="answer-container-31878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31878-score" class="post-score" title="current number of votes">0</div><span id="post-31878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Turn off the Ethernet protocol preference "Assume packets have FCS". Either through the preferences dialog or by right clicking the Ethernet part of the frame in the packet details pane following the Protcol Preferences link on the menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31878" class="comments-container"><span id="31908"></span><div id="comment-31908" class="comment"><div id="post-31908-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your replay. I want to understand meaning of this message. Is send and received is activity is successful or partially completed ? Thanks</p></div><div id="comment-31908-info" class="comment-info"><span class="comment-age">(16 Apr '14, 23:08)</span> <span class="comment-user userinfo">lalitvedak</span></div></div><span id="31916"></span><div id="comment-31916" class="comment"><div id="post-31916-score" class="comment-score"></div><div class="comment-text"><p>Turning off the protocol preference allows the Modbus dissection to proceed and all the requests and responses looked good to me.</p><p>Did you try it, and if so did you see any issues?</p></div><div id="comment-31916-info" class="comment-info"><span class="comment-age">(17 Apr '14, 02:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-31878" class="comment-tools"></div><div class="clear"></div><div id="comment-31878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

