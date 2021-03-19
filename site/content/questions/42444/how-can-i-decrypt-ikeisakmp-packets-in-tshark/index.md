+++
type = "question"
title = "How can I decrypt IKE/ISAKMP packets in tshark"
description = '''Hi, I&#x27;m looking for a way to decrypt ISAKMP ikev2 messages using tshark. I was able to do through preferences in wireshark. But not sure how will I give that preference with the &quot;-o&quot; option in tshark. Any help is appreciated.'''
date = "2015-05-16T18:29:00Z"
lastmod = "2015-05-17T07:03:00Z"
weight = 42444
keywords = [ "isakmp", "tshark", "ike" ]
aliases = [ "/questions/42444" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I decrypt IKE/ISAKMP packets in tshark](/questions/42444/how-can-i-decrypt-ikeisakmp-packets-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42444-score" class="post-score" title="current number of votes">0</div><span id="post-42444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm looking for a way to decrypt ISAKMP ikev2 messages using <strong><em>tshark</em></strong>. I was able to do through preferences in wireshark. But not sure how will I give that preference with the "-o" option in tshark.</p><p>Any help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-isakmp" rel="tag" title="see questions tagged &#39;isakmp&#39;">isakmp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ike" rel="tag" title="see questions tagged &#39;ike&#39;">ike</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '15, 18:29</strong></p><img src="https://secure.gravatar.com/avatar/d9de69b2dfe0aaf9226e064fde4f17f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shakti&#39;s gravatar image" /><p><span>shakti</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shakti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '15, 07:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-42444" class="comments-container"></div><div id="comment-tools-42444" class="comment-tools"></div><div class="clear"></div><div id="comment-42444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42446"></span>

<div id="answer-container-42446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42446-score" class="post-score" title="current number of votes">0</div><span id="post-42446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You would use -o if you want to override a current preferences value. You already configured the decryption in Wireshark and if it works there, it will also work in tshark. Both read the same preferences file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-42446" class="comments-container"></div><div id="comment-tools-42446" class="comment-tools"></div><div class="clear"></div><div id="comment-42446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42460"></span>

<div id="answer-container-42460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42460-score" class="post-score" title="current number of votes">0</div><span id="post-42460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To decrypt ISAKMP/IKE frames, please fill the following file with the same paramaters you entered in the GUI:</p><p><strong>IKEv1:</strong></p><blockquote><p>File: %APPDATA%\Wireshark\ikev1_decryption_table</p></blockquote><p><strong>IKEv2:</strong></p><blockquote><p>File: %APPDATA%\Wireshark\ikev2_decryption_table</p></blockquote><p>If you don't know what to put into those files, first fill in the values in the GUI and then take the generated files as an example.</p><p>Then enable ISAKMP/IKE decryption in tshark, you need the following -o options:</p><blockquote><p>tshark -nr ipsec.cap -o <strong>isakmp.ikev1_decryption_table:TRUE</strong> -V &gt; IKEv1_decrypted.txt<br />
tshark -nr ipsec.cap -o <strong>isakmp.ikev2_decryption_table:TRUE</strong> -V &gt; IKEv2_decrypted.txt<br />
</p></blockquote><p>After that, you'll see the decrypted IKE frames in the output files.</p><pre><code>   Encrypted Data (40 bytes)    &lt;================ HERE 
        Type Payload: Identification (5)
            Next payload: Hash (8)
            Payload length: 12
            ID type: IPV4_ADDR (1)
            Protocol ID: Unused
            Port: Unused
            Identification Data:192.168.140.205
                ID_IPV4_ADDR: 192.168.140.205 (192.168.140.205)
        Type Payload: Hash (8)
            Next payload: NONE / No Next Payload  (0)
            Payload length: 24
            Hash DATA: 3321b19237fb86a3231239d2049260d1b4a6e0e7
        Extra data: 00000000</code></pre><p>See also my other answers related to IKE/ESP decryption:</p><blockquote><p><a href="https://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets">https://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-andor-esp-packets</a><br />
<a href="https://ask.wireshark.org/questions/22874/tshark-decrypt-esp-packets-with-command-line-arguments">https://ask.wireshark.org/questions/22874/tshark-decrypt-esp-packets-with-command-line-arguments</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '15, 07:04</strong> </span></p></div></div><div id="comments-container-42460" class="comments-container"></div><div id="comment-tools-42460" class="comment-tools"></div><div class="clear"></div><div id="comment-42460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

