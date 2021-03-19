+++
type = "question"
title = "Traffic slowing network"
description = '''Hello, I have an issue on 2 servers where there appears to be traffic that is slowing down the internet connection considerably. Appears to be a DoS. Does anything in this log stick out? I see constant external IP&#x27;s as a source, and destination as the LAN address: Transmission Control Protocol, Src ...'''
date = "2011-08-24T09:41:00Z"
lastmod = "2011-08-24T17:12:00Z"
weight = 5845
keywords = [ "traffic", "troubleshooting", "analysis" ]
aliases = [ "/questions/5845" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic slowing network](/questions/5845/traffic-slowing-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5845-score" class="post-score" title="current number of votes">0</div><span id="post-5845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have an issue on 2 servers where there appears to be traffic that is slowing down the internet connection considerably. Appears to be a DoS. Does anything in this log stick out? I see constant external IP's as a source, and destination as the LAN address:</p><pre><code>Transmission Control Protocol, Src Port: ms-wbt-server (3389), Dst Port: 4935 (4935), Seq: 1, Ack: 1, Len: 0

8   0.002206    217.18.199.100  10.0.1.41   TCP 60  ms-wbt-server &gt; 4935 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '11, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/e08707fd48751f3d66b0e4e2360ebba2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isilber&#39;s gravatar image" /><p><span>isilber</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isilber has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '11, 17:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5845" class="comments-container"></div><div id="comment-tools-5845" class="comment-tools"></div><div class="clear"></div><div id="comment-5845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5855"></span>

<div id="answer-container-5855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5855-score" class="post-score" title="current number of votes">0</div><span id="post-5855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have the same issue. Many of our servers are connection fast to outside ip's on port 3389 with source port 4935. Anyone know what this could be and how to fix it? We ran two different virusscanners, but both couldn't solve it. Our firewall crashes when I start 2 or more of these infected servers. Huge problem, can you help?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/b1abe8845c36c0c5c846fb0e5808f71b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sander&#39;s gravatar image" /><p><span>sander</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sander has no accepted answers">0%</span></p></div></div><div id="comments-container-5855" class="comments-container"></div><div id="comment-tools-5855" class="comment-tools"></div><div class="clear"></div><div id="comment-5855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5858"></span>

<div id="answer-container-5858" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5858-score" class="post-score" title="current number of votes">0</div><span id="post-5858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like the same exact problem. I have configured our firewall to block 3389 traffic from the affected machines LAN &gt; WAN...until i can resolve this problem.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/e08707fd48751f3d66b0e4e2360ebba2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="isilber&#39;s gravatar image" /><p><span>isilber</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="isilber has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-5858" class="comments-container"></div><div id="comment-tools-5858" class="comment-tools"></div><div class="clear"></div><div id="comment-5858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

