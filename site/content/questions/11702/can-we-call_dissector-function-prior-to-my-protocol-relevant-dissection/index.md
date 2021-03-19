+++
type = "question"
title = "Can we call_dissector function prior to my protocol relevant dissection ?"
description = '''I am using eth heuristic dissector and my protocol relevant data will be part of ethernet payload and located at the end of ethernet payload. Now in dissect_myproto , the tvb pointer will directly/autonomously point to my protocol relevant data when my dissector gets called or i will have to manipul...'''
date = "2012-06-05T19:59:00Z"
lastmod = "2012-06-06T01:14:00Z"
weight = 11702
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/11702" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can we call\_dissector function prior to my protocol relevant dissection ?](/questions/11702/can-we-call_dissector-function-prior-to-my-protocol-relevant-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11702-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using eth heuristic dissector and my protocol relevant data will be part of ethernet payload and located at the end of ethernet payload. Now in dissect_myproto , the tvb pointer will directly/autonomously point to my protocol relevant data when my dissector gets called or i will have to manipulate it to point to my protocol relevant data and if yes then how ? ..</p><p>earlier my protocol relevant data was coming first thing in ethernet payload and i was dissecting it followed by call to call_dissector for ip for eg. :-</p><p>call_dissector(ip_handle,.... (inside diseector function) .. where ip_handle is ip_handle = find_dissector("ip");(inside reg_handoff)</p><p>But now my protocol relevant data is at end of eth payload so if i call call_dissector first for "eth" and then do my dissection , will it work ?</p></div><div id="question-tags" class="tags-container tags">plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 19:59</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11702" class="comments-container"></div><div id="comment-tools-11702" class="comment-tools"></div><div class="clear"></div><div id="comment-11702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11712"></span>

<div id="answer-container-11712" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Ethernet dissector has an eth.trailer subdissector list which you can use. Have a look at the Ethernet dissector how this is called.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '12, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-11712" class="comments-container"><span id="11718"></span><div id="comment-11718" class="comment"><div id="post-11718-score" class="comment-score"></div><div class="comment-text"><p>Is it possible anyhow that i can dissect http payload while having heuristic dissector of eth , normally i guess if we have eth heuristic dissector then tvb will point to eth payload but i want http payload which will effectively form last part of eth payload.</p></div><div id="comment-11718-info" class="comment-info"><span class="comment-age">(06 Jun '12, 09:22)</span> yogeshg</div></div></div><div id="comment-tools-11712" class="comment-tools"></div><div class="clear"></div><div id="comment-11712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

