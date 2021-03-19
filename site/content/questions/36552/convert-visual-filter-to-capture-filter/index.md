+++
type = "question"
title = "convert visual filter to capture filter"
description = '''Hello, i don&#x27;t really get the syntax on the capture filter, how would this translate into capturing filter? Thanks. wlan.fc.type_subtype eq 4 and wlan.addr == ff:ff:ff:ff:ff:ff'''
date = "2014-09-23T19:08:00Z"
lastmod = "2014-10-02T11:48:00Z"
weight = 36552
keywords = [ "filter", "convert" ]
aliases = [ "/questions/36552" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [convert visual filter to capture filter](/questions/36552/convert-visual-filter-to-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36552-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i don't really get the syntax on the capture filter, how would this translate into capturing filter?</p><p>Thanks.</p><p>wlan.fc.type_subtype eq 4 and wlan.addr == ff:ff:ff:ff:ff:ff</p></div><div id="question-tags" class="tags-container tags">filter convert</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '14, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/e54cf26a64c34eb15eea0ec74e6e614f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pato-llaguno&#39;s gravatar image" /><p>pato-llaguno<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pato-llaguno has no accepted answers">0%</span></p></div></div><div id="comments-container-36552" class="comments-container"></div><div id="comment-tools-36552" class="comment-tools"></div><div class="clear"></div><div id="comment-36552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36804"></span>

<div id="answer-container-36804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36804-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>4 is a probe request, and wlan.addr matches all possible MAC addresses, so that would be</p><pre><code>subtype probe-req and (wlan addr1 ff:ff:ff:ff:ff:ff or wlan addr2 ff:ff:ff:ff:ff:ff or wlan addr3 ff:ff:ff:ff:ff:ff or wlan addr4 ff:ff:ff:ff:ff:ff)</code></pre><p>although not all versions of libpcap support "wlan addrN".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '14, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36804" class="comments-container"></div><div id="comment-tools-36804" class="comment-tools"></div><div class="clear"></div><div id="comment-36804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

