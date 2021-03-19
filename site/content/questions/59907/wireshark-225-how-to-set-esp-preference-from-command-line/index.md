+++
type = "question"
title = "wireshark 2.2.5 - how to set ESP preference from command line"
description = '''Hello there, I&#x27;m finding a way to set ESP preference, i.e. encryption keys, authentication keys, from command line. I have tried below command but wireshark always says no preference matches mine tshark -i - -Y &quot;sip||esp&quot; -d tcp.port==&quot;5000-65535&quot;,sip -d udp.port==&quot;5000-65535&quot;,sip -T text -l -O &quot;sip...'''
date = "2017-03-08T00:16:00Z"
lastmod = "2017-03-08T08:12:00Z"
weight = 59907
keywords = [ "esp_preferences", "command-line", "wireshark" ]
aliases = [ "/questions/59907" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark 2.2.5 - how to set ESP preference from command line](/questions/59907/wireshark-225-how-to-set-esp-preference-from-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59907-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there,</p><p>I'm finding a way to set ESP preference, i.e. encryption keys, authentication keys, from command line. I have tried below command but wireshark always says no preference matches mine</p><pre><code>tshark -i - -Y &quot;sip||esp&quot; -d tcp.port==&quot;5000-65535&quot;,sip -d udp.port==&quot;5000-65535&quot;,sip -T text -l -O &quot;sip,esp&quot; -o esp.enable\_null\_encryption\_decode\_heuristic:true -o esp.enable\_authentication\_check:true -o esp.enable\_encryption\_decode:true -o &quot;esp.sa\_1:IPv4|\*|\*|\*&quot; -o &quot;esp.encryption\_algorithm\_1:AES-CBC [RFC3602]&quot; -o &quot;esp.encryption\_key\_1:0xC5DA46E7FF43C8D6C0DD3A2707E42E05&quot; -o &quot;esp.authentication\_algorithm\_1:HMAC-MD5-96 [RFC2403]&quot; -o &quot;esp.authentication\_key\_1:0xE5A349FCBAD409D15C766702CD400BA4&quot; &gt; D:\test\dump2.txt</code></pre><p>It's always said that "esp.sa_1" flag is unknown. Same as esp.encryption_algorithm_1 and esp.authentication_algorithm_1, and so on.</p><p>I have searched around and think that esp.sa_1 is only available in older version of wireshark.</p><p>Does anyone know how to have these preference on wireshark 2.2.5?</p><p>Thank so much!</p></div><div id="question-tags" class="tags-container tags">esp_preferences command-line wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/a040c26be3c4ca664c92358f3799ae81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viet-Anh%20Dinh&#39;s gravatar image" /><p>Viet-Anh Dinh<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viet-Anh Dinh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Mar '17, 08:13</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-59907" class="comments-container"></div><div id="comment-tools-59907" class="comment-tools"></div><div class="clear"></div><div id="comment-59907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59929"></span>

<div id="answer-container-59929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59929-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to <a href="http://stackoverflow.com/questions/42666665/wireshark-2-2-5-how-to-set-esp-preference-from-command-line">this same question</a> over at stackoverflow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '17, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59929" class="comments-container"></div><div id="comment-tools-59929" class="comment-tools"></div><div class="clear"></div><div id="comment-59929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

