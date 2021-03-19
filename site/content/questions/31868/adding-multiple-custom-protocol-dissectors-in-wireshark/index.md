+++
type = "question"
title = "Adding multiple Custom protocol dissectors in wireshark"
description = '''I am trying to add custom protocols in the wireshark. There are multiple protocols which communicate on the same tcp port i.e. tcp port for all the protocols would be the same . How can i make wireshark to call a dissector specific to the protocol As according to my understanding the dissector would...'''
date = "2014-04-16T01:43:00Z"
lastmod = "2014-04-16T02:21:00Z"
weight = 31868
keywords = [ "development", "protocol", "dissector", "tcp.port", "plugin" ]
aliases = [ "/questions/31868" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding multiple Custom protocol dissectors in wireshark](/questions/31868/adding-multiple-custom-protocol-dissectors-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to add custom protocols in the wireshark. There are multiple protocols which communicate on the same tcp port i.e. tcp port for all the protocols would be the same . How can i make wireshark to call a dissector specific to the protocol As according to my understanding the dissector would be called when it detects traffic on the specified tcp port. So how it will decide to call the specific dissector from multiple dissectors</p></div><div id="question-tags" class="tags-container tags">development protocol dissector tcp.port plugin</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/3bd1cf7096b417e3b2be586527ec8002?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Balpreet%20Singh&#39;s gravatar image" /><p>Balpreet Singh<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Balpreet Singh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Apr '14, 02:03</p></div></div><div id="comments-container-31868" class="comments-container"></div><div id="comment-tools-31868" class="comment-tools"></div><div class="clear"></div><div id="comment-31868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31869"></span>

<div id="answer-container-31869" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31869-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your dissectors will have to either use a heuristic by examining the first few bytes of data to determine if the data is for that protocol and not dissecting anything and returning 0 if not, or you can manually disable the dissectors as required.</p><p>Have a look at <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.heuristic">README.heuristic</a> in the doc directory of the source.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-31869" class="comments-container"><span id="31888"></span><div id="comment-31888" class="comment"><div id="post-31888-score" class="comment-score">1</div><div class="comment-text"><p>Or in your main dissector read the bytes needed to find out which sub dissector to call and call that dissector with the tvb.</p></div><div id="comment-31888-info" class="comment-info"><span class="comment-age">(16 Apr '14, 07:44)</span> Anders ♦</div></div></div><div id="comment-tools-31869" class="comment-tools"></div><div class="clear"></div><div id="comment-31869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

