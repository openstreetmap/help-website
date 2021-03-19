+++
type = "question"
title = "Decoding the last bytes of a stream?"
description = '''I am making a dissector that calculates the remaining length of a stream, and decodes it in as many groups of 11 bytes as possible. However, whenever it decodes the last couple of bytes I get an error saying malformed packets. This does not happen when the last possible 11 byte group ends and there ...'''
date = "2012-08-07T07:41:00Z"
lastmod = "2012-08-07T08:30:00Z"
weight = 13424
keywords = [ "stream", "bytes", "packet", "malformed" ]
aliases = [ "/questions/13424" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding the last bytes of a stream?](/questions/13424/decoding-the-last-bytes-of-a-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13424-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am making a dissector that calculates the remaining length of a stream, and decodes it in as many groups of 11 bytes as possible. However, whenever it decodes the last couple of bytes I get an error saying malformed packets.</p><p>This does not happen when the last possible 11 byte group ends and there are 6 or so bytes left over.</p><p>The packets that I am testing this on I had created using a custom packet building program. So I'm wondering if this malformed packet message is due to me creating bad packets or if you are just unable to decode the last couple bits in a stream.</p></div><div id="question-tags" class="tags-container tags">stream bytes packet malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p>bball2601<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span></p></div></div><div id="comments-container-13424" class="comments-container"></div><div id="comment-tools-13424" class="comment-tools"></div><div class="clear"></div><div id="comment-13424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13429"></span>

<div id="answer-container-13429" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13429-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out. It was just a mistake in the creation of my packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p>bball2601<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span></p></div></div><div id="comments-container-13429" class="comments-container"></div><div id="comment-tools-13429" class="comment-tools"></div><div class="clear"></div><div id="comment-13429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

