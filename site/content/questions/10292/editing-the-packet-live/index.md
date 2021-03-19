+++
type = "question"
title = "Editing the packet live?"
description = '''Hi! I wonder if it is possible for Wireshark (or any compatible extension for Win7) to modify the packets being sent to the server based on some conditions (like checking the POST field value and taking action upon that)? For example, when sending an application/x-www-form-urlencoded with a field li...'''
date = "2012-04-19T10:56:00Z"
lastmod = "2012-04-19T16:45:00Z"
weight = 10292
keywords = [ "edit", "live", "modify", "packet" ]
aliases = [ "/questions/10292" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Editing the packet live?](/questions/10292/editing-the-packet-live)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10292-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I wonder if it is possible for Wireshark (or any compatible extension for Win7) to modify the packets being sent to the server based on some conditions (like checking the POST field value and taking action upon that)?</p><p>For example, when sending an application/x-www-form-urlencoded with a field like "login=user", is there a way to script it to change that to something like "login=otheruser"?</p></div><div id="question-tags" class="tags-container tags">edit live modify packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/931d7ae976d4b6bc0463ebc6f04a6a9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="detariael&#39;s gravatar image" /><p>detariael<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="detariael has no accepted answers">0%</span></p></div></div><div id="comments-container-10292" class="comments-container"></div><div id="comment-tools-10292" class="comment-tools"></div><div class="clear"></div><div id="comment-10292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10293"></span>

<div id="answer-container-10293" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10293-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, there isn't any way to do that.</p><p>Wireshark is an application for passively capturing network traffic, and the mechanisms it uses for capturing network traffic do not offer any ability to "edit" network traffic sent by or received by the machine on which it's running.</p><p>You'd have to find another tool to do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10293" class="comments-container"></div><div id="comment-tools-10293" class="comment-tools"></div><div class="clear"></div><div id="comment-10293-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10294"></span>

<div id="answer-container-10294" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10294-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark is a packet analyzer, not a packet generator. See the Wiki page on <a href="http://wiki.wireshark.org/Tools#Traffic_generators">tools</a> for some traffic generators that might help you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10294" class="comments-container"><span id="10301"></span><div id="comment-10301" class="comment"><div id="post-10301-score" class="comment-score">2</div><div class="comment-text"><p>A traffic generator might not help here, if the goal is to modify traffic sent by the machine on the fly. There may be tools that can insert themselves into the networking stack (meaning they'll need a kernel-mode driver) and do that sort of rewriting - but that sort of rewriting is a bit difficult, as it involves changing the <em>size</em> of a TCP segment.</p></div><div id="comment-10301-info" class="comment-info"><span class="comment-age">(19 Apr '12, 12:21)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10294" class="comment-tools"></div><div class="clear"></div><div id="comment-10294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10316"></span>

<div id="answer-container-10316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10316-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It sounds like what you are asking for is a general purpose man-in-the-middle security attack tool! Wireshark will not even show you the HTTP packets if they are going over HTTPS, as should be the case for anything for which the user identity makes a difference. (OK, Wireshark <em>will</em> decrypt the packets if you know the private key of the server's SSS/TLS certificate and capture the entire handshake.) If you control the browser being used, you can edit the values on the fly with a browser plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-10316" class="comments-container"><span id="10317"></span><div id="comment-10317" class="comment"><div id="post-10317-score" class="comment-score"></div><div class="comment-text"><p>It's HTTP only, so SSL encryption is not a problem in that case. Your comment about trying browser plugins is interesting though, I'll look into that (I'm not sure, however, if there is a one that'd let me modify the content of a POST request send through Flash, but maybe I'm dead wrong)!</p></div><div id="comment-10317-info" class="comment-info"><span class="comment-age">(19 Apr '12, 16:48)</span> detariael</div></div><span id="10318"></span><div id="comment-10318" class="comment"><div id="post-10318-score" class="comment-score"></div><div class="comment-text"><p>Going a little far afield for this forum, but try Charles Proxy which inserts itself as a man-in-the-middle HTTP proxy and can do scripted modification, or a tool like TamperData or Firebug in the browser. Only the Proxy approach can guarantee capturing the traffic originating within Flash, IMHO.</p></div><div id="comment-10318-info" class="comment-info"><span class="comment-age">(19 Apr '12, 16:51)</span> inetdog</div></div></div><div id="comment-tools-10316" class="comment-tools"></div><div class="clear"></div><div id="comment-10316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

