+++
type = "question"
title = "Problems with Cassandra CQL"
description = '''I am having problems with viewing CQL. I am using WS 2.2.0rc2 (just released yesterday). I load the pcap and it comes up as TCP frames. I try to do &quot;Analyze-&amp;gt;Decode As...&quot; using CQL, it rescans the file and, again, displays as TCP frames. In the early frames from my Cassandra box I can see &quot;CQL_V...'''
date = "2016-09-01T07:58:00Z"
lastmod = "2016-09-01T09:59:00Z"
weight = 55270
keywords = [ "cql" ]
aliases = [ "/questions/55270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problems with Cassandra CQL](/questions/55270/problems-with-cassandra-cql)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having problems with viewing CQL. I am using WS 2.2.0rc2 (just released yesterday). I load the pcap and it comes up as TCP frames. I try to do "Analyze-&gt;Decode As..." using CQL, it rescans the file and, again, displays as TCP frames.</p><p>In the early frames from my Cassandra box I can see "CQL_VERSION....3.4.2". In the release notes it says "New Protocol Support" "Apache Cassandra - CQL version 3.0". Is this an issue with a minor release of CQL?</p></div><div id="question-tags" class="tags-container tags">cql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '16, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/46b87b223691d3d8951ebf7afae18d77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ekleinpaste&#39;s gravatar image" /><p>ekleinpaste<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ekleinpaste has no accepted answers">0%</span></p></div></div><div id="comments-container-55270" class="comments-container"></div><div id="comment-tools-55270" class="comment-tools"></div><div class="clear"></div><div id="comment-55270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55272"></span>

<div id="answer-container-55272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55272-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It could very well be. The dissector checks the very first byte of every packet and if it's not 0x03 or 0x83 then it will spit it out. If you can share the capture file this could be confirmed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Sep '16, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55272" class="comments-container"><span id="55273"></span><div id="comment-55273" class="comment"><div id="post-55273-score" class="comment-score"></div><div class="comment-text"><p>That is it. They start with 0x04 and 0x84. Where would you like the capture file to go?</p></div><div id="comment-55273-info" class="comment-info"><span class="comment-age">(01 Sep '16, 10:36)</span> ekleinpaste</div></div><span id="55274"></span><div id="comment-55274" class="comment"><div id="post-55274-score" class="comment-score"></div><div class="comment-text"><p>Either attached to a bug report, on cloudshark.org, or any other publicly accessible place.</p></div><div id="comment-55274-info" class="comment-info"><span class="comment-age">(01 Sep '16, 13:31)</span> Jaap ♦</div></div><span id="55294"></span><div id="comment-55294" class="comment"><div id="post-55294-score" class="comment-score"></div><div class="comment-text"><p>I created a trial account on cloudshark.org and uploaded CQL-3-4-2.cap.gz. I did not see a choice for doing a bug report.</p></div><div id="comment-55294-info" class="comment-info"><span class="comment-age">(02 Sep '16, 07:25)</span> ekleinpaste</div></div><span id="55298"></span><div id="comment-55298" class="comment"><div id="post-55298-score" class="comment-score"></div><div class="comment-text"><p>Wireshark bug report should be submitted at bugs.wireshark.org</p></div><div id="comment-55298-info" class="comment-info"><span class="comment-age">(02 Sep '16, 07:38)</span> Bill Meier ♦♦</div></div><span id="55303"></span><div id="comment-55303" class="comment"><div id="post-55303-score" class="comment-score"></div><div class="comment-text"><p>Bug submitted on bugs.wireshark.org. Bug 12818.</p></div><div id="comment-55303-info" class="comment-info"><span class="comment-age">(02 Sep '16, 10:49)</span> ekleinpaste</div></div></div><div id="comment-tools-55272" class="comment-tools"></div><div class="clear"></div><div id="comment-55272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

