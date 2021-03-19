+++
type = "question"
title = "How to install wireshark while disabling Live Monitor"
description = '''I need to install wireshark to read PCAP files, while at the same time disabling the Live Monitoring feature so that we cannot access sensitive data on our corporate network. Is there there a way to do this? I&#x27;ve read that there is on several articles, but none actually post anything as far as the a...'''
date = "2014-03-11T15:48:00Z"
lastmod = "2014-03-11T15:55:00Z"
weight = 30695
keywords = [ "disable", "monitor" ]
aliases = [ "/questions/30695" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to install wireshark while disabling Live Monitor](/questions/30695/how-to-install-wireshark-while-disabling-live-monitor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30695-score" class="post-score" title="current number of votes">0</div><span id="post-30695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to install wireshark to read PCAP files, while at the same time disabling the Live Monitoring feature so that we cannot access sensitive data on our corporate network.</p><p>Is there there a way to do this?</p><p>I've read that there is on several articles, but none actually post anything as far as the actual process.</p><p>Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '14, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/2d008f9ee5bdb15aa941439d271f6ef8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="countryboyofal&#39;s gravatar image" /><p><span>countryboyofal</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="countryboyofal has no accepted answers">0%</span></p></div></div><div id="comments-container-30695" class="comments-container"></div><div id="comment-tools-30695" class="comment-tools"></div><div class="clear"></div><div id="comment-30695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30696"></span>

<div id="answer-container-30696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30696-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30696-score" class="post-score" title="current number of votes">0</div><span id="post-30696-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Install Wireshark, but skip the installation of WinPCAP (if on Windows). On Linux, non-root users cannot capture anyway, unless given the specific rights.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '14, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30696" class="comments-container"></div><div id="comment-tools-30696" class="comment-tools"></div><div class="clear"></div><div id="comment-30696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30698"></span>

<div id="answer-container-30698" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30698-score" class="post-score" title="current number of votes">0</div><span id="post-30698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a very similar question</p><blockquote><p><a href="http://ask.wireshark.org/questions/29455/how-can-a-business-use-wireshark-and-disable-live-packet-sniffing">http://ask.wireshark.org/questions/29455/how-can-a-business-use-wireshark-and-disable-live-packet-sniffing</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '14, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30698" class="comments-container"></div><div id="comment-tools-30698" class="comment-tools"></div><div class="clear"></div><div id="comment-30698-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

