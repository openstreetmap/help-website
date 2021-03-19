+++
type = "question"
title = "Remote Interface"
description = '''OK, here goes. I have a Win 7 box on our corporate network running Wireshark 1.12.3. I am attempting to contact a device within another network using the Remote Interface option. The designer of the device has showed me how to set this up (and how well it works) if the computer is on the same net as...'''
date = "2015-02-06T10:59:00Z"
lastmod = "2016-01-29T16:32:00Z"
weight = 39687
keywords = [ "remote" ]
aliases = [ "/questions/39687" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Interface](/questions/39687/remote-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39687-score" class="post-score" title="current number of votes">0</div><span id="post-39687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, here goes.</p><p>I have a Win 7 box on our corporate network running Wireshark 1.12.3. I am attempting to contact a device within another network using the Remote Interface option. The designer of the device has showed me how to set this up (and how well it works) if the computer is on the same net as the device. So... I am creating a tunnel to a machine attached to both networks. The tunnel connects perfectly, when I hit the forwarded port to the device I get a full list of the interfaces back as exppected. The trouble comes when I select the interface then hit "Start". I get</p><p>Error while capturing packets: Is the server properly installed on 127.0.0.1? connect() failed: No connection could be made because the target machine actively refused it. (code 10061)</p><p>Anybody have any thoughts? I am listening to port 2002 on the target device.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '15, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/cea4a0c80514b8cad793e8a8cbce7b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wadelouky&#39;s gravatar image" /><p><span>wadelouky</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wadelouky has no accepted answers">0%</span></p></div></div><div id="comments-container-39687" class="comments-container"><span id="39688"></span><div id="comment-39688" class="comment"><div id="post-39688-score" class="comment-score"></div><div class="comment-text"><p>Sorry I forgot about this other error I have gotten a couple of times.</p><p>The capture session could not be initiated on interface 'rpcap://[127.0.0.1]:1234/eth0' (Unknown error (pcap bug; actual error cause not reported))</p></div><div id="comment-39688-info" class="comment-info"><span class="comment-age">(06 Feb '15, 11:02)</span> <span class="comment-user userinfo">wadelouky</span></div></div><span id="49639"></span><div id="comment-49639" class="comment"><div id="post-49639-score" class="comment-score"></div><div class="comment-text"><p>When you say "127.0.0.1", do you mean "127.0.0.1", or are you hiding the real IP address from public view by using the loopback IP address?</p></div><div id="comment-49639-info" class="comment-info"><span class="comment-age">(29 Jan '16, 16:32)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-39687" class="comment-tools"></div><div class="clear"></div><div id="comment-39687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39725"></span>

<div id="answer-container-39725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39725-score" class="post-score" title="current number of votes">0</div><span id="post-39725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>in the windows empire error code 10061 means TCP RESET, so the port you are trying to connect to is not open (anymore).</p><p>It sounds like you created a SSH tunnel (port forwarding), so the reason for the TCP RESET could be:</p><ul><li>your local ssh client stopped listening to port 2002 (test with netstat -na)</li><li>the remote sshd stopped forwarding port 2002 to the target (check the sshd debug logs)</li><li>the remote rpcap daemon stopped listening to whatever port it was configured to listen to, maybe also 2002 (check with netstat -na).</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39725" class="comments-container"></div><div id="comment-tools-39725" class="comment-tools"></div><div class="clear"></div><div id="comment-39725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

