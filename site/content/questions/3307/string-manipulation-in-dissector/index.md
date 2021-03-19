+++
type = "question"
title = "String manipulation in dissector"
description = '''Hi, I would know how to extract a string from a packet, manipulate it and display it easily using the wireshark API. My string has a lenght of 10, I need to put a comma between the 6th and 7th characters and display it in the tree. '''
date = "2011-04-03T12:42:00Z"
lastmod = "2011-04-05T07:12:00Z"
weight = 3307
keywords = [ "development", "dissector" ]
aliases = [ "/questions/3307" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [String manipulation in dissector](/questions/3307/string-manipulation-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3307-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would know how to extract a string from a packet, manipulate it and display it easily using the wireshark API.</p><p>My string has a lenght of 10, I need to put a comma between the 6th and 7th characters and display it in the tree.</p></div><div id="question-tags" class="tags-container tags">development dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '11, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/a8e5c9438725b82bdee34d32a2068b80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chronidev&#39;s gravatar image" /><p>chronidev<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chronidev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '11, 12:42</p></div></div><div id="comments-container-3307" class="comments-container"></div><div id="comment-tools-3307" class="comment-tools"></div><div class="clear"></div><div id="comment-3307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3342"></span>

<div id="answer-container-3342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3342-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's probably a cleaner way to do this, but this is a quick-and-dirty way to accomplish adding these things to the tree as a single string.</p><pre><code>proto_item_append_text(item, &quot;%s,%s,%s&quot;,
    tvb_get_ephemeral_string(tvb, offset, 6),     /*before the commas */
    tvb_get_ephemeral_string(tvb, offset + 6, 1), /*between the commas */
    tvb_get_ephemeral_string(tvb, offset + 7, 3)) /*after the commas to the end */</code></pre><p>If you need to be able to filter one these strings, you'll need to do this differently, obviously, but for now, using <code>tvb_get_ephemeral_string</code> lets you ignore the strings after the call since the data will be copied into the tree, and the buffers will be automatically freed after dissecting the packet has finished. Since you know the length of the string, there's no need to use <code>tvb_get_*_stringz</code>, since those functions are dangerous (there's no guarantee the <code>NULL</code> was sent correctly with the rest of the packet).</p><p>These functions are documented in <code>epan/proto.h</code> (<code>proto_item_append_text</code>) and <code>epan/tvbuff.h</code> (<code>tvb_*</code>). If you need a different method of doing this, you should check those files for different functions that might satisfy your requirements.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '11, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '11, 14:08</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-3342" class="comments-container"></div><div id="comment-tools-3342" class="comment-tools"></div><div class="clear"></div><div id="comment-3342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

