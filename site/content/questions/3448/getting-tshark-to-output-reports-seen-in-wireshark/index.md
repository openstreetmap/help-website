+++
type = "question"
title = "Getting tshark to output reports seen in Wireshark?"
description = '''In Wireshark I can pull down Statistics and go to Conversation Lists / TCP and get a nice report with packet and byte counts, stations &amp;amp; ports as well as start times and durations. How can I get this same report from tshark? Using -z conv,tcp gets me some of it but not all. Plus, my captures are...'''
date = "2011-04-11T12:03:00Z"
lastmod = "2011-04-11T12:52:00Z"
weight = 3448
keywords = [ "filters", "tshark", "reports" ]
aliases = [ "/questions/3448" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting tshark to output reports seen in Wireshark?](/questions/3448/getting-tshark-to-output-reports-seen-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3448-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark I can pull down Statistics and go to Conversation Lists / TCP and get a nice report with packet and byte counts, stations &amp; ports as well as start times and durations.</p><p>How can I get this same report from tshark? Using -z conv,tcp gets me some of it but not all.</p><p>Plus, my captures are too big and Wireshark keeps bombing out.</p><p>Thanks, Shae</p></div><div id="question-tags" class="tags-container tags">filters tshark reports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/dedca9e4c822c1a4f09f2efddce11dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iamshae&#39;s gravatar image" /><p>iamshae<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iamshae has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '11, 12:03</p></div></div><div id="comments-container-3448" class="comments-container"></div><div id="comment-tools-3448" class="comment-tools"></div><div class="clear"></div><div id="comment-3448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3450"></span>

<div id="answer-container-3450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3450-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's not possible at the moment. The code for the conversation statistics is not (yet) shared between wireshark and tshark. Hence the differences.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3450" class="comments-container"></div><div id="comment-tools-3450" class="comment-tools"></div><div class="clear"></div><div id="comment-3450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

