+++
type = "question"
title = "filter traffic by protocol"
description = '''I want to use a command line filter to sort out the traffic by protocol. For example, how can I show other traffic aside from http? Also how can I then get a count of how many TCP sessions exist my packet capture?'''
date = "2013-10-15T13:45:00Z"
lastmod = "2013-10-15T14:19:00Z"
weight = 26021
keywords = [ "protocol" ]
aliases = [ "/questions/26021" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filter traffic by protocol](/questions/26021/filter-traffic-by-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26021-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use a command line filter to sort out the traffic by protocol. For example, how can I show other traffic aside from http? Also how can I then get a count of how many TCP sessions exist my packet capture?</p></div><div id="question-tags" class="tags-container tags">protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '13, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/2edb03e305750de4edc73c5cec02a057?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jayhawk100&#39;s gravatar image" /><p>jayhawk100<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jayhawk100 has no accepted answers">0%</span></p></div></div><div id="comments-container-26021" class="comments-container"></div><div id="comment-tools-26021" class="comment-tools"></div><div class="clear"></div><div id="comment-26021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26022"></span>

<div id="answer-container-26022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26022-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several ways of doing this. A simple display filter like "not tcp.port==80" (or whatever port http is using) will do it.</p><p>Also, Statistics, Conversations (TCP Tab) will show you how many streams are in play.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span></p></div></div><div id="comments-container-26022" class="comments-container"><span id="26025"></span><div id="comment-26025" class="comment"><div id="post-26025-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I figured I could use a filter syntax like "not http",etc. For the second question, how would I get those conversation statistics from the command line? I don't have the gui on my older linux OS.</p></div><div id="comment-26025-info" class="comment-info"><span class="comment-age">(15 Oct '13, 15:00)</span> jayhawk100</div></div><span id="26031"></span><div id="comment-26031" class="comment"><div id="post-26031-score" class="comment-score">1</div><div class="comment-text"><p>tshark -z conv,tcp -q -r somefilehere.pcap</p><p>-z says give me the stats for tcp conversation -q says give me the summary and not a per packet info.</p></div><div id="comment-26031-info" class="comment-info"><span class="comment-age">(15 Oct '13, 17:26)</span> hansangb</div></div></div><div id="comment-tools-26022" class="comment-tools"></div><div class="clear"></div><div id="comment-26022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

