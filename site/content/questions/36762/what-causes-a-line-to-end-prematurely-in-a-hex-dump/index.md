+++
type = "question"
title = "What causes a line to end prematurely in a hex dump?"
description = '''In a hex dump from WireShark, the line of my capture only contains 0b and the offset skips from 00 to 01 to 11 instead of 00 10 20 like im used to seeing: 00000000 0b . 00000001 4d 53 48 7c 5e 7e 5c 26 7c 43 45 52 4e 45 52 7c MSH|^~&#92;&amp;amp; |CERNER|  what I&#x27;m used to seeing: 00000000 0b 4d 53 48 7c 5e...'''
date = "2014-10-01T11:53:00Z"
lastmod = "2014-10-01T11:53:00Z"
weight = 36762
keywords = [ "newline", "hex", "carriagereturn" ]
aliases = [ "/questions/36762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What causes a line to end prematurely in a hex dump?](/questions/36762/what-causes-a-line-to-end-prematurely-in-a-hex-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36762-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a hex dump from WireShark, the line of my capture only contains 0b and the offset skips from 00 to 01 to 11 instead of 00 10 20 like im used to seeing:</p><pre><code>00000000     0b                                                  .
00000001     4d 53 48 7c 5e 7e 5c 26  7c 43 45 52 4e 45 52 7c    MSH|^~\&amp; |CERNER|</code></pre><p>what I'm used to seeing:</p><pre><code>00000000     0b 4d 53 48 7c 5e 7e 5c  26 7c 43 45 52 4e 45 52    .MSH|^~\ &amp;|CERNER
00000010     7c 4a 2d 55 72 6f 43 49  42 34 7c 41 42 45 4c 4d    |J-UroCI B4|ABELM</code></pre><p>I thought a carriage return or line feed would show as another hex character? what causes the first line to end so abruptly?</p></div><div id="question-tags" class="tags-container tags">newline hex carriagereturn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '14, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/637f21f811d4f6b4b2f35f62311e505b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsampson&#39;s gravatar image" /><p>jsampson<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsampson has no accepted answers">0%</span></p></div></div><div id="comments-container-36762" class="comments-container"></div><div id="comment-tools-36762" class="comment-tools"></div><div class="clear"></div><div id="comment-36762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

