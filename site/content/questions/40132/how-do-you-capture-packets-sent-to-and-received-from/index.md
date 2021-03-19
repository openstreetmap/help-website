+++
type = "question"
title = "How do you capture packets sent to and received from..."
description = '''We have an iSeries server receiving an RST and we want to trace the client side to verify it is sending the RST, but it&#x27;s only capturing what the iSeries sent to the PC. How can I capture both send and received packets?'''
date = "2015-02-27T07:40:00Z"
lastmod = "2015-02-27T14:40:00Z"
weight = 40132
keywords = [ "receive", "capture", "packets", "send" ]
aliases = [ "/questions/40132" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do you capture packets sent to and received from...](/questions/40132/how-do-you-capture-packets-sent-to-and-received-from)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40132-score" class="post-score" title="current number of votes">0</div><span id="post-40132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have an iSeries server receiving an RST and we want to trace the client side to verify it is sending the RST, but it's only capturing what the iSeries sent to the PC. How can I capture both send and received packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-receive" rel="tag" title="see questions tagged &#39;receive&#39;">receive</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-send" rel="tag" title="see questions tagged &#39;send&#39;">send</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '15, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/b3e4ea484bfab5e8734882703cca2cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="radclan&#39;s gravatar image" /><p><span>radclan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="radclan has no accepted answers">0%</span></p></div></div><div id="comments-container-40132" class="comments-container"><span id="40135"></span><div id="comment-40135" class="comment"><div id="post-40135-score" class="comment-score"></div><div class="comment-text"><p>how do you capture on the client? How does the client connect to the network? If it's WiFi, you cannot capture what the card is sending in most cases because wireless is half duplex.</p></div><div id="comment-40135-info" class="comment-info"><span class="comment-age">(27 Feb '15, 09:41)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="40136"></span><div id="comment-40136" class="comment"><div id="post-40136-score" class="comment-score"></div><div class="comment-text"><p>the client is the pc with an Intel(R) 82579LM Gigabit network connection, I've been doing more research and several people mention VPN, Firewall or Security software on their PC's that are blocking outgoing traffic. We have not found the right combination of services to stop to get this to work.</p></div><div id="comment-40136-info" class="comment-info"><span class="comment-age">(27 Feb '15, 09:55)</span> <span class="comment-user userinfo">radclan</span></div></div><span id="40140"></span><div id="comment-40140" class="comment"><div id="post-40140-score" class="comment-score"></div><div class="comment-text"><p>Stopping the services may not be enough, they might have to be removed all together (it isn't pretty, but true).</p></div><div id="comment-40140-info" class="comment-info"><span class="comment-age">(27 Feb '15, 14:40)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-40132" class="comment-tools"></div><div class="clear"></div><div id="comment-40132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

