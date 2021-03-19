+++
type = "question"
title = "Best practice for stateful packet dissection"
description = '''Hi, I have a protocol where the dissection of a current frame depends on information provided in a previous (header) packet. What is the common way to implement such a behaviour in the dissector? I.e. how to deal with transfering state information from one packet to a subsequent packet in the first ...'''
date = "2014-11-17T16:27:00Z"
lastmod = "2014-11-17T16:27:00Z"
weight = 37922
keywords = [ "dissector" ]
aliases = [ "/questions/37922" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Best practice for stateful packet dissection](/questions/37922/best-practice-for-stateful-packet-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a protocol where the dissection of a current frame depends on information provided in a previous (header) packet.</p><p>What is the common way to implement such a behaviour in the dissector? I.e. how to deal with transfering state information from one packet to a subsequent packet in the <em>first</em> run? From my point of view I would only need to store the protocol state in a global (maybe wmem-allocated) variable and update upon reception of a new state-changing (header) packet.. Any hints for me?</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 16:27</strong></p><img src="https://secure.gravatar.com/avatar/e25b721141c2cdf05a96346bd47da782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Enrico&#39;s gravatar image" /><p>Enrico<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Enrico has no accepted answers">0%</span></p></div></div><div id="comments-container-37922" class="comments-container"></div><div id="comment-tools-37922" class="comment-tools"></div><div class="clear"></div><div id="comment-37922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

