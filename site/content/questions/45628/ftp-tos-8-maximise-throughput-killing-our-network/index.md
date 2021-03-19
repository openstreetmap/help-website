+++
type = "question"
title = "ftp tos 8 Maximise throughput killing our network"
description = '''I have a problem on my network where ftp transfers are taking all the bandwidth and bypassing all the QoS configured. This is actually causing voice calls to drop when a ftp transfer is taking place. My management station shows that packets are coming in with a &#x27;ToS of 8 Maximise throughput&#x27;. On the...'''
date = "2015-09-04T03:29:00Z"
lastmod = "2015-09-07T16:44:00Z"
weight = 45628
keywords = [ "ftp", "centos", "tos" ]
aliases = [ "/questions/45628" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ftp tos 8 Maximise throughput killing our network](/questions/45628/ftp-tos-8-maximise-throughput-killing-our-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45628-score" class="post-score" title="current number of votes">0</div><span id="post-45628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem on my network where ftp transfers are taking all the bandwidth and bypassing all the QoS configured. This is actually causing voice calls to drop when a ftp transfer is taking place.</p><p>My management station shows that packets are coming in with a 'ToS of 8 Maximise throughput'. On the wireshark trace taken at the source I believe this is shown.</p><p>Question is what to do about it:) Is this normal ftp-data behaviour to have ToS 8 set? Its hosted on a linux box under AWS which I am told was a out of the box config.</p><p>Differentiated Services Field: <strong>0x08 (DSCP 0x02: Unknown DSCP; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-tos" rel="tag" title="see questions tagged &#39;tos&#39;">tos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '15, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/faf64296259c376719e7eefedea20cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leelaw&#39;s gravatar image" /><p><span>leelaw</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leelaw has no accepted answers">0%</span></p></div></div><div id="comments-container-45628" class="comments-container"><span id="45679"></span><div id="comment-45679" class="comment"><div id="post-45679-score" class="comment-score"></div><div class="comment-text"><blockquote><p>where ftp transfers are taking all the bandwidth and bypassing all the QoS configured.</p></blockquote><p>some questions:</p><ul><li>ftp transfer from where to where?</li><li>where exactly did you configure QoS?</li><li>can you provide a capture file?</li></ul><blockquote><p>Is this normal ftp-data behaviour to have ToS 8 set?</p></blockquote><p>Maybe, it depends on your FTP software and possibly also it's configuration.</p><blockquote><p>killing our network</p></blockquote><p>What exactly do you mean by <strong>killing the network</strong>? Does that mean you can't work any longer on the local network, or do you mean internet download speed, or anything else?</p></div><div id="comment-45679-info" class="comment-info"><span class="comment-age">(07 Sep '15, 16:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45628" class="comment-tools"></div><div class="clear"></div><div id="comment-45628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

