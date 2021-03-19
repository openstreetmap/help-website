+++
type = "question"
title = "record only 1 instance of source to destination ip and ignore any other communication"
description = '''We are doing an audit on a SPAN port to verify source ip traffic to destination for a week . Is there a way to only record 1 instance of ip hosts (source to destination) and then ignore any continuos communications between the 2 ? We realy dont need any more data and need to leave wireshark on for a...'''
date = "2015-07-17T05:15:00Z"
lastmod = "2015-07-17T05:19:00Z"
weight = 44235
keywords = [ "ip", "source", "destination", "to" ]
aliases = [ "/questions/44235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [record only 1 instance of source to destination ip and ignore any other communication](/questions/44235/record-only-1-instance-of-source-to-destination-ip-and-ignore-any-other-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are doing an audit on a SPAN port to verify source ip traffic to destination for a week . Is there a way to only record 1 instance of ip hosts (source to destination) and then ignore any continuos communications between the 2 ? We realy dont need any more data and need to leave wireshark on for about a week.</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">ip source destination to</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '15, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/9588e25af98c165fc3d6581e3affd093?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtrujillano&#39;s gravatar image" /><p>mtrujillano<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtrujillano has no accepted answers">0%</span></p></div></div><div id="comments-container-44235" class="comments-container"></div><div id="comment-tools-44235" class="comment-tools"></div><div class="clear"></div><div id="comment-44235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44237"></span>

<div id="answer-container-44237" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44237-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, Wireshark does not support adaptive filtering based on what it has seen in packets. You may want to look at Netflow statistics gathering which seems to be more like what you're looking for.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44237" class="comments-container"></div><div id="comment-tools-44237" class="comment-tools"></div><div class="clear"></div><div id="comment-44237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

