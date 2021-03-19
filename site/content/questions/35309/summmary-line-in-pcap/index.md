+++
type = "question"
title = "Summmary line in pcap"
description = '''Does the summary line in pcap follow a specific format. I have a dump from wireshark based on only the summary line and i need to add tcp/ip analysis based on ftp/http/icmp etc. Any suggestions'''
date = "2014-08-07T08:50:00Z"
lastmod = "2014-08-07T08:53:00Z"
weight = 35309
keywords = [ "line", "pcap", "summary" ]
aliases = [ "/questions/35309" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Summmary line in pcap](/questions/35309/summmary-line-in-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35309-score" class="post-score" title="current number of votes">0</div><span id="post-35309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does the summary line in pcap follow a specific format. I have a dump from wireshark based on only the summary line and i need to add tcp/ip analysis based on ftp/http/icmp etc. Any suggestions</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-line" rel="tag" title="see questions tagged &#39;line&#39;">line</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-summary" rel="tag" title="see questions tagged &#39;summary&#39;">summary</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '14, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/d6363f2cb7b8c054a0ecca0e803c595e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anilkumarxceed&#39;s gravatar image" /><p><span>anilkumarxceed</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anilkumarxceed has no accepted answers">0%</span></p></div></div><div id="comments-container-35309" class="comments-container"></div><div id="comment-tools-35309" class="comment-tools"></div><div class="clear"></div><div id="comment-35309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35310"></span>

<div id="answer-container-35310" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35310-score" class="post-score" title="current number of votes">0</div><span id="post-35310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The content of the summary line in Wireshark is specified by the highest level dissector, e.g. if you have a TCP packet with no payload the TCP dissector decides what to put in. For HTTP packets, its the HTTP dissector, etc.</p><p>If you need to add more details you should just configure all columns to show what you need, and then use the "Export packet dissections" to CSV feature to save the list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35310" class="comments-container"></div><div id="comment-tools-35310" class="comment-tools"></div><div class="clear"></div><div id="comment-35310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

