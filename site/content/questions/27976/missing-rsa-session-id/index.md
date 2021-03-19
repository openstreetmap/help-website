+++
type = "question"
title = "Missing RSA session ID"
description = '''Hello,  I&#x27;ve come across this a few times at work and am wondering if anyone has a possible explanation. When trying to decrypt traces with Wireshark, decryption works fine, but when exporting the session keys from the file menu, the RSA-Session ID comes up as empty.'''
date = "2013-12-10T09:54:00Z"
lastmod = "2013-12-13T03:11:00Z"
weight = 27976
keywords = [ "empty", "id", "rsa-session" ]
aliases = [ "/questions/27976" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing RSA session ID](/questions/27976/missing-rsa-session-id)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27976-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I've come across this a few times at work and am wondering if anyone has a possible explanation. When trying to decrypt traces with Wireshark, decryption works fine, but when exporting the session keys from the file menu, the RSA-Session ID comes up as empty.</p></div><div id="question-tags" class="tags-container tags">empty id rsa-session</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '13, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/41fa3944980693e72e882a5ec1349d00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voiper&#39;s gravatar image" /><p>voiper<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voiper has no accepted answers">0%</span></p></div></div><div id="comments-container-27976" class="comments-container"></div><div id="comment-tools-27976" class="comment-tools"></div><div class="clear"></div><div id="comment-27976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28072"></span>

<div id="answer-container-28072" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28072-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not all TLS sessions have a Session ID (i.e. SessionID length is zero). Due to <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9546">a bug</a>, pre-master secrets with an empty session ID are stored anyway. You can try using <a href="https://developer.mozilla.org/en-US/docs/NSS_Key_Log_Format">key log files</a> instead, either by using it directly on the application you are analyzing or by copying the Random field from the ClientHello and combine it with the pre-master secret.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-28072" class="comments-container"></div><div id="comment-tools-28072" class="comment-tools"></div><div class="clear"></div><div id="comment-28072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

