+++
type = "question"
title = "Hide trees in pane2"
description = '''How to hide Ethernet and frame trees in pane 2....  (hiding without disabling )'''
date = "2011-09-07T00:39:00Z"
lastmod = "2011-09-07T04:14:00Z"
weight = 6154
keywords = [ "dissector" ]
aliases = [ "/questions/6154" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Hide trees in pane2](/questions/6154/hide-trees-in-pane2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6154-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to hide Ethernet and frame trees in pane 2.... (hiding without disabling )</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6154" class="comments-container"></div><div id="comment-tools-6154" class="comment-tools"></div><div class="clear"></div><div id="comment-6154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6173"></span>

<div id="answer-container-6173" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6173-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>PROTO_ITEM_SET_HIDDEN(); worked for me</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6173" class="comments-container"></div><div id="comment-tools-6173" class="comment-tools"></div><div class="clear"></div><div id="comment-6173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6157"></span>

<div id="answer-container-6157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6157-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can always collapse the Frame and Ethernet trees to a single line (for each) by clicking on the "-" in front of them. There is no way to completely remove them from the details pane (unless you write the code for it yourself).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 00:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6157" class="comments-container"><span id="6160"></span><div id="comment-6160" class="comment"><div id="post-6160-score" class="comment-score"></div><div class="comment-text"><p>how about adding the PROTO_ITEM_SET_HIDDEN() in ..packet-eth.c .... i will be trying that in a while now</p></div><div id="comment-6160-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:12)</span> flashkicker</div></div><span id="6165"></span><div id="comment-6165" class="comment"><div id="post-6165-score" class="comment-score"></div><div class="comment-text"><p>Not sure that will work, but you can always try :-)</p></div><div id="comment-6165-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:39)</span> SYN-bit ♦♦</div></div><span id="6167"></span><div id="comment-6167" class="comment"><div id="post-6167-score" class="comment-score"></div><div class="comment-text"><p>Yep will be trying that i will write down the answer once i get it</p></div><div id="comment-6167-info" class="comment-info"><span class="comment-age">(07 Sep '11, 02:00)</span> flashkicker</div></div></div><div id="comment-tools-6157" class="comment-tools"></div><div class="clear"></div><div id="comment-6157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

