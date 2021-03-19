+++
type = "question"
title = "Create delta column - pkt timestamp &amp; FIX SendingTime"
description = '''Could someone let me know if it&#x27;s possible to create a column that displays the delta between a packet&#x27;s arrival time and the FIX SendingTime in the payload? I have the two timestamps in adjacent columns - just not sure how to add a delta column. Many thanks, Tim'''
date = "2013-04-23T06:49:00Z"
lastmod = "2013-04-23T07:28:00Z"
weight = 20734
keywords = [ "fix" ]
aliases = [ "/questions/20734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create delta column - pkt timestamp & FIX SendingTime](/questions/20734/create-delta-column-pkt-timestamp-fix-sendingtime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could someone let me know if it's possible to create a column that displays the delta between a packet's arrival time and the FIX SendingTime in the payload? I have the two timestamps in adjacent columns - just not sure how to add a delta column.</p><p>Many thanks,</p><p>Tim</p></div><div id="question-tags" class="tags-container tags">fix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/31534d84848dcc810494dce199a020f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timchampion&#39;s gravatar image" /><p>Timchampion<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timchampion has no accepted answers">0%</span></p></div></div><div id="comments-container-20734" class="comments-container"></div><div id="comment-tools-20734" class="comment-tools"></div><div class="clear"></div><div id="comment-20734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20735"></span>

<div id="answer-container-20735" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20735-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Could someone let me know if it's possible to create a column that displays the delta between a packet's arrival time and the FIX SendingTime in the payload?</p></blockquote><p>Unfortunately that's not possible without (a rather big) change of the Wireshark code.</p><blockquote><p>I have the two timestamps in adjacent columns - just not sure how to add a delta column.</p></blockquote><p>You could 'print' the columns you need with tshark and then use a script (perl, python, etc.) to calculate the delta time.</p><blockquote><p><code>tshark -nr FIX.cap -T fields -e frame.number -e frame.time  -e fix.SendingTime -e ip.src -e ip.dst -E separator=;</code><br />
</p></blockquote><p>or</p><blockquote><p><code>tshark -nr FIX.cap -T fields -e frame.number -e frame.time_epoch  -e fix.SendingTime -e ip.src -e ip.dst -E separator=;</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '13, 07:29</p></div></div><div id="comments-container-20735" class="comments-container"></div><div id="comment-tools-20735" class="comment-tools"></div><div class="clear"></div><div id="comment-20735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

