+++
type = "question"
title = "exporting media.type content into character string instead of hex?"
description = '''Following command outputs the &quot;media.type&quot; content as a hex string in my csv file. Is there a way to write this as ascii characters in the csv file? tshark -r xyz.pcap -T fields -e frame.number -e frame.time -e media.type -E header=y -E separator=, -E quote=d &amp;gt; abc.csv  Thanks.'''
date = "2016-01-17T17:40:00Z"
lastmod = "2016-01-17T19:33:00Z"
weight = 49312
keywords = [ "csv", "tshark" ]
aliases = [ "/questions/49312" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [exporting media.type content into character string instead of hex?](/questions/49312/exporting-mediatype-content-into-character-string-instead-of-hex)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49312-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Following command outputs the "media.type" content as a hex string in my csv file. Is there a way to write this as ascii characters in the csv file?</p><pre><code>tshark -r xyz.pcap -T fields -e frame.number -e frame.time -e media.type -E header=y -E separator=, -E quote=d &gt; abc.csv</code></pre><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">csv tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '16, 17:40</strong></p><img src="https://secure.gravatar.com/avatar/2d3358e5b4a4507b418f0f015c5377bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hvs&#39;s gravatar image" /><p>hvs<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hvs has no accepted answers">0%</span></p></div></div><div id="comments-container-49312" class="comments-container"></div><div id="comment-tools-49312" class="comment-tools"></div><div class="clear"></div><div id="comment-49312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49313"></span>

<div id="answer-container-49313" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49313-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to write this as ascii characters in the csv file?</p></blockquote><p>Unfortunately, there isn't any; for some not-immediately-obvious reason, the "media.type" field has the type "bytes" rather than "string", meaning it gets dumped as a hex value.</p><p>Please file a bug on this at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '16, 19:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49313" class="comments-container"></div><div id="comment-tools-49313" class="comment-tools"></div><div class="clear"></div><div id="comment-49313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

