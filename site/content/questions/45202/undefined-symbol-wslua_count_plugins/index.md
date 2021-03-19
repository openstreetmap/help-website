+++
type = "question"
title = "undefined symbol: wslua_count_plugins"
description = '''I&#x27;m using XUbuntu 14.04 and the Wireshark available in repo is old (1.10) and crashes all the time I try to analyze VoIP. Them I&#x27;m trying to get pre-compiled versions from ppa, but I&#x27;m getting this error all the time: ./wireshark: symbol lookup error: ./wireshark: undefined symbol: wslua_count_plugi...'''
date = "2015-08-18T08:01:00Z"
lastmod = "2015-08-20T08:57:00Z"
weight = 45202
keywords = [ "crash", "xubuntu", "linux" ]
aliases = [ "/questions/45202" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [undefined symbol: wslua\_count\_plugins](/questions/45202/undefined-symbol-wslua_count_plugins)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45202-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using XUbuntu 14.04 and the Wireshark available in repo is old (1.10) and crashes all the time I try to analyze VoIP. Them I'm trying to get pre-compiled versions from ppa, but I'm getting this error all the time:</p><p><strong><em>./wireshark: symbol lookup error: ./wireshark: undefined symbol: wslua_count_plugins</em></strong></p><p>Somebody can help me with this? What Am I missing?</p></div><div id="question-tags" class="tags-container tags">crash xubuntu linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/e02fa1033ff0516e2a082408ad384a6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="takaite&#39;s gravatar image" /><p>takaite<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="takaite has no accepted answers">0%</span></p></div></div><div id="comments-container-45202" class="comments-container"></div><div id="comment-tools-45202" class="comment-tools"></div><div class="clear"></div><div id="comment-45202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45271"></span>

<div id="answer-container-45271" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45271-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That worked for me - try deleting:</p><p>/usr/local/lib/libwsutil.so.*</p><p>/usr/local/lib/libwireshark.so.*</p><p>/usr/local/lib/libwiretap.so.*</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '15, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/130bc92b9348328bbe5a83bfc872648c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mev&#39;s gravatar image" /><p>mev<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mev has one accepted answer">100%</span></p></div></div><div id="comments-container-45271" class="comments-container"><span id="45346"></span><div id="comment-45346" class="comment"><div id="post-45346-score" class="comment-score"></div><div class="comment-text"><p>It worked here too! Tks!</p></div><div id="comment-45346-info" class="comment-info"><span class="comment-age">(25 Aug '15, 09:29)</span> takaite</div></div></div><div id="comment-tools-45271" class="comment-tools"></div><div class="clear"></div><div id="comment-45271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

