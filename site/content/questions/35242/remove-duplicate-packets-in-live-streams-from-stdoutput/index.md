+++
type = "question"
title = "Remove duplicate packets in live streams (from stdoutput)"
description = '''Hi, is it possible to remove duplicate packets not from a pcap file, but from a stream of packets from standard output? In other words, I would like to remove duplicates on-the-fly (with of course some buffering delay). editcap doesn&#x27;t seem to provide that, but I might be mistaken. Thank you in adva...'''
date = "2014-08-05T23:25:00Z"
lastmod = "2014-08-06T01:28:00Z"
weight = 35242
keywords = [ "editcap" ]
aliases = [ "/questions/35242" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remove duplicate packets in live streams (from stdoutput)](/questions/35242/remove-duplicate-packets-in-live-streams-from-stdoutput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35242-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is it possible to remove duplicate packets not from a pcap file, but from a stream of packets from standard output? In other words, I would like to remove duplicates on-the-fly (with of course some buffering delay). editcap doesn't seem to provide that, but I might be mistaken.</p><p>Thank you in advance for the help.</p></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '14, 23:25</strong></p><img src="https://secure.gravatar.com/avatar/56f7d19bf1e586b1578061391861d7f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Al%20Bundy&#39;s gravatar image" /><p>Al Bundy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Al Bundy has no accepted answers">0%</span></p></div></div><div id="comments-container-35242" class="comments-container"><span id="35249"></span><div id="comment-35249" class="comment"><div id="post-35249-score" class="comment-score"></div><div class="comment-text"><p>Honestly, I can't imagine an environment where that would be necessary. Could you please add a real world use case?</p></div><div id="comment-35249-info" class="comment-info"><span class="comment-age">(06 Aug '14, 01:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-35242" class="comment-tools"></div><div class="clear"></div><div id="comment-35242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35248"></span>

<div id="answer-container-35248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35248-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The only way to do that that I know of is to use a special capture card or "intelligent" hardware TAP (both in the price range of at least 4 digits). I haven't seen a software solution that would do this on the fly. And you're right, editcap only works on pcap files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '14, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35248" class="comments-container"></div><div id="comment-tools-35248" class="comment-tools"></div><div class="clear"></div><div id="comment-35248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

