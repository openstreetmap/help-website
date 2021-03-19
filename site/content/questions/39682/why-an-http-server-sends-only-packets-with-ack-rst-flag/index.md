+++
type = "question"
title = "why an http server sends only packets with ACK RST flag"
description = '''Hello, I have found in traffic traces a strange phénomena that I can&#x27;t explained. The traffic comes from the repository mawilab. Among this traffic I have a strange thing. There is an http server (216.118.180.205 ) which sends only TCP packets with the RSt ACK flag. I wonder why its does such a thin...'''
date = "2015-02-06T05:57:00Z"
lastmod = "2015-02-09T15:56:00Z"
weight = 39682
keywords = [ "ack", "rst" ]
aliases = [ "/questions/39682" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [why an http server sends only packets with ACK RST flag](/questions/39682/why-an-http-server-sends-only-packets-with-ack-rst-flag)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39682-score" class="post-score" title="current number of votes">0</div><span id="post-39682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have found in traffic traces a strange phénomena that I can't explained. The traffic comes from the repository mawilab. Among this traffic I have a strange thing. There is an http server (216.118.180.205 ) which sends only TCP packets with the RSt ACK flag.</p><p>I wonder why its does such a thing. Why does it send these packets ? Here is a screenshot of this strange phenomena. It shows the traffic from and to the HTTP server. My question is why does it do such a thing. Is it an anomaly, a bug of the server, an attack ?...</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_du_2015-02-06_14:46:17.png" alt="alt text" /></p><p>Thaks in advance for any answer</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '15, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/c744601f20079b6eb8bd528fc55098a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="district9&#39;s gravatar image" /><p><span>district9</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="district9 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-39682" class="comments-container"><span id="39729"></span><div id="comment-39729" class="comment"><div id="post-39729-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The traffic comes from the repository mawilab.</p></blockquote><p>What is the "repository mawilab"?</p><p>BTW: Are you sure you are seeing the <strong>whole</strong> traffic while capturing the frames? Where and how did you capture that traffic?</p></div><div id="comment-39729-info" class="comment-info"><span class="comment-age">(09 Feb '15, 15:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-39682" class="comment-tools"></div><div class="clear"></div><div id="comment-39682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39708"></span>

<div id="answer-container-39708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39708-score" class="post-score" title="current number of votes">0</div><span id="post-39708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without a more detailed description of the origin of the capture file it's hard to tell what this is. It could be a TCP reset attack, although the information here is a bit limited.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39708" class="comments-container"></div><div id="comment-tools-39708" class="comment-tools"></div><div class="clear"></div><div id="comment-39708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

