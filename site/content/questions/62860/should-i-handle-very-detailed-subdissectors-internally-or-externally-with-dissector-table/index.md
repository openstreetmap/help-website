+++
type = "question"
title = "Should I handle very detailed subdissectors internally or externally with dissector table"
description = '''Hi, forks, this is a best practice question. I am decoding a protocol set on top of UDP. The UDP payload is encapsulated in MotherProto, and the payload of MotherProto takes on several dozens of forms. Each form represents a different message type, and is identified with UDP port number. For example...'''
date = "2017-07-18T20:09:00Z"
lastmod = "2017-07-18T23:04:00Z"
weight = 62860
keywords = [ "dissectortable", "subdissector" ]
aliases = [ "/questions/62860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Should I handle very detailed subdissectors internally or externally with dissector table](/questions/62860/should-i-handle-very-detailed-subdissectors-internally-or-externally-with-dissector-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62860-score" class="post-score" title="current number of votes">0</div><span id="post-62860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, forks, this is a best practice question. I am decoding a protocol set on top of UDP. The UDP payload is encapsulated in MotherProto, and the payload of MotherProto takes on several dozens of forms.</p><p>Each form represents a different message type, and is identified with UDP port number. For example,</p><pre><code>udp port 64000 means A01 message, in which byte 1 is status, byte 2 is data_freshness, byte 3-4 is measurement_1
udp port 64001 means B02 message, in which byte 1 is status, byte 2 is data_freshness, byte 3 is command_1, byte 4-5 is command_2</code></pre><p>...</p><p>There are two ways to handle this as I see it. One way is to set up a sub_dissector table "mothеr.port", and register each tiny little message type as a sub-dissector</p><p>Or, I can make call a unique subdissector in MotherProto, Childproto, and handle the message classification internally. One good thing about this is that I don't need to write so many handoff routines and I can put port-to-messageType information in a xml, which is easy to maintain and update (the correlation between port and message type may change between different releases).</p><p>Which is the best practice? Or is there a better/standard way? Mother and Child proto are both niche protocols unlikely to be encapsulated in any other way.</p><p>Thank you for your help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissectortable" rel="tag" title="see questions tagged &#39;dissectortable&#39;">dissectortable</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '17, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/4222adcf6d70b2c359746d893f30c045?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nickzhang&#39;s gravatar image" /><p><span>nickzhang</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nickzhang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jul '17, 21:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-62860" class="comments-container"></div><div id="comment-tools-62860" class="comment-tools"></div><div class="clear"></div><div id="comment-62860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62863"></span>

<div id="answer-container-62863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62863-score" class="post-score" title="current number of votes">1</div><span id="post-62863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So basically the question is maintainability, which is an important metric to consider. But also one of the tougher to grasp, because of the amount of uncertainty of future developments. So, both mechanisms you described are in place to handle either situation. Whichever is best, that is something for you to determine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 23:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62863" class="comments-container"></div><div id="comment-tools-62863" class="comment-tools"></div><div class="clear"></div><div id="comment-62863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

