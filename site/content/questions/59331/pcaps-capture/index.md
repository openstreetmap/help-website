+++
type = "question"
title = "pcaps capture"
description = '''Hello Everybody, I the following situation. I have one PC with two wireless cards (NICs) and one laptop. The one NIC is responsible for an Access point, let&#x27;s say MyAP and the other one is a normal receiver, let&#x27;s say PC_Recv. I want to ping from PC_Recv to MyAP and then do the same thing backwards,...'''
date = "2017-02-10T07:44:00Z"
lastmod = "2017-02-10T08:14:00Z"
weight = 59331
keywords = [ "capture", "pcaps" ]
aliases = [ "/questions/59331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pcaps capture](/questions/59331/pcaps-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59331-score" class="post-score" title="current number of votes">0</div><span id="post-59331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Everybody,</p><p>I the following situation. I have one PC with two wireless cards (NICs) and one laptop. The one NIC is responsible for an Access point, let's say MyAP and the other one is a normal receiver, let's say PC_Recv. I want to ping from PC_Recv to MyAP and then do the same thing backwards, ping from MyAP to PC_Recv. After that I want capture pcaps for these pings from my laptop. The PC and laptop are connected in one network via hostapd (MyAP).</p><p>so, could someone tell me how do I capture pcaps from above? Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-pcaps" rel="tag" title="see questions tagged &#39;pcaps&#39;">pcaps</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '17, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/cac26d51acd54f6a2df9a7a675426adf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Euclid&#39;s gravatar image" /><p><span>Euclid</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Euclid has no accepted answers">0%</span></p></div></div><div id="comments-container-59331" class="comments-container"></div><div id="comment-tools-59331" class="comment-tools"></div><div class="clear"></div><div id="comment-59331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59333"></span>

<div id="answer-container-59333" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59333-score" class="post-score" title="current number of votes">0</div><span id="post-59333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't need to view the packets live, I would install wireshark on the PC, capture the traffic on the interfaces that you are interested in (MyAP and PC_Recv), save the file, and transfer to your laptop and view the capture file there.</p><p>If you need to view the traffic live, you should be able to do that also. The exact method would depend on your setup. Do you have Windows installed on both computers? The easiest solution I can think of, and others may have better suggestions, is to just use a remote desktop program (TeamViewer, NX, LogMeIn, etc) to connect from the laptop to the PC. The PC is still the one capturing the packets in wireshark, but you can see them from the laptop, and save off a file if you need to. A slightly more complicated solution would involve installing cygwin and ssh on both machines (unless you have Linux, then you should already have the tools installed). You could monitor the packets like this:</p><p>From the laptop (with cygwin and ssh installed):</p><pre><code>ssh [email protected] &quot;tshark -i &lt;PC-INTERFACE1&gt; -s0 -U -F pcapng -w - &quot; | wireshark -k -i -</code></pre><p>This will run tshark on the PC and will output the packets to standard output, which then gets sent over the ssh tunnel to your laptop, which then gets fed into wireshark and displayed on your laptop. This would take some further configuration to start the ssh server on the PC (openssh) and get the tshark executable in the path. But it is a handy tool to have once you get it working.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '17, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/e96b0196e8e968b1a2d8f6ddfda87ab1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lemurshark&#39;s gravatar image" /><p><span>Lemurshark</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lemurshark has no accepted answers">0%</span></p></div></div><div id="comments-container-59333" class="comments-container"></div><div id="comment-tools-59333" class="comment-tools"></div><div class="clear"></div><div id="comment-59333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

