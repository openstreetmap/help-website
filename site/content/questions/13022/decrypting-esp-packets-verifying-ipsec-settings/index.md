+++
type = "question"
title = "Decrypting ESP packets, verifying IPSec settings"
description = '''I&#x27;m trying to decrypt ESP packets that I captured. I have a VPN setup using L2TP. I&#x27;ve read the http://wiki.wireshark.org/ESP_Preferences page. However, I don&#x27;t know how to verify all the fields required for a windows 7 Machine. For example the Encryption Algorithm, Authentication Algorithm, Encrypt...'''
date = "2012-07-26T09:01:00Z"
lastmod = "2012-07-26T09:12:00Z"
weight = 13022
keywords = [ "ipsec", "vpn", "algorithm", "l2tp", "esp" ]
aliases = [ "/questions/13022" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting ESP packets, verifying IPSec settings](/questions/13022/decrypting-esp-packets-verifying-ipsec-settings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13022-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt ESP packets that I captured. I have a VPN setup using L2TP. I've read the <a href="http://wiki.wireshark.org/ESP_Preferences">http://wiki.wireshark.org/ESP_Preferences</a> page. However, I don't know how to verify all the fields required for a windows 7 Machine. For example the Encryption Algorithm, Authentication Algorithm, Encryption key ect. Any guidance would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">ipsec vpn algorithm l2tp esp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '12, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/4f55d651c014d04412eded6682316720?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milesmeridith&#39;s gravatar image" /><p>milesmeridith<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milesmeridith has no accepted answers">0%</span></p></div></div><div id="comments-container-13022" class="comments-container"></div><div id="comment-tools-13022" class="comment-tools"></div><div class="clear"></div><div id="comment-13022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13025"></span>

<div id="answer-container-13025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13025-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please see my answer here: <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets</a></p><p>Search for "ESP Decryption".</p><p>To be able to decrypt ESP packets you need a lot of internal state data from your IPSEC implementation. Some Linux versions will give access to that data with this command: <strong>ip xfrm state</strong>. So, we need to figure out how to get that data from your L2TP server.</p><p>Is your L2TP server:</p><ul><li>a windows system (which one)</li><li>a firewall/vpn device (which one)</li><li>a Linux/Unix system (which one)</li></ul><p><strong>UPDATE</strong>:</p><blockquote><p>It's a SonicWall</p></blockquote><p>You need to boot a debug kernel (diagnostics firmware).</p><blockquote><p><code>http://www.sonicwall.com/app/projects/file_downloader/document_lib.php?t=TN&amp;id=240</code><br />
</p></blockquote><p>Then run some of the IPSEC debug commands mentioned in that document. I suggest at least these three:</p><blockquote><p><code>ipsec_debug=10</code><br />
<code>DumpIpsecSadb</code><br />
<code>PrintIpsecSas</code><br />
</p></blockquote><p>Maybe there is a way to get that information from the Windows 7 client as well, however I can't find any decent information about that.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '12, 10:23</p></div></div><div id="comments-container-13025" class="comments-container"><span id="13030"></span><div id="comment-13030" class="comment"><div id="post-13030-score" class="comment-score"></div><div class="comment-text"><p>It's a sonicwall FW. Thank you for your help btw.</p></div><div id="comment-13030-info" class="comment-info"><span class="comment-age">(26 Jul '12, 09:37)</span> milesmeridith</div></div><span id="13031"></span><div id="comment-13031" class="comment"><div id="post-13031-score" class="comment-score"></div><div class="comment-text"><p>I'll have to check how to get the required data from SonicWall debug output, if it's possible at all...</p><p><strong>UPDATE:</strong> see my update in the answer</p></div><div id="comment-13031-info" class="comment-info"><span class="comment-age">(26 Jul '12, 09:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13025" class="comment-tools"></div><div class="clear"></div><div id="comment-13025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

