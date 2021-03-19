+++
type = "question"
title = "Using Wireshark"
description = '''I&#x27;m new to wireshark and analyzing traces. I have a tcpdump from a linux system. Once opened in wireshark, how can I get the Ip address so show in xxx.xxx.xxx.xxx format and the protocol to show not in hex, so I know what I&#x27;m looking at?'''
date = "2011-05-11T05:59:00Z"
lastmod = "2011-05-11T09:08:00Z"
weight = 4032
keywords = [ "analysis", "format" ]
aliases = [ "/questions/4032" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark](/questions/4032/using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4032-score" class="post-score" title="current number of votes">0</div><span id="post-4032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to wireshark and analyzing traces. I have a tcpdump from a linux system. Once opened in wireshark, how can I get the Ip address so show in xxx.xxx.xxx.xxx format and the protocol to show not in hex, so I know what I'm looking at?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '11, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/465f5ceb8490d28a525e0bbf019f14c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mros2stf&#39;s gravatar image" /><p><span>mros2stf</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mros2stf has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>24 May '11, 22:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4032" class="comments-container"></div><div id="comment-tools-4032" class="comment-tools"></div><div class="clear"></div><div id="comment-4032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4040"></span>

<div id="answer-container-4040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4040-score" class="post-score" title="current number of votes">1</div><span id="post-4040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you open a trace file containing frames with IP inside Wireshark should decode IP addresses and everything else automatically. The protocol in hex is probably the ethernet protocol type you're looking at - it should be 0x0800 for IP, in which case you'll find the IP information in the next layers. If you see ethertypes other than 0x0800 you're not looking at IPv4 packets, thus not containing IPv4 addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '11, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4040" class="comments-container"></div><div id="comment-tools-4040" class="comment-tools"></div><div class="clear"></div><div id="comment-4040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

