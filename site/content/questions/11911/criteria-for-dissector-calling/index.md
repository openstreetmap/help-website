+++
type = "question"
title = "Criteria for dissector calling"
description = '''Hi, allI am a newbie on dissector development. I have a question about the &quot;dissector_add( )&quot; function. I went through a few examples, most of them are using &quot;tcp.port&quot; or &quot;udp.port&quot; or something like that.My dissector not uses any port number to instruct wireshark to pass packets to my dissector, i...'''
date = "2012-06-14T17:50:00Z"
lastmod = "2012-06-15T15:32:00Z"
weight = 11911
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/11911" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Criteria for dissector calling](/questions/11911/criteria-for-dissector-calling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11911-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, allI am a newbie on dissector development. I have a question about the "dissector_add( )" function.</p><p>I went through a few examples, most of them are using "tcp.port" or "udp.port" or something like <a href="http://that.My">that.My</a> dissector not uses any port number to instruct wireshark to pass packets to my dissector, instead i want it to be called only when eth.dst is of certain pattern and i don't want to use heuristic dissector coz that's getting complicated.</p><p>So i was wondering if we have any way to get my dissector called for all packets ?</p></div><div id="question-tags" class="tags-container tags">plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '12, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11911" class="comments-container"></div><div id="comment-tools-11911" class="comment-tools"></div><div class="clear"></div><div id="comment-11911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11980"></span>

<div id="answer-container-11980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11980-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to know how dissection chaining works in the case, have a look at epan/dissectors/packet-udp.c and epan/dissectors/packet-tcp.c. They each have a call to register_dissector_table(), one with "udp.port", the other with "tcp.port". Now look at epan/dissectors/packet-eth.c, it doesn't have one, so that won't work.</p><p>What it does have is register_heur_dissector_list("eth",...) which is used when the frame comes in. That would be perfect for you. Check if the destination address is yours/dissect/return true, otherwise simply return false.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-11980" class="comments-container"></div><div id="comment-tools-11980" class="comment-tools"></div><div class="clear"></div><div id="comment-11980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

