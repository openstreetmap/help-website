+++
type = "question"
title = "SMB vs NBSS, swapping 2 identical APs and getting different output."
description = '''Hello, First of all, thanks in advance for all of your expert opinions. I am attempting to get a better understanding of expected behavior during a file transfer, and whether what I am seeing is normal or abnormal. I have two packet captures between a WLC and Windows Laptop where we are doing a file...'''
date = "2017-07-09T19:50:00Z"
lastmod = "2017-07-09T19:50:00Z"
weight = 62629
keywords = [ "smb", "nbss" ]
aliases = [ "/questions/62629" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB vs NBSS, swapping 2 identical APs and getting different output.](/questions/62629/smb-vs-nbss-swapping-2-identical-aps-and-getting-different-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62629-score" class="post-score" title="current number of votes">0</div><span id="post-62629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>First of all, thanks in advance for all of your expert opinions.</p><p>I am attempting to get a better understanding of expected behavior during a file transfer, and whether what I am seeing is normal or abnormal. I have two packet captures between a WLC and Windows Laptop where we are doing a file transfer to test qos changes on the network. During one file transfer I am seeing the process happen through SMB packets, which I understand to be expected behavior. When I switch out the Access Point with another identical Access Point I am instead getting "NBSS 1485 Continuation Messages." The problem with this is that it appears that the "NBSS 1485 Continuation Messages" has a DSCP value of EF instead of the expected data traffic default of 0. This, in turn, could mean that data traffic is being transferred at the highest priority level, which could interfere with our Voip devices.</p><p>I see from one of the prior posts regarding NBSS that this possibly "means that the "previous segment" wasn't captured because it didn't make it to the machine running Wireshark, i.e. a packet got lost in transit."</p><p>Also stated within that post was "Wireshark couldn't reassemble the message (NetBIOS Session Service, "NBSS", over TCP - port 139 - which is used to transport SMB in older systems such as OS/2) because the chunk was missing, but it inferred from port 139 that it's NBSS, so it assumed it was a continuation of an earlier message as it didn't begin with an SMB header. It probably was a continuation, but there was a piece missing before it."</p><p>Is the DSCP marking of "NBSS 1485 Continuation Messages" an expected behavior designed to prioritize the re transmission of lost packets that can create conflicts on a network utilizing qos? Are the NBSS packets in fact transmitting at DSCP EF? Do our device prioritize using SMB to transfer files and then defer to NBSS as a fall-back which then is prioritized at DSCP EF?</p><p>Anything you can do to assist my understanding of NBSS and SMB would be appreciated. Thank you all for your time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-nbss" rel="tag" title="see questions tagged &#39;nbss&#39;">nbss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '17, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/ee58389e6b49e9bc04e206e6ebd698a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlphaHertz&#39;s gravatar image" /><p><span>AlphaHertz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlphaHertz has no accepted answers">0%</span></p></div></div><div id="comments-container-62629" class="comments-container"></div><div id="comment-tools-62629" class="comment-tools"></div><div class="clear"></div><div id="comment-62629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

