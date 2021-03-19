+++
type = "question"
title = "Multiple ACKs Dup-ACKs and Out-of-Order packets"
description = '''Hello, I&#x27;m trying to troubleshoot an issue we are experiencing with a cloud based solution. Several of our users are complaining about severe latency. We&#x27;ve exempted the site from our Web Filter which has usually fixed these types of issues but, this time it has not. We&#x27;ve gotten several packet capt...'''
date = "2016-05-03T13:01:00Z"
lastmod = "2016-05-03T13:18:00Z"
weight = 52186
keywords = [ "ack", "dup", "tlsv1.2", "out-of-order", "seq" ]
aliases = [ "/questions/52186" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple ACKs Dup-ACKs and Out-of-Order packets](/questions/52186/multiple-acks-dup-acks-and-out-of-order-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52186-score" class="post-score" title="current number of votes">0</div><span id="post-52186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/seq_number_etc.PNG" alt="alt text" />Hello, I'm trying to troubleshoot an issue we are experiencing with a cloud based solution. Several of our users are complaining about severe latency. We've exempted the site from our Web Filter which has usually fixed these types of issues but, this time it has not. We've gotten several packet captures but the one that I'll provide seems to speak to the issue directly. In this packet capture I am seeing the same sequence number re-appear several times. Also, I'm seeing a bunch of Out-of-Order packets as well Dup ACKs. We think that the issue is on the remote end, possibly too many TLSv1.2 renegotiations real-time which is causing the data to have to be resent/re-acked. Can you take a look and let me know if you are seeing the same thing or point out some problems that maybe we are overlooking? I have the full capture but cannot figure out how to attach it.... anyone help me with this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-dup" rel="tag" title="see questions tagged &#39;dup&#39;">dup</span> <span class="post-tag tag-link-tlsv1.2" rel="tag" title="see questions tagged &#39;tlsv1.2&#39;">tlsv1.2</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span> <span class="post-tag tag-link-seq" rel="tag" title="see questions tagged &#39;seq&#39;">seq</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/89dfbf4981224d54fdcfdac449ad9e82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MadCapper&#39;s gravatar image" /><p><span>MadCapper</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MadCapper has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '16, 13:06</strong> </span></p></div></div><div id="comments-container-52186" class="comments-container"><span id="52189"></span><div id="comment-52189" class="comment"><div id="post-52189-score" class="comment-score"></div><div class="comment-text"><p>You cannot attach a capture. The way to do it is to publish it, login-free, somewhere at Cloudshark (preferred by the community here), Google Drive, Dropbox, ... and edit your Question with a link to it.</p></div><div id="comment-52189-info" class="comment-info"><span class="comment-age">(03 May '16, 13:18)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52186" class="comment-tools"></div><div class="clear"></div><div id="comment-52186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

