+++
type = "question"
title = "Follow TCP Stream troubleshooting"
description = '''I have just installed the latest Wireshark on my Macbook Pro. I want to analyze some pcaps that were sent to me. I can open the pcap files just fine, and all looks normal on the screen. However, when I go to filter on &#x27;TCP&#x27; and apply the filter, nothing happens. Moreover, when I right-click on the r...'''
date = "2014-01-21T16:18:00Z"
lastmod = "2014-01-24T07:53:00Z"
weight = 29075
keywords = [ "filter", "troubleshooting", "display-filter" ]
aliases = [ "/questions/29075" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Follow TCP Stream troubleshooting](/questions/29075/follow-tcp-stream-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29075-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have just installed the latest Wireshark on my Macbook Pro. I want to analyze some pcaps that were sent to me. I can open the pcap files just fine, and all looks normal on the screen. However, when I go to filter on 'TCP' and apply the filter, nothing happens. Moreover, when I right-click on the row/packet I am interested in, nothing happens.</p><p>Any thoughts or ideas are appreciated.</p></div><div id="question-tags" class="tags-container tags">filter troubleshooting display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '14, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/a25ca05f584f15956e10edd42ce0bd5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slinky&#39;s gravatar image" /><p>slinky<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slinky has no accepted answers">0%</span></p></div></div><div id="comments-container-29075" class="comments-container"></div><div id="comment-tools-29075" class="comment-tools"></div><div class="clear"></div><div id="comment-29075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29142"></span>

<div id="answer-container-29142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29142-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>when I go to filter on 'TCP' and apply the filter, nothing happens.</p></blockquote><p>well, if the first few frames (the ones visible in Wireshark) are all TCP, you won't see any difference if you apply the display filter: <code>tcp</code> ;-) Is that the case?</p><blockquote><p>Moreover, when I right-click on the row/packet I am interested in, <strong>nothing happens</strong></p></blockquote><p>What does that actually mean? Don't you get a pop-menu where you can select "Follow TCP Stream" (and other options)?</p><p>If so, here are some questions</p><ul><li>what is your OS version</li><li>what is your Wireshark version</li><li>is there anything special on your system, like swapped mouse button, etc.?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '14, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '14, 07:54</p></div></div><div id="comments-container-29142" class="comments-container"></div><div id="comment-tools-29142" class="comment-tools"></div><div class="clear"></div><div id="comment-29142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

