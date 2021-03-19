+++
type = "question"
title = "How can I extract email content from IMF packets using tshark?"
description = '''I&#x27;m working on a bash script which can show email text. I can find what I want in an IMF packet: -&amp;gt; IMF (Internet Message Format) ---&amp;gt; MIME Multipart Media Encapsulation, Type: multipart/alternative, Boundary: ------&amp;gt; Encapsulated multipart part: (text/plain) ---------&amp;gt; Line-based text d...'''
date = "2012-02-01T11:38:00Z"
lastmod = "2012-02-01T11:38:00Z"
weight = 8754
keywords = [ "email", "tshark", "imf" ]
aliases = [ "/questions/8754" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I extract email content from IMF packets using tshark?](/questions/8754/how-can-i-extract-email-content-from-imf-packets-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8754-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on a bash script which can show email text. I can find what I want in an IMF packet:</p><pre><code>-&gt; IMF (Internet Message Format)
---&gt; MIME Multipart Media Encapsulation, Type: multipart/alternative, Boundary:
------&gt; Encapsulated multipart part:  (text/plain)
---------&gt; Line-based text data: text/plain
--------------&gt; **** Content to extract is here ****</code></pre><p>I only want the <code>text/plain</code> data, but I can't retrieve it. The solution I've found is <code>tshark -i 3 -R data-text-lines -V</code>, but it shows me the entire packet. If I try <code>tshark -i 3 -R "imf || smtp || data-text-lines" -V -T fields -e mime_multipart.part -e data-text-lines</code> in stead, nothing displays --only empty lines. What's going on here, and how can I get only the data I want?</p></div><div id="question-tags" class="tags-container tags">email tshark imf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '12, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/5cb9dd3678bfab432157941dc1222b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cl%C3%A9ment%20Bonnal&#39;s gravatar image" /><p>Clément Bonnal<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clément Bonnal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Feb '12, 12:04</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8754" class="comments-container"></div><div id="comment-tools-8754" class="comment-tools"></div><div class="clear"></div><div id="comment-8754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

