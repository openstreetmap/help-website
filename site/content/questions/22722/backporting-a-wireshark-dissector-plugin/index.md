+++
type = "question"
title = "Backporting a wireshark dissector plugin"
description = '''Hi, i have a custom dissector plugin that i am trying to backport from wireshark 1.11 that i developed it for to wireshark 1.2.18. (It works on 1.11) Now i get errors while compiling with the old version of wireshark: error C2065 : ENC_BIG_ENDIAN : undeclared identifier I am using the variable in pr...'''
date = "2013-07-08T04:22:00Z"
lastmod = "2013-07-08T07:21:00Z"
weight = 22722
keywords = [ "dissector", "plugin", "backporting" ]
aliases = [ "/questions/22722" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Backporting a wireshark dissector plugin](/questions/22722/backporting-a-wireshark-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22722-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have a custom dissector plugin that i am trying to backport from wireshark 1.11 that i developed it for to wireshark 1.2.18. (It works on 1.11)</p><p>Now i get errors while compiling with the old version of wireshark: error C2065 : ENC_BIG_ENDIAN : undeclared identifier</p><p>I am using the variable in proto_tree_add_item(tree,id,tvb,offset,length,ENC_BIG_ENDIAN); The same error occurs when i use ENC_NA. I could get rid of the error by replacing ENC_BIG_ENDIAN with FALSE but i am not sure if that is the correct way to do it ?</p><p>/Kit</p></div><div id="question-tags" class="tags-container tags">dissector plugin backporting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '13, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/b93cb303b8ca7bc14188730687491169?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kitg&#39;s gravatar image" /><p>Kitg<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kitg has no accepted answers">0%</span></p></div></div><div id="comments-container-22722" class="comments-container"></div><div id="comment-tools-22722" class="comment-tools"></div><div class="clear"></div><div id="comment-22722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22726"></span>

<div id="answer-container-22726" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22726-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, in older versions the last argument to <code>proto_tree_add_item()</code> was a gboolean named <code>little_endian</code>. So FALSE would be the appropriate value to replace <code>ENC_BIG_ENDIAN</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '13, 07:22</p></div></div><div id="comments-container-22726" class="comments-container"><span id="22728"></span><div id="comment-22728" class="comment"><div id="post-22728-score" class="comment-score"></div><div class="comment-text"><p>okej, thanks alot.I was just curious since it fixed the compiler errors but wanted to know that the functionality wasnt affected.</p></div><div id="comment-22728-info" class="comment-info"><span class="comment-age">(08 Jul '13, 07:52)</span> Kitg</div></div></div><div id="comment-tools-22726" class="comment-tools"></div><div class="clear"></div><div id="comment-22726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

