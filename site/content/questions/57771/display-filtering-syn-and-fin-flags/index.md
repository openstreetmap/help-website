+++
type = "question"
title = "Display filtering SYN and FIN flags"
description = '''I am having a hard time finding a way to Display filter packets with SYN+FIN combo, regardless if other flags are set. Would this be the correct syntax? tcp.flags.syn==1 &amp;amp;&amp;amp; tcp.flags.fin==1 When i do this but use other flags that one would expect together, the results only give me packets wi...'''
date = "2016-12-01T14:09:00Z"
lastmod = "2016-12-02T00:58:00Z"
weight = 57771
keywords = [ "tcpflags", "wireshark", "display-filter" ]
aliases = [ "/questions/57771" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display filtering SYN and FIN flags](/questions/57771/display-filtering-syn-and-fin-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57771-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having a hard time finding a way to Display filter packets with SYN+FIN combo, regardless if other flags are set. Would this be the correct syntax? tcp.flags.syn==1 &amp;&amp; tcp.flags.fin==1 When i do this but use other flags that one would expect together, the results only give me packets with either one or the other flag set. I need packets with BOTH set. someone please help?</p></div><div id="question-tags" class="tags-container tags">tcpflags wireshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '16, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/c4371d9aef8fe4aaee67a67498c8cf0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sonocroc&#39;s gravatar image" /><p>sonocroc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sonocroc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Dec '16, 14:10</p></div></div><div id="comments-container-57771" class="comments-container"></div><div id="comment-tools-57771" class="comment-tools"></div><div class="clear"></div><div id="comment-57771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57778"></span>

<div id="answer-container-57778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57778-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tcp.flags.syn==1 &amp;&amp; tcp.flags.fin==1</code> is the correct filter to get all packets with SYN and FIN flag set - which should never happen as it's an invalid combination. If you see that kind of flag set it's usually a scan tool doing it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '16, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-57778" class="comments-container"></div><div id="comment-tools-57778" class="comment-tools"></div><div class="clear"></div><div id="comment-57778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

