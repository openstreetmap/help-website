+++
type = "question"
title = "No decryption of ISAKMP packets?"
description = '''I&#x27;d like to see decryption of encrypted ISAKMP traffic. I entered the cookie and the key into the IKEv1 Decryption Table, but in the ISAKMP packets, the &quot;Encrypted Data&quot; doesn&#x27;t have the clicky-box to expand and see it decrypted. I&#x27;m using Wireshark 1.8.4 with GCrypt on Windows 7. Is there something...'''
date = "2013-02-07T14:55:00Z"
lastmod = "2013-02-07T16:27:00Z"
weight = 18418
keywords = [ "isakmp", "gcrypt", "decryption", "ike", "ikev1" ]
aliases = [ "/questions/18418" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No decryption of ISAKMP packets?](/questions/18418/no-decryption-of-isakmp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18418-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to see decryption of encrypted ISAKMP traffic. I entered the cookie and the key into the IKEv1 Decryption Table, but in the ISAKMP packets, the "Encrypted Data" doesn't have the clicky-box to expand and see it decrypted. I'm using Wireshark 1.8.4 with GCrypt on Windows 7. Is there something else I need to do?</p></div><div id="question-tags" class="tags-container tags">isakmp gcrypt decryption ike ikev1</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '13, 14:55</strong></p><img src="https://secure.gravatar.com/avatar/4825de8eab0ec31a6d238250ee8a9f21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scherertim&#39;s gravatar image" /><p>scherertim<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scherertim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Feb '13, 14:59</p></div></div><div id="comments-container-18418" class="comments-container"></div><div id="comment-tools-18418" class="comment-tools"></div><div class="clear"></div><div id="comment-18418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18426"></span>

<div id="answer-container-18426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18426-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>please read my answer of the following questions to see if there is anything that can help you.</p><blockquote><p><code>http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '13, 16:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18426" class="comments-container"><span id="18430"></span><div id="comment-18430" class="comment"><div id="post-18430-score" class="comment-score"></div><div class="comment-text"><p>I did read that, thanks. No luck though. I'm using Windows IPSec rather than StrongSwan/Linux, so I copied the cookie from the Wireshark packets and got the key by converting the preshared string to hex with a helpful web calculator.</p></div><div id="comment-18430-info" class="comment-info"><span class="comment-age">(07 Feb '13, 16:42)</span> scherertim</div></div><span id="18432"></span><div id="comment-18432" class="comment"><div id="post-18432-score" class="comment-score"></div><div class="comment-text"><blockquote><p>got the key by converting the preshared string to hex with a helpful web calculator.</p></blockquote><p>can you please post the URL for that web calculator? If it just 'converted' your PSK to hex, then you have two problems:</p><ol><li>you have exposed your PSK to an unknown party, probably with the IP address of your gateway. If so, I urgently recommend to change the PSK ;-))</li><li>the PSK (even in HEX) and the <strong>enc key</strong> needed, is <strong>not</strong> the same thing! Unfortunately I don't know how to get the <strong>enc key</strong> in a windows environment. I'm not even sure if that information will be exposed by the system at all.</li></ol></div><div id="comment-18432-info" class="comment-info"><span class="comment-age">(07 Feb '13, 16:49)</span> Kurt Knochner ♦</div></div><span id="18446"></span><div id="comment-18446" class="comment"><div id="post-18446-score" class="comment-score"></div><div class="comment-text"><p>No worries about the security, it's just a test setup. The calculator is <a href="http://easycalculation.com/ascii-hex.php.">http://easycalculation.com/ascii-hex.php.</a> I removed the spaces before entering it into Wireshark. But if the only problem is that I gave Wireshark the wrong key, wouldn't it decrypt the data and end up with garbage? It seems like it didn't even try, as if I missed a "Decrypt Now" button or something.</p></div><div id="comment-18446-info" class="comment-info"><span class="comment-age">(08 Feb '13, 08:45)</span> scherertim</div></div><span id="18447"></span><div id="comment-18447" class="comment"><div id="post-18447-score" class="comment-score"></div><div class="comment-text"><blockquote><p>But if the only problem is that I gave Wireshark the wrong key, wouldn't it decrypt the data and end up with garbage?</p></blockquote><p>I guess so, however I never intentionally tried it with a wrong key. You can try it with the sample file and the crypto parameters in my answer to the question I mentioned, to see if IKE decryption works on your system.</p><p>BTW: What is your Wireshark version (wireshark -v)?</p></div><div id="comment-18447-info" class="comment-info"><span class="comment-age">(08 Feb '13, 12:04)</span> Kurt Knochner ♦</div></div><span id="18453"></span><div id="comment-18453" class="comment"><div id="post-18453-score" class="comment-score"></div><div class="comment-text"><p>Version 1.8.4 (SVN Rev 46250 from /trunk-1.8). I get the same result with the sample file: no clickable box to show the decrypted data.</p></div><div id="comment-18453-info" class="comment-info"><span class="comment-age">(08 Feb '13, 16:05)</span> scherertim</div></div><span id="18465"></span><div id="comment-18465" class="comment not_top_scorer"><div id="post-18465-score" class="comment-score"></div><div class="comment-text"><p>O.K. I just tried it with 1.8.4 and you are right. It does not work any longer. I'll file a bug report and look into the code changes myself.</p><p>@Gerald Combs: The screenshots in <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">my answer</a> are missing (they were in the part "Result without decryption:" and "Result with decryption:". Is it possible to restore them?</p></div><div id="comment-18465-info" class="comment-info"><span class="comment-age">(09 Feb '13, 02:36)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18426" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-18426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

