+++
type = "question"
title = "attempt to index global &#x27;bit32&#x27; (a nil value)"
description = '''Hi, I am writing a dissector for wireshark, I used bit32.band operation in that.  I tried to run the dissector, got an error &quot;attempt to index global &#x27;bit32&#x27; (a nil value). I realized that my version has lua 5.1, which doesn&#x27;t have bit32. Can someone please give me an alternative? TIA, Abhilash'''
date = "2014-08-06T08:53:00Z"
lastmod = "2014-08-07T07:33:00Z"
weight = 35270
keywords = [ "lua", "bit32" ]
aliases = [ "/questions/35270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [attempt to index global 'bit32' (a nil value)](/questions/35270/attempt-to-index-global-bit32-a-nil-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35270-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am writing a dissector for wireshark, I used bit32.band operation in that. I tried to run the dissector, got an error "attempt to index global 'bit32' (a nil value).</p><p>I realized that my version has lua 5.1, which doesn't have bit32. Can someone please give me an alternative?</p><p>TIA, Abhilash</p></div><div id="question-tags" class="tags-container tags">lua bit32</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/cdba9ca71a2cc31a8961c51fb80edb6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abhilash&#39;s gravatar image" /><p>abhilash<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abhilash has no accepted answers">0%</span></p></div></div><div id="comments-container-35270" class="comments-container"></div><div id="comment-tools-35270" class="comment-tools"></div><div class="clear"></div><div id="comment-35270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35305"></span>

<div id="answer-container-35305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35305-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has Mike Pall's BitOp library built-in, regardless of Lua engine version. I'm not sure why it's not documented in the API docs, but you can find info <a href="http://bitop.luajit.org/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-35305" class="comments-container"></div><div id="comment-tools-35305" class="comment-tools"></div><div class="clear"></div><div id="comment-35305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

