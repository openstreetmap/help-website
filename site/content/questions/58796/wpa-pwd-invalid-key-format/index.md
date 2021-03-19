+++
type = "question"
title = "wpa-pwd invalid key format"
description = '''Hi, this is my first time to answer a question to WS. After upgrading OS from 2.0.x to 2.2.3, WPA-PWD decryption does not work for me. Both my Macbook and Windows10 PC have same error like this: &#x27;Invalid Key Format&#x27; After forcing close/open WS several times, the error does not happen and i can put i...'''
date = "2017-01-15T19:00:00Z"
lastmod = "2017-01-16T07:03:00Z"
weight = 58796
keywords = [ "wpa-pwd" ]
aliases = [ "/questions/58796" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wpa-pwd invalid key format](/questions/58796/wpa-pwd-invalid-key-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58796-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>this is my first time to answer a question to WS.</p><p>After upgrading OS from 2.0.x to 2.2.3, WPA-PWD decryption does not work for me. Both my Macbook and Windows10 PC have same error like this:</p><p>'Invalid Key Format'</p><p>After forcing close/open WS several times, the error does not happen and i can put in 'SSID:PW' normally and click 'OK' to save, but in actual, the wireless 'QoS' packets are not decrypted. Once, i 'reload' the file, the WS will auto closed unexpectedly.</p><p>I use WS to look at wireless packets captures every day. WS is very important for me. Any comments or help would be very appreciated.</p><p>Thanks, Elaine</p></div><div id="question-tags" class="tags-container tags">wpa-pwd</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '17, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/eb99f79d579faa3ec67a846d16ee412c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Elaine%20LL&#39;s gravatar image" /><p>Elaine LL<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Elaine LL has no accepted answers">0%</span></p></div></div><div id="comments-container-58796" class="comments-container"><span id="58806"></span><div id="comment-58806" class="comment"><div id="post-58806-score" class="comment-score"></div><div class="comment-text"><p>It would be interesting to see the 80211_keys file from your Personal configuration directory (see About Wireshark dialog, on the Folders tab), unless this contains security sensitive information.</p></div><div id="comment-58806-info" class="comment-info"><span class="comment-age">(16 Jan '17, 04:25)</span> Jaap ♦</div></div></div><div id="comment-tools-58796" class="comment-tools"></div><div class="clear"></div><div id="comment-58796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58811"></span>

<div id="answer-container-58811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58811-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had a similar issue awhile back. This might sound trivial, but did you try to completely uninstall Wireshark (removing all directories on the system after uninstall) and try a new installation?</p><p>It worked for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '17, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-58811" class="comments-container"><span id="58823"></span><div id="comment-58823" class="comment"><div id="post-58823-score" class="comment-score"></div><div class="comment-text"><p>just gone ahead to uninstall and installed it again, and worked. thanks for your comment!</p></div><div id="comment-58823-info" class="comment-info"><span class="comment-age">(16 Jan '17, 16:54)</span> Elaine LL</div></div><span id="58834"></span><div id="comment-58834" class="comment"><div id="post-58834-score" class="comment-score"></div><div class="comment-text"><p>@Elaine LL: If you found the answer useful to the the question, please accept the answer for others.</p></div><div id="comment-58834-info" class="comment-info"><span class="comment-age">(17 Jan '17, 05:51)</span> Amato_C</div></div></div><div id="comment-tools-58811" class="comment-tools"></div><div class="clear"></div><div id="comment-58811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

