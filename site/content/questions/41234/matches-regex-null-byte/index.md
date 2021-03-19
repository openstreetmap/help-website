+++
type = "question"
title = "Matches regex NULL byte"
description = '''The following display filter works for my purposes, but has lots of false positives:  tcp matches &quot;&#92;xff....&#92;xfe&quot; A better way would be to match two null bytes, like:  tcp matches &quot;&#92;xff&#92;x00&#92;x00..&#92;xfe&quot; But then, since the string/input to matches is a null terminated string, the regex searches only for...'''
date = "2015-04-06T14:40:00Z"
lastmod = "2015-04-08T16:10:00Z"
weight = 41234
keywords = [ "matches", "regex", "null" ]
aliases = [ "/questions/41234" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Matches regex NULL byte](/questions/41234/matches-regex-null-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41234-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>The following display filter works for my purposes, but has lots of false positives: <code>tcp matches "\xff....\xfe"</code></p><p>A better way would be to match two null bytes, like: <code>tcp matches "\xff\x00\x00..\xfe"</code></p><p>But then, since the string/input to <em>matches</em> is a null terminated string, the regex searches only for the \xff byte, the following \x00 ends the string :/</p><p>Is there any way i didn't thought of to include null bytes in the regex? Tried it with \0 and \000. Maybe some sort of (undocumented) special escape char?</p><p>Btw. <code>tcp contains ff:00...</code> doesn't work for me because i need the regex power of matching 2 "dont care" bytes (but dontcare/wildcard for <em>contains</em> would be nice tho too ^^)</p></div><div id="question-tags" class="tags-container tags">matches regex null</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '15, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/0fe2e1722ac89081ada5c911a481f248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="topview&#39;s gravatar image" /><p>topview<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="topview has one accepted answer">100%</span></p></div></div><div id="comments-container-41234" class="comments-container"></div><div id="comment-tools-41234" class="comment-tools"></div><div class="clear"></div><div id="comment-41234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41304"></span>

<div id="answer-container-41304" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41304-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok got it ;-) While it might be really usefull that Wireshark would not use NULL terminated c-strings (for a software that deals mostly with BINARY data and not text...), there is a simple solution:</p><p><code>[^\x01-\xFF]</code> matches a null byte</p><p>Instead of <code>tcp matches "\xff\x00\x00..\xfe"</code> which wont work as intended,</p><p>use: <code>tcp matches "\xff[^\x01-\xFF]{2}..\xfe"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '15, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/0fe2e1722ac89081ada5c911a481f248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="topview&#39;s gravatar image" /><p>topview<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="topview has one accepted answer">100%</span></p></div></div><div id="comments-container-41304" class="comments-container"></div><div id="comment-tools-41304" class="comment-tools"></div><div class="clear"></div><div id="comment-41304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

