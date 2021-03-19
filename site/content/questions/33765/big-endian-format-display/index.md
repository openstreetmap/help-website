+++
type = "question"
title = "BIG endian format display"
description = '''Hi all, I have put the encoding format in the proto_tree_add_item as ENC_BIG_ENDIAN. Will it show the values as calculated for Bid Endian when I call the corresponding dissector function for that PDU ? For example, 0x0102 will have its value displayed as 0x0201?? Please give a feedback . '''
date = "2014-06-13T04:36:00Z"
lastmod = "2014-06-13T17:01:00Z"
weight = 33765
keywords = [ "big-endian", "proto_tree_add_item", "plugin" ]
aliases = [ "/questions/33765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [BIG endian format display](/questions/33765/big-endian-format-display)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33765-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have put the encoding format in the proto_tree_add_item as ENC_BIG_ENDIAN. Will it show the values as calculated for Bid Endian when I call the corresponding dissector function for that PDU ? For example, 0x0102 will have its value displayed as 0x0201??</p><p>Please give a feedback .</p></div><div id="question-tags" class="tags-container tags">big-endian proto_tree_add_item plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '14, 04:36</strong></p><img src="https://secure.gravatar.com/avatar/5a3c4db36bd55fe80a90e7fe1b9788c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amit%20Bhanja&#39;s gravatar image" /><p>Amit Bhanja<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amit Bhanja has no accepted answers">0%</span></p></div></div><div id="comments-container-33765" class="comments-container"></div><div id="comment-tools-33765" class="comment-tools"></div><div class="clear"></div><div id="comment-33765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33794"></span>

<div id="answer-container-33794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33794-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a 2-byte field, where the first byte is 0x01 and the second byte is 0x02, then:</p><ul><li>if you add that two-byte field with <code>ENC_BIG_ENDIAN</code>, its value will be 0x0102;</li><li>if you add that two-byte field with <code>ENC_LITTLE_ENDIAN</code>, its value will be 0x0201.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '14, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33794" class="comments-container"></div><div id="comment-tools-33794" class="comment-tools"></div><div class="clear"></div><div id="comment-33794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

