+++
type = "question"
title = "How do I get TCP problem list?"
description = '''I need to use wireshark for a couple hours and list all the TCP problems like &quot;zero window&quot; and &quot;window update&quot;. Where do I find that information after a capture? thanks'''
date = "2012-02-19T13:27:00Z"
lastmod = "2012-02-19T15:21:00Z"
weight = 9132
keywords = [ "tcp" ]
aliases = [ "/questions/9132" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I get TCP problem list?](/questions/9132/how-do-i-get-tcp-problem-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9132-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to use wireshark for a couple hours and list all the TCP problems like "zero window" and "window update". Where do I find that information after a capture? thanks</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '12, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/a3db010ac66d0db9efa2f8296a9cf25b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sssddd&#39;s gravatar image" /><p>sssddd<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sssddd has no accepted answers">0%</span></p></div></div><div id="comments-container-9132" class="comments-container"></div><div id="comment-tools-9132" class="comment-tools"></div><div class="clear"></div><div id="comment-9132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9133"></span>

<div id="answer-container-9133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9133-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just put in the display filter "<code>tcp.analysis.flags</code>". Please keep in mind that not all those messages are in fact "problems". A "Window Update" for example can be pretty much ignored if it doesn't include any delays for the TCP communication.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '12, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9133" class="comments-container"></div><div id="comment-tools-9133" class="comment-tools"></div><div class="clear"></div><div id="comment-9133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9135"></span>

<div id="answer-container-9135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9135-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>its not easy to determine what these 'problems mean' and more importantly, how to address it.</p><p>I've got some info on my website @ http://www.thetechfirm.com and google is your friend.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '12, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p>thetechfirm<br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-9135" class="comments-container"></div><div id="comment-tools-9135" class="comment-tools"></div><div class="clear"></div><div id="comment-9135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

