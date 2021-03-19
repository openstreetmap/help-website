+++
type = "question"
title = "Fix Dissector in LUA"
description = '''I am looking for a Fix dissector in lua. i got hope from this link  https://ask.wireshark.org/questions/1023/fix-protocol-dissector that we have it already working some where so that I am not reinventing the wheel and more interested to find that FIX dissector. Can any one please let me know how I c...'''
date = "2016-02-14T17:20:00Z"
lastmod = "2016-02-14T18:37:00Z"
weight = 50190
keywords = [ "fix" ]
aliases = [ "/questions/50190" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Fix Dissector in LUA](/questions/50190/fix-dissector-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50190-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a Fix dissector in lua. i got hope from this link</p><p><a href="https://ask.wireshark.org/questions/1023/fix-protocol-dissector">https://ask.wireshark.org/questions/1023/fix-protocol-dissector</a></p><p>that we have it already working some where so that I am not reinventing the wheel and more interested to find that FIX dissector. Can any one please let me know how I can get the Fix Dissectr in wireshark(or tshark in linux)</p></div><div id="question-tags" class="tags-container tags">fix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '16, 17:20</strong></p><img src="https://secure.gravatar.com/avatar/d20d7102fd9001359c35732770f6f143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fixmessenger&#39;s gravatar image" /><p>fixmessenger<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fixmessenger has no accepted answers">0%</span></p></div></div><div id="comments-container-50190" class="comments-container"></div><div id="comment-tools-50190" class="comment-tools"></div><div class="clear"></div><div id="comment-50190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50192"></span>

<div id="answer-container-50192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has a FIX dissector, but it's written in C, not Lua. In the Wireshark source tree, see <code>epan/dissectors/packet-fix.c</code> on UN*X or <code>epan\dissectors\packet-fix.c</code> on Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '16, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50192" class="comments-container"><span id="50193"></span><div id="comment-50193" class="comment"><div id="post-50193-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply Guys Harris. Lets take the example of Linux.</p><p>Where can I read the .pcap file and how to extract the FIX message out of the pcap file using that packet-fix.c</p></div><div id="comment-50193-info" class="comment-info"><span class="comment-age">(14 Feb '16, 20:30)</span> fixmessenger</div></div><span id="50195"></span><div id="comment-50195" class="comment"><div id="post-50195-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Where can I read the .pcap file</p></blockquote><p>With Wireshark or TShark.</p><blockquote><p>how to extract the FIX message out of the pcap file</p></blockquote><p>What do you want to extract? The raw bytes of the message? Specific fields in the message? Something else?</p></div><div id="comment-50195-info" class="comment-info"><span class="comment-age">(14 Feb '16, 23:18)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-50192" class="comment-tools"></div><div class="clear"></div><div id="comment-50192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

