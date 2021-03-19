+++
type = "question"
title = "TCP - CWND"
description = '''Is there any way to check CWND ?'''
date = "2015-04-18T22:14:00Z"
lastmod = "2015-04-19T02:22:00Z"
weight = 41566
keywords = [ "cwnd", "-", "tcp" ]
aliases = [ "/questions/41566" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP - CWND](/questions/41566/tcp-cwnd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to check CWND ?</p></div><div id="question-tags" class="tags-container tags">cwnd - tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '15, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p>srinu_bel<br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div></div><div id="comments-container-41566" class="comments-container"></div><div id="comment-tools-41566" class="comment-tools"></div><div class="clear"></div><div id="comment-41566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41569"></span>

<div id="answer-container-41569" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41569-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Similar question <a href="https://ask.wireshark.org/questions/27648/how-can-i-get-congestion-window-from-traces">here</a>.</p><p>Basically it is not something that you will see as a value in a packet capture.</p><p>If you have Linux on the sending host you can do the following:</p><ul><li>check the available and used congestion algorithm with "sysctl -a | grep congestion"</li><li>see the cwnd of all the established connections with "ss -ti"</li><li>see the cwnd for the last connections with "ip route show cache"</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '15, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-41569" class="comments-container"></div><div id="comment-tools-41569" class="comment-tools"></div><div class="clear"></div><div id="comment-41569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41567"></span>

<div id="answer-container-41567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41567-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, not from packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '15, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41567" class="comments-container"></div><div id="comment-tools-41567" class="comment-tools"></div><div class="clear"></div><div id="comment-41567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

