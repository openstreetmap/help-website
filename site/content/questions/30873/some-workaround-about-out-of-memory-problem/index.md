+++
type = "question"
title = "Some workaround about out of memory problem"
description = '''I find some workaround analyze about out of memory problem at http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/. In &quot;Around #2&quot;, the author noted that &quot;Most things Wireshark displays about a frame is stored in there. Additionally there are hash tables of reassembled d...'''
date = "2014-03-17T01:48:00Z"
lastmod = "2014-03-17T04:58:00Z"
weight = 30873
keywords = [ "out-of-memory" ]
aliases = [ "/questions/30873" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Some workaround about out of memory problem](/questions/30873/some-workaround-about-out-of-memory-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30873-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I find some workaround analyze about out of memory problem at <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/.">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/.</a> In "Around #2", the author noted that "Most things Wireshark displays about a frame is stored in there. Additionally there are hash tables of reassembled data conversation".</p><ol><li><p>I've found the fdata in process_packet(tshark.c), but it's freed at the bottom of the function. Are there any more fdatas not freed ?</p></li><li><p>Where are the hash tables that store reassembled data conversation ?</p></li></ol><p>@kurt @Guy Harris</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">out-of-memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p>metamatrix<br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Mar '14, 01:50</p></div></div><div id="comments-container-30873" class="comments-container"></div><div id="comment-tools-30873" class="comment-tools"></div><div class="clear"></div><div id="comment-30873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30879"></span>

<div id="answer-container-30879" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30879-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not to supprisingly reassemble.c, conversation.c in epan</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '14, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-30879" class="comments-container"></div><div id="comment-tools-30879" class="comment-tools"></div><div class="clear"></div><div id="comment-30879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

