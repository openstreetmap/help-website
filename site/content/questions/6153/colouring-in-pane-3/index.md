+++
type = "question"
title = "colouring in pane 3"
description = '''Can we have colouring of bytes in pane3 from an offset specified ??'''
date = "2011-09-07T00:34:00Z"
lastmod = "2011-09-07T00:53:00Z"
weight = 6153
keywords = [ "pane" ]
aliases = [ "/questions/6153" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [colouring in pane 3](/questions/6153/colouring-in-pane-3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6153-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can we have colouring of bytes in pane3 from an offset specified ??</p></div><div id="question-tags" class="tags-container tags">pane</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '11, 00:34</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6153" class="comments-container"></div><div id="comment-tools-6153" class="comment-tools"></div><div class="clear"></div><div id="comment-6153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6156"></span>

<div id="answer-container-6156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6156-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't do any coloring yourself in pane3 (unless you write that functionality from scratch). What will work is use the proto_tree_add_* functions, in which you can point to the offset in the tvb where your field begins and by supplying a length, all the bytes of your field will be highlighted when you select the field in the details pane (pane2).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6156" class="comments-container"><span id="6158"></span><div id="comment-6158" class="comment"><div id="post-6158-score" class="comment-score"></div><div class="comment-text"><p>Yes got it ..... the thing is i'm more interested in the byte data from the 18 byte ....i.e i would like to hide (source ,destination ,protocol ) +2 bytes in pane three ....Is it possible to do so</p></div><div id="comment-6158-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:09)</span> flashkicker</div></div><span id="6164"></span><div id="comment-6164" class="comment"><div id="post-6164-score" class="comment-score"></div><div class="comment-text"><p>Not with the provided functions. But you may be able to write something yourself...</p></div><div id="comment-6164-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:39)</span> SYN-bit ♦♦</div></div><span id="6166"></span><div id="comment-6166" class="comment"><div id="post-6166-score" class="comment-score"></div><div class="comment-text"><p>ohk thanks a lot !!!</p></div><div id="comment-6166-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:59)</span> flashkicker</div></div></div><div id="comment-tools-6156" class="comment-tools"></div><div class="clear"></div><div id="comment-6156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

