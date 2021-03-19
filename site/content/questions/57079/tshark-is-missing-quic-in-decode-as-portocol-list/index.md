+++
type = "question"
title = "tshark is missing QUIC in &quot;decode-as&quot; portocol list"
description = '''In trying to dissect captured QUIC traffic with tshark cannot set &quot;decode as&quot; (-d udp.port==5555,quic) protocol because quic is not recognized by tshark as layer protocol (-d &#x27;&#x27; does not list it). It is listed in decode_as_entries.  &quot;tshark -G decodes&quot; does list it as well but tshark does not pick i...'''
date = "2016-11-07T10:08:00Z"
lastmod = "2016-11-07T13:03:00Z"
weight = 57079
keywords = [ "decode_as", "tshark", "quic" ]
aliases = [ "/questions/57079" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark is missing QUIC in "decode-as" portocol list](/questions/57079/tshark-is-missing-quic-in-decode-as-portocol-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57079-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In trying to dissect captured QUIC traffic with tshark cannot set "decode as" (-d udp.port==5555,quic) protocol because quic is not recognized by tshark as layer protocol (-d '' does not list it). It is listed in decode_as_entries. "tshark -G decodes" does list it as well but tshark does not pick it up for some reason.</p><p>Would appreciate any suggestion on how to resolve this.</p></div><div id="question-tags" class="tags-container tags">decode_as tshark quic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/607514c7c1cfed6f0de7979450b85e86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iez&#39;s gravatar image" /><p>iez<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iez has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '16, 10:33</p></div></div><div id="comments-container-57079" class="comments-container"></div><div id="comment-tools-57079" class="comment-tools"></div><div class="clear"></div><div id="comment-57079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57088"></span>

<div id="answer-container-57088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57088-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The solution is to either:</p><ol><li>Modify the Wireshark source code for the version you're using to register QUIC as eligible for Decode-As (how you do this depends on the version you're running)</li><li>(or) upgrade to Wireshark 2.2 (in which QUIC is eligible for Decode-As)</li></ol><p>(It might work in versions earlier than 2.2--I didn't check exactly what version that functionality showed up in.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-57088" class="comments-container"><span id="57089"></span><div id="comment-57089" class="comment"><div id="post-57089-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jeff. I am running "Version 2.2.1 (v2.2.1-0-ga6fbd27 from master-2.2)". Wireshark has no problem with decode_as. tshark does not recognize it</p></div><div id="comment-57089-info" class="comment-info"><span class="comment-age">(07 Nov '16, 13:10)</span> iez</div></div></div><div id="comment-tools-57088" class="comment-tools"></div><div class="clear"></div><div id="comment-57088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

