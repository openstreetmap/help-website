+++
type = "question"
title = "Display XML data is tree view"
description = '''If a packet contains xml data, is it possible for wireshark to get that data and display it in a tree view in the display pane? The dissection information is contained in the xml data.'''
date = "2015-05-20T09:44:00Z"
lastmod = "2015-05-20T10:46:00Z"
weight = 42585
keywords = [ "xml", "display", "wireshark" ]
aliases = [ "/questions/42585" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Display XML data is tree view](/questions/42585/display-xml-data-is-tree-view)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42585-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If a packet contains xml data, is it possible for wireshark to get that data and display it in a tree view in the display pane? The dissection information is contained in the xml data.</p></div><div id="question-tags" class="tags-container tags">xml display wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '15, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/42f084d62348c04d00bd67b129116cc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XQW1123&#39;s gravatar image" /><p>XQW1123<br />
<span class="score" title="46 reputation points">46</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XQW1123 has no accepted answers">0%</span></p></div></div><div id="comments-container-42585" class="comments-container"></div><div id="comment-tools-42585" class="comment-tools"></div><div class="clear"></div><div id="comment-42585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42587"></span>

<div id="answer-container-42587" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42587-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, there is an XML dissector that can do that. It tries to feed of conversations which apply the proper MIME type, or you can set heuristic parameters in the dissector preferences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '15, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42587" class="comments-container"></div><div id="comment-tools-42587" class="comment-tools"></div><div class="clear"></div><div id="comment-42587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42588"></span>

<div id="answer-container-42588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42588-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a xml dissector in Wiresahrk, that can be invoked if you retrieve the dissector handle with find_dissector("xml") function call. See <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-gadu-gadu.c;h=ba079d0f15c9fbf739cfbdadf95bccb94ab9a42f;hb=refs/heads/master">packet-gadu-gadu.c</a> dissector for example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 May '15, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-42588" class="comments-container"></div><div id="comment-tools-42588" class="comment-tools"></div><div class="clear"></div><div id="comment-42588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

