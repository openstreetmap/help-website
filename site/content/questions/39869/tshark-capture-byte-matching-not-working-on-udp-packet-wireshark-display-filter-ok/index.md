+++
type = "question"
title = "tshark capture, byte matching not working on udp packet, wireshark display filter ok"
description = '''I am trying to use tshark to capture all udp packets that do not contain 0xFFFFFFFF or 0xD5D5D5. The capture filter I have defined is as follows:tshark -i eth0 -f &quot;udp and udp[17:4] != 0xFFFFFFFF and udp[17:4] != 0xDBDBDBDB&quot; The bytes I do not want to capture have either 0xFF or 0xDB from byte numbe...'''
date = "2015-02-15T11:11:00Z"
lastmod = "2015-02-15T11:48:00Z"
weight = 39869
keywords = [ "capture-filter", "tshark", "byte-filter" ]
aliases = [ "/questions/39869" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark capture, byte matching not working on udp packet, wireshark display filter ok](/questions/39869/tshark-capture-byte-matching-not-working-on-udp-packet-wireshark-display-filter-ok)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39869-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use tshark to capture all udp packets that do not contain 0xFFFFFFFF or 0xD5D5D5. The capture filter I have defined is as follows:<code>tshark -i eth0 -f "udp and udp[17:4] != 0xFFFFFFFF and udp[17:4] != 0xDBDBDBDB"</code> The bytes I do not want to capture have either 0xFF or 0xDB from byte number 17 to 80, all the udp packets have 80 bytes in the data payload. With tshark running all packets are being captured with no filtering happening. Using wireshark and the following display filter: <code>udp and not (frame contains 0xFFFFFFFF or frame contains 0xDBDBDBDB)</code> successfully removes all packets not meeting the specified criteria.</p><p>Can anyone work out where (if anywhere) I have gone wrong with the capture filter?</p></div><div id="question-tags" class="tags-container tags">capture-filter tshark byte-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '15, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/aca92b1346da932886779daed561c95f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="time2innov8&#39;s gravatar image" /><p>time2innov8<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="time2innov8 has no accepted answers">0%</span></p></div></div><div id="comments-container-39869" class="comments-container"></div><div id="comment-tools-39869" class="comment-tools"></div><div class="clear"></div><div id="comment-39869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39871"></span>

<div id="answer-container-39871" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39871-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Display filter and capture filter are two different filter systems. Capture filters are optimized for high speed filtering while capturing frames, while display filters can filter on much more complicated things. Display filters are not time critical, so it doesn't matter how complex the filtering process is.</p><p>"frame contains" searches for the pattern in the whole frame. Your tshark filter basically requires that certain patterns do not appear at the offsets you specify, which is much more specific - the pattern must be at a very specific position or the filter won't apply.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '15, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39871" class="comments-container"><span id="39872"></span><div id="comment-39872" class="comment"><div id="post-39872-score" class="comment-score"></div><div class="comment-text"><p>The packets transmitted that are to be discarded have the required bytes in the specified positions. The only error may be in the slicing [17:4] however I am using a modifed version from one listed in the tshark documentation so don't think that's the issue. Can anyone confirm that the syntax of the supplied capture and display filters are performing the same function?</p></div><div id="comment-39872-info" class="comment-info"><span class="comment-age">(15 Feb '15, 12:21)</span> time2innov8</div></div></div><div id="comment-tools-39871" class="comment-tools"></div><div class="clear"></div><div id="comment-39871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

