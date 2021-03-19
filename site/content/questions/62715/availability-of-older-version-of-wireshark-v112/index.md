+++
type = "question"
title = "availability of older version of Wireshark v1.12"
description = '''I am trying to run up Nordic nRF Sniffer that uses Wireshark 1.12 but cann&#x27;t find earlier archives of wireshark. Where are the archives? nRF Sniffer fails when run with the latrest Wireshark 2.7, so I need to install the older version. Thanks Peter'''
date = "2017-07-12T10:49:00Z"
lastmod = "2017-07-12T12:34:00Z"
weight = 62715
keywords = [ "sniffer", "v1.12", "blesniffer", "nrf", "wireshark" ]
aliases = [ "/questions/62715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [availability of older version of Wireshark v1.12](/questions/62715/availability-of-older-version-of-wireshark-v112)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to run up Nordic nRF Sniffer that uses Wireshark 1.12 but cann't find earlier archives of wireshark.</p><p>Where are the archives?</p><p>nRF Sniffer fails when run with the latrest Wireshark 2.7, so I need to install the older version.</p><p>Thanks</p><p>Peter</p></div><div id="question-tags" class="tags-container tags">sniffer v1.12 blesniffer nrf wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '17, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/b00922cde16141717647820c6bb16155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bledev10471&#39;s gravatar image" /><p>bledev10471<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bledev10471 has no accepted answers">0%</span></p></div></div><div id="comments-container-62715" class="comments-container"><span id="62732"></span><div id="comment-62732" class="comment"><div id="post-62732-score" class="comment-score"></div><div class="comment-text"><p>The Nordic nRF Sniffer works with the latest development release (2.4.0rc2). The final version 2.4.0 will be released later this summer.</p></div><div id="comment-62732-info" class="comment-info"><span class="comment-age">(13 Jul '17, 01:49)</span> stig ♦</div></div><span id="62738"></span><div id="comment-62738" class="comment"><div id="post-62738-score" class="comment-score"></div><div class="comment-text"><p>Do I need a new dissector? v2.2.7 complains that it cannt find the entry point 'new_create_dissector_handle' in the nordic_ble.dll dissector.</p><p>I'll try changing to 2.4.0rc2</p><p>Thanks</p></div><div id="comment-62738-info" class="comment-info"><span class="comment-age">(13 Jul '17, 04:23)</span> bledev10471</div></div><span id="62754"></span><div id="comment-62754" class="comment"><div id="post-62754-score" class="comment-score"></div><div class="comment-text"><p>The nordic_ble dissector is built-in to 2.4.0rc2 (and nordic_ble.dll will be ignored) so this should be fine.</p></div><div id="comment-62754-info" class="comment-info"><span class="comment-age">(13 Jul '17, 11:14)</span> stig ♦</div></div></div><div id="comment-tools-62715" class="comment-tools"></div><div class="clear"></div><div id="comment-62715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62719"></span>

<div id="answer-container-62719" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62719-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>All versions of Wireshark are available in the "all-versions" subdirectories on each download server, e.g. <a href="https://2.na.dl.wireshark.org/win64/all-versions/">https://2.na.dl.wireshark.org/win64/all-versions/</a> or <a href="https://www.wireshark.org/download/osx/all-versions/">https://www.wireshark.org/download/osx/all-versions/</a>. For a complete list of download servers, go to the <a href="https://www.wireshark.org/">Wireshark home page</a>, click on "<a href="https://www.wireshark.org/#download">Download</a>", then "<a href="https://www.wireshark.org/download.html">More downloads and documentation can be found on the downloads page</a>". The servers are listed under under "Go Spelunking".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '17, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-62719" class="comments-container"></div><div id="comment-tools-62719" class="comment-tools"></div><div class="clear"></div><div id="comment-62719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

