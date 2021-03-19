+++
type = "question"
title = "offset in packet byte pane"
description = '''Hello, I would like to have the packet byte pane show the payload bytes rather ..I.e. i would like the packet bytes pane to ignore the first 14 bytes...What has to be done to modify ??'''
date = "2011-09-05T04:07:00Z"
lastmod = "2011-09-06T01:20:00Z"
weight = 6091
keywords = [ "bytes", "packet" ]
aliases = [ "/questions/6091" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [offset in packet byte pane](/questions/6091/offset-in-packet-byte-pane)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to have the packet byte pane show the payload bytes rather ..I.e. i would like the packet bytes pane to ignore the first 14 bytes...What has to be done to modify ??</p></div><div id="question-tags" class="tags-container tags">bytes packet</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '11, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6091" class="comments-container"></div><div id="comment-tools-6091" class="comment-tools"></div><div class="clear"></div><div id="comment-6091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6114"></span>

<div id="answer-container-6114" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6114-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>From your comment above you'll need to create a new tvb which is the subset of the original tvb using <code>tvb_set_subset()</code> or <code>tvb_new_subset()</code> or <code>tvb_new_subset_remaining()</code> as appropriate and then call <code>add_new_data_source()</code>.</p><p>This will get you a new tab on the hex bytes pane with your required data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '11, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6114" class="comments-container"><span id="6118"></span><div id="comment-6118" class="comment"><div id="post-6118-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot i will try it out and see</p></div><div id="comment-6118-info" class="comment-info"><span class="comment-age">(06 Sep '11, 02:58)</span> flashkicker</div></div></div><div id="comment-tools-6114" class="comment-tools"></div><div class="clear"></div><div id="comment-6114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6092"></span>

<div id="answer-container-6092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6092-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The packet bytes pane normally displays the bytes contained in the frame, with the highlighted area being set to the node selected in the packet details tree. The length of the highlight is dictated by the code that added the item to the tree, e.g. in <code>proto_tree_add_item()</code> the <code>start</code> parameter specifies the offset in the tvb that the item starts at, and the <code>length</code> parameter specifies the length of the item. Passing a length of -1 highlights to the end of the packet.</p><p>An additional tab containing a subset or a synthesised buffer (e.g. a decrypted buffer) can be added to the packet bytes pane by creating a new tvb and calling <code>add_new_data_source()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '11, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-6092" class="comments-container"><span id="6105"></span><div id="comment-6105" class="comment"><div id="post-6105-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply ... Yes the packet byte pane shows the bytes in frame <strong>is there a way in which we can add an offset of 14 or any other number and make our third pane show only the bytes</strong> that we intend to show ....</p><p>for example 0000 30 10 11 11 01 11 00 00 00 01 11 00 11 9f 13 14 ASCIISEQ</p><p>if i would like the output to start from 9f where can we do that</p></div><div id="comment-6105-info" class="comment-info"><span class="comment-age">(05 Sep '11, 23:47)</span> flashkicker</div></div><span id="6108"></span><div id="comment-6108" class="comment"><div id="post-6108-score" class="comment-score"></div><div class="comment-text"><p>Have you tried modifying main_proto_draw.c in gtk folder? Hope it helps..</p></div><div id="comment-6108-info" class="comment-info"><span class="comment-age">(06 Sep '11, 00:17)</span> Terrestrial ...</div></div></div><div id="comment-tools-6092" class="comment-tools"></div><div class="clear"></div><div id="comment-6092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

