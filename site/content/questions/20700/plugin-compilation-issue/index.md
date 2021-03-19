+++
type = "question"
title = "plugin compilation issue"
description = '''I was able to compile amin as well as foo dissector, but the dissector that I had written is not getting compiled as well as (amin,foo also not working). Error when doing nmake all is: Making plugin.c (using python) Updating plugin.c NMAKE : fatal error U1073: don&#x27;t know how to make &#x27;..&#92;..&#92;epan&#92;libw...'''
date = "2013-04-22T03:15:00Z"
lastmod = "2013-04-22T07:19:00Z"
weight = 20700
keywords = [ "compile", "plugin" ]
aliases = [ "/questions/20700" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [plugin compilation issue](/questions/20700/plugin-compilation-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20700-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was able to compile amin as well as foo dissector, but the dissector that I had written is not getting compiled as well as (amin,foo also not working). Error when doing nmake all is:</p><pre><code>Making plugin.c (using python)
Updating plugin.c
NMAKE : fatal error U1073: don&#39;t know how to make &#39;..\..\epan\libwireshark.lib&#39;stop.</code></pre><p>Can anybody help promptly?</p></div><div id="question-tags" class="tags-container tags">compile plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/afa04deca78e2ac8df31ecc4deea5bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajain&#39;s gravatar image" /><p>ajain<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajain has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '13, 07:15</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-20700" class="comments-container"></div><div id="comment-tools-20700" class="comment-tools"></div><div class="clear"></div><div id="comment-20700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20708"></span>

<div id="answer-container-20708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20708-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should probably start by reading (or possibly re-reading) <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.plugins?revision=47992&amp;view=markup">README.plugins</a> very carefully.</p><p>And don't forget about <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=48861&amp;view=markup">README.developer</a>, as well as the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Wireshark developer's guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '13, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-20708" class="comments-container"></div><div id="comment-tools-20708" class="comment-tools"></div><div class="clear"></div><div id="comment-20708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

