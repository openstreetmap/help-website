+++
type = "question"
title = "SSH login getting terminated after entering user name"
description = '''Hi All, I am trying to login to the linux based device via SSH port i.e., 22 using putty. When trying to login, device is prompting for User name, but after entering to the device, ssh session terminates. Captured log using wireshark tool while performing this. Pasted below for your reference. Can a...'''
date = "2017-02-20T01:48:00Z"
lastmod = "2017-02-21T05:26:00Z"
weight = 59548
keywords = [ "ssh" ]
aliases = [ "/questions/59548" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSH login getting terminated after entering user name](/questions/59548/ssh-login-getting-terminated-after-entering-user-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59548-score" class="post-score" title="current number of votes">0</div><span id="post-59548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I am trying to login to the linux based device via SSH port i.e., 22 using putty. When trying to login, device is prompting for User name, but after entering to the device, ssh session terminates. Captured log using wireshark tool while performing this. Pasted below for your reference. Can anyone help me what would be a reason for this kind of behavior.</p><p>In this image, could see that device (IP address 172.27.129.134) is sending FIN,ACK to the Client.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/WiresharkLog.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '17, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/c1c05f08f9deab44525c00ce3b061428?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chandrashekar_MV&#39;s gravatar image" /><p><span>Chandrasheka...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chandrashekar_MV has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59548" class="comments-container"><span id="59549"></span><div id="comment-59549" class="comment"><div id="post-59549-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-59549-info" class="comment-info"><span class="comment-age">(20 Feb '17, 02:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="59553"></span><div id="comment-59553" class="comment"><div id="post-59553-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, Please view captured log from the below link:</p><p><a href="https://www.cloudshark.org/captures/6485a02ba3df?filter=ip.addr%3D%3D172.27.129.134">https://www.cloudshark.org/captures/6485a02ba3df?filter=ip.addr%3D%3D172.27.129.134</a></p></div><div id="comment-59553-info" class="comment-info"><span class="comment-age">(20 Feb '17, 05:56)</span> <span class="comment-user userinfo">Chandrasheka...</span></div></div></div><div id="comment-tools-59548" class="comment-tools"></div><div class="clear"></div><div id="comment-59548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59580"></span>

<div id="answer-container-59580" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59580-score" class="post-score" title="current number of votes">0</div><span id="post-59580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The capture does show, as mentioned in your question, the server closing the connection after the second packet of encrypted data from the client.</p><p>Unfortunately this is all that the capture can tell us, Wireshark is unable to decrypt SSH sessions. To determine why the server application closed the connection you will need to inspect the ssh logs on the server, possibly turning on debug logging to assist.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '17, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59580" class="comments-container"></div><div id="comment-tools-59580" class="comment-tools"></div><div class="clear"></div><div id="comment-59580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

