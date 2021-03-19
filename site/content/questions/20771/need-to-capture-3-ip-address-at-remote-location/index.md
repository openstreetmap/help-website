+++
type = "question"
title = "Need to capture 3 IP address at remote location"
description = '''I need to use wireshark to capture packets to and from 3 specific IP addresses. I have never used Wireshark before. I would like to set the capture to monitor the 3 IP addresses for 5 days. I an at a loss trying to set it up from my machine. Thanks in advance.'''
date = "2013-04-24T09:57:00Z"
lastmod = "2013-08-24T23:10:00Z"
weight = 20771
keywords = [ "specific", "ip", "remote", "wireshark" ]
aliases = [ "/questions/20771" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to capture 3 IP address at remote location](/questions/20771/need-to-capture-3-ip-address-at-remote-location)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20771-score" class="post-score" title="current number of votes">0</div><span id="post-20771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to use wireshark to capture packets to and from 3 specific IP addresses. I have never used Wireshark before. I would like to set the capture to monitor the 3 IP addresses for 5 days. I an at a loss trying to set it up from my machine. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-specific" rel="tag" title="see questions tagged &#39;specific&#39;">specific</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '13, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/b14fdc9a8ea8f29482ab029888442bf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mugwione19&#39;s gravatar image" /><p><span>Mugwione19</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mugwione19 has no accepted answers">0%</span></p></div></div><div id="comments-container-20771" class="comments-container"></div><div id="comment-tools-20771" class="comment-tools"></div><div class="clear"></div><div id="comment-20771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20843"></span>

<div id="answer-container-20843" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20843-score" class="post-score" title="current number of votes">0</div><span id="post-20843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The placement of a sniffer is very important to get your desired results. Typically, a sniffer would be placed with visibility of the interesting traffic (your 3 IPs). This could be a WAN port for example, or inline via a network tap, or via a SPAN port.<br />
To do an extended capture for 5 days I would use dumpcap with a HOST filter since it's stateless and you can use ring buffers to manage the storage.</p><p>Since you have not used Wireshark before, I highly recommend you experiment with it on your local interface and LAN first.<br />
There are many ways to study up on Protocol Analysis. I would get Laura Chappell's Wireshark Network Analysis book, and check out <a href="http://wiresharktraining.com">http://wiresharktraining.com</a></p><p>Wireshark is a great tool, but your synopsis doesn't offer enough topology information to offer a more specific solution, sorry.</p><p>Hope this is helpful though, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '13, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-20843" class="comments-container"><span id="24001"></span><div id="comment-24001" class="comment"><div id="post-24001-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>That was very informative. However would it be possible to sniff out without being physically near to the target machine? The methods outlined above would require one to have a close proximity to hardware in question.</p><p>Thanks</p></div><div id="comment-24001-info" class="comment-info"><span class="comment-age">(24 Aug '13, 10:57)</span> <span class="comment-user userinfo">igodspeed</span></div></div><span id="24015"></span><div id="comment-24015" class="comment"><div id="post-24015-score" class="comment-score"></div><div class="comment-text"><p>You need to sniff something in the line-of-path of traffic to and from the target machines. Where exactly to do that depends on your network topology.</p></div><div id="comment-24015-info" class="comment-info"><span class="comment-age">(24 Aug '13, 23:10)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-20843" class="comment-tools"></div><div class="clear"></div><div id="comment-20843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

