+++
type = "question"
title = "Built in Dissector compiles but doesn&#x27;t load."
description = '''I wrote the foo dissector example, put it in epan/dissectors, changed the Makefile.common, and ran the whole autogen, configure, make, make install. My code compiles just fine now and i don&#x27;t run into any errors or warnings. However when i run wireshark my protocol is not there. It is red when i typ...'''
date = "2012-06-18T11:11:00Z"
lastmod = "2012-06-18T13:48:00Z"
weight = 12028
keywords = [ "compile", "dissector", "built-in" ]
aliases = [ "/questions/12028" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Built in Dissector compiles but doesn't load.](/questions/12028/built-in-dissector-compiles-but-doesnt-load)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12028-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote the foo dissector example, put it in epan/dissectors, changed the Makefile.common, and ran the whole autogen, configure, make, make install. My code compiles just fine now and i don't run into any errors or warnings. However when i run wireshark my protocol is not there. It is red when i type it in the filter and it does not appear on the list of supported protocols. How can I get my protocol to show up in wireshark?</p></div><div id="question-tags" class="tags-container tags">compile dissector built-in</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/9370e965a8cb362339126710f94fd714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rewindmad&#39;s gravatar image" /><p>rewindmad<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rewindmad has no accepted answers">0%</span></p></div></div><div id="comments-container-12028" class="comments-container"><span id="12060"></span><div id="comment-12060" class="comment"><div id="post-12060-score" class="comment-score"></div><div class="comment-text"><p>Nevermind, I managed to get it working as a plugin instead thank you.</p></div><div id="comment-12060-info" class="comment-info"><span class="comment-age">(19 Jun '12, 09:04)</span> rewindmad</div></div><span id="12063"></span><div id="comment-12063" class="comment"><div id="post-12063-score" class="comment-score"></div><div class="comment-text"><p>Well, if you want to change it to a built-in dissector, then have a look at the example provided in section 1.2 of <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=43228&amp;view=markup">README.developer</a>.</p></div><div id="comment-12063-info" class="comment-info"><span class="comment-age">(19 Jun '12, 11:13)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-12028" class="comment-tools"></div><div class="clear"></div><div id="comment-12028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12030"></span>

<div id="answer-container-12030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12030-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure you're running your newly compiled version of Wireshark and not an already installed version, perhaps? In particular, did you follow all the steps in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcRunFirstTime.html">developer's guide</a> and run the following from your build directory?</p><pre><code>WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-12030" class="comments-container"></div><div id="comment-tools-12030" class="comment-tools"></div><div class="clear"></div><div id="comment-12030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

