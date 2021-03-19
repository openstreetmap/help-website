+++
type = "question"
title = "Authentication packets"
description = '''I would like to ask when I check the authentication packets, what is the meaning of Flags=.......C, when I expand the packet, I could not find where is the C Is it a carry bit? Where can I find it? Also, is it possible to have seq=0 of the authentication packet send by client?21'''
date = "2016-04-15T21:41:00Z"
lastmod = "2016-04-20T03:04:00Z"
weight = 51713
keywords = [ "auth" ]
aliases = [ "/questions/51713" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Authentication packets](/questions/51713/authentication-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51713-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to ask when I check the authentication packets, what is the meaning of Flags=.......C, when I expand the packet, I could not find where is the C Is it a carry bit? Where can I find it? Also, is it possible to have seq=0 of the authentication packet send by client?21</p></div><div id="question-tags" class="tags-container tags">auth</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '16, 21:41</strong></p><img src="https://secure.gravatar.com/avatar/8165774b31254ba3d1c1a64f8d09b894?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kristy%20Lau&#39;s gravatar image" /><p>Kristy Lau<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kristy Lau has no accepted answers">0%</span></p></div></div><div id="comments-container-51713" class="comments-container"><span id="51788"></span><div id="comment-51788" class="comment"><div id="post-51788-score" class="comment-score"></div><div class="comment-text"><blockquote><p>when I check the authentication packets,</p></blockquote><p>the authentication packets of <strong>which protocol</strong> ?? Can you please provide a sample capture file and/or a screenshot?</p><p>Regards Kurt</p></div><div id="comment-51788-info" class="comment-info"><span class="comment-age">(19 Apr '16, 06:55)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-51713" class="comment-tools"></div><div class="clear"></div><div id="comment-51713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51812"></span>

<div id="answer-container-51812" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51812-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like an 802.11 wireless frame that you are referring to, as it is the only one I know that has that type of information in the Info field. The <strong>C</strong> refers to the checksum, if available.<br />
</p><p>Example snapshot - two wireless capture devices set to the same channel, for comparison. One passes up the FCS, the other does not:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Compare.png" alt="alt text" /></p><p>and the body looks like this (pertinent part):</p><p><img src="https://osqa-ask.wireshark.org/upfiles/compare2.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '16, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></img></div></div><div id="comments-container-51812" class="comments-container"></div><div id="comment-tools-51812" class="comment-tools"></div><div class="clear"></div><div id="comment-51812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

