+++
type = "question"
title = "No Decryption of Instagram"
description = '''I&#x27;m running Wireshark v2.2.0 in a Kali Linux VM. I have the SSLKEYLOGFILE environment variable set, so that SSL keys will be saved and Wireshark pointed to that file. I&#x27;ve got Chrome v55.0 installed in Kali also. This setup works and I&#x27;m able to capture sessions from SSL websites, store the SSL keys...'''
date = "2016-12-28T11:33:00Z"
lastmod = "2017-01-03T14:50:00Z"
weight = 58406
keywords = [ "sslkeylogfile", "ssl_decrypt" ]
aliases = [ "/questions/58406" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No Decryption of Instagram](/questions/58406/no-decryption-of-instagram)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58406-score" class="post-score" title="current number of votes">0</div><span id="post-58406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Wireshark v2.2.0 in a Kali Linux VM. I have the SSLKEYLOGFILE environment variable set, so that SSL keys will be saved and Wireshark pointed to that file. I've got Chrome v55.0 installed in Kali also. This setup works and I'm able to capture sessions from SSL websites, store the SSL keys, view the decrypted packets and export HTTP objects. However, when I try this on Instagram the decryption fails. Everything seems to be working the same, i.e., SSL keys are being stored to the log file and the packets are being captured. But it doesn't show the "decrypted" tab for the packets and on the the export HTTP objects window, no objects are shown. Anyone got an idea how I can decrypt this session?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sslkeylogfile" rel="tag" title="see questions tagged &#39;sslkeylogfile&#39;">sslkeylogfile</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '16, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/5c1523031f7e14e9ed410977af251286?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="who_me&#39;s gravatar image" /><p><span>who_me</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="who_me has no accepted answers">0%</span></p></div></div><div id="comments-container-58406" class="comments-container"></div><div id="comment-tools-58406" class="comment-tools"></div><div class="clear"></div><div id="comment-58406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58440"></span>

<div id="answer-container-58440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58440-score" class="post-score" title="current number of votes">1</div><span id="post-58440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For SSL/TLS decryption, ensure that the full handshake is captured (clear browser cache).</p><p>For Export HTTP Objects, note that this is currently not supported for HTTP/2 (which is what Instagram seems to use).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '16, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-58440" class="comments-container"><span id="58441"></span><div id="comment-58441" class="comment"><div id="post-58441-score" class="comment-score"></div><div class="comment-text"><p>This fixed the SSL problem. Thanks!</p></div><div id="comment-58441-info" class="comment-info"><span class="comment-age">(31 Dec '16, 08:23)</span> <span class="comment-user userinfo">who_me</span></div></div><span id="58486"></span><div id="comment-58486" class="comment"><div id="post-58486-score" class="comment-score"></div><div class="comment-text"><p>Since the answer appears to have answered your question please be sure to Accept it (by checking on the checkmark next to it). See the FAQ.</p></div><div id="comment-58486-info" class="comment-info"><span class="comment-age">(03 Jan '17, 14:50)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-58440" class="comment-tools"></div><div class="clear"></div><div id="comment-58440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

