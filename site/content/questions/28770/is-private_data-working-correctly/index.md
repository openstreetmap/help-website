+++
type = "question"
title = "Is private_data working correctly ?"
description = '''Hi, I&#x27;m having some issues with pinfo-&amp;gt;private_data method , I think I&#x27;m using it correctly and I&#x27;v seen in some revision that private_data is removed. So is private_data working ? Is there another method to pass data to a sub-dissector ? '''
date = "2014-01-10T07:28:00Z"
lastmod = "2014-01-10T07:50:00Z"
weight = 28770
keywords = [ "pinfo", "privata", "data" ]
aliases = [ "/questions/28770" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is private\_data working correctly ?](/questions/28770/is-private_data-working-correctly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28770-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm having some issues with pinfo-&gt;private_data method , I think I'm using it correctly and I'v seen in some revision that private_data is removed. So is private_data working ? Is there another method to pass data to a sub-dissector ?</p></div><div id="question-tags" class="tags-container tags">pinfo privata data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '14, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-28770" class="comments-container"></div><div id="comment-tools-28770" class="comment-tools"></div><div class="clear"></div><div id="comment-28770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28771"></span>

<div id="answer-container-28771" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28771-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Passing data between dissectors using <code>pinfo-&gt;private_data</code> still <em>mostly</em> works (for example, there can be problems if exceptions occur), but it is not the recommended method and one day this method may disappear altogether. It is far better to pass the data using the "new-style" dissection API's. Look into using such functions as, <code>new_create_dissector_handle()</code>, <code>dissector_try_uint_new()</code>, ...</p><p>You can see the difference in coding by looking at several fairly recent commits by Michael Mann, who spent some time converting many cases:</p><ul><li><a href="http://anonsvn.wireshark.org/viewvc?revision=52698&amp;view=revision">r52698</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52707">r52707</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52718">r52718</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52723">r52723</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52728">r52728</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52729">r52729</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52750">r52750</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52751">r52751</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52810">r52810</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52836">r52836</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52856">r52856</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52877">r52877</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52883">r52883</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52885">r52885</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52893">r52893</a></li><li><a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=52894">r52894</a></li></ul><p>... etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '14, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-28771" class="comments-container"><span id="28773"></span><div id="comment-28773" class="comment"><div id="post-28773-score" class="comment-score"></div><div class="comment-text"><p>Ok that's what I needed thank you</p></div><div id="comment-28773-info" class="comment-info"><span class="comment-age">(10 Jan '14, 08:17)</span> Afrim</div></div></div><div id="comment-tools-28771" class="comment-tools"></div><div class="clear"></div><div id="comment-28771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

