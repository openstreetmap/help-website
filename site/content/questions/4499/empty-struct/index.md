+++
type = "question"
title = "empty struct"
description = '''i saw an empty struct as struct pref_module; defined in epanpref.h, what is the significance of such structures, i have not come accross such structures.'''
date = "2011-06-10T07:25:00Z"
lastmod = "2011-06-10T08:22:00Z"
weight = 4499
keywords = [ "empty_structure" ]
aliases = [ "/questions/4499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [empty struct](/questions/4499/empty-struct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i saw an empty struct as struct pref_module; defined in epanpref.h, what is the significance of such structures, i have not come accross such structures.</p></div><div id="question-tags" class="tags-container tags">empty_structure</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '11, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p>sagu072<br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div></div><div id="comments-container-4499" class="comments-container"></div><div id="comment-tools-4499" class="comment-tools"></div><div class="clear"></div><div id="comment-4499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4505"></span>

<div id="answer-container-4505" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4505-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not an empty struct, it is a struct whose contents are not visible to users of prefs.h. The full structure definition of the structure is in prefs-int.h .</p><p>Such structures are generally used to make them opaque to the users (so they can't view or change the contents). See the <a href="http://en.wikipedia.org/wiki/Opaque_data_type">Wikipedia article</a> on such things.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '11, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 07:04</p></div></div><div id="comments-container-4505" class="comments-container"></div><div id="comment-tools-4505" class="comment-tools"></div><div class="clear"></div><div id="comment-4505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

