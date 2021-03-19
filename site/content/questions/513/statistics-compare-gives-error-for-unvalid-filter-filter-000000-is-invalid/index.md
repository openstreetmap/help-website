+++
type = "question"
title = "Statistics / Compare gives error for unvalid filter (Filter &quot;000000&quot; - is invalid)"
description = '''Hello, When trying to compare two capture-files (following this article http://www.wireshark.org/docs/wsug_html_chunked/ChStatCompareCaptureFiles.html) I get an error-message when trying to run the compare. It seems that the filter-value is pre-populated even though I haven&#x27;t selected anything. The ...'''
date = "2010-10-15T00:00:00Z"
lastmod = "2010-10-15T00:00:00Z"
weight = 513
keywords = [ "filter", "compare", "000000" ]
aliases = [ "/questions/513" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Statistics / Compare gives error for unvalid filter (Filter "000000" - is invalid)](/questions/513/statistics-compare-gives-error-for-unvalid-filter-filter-000000-is-invalid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>When trying to compare two capture-files (following this article http://www.wireshark.org/docs/wsug_html_chunked/ChStatCompareCaptureFiles.html) I get an error-message when trying to run the compare. It seems that the filter-value is pre-populated even though I haven't selected anything.</p><p>The error-message I get is: Filter "000000" is invalid - "000000" is neither a field nor a protocol name.</p><p>If I click OK and try to apply a filter, I get the same error again, but this time it might look like this: Filter "000000,tcp.stream eq 1139" is invalid - Syntax error.</p><p>Version/OS: Version 1.4.1 (SVN Rev 34476 from /trunk-1.4) Running on 64-bit Windows 7, build 7600, with WinPcap version 4.1.2 (packet.dll version 4.1.0.2001), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.8.5, Gcrypt 1.4.5, without AirPcap.</p><p>Anyone seen this problem before and found a resolution??</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">filter compare 000000</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '10, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/2e8212a523915646b1773705ccd6f689?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="p0wned&#39;s gravatar image" /><p>p0wned<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="p0wned has no accepted answers">0%</span></p></div></div><div id="comments-container-513" class="comments-container"><span id="521"></span><div id="comment-521" class="comment"><div id="post-521-score" class="comment-score"></div><div class="comment-text"><p>Did you have 000000 in the Filter: box in the main window? If so, then that will be copied to the filter box in the "Compare" window (you can edit that filter box and remove the copied filter).</p></div><div id="comment-521-info" class="comment-info"><span class="comment-age">(17 Oct '10, 12:12)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-513" class="comment-tools"></div><div class="clear"></div><div id="comment-513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

