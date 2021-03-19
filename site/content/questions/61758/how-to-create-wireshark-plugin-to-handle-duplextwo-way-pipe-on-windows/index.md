+++
type = "question"
title = "How to create Wireshark plugin to handle duplex/two-way pipe on Windows?"
description = '''Hi all, We are currently using a code to parse CAN Bus messages into Wireshark from a data logger. As part of this, we are using a named pipe to feed the data. We are interested in also doing the reverse, i.e. using a plugin GUI in Wireshark to feed custom CAN bus messages from that GUI back through...'''
date = "2017-06-03T11:05:00Z"
lastmod = "2017-06-03T11:47:00Z"
weight = 61758
keywords = [ "pipe", "transmits", "canbus", "can", "wireshark" ]
aliases = [ "/questions/61758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create Wireshark plugin to handle duplex/two-way pipe on Windows?](/questions/61758/how-to-create-wireshark-plugin-to-handle-duplextwo-way-pipe-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61758-score" class="post-score" title="current number of votes">0</div><span id="post-61758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>We are currently using a code to parse CAN Bus messages into Wireshark from a data logger. As part of this, we are using a named pipe to feed the data.</p><p>We are interested in also doing the reverse, i.e. using a plugin GUI in Wireshark to feed custom CAN bus messages from that GUI back through the pipe so that the logger can transmit it to the CAN bus.</p><p>Has anyone seen something similar done and/or have suggestions for how to set up a duplex named pipe solution for this for Windows?</p><p>If any of you have an idea, we would be grateful!</p><p>Best, Martin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-transmits" rel="tag" title="see questions tagged &#39;transmits&#39;">transmits</span> <span class="post-tag tag-link-canbus" rel="tag" title="see questions tagged &#39;canbus&#39;">canbus</span> <span class="post-tag tag-link-can" rel="tag" title="see questions tagged &#39;can&#39;">can</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '17, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/bb505f6832bb10125678c300fff66aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfcss&#39;s gravatar image" /><p><span>mfcss</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfcss has no accepted answers">0%</span></p></div></div><div id="comments-container-61758" class="comments-container"></div><div id="comment-tools-61758" class="comment-tools"></div><div class="clear"></div><div id="comment-61758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61759"></span>

<div id="answer-container-61759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61759-score" class="post-score" title="current number of votes">0</div><span id="post-61759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't generate messages, so while you <em>could</em> do that in a custom plugin, there is no support for that.</p><p>You should also look at the extcap interface specification which allows external data sources to be added as pseudo interface. See the <a href="https://wiki.wireshark.org/Development/Extcap">extcap wiki page</a> and doc/README.extcap in the source tree for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '17, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61759" class="comments-container"></div><div id="comment-tools-61759" class="comment-tools"></div><div class="clear"></div><div id="comment-61759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

