+++
type = "question"
title = "packet_write_wait during SSH connection (Unexplained SSH disconnection)"
description = '''Hi guys,  I am trying to debug an odd SSH disconnection issue. I am logging in from my laptop to a server (which is a vmware vm) and every few minutes or even within one minute, I am thrown out of the SSH session. The message that appears with -vvvv is:  packet_write_wait: Connection to &amp;lt;host&amp;gt;...'''
date = "2017-02-13T05:21:00Z"
lastmod = "2017-02-13T05:21:00Z"
weight = 59367
keywords = [ "ssh", "packet" ]
aliases = [ "/questions/59367" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet\_write\_wait during SSH connection (Unexplained SSH disconnection)](/questions/59367/packet_write_wait-during-ssh-connection-unexplained-ssh-disconnection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59367-score" class="post-score" title="current number of votes">0</div><span id="post-59367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I am trying to debug an odd SSH disconnection issue. I am logging in from my laptop to a server (which is a vmware vm) and every few minutes or even within one minute, I am thrown out of the SSH session. The message that appears with -vvvv is:</p><p>packet_write_wait: Connection to &lt;host&gt; port 22: Broken pipe</p><p>Now, there could be problems outside the scope of networking, such as duplicate MAC address/IP address assigned to this vm. But without bugging the vm folks, is there a way that I can at least point out where the problem lies?</p><p>&lt;debugging_done&gt;</p><p>1) I must mention that I am seeing heavy packet losses in the vm. The RX drop counter is totally off the chart.</p><p>2) The kernel module in use is vmxnet3. Kernel is 3.10.0-327.el7.x86_64.</p><p>3) In my client side tcpdump (from my laptop), I am seeing that a RST packet is being sent from the vm (apparently a zero window packet). Could that be problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '17, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/f036e4a90a3f289bea20d87dee796736?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="costeira&#39;s gravatar image" /><p><span>costeira</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="costeira has no accepted answers">0%</span></p></div></div><div id="comments-container-59367" class="comments-container"></div><div id="comment-tools-59367" class="comment-tools"></div><div class="clear"></div><div id="comment-59367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

