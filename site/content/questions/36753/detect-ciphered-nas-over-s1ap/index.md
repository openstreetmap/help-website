+++
type = "question"
title = "Detect ciphered NAS over S1AP"
description = '''Hello, We have seen cases were ciphered NAS header actually contains plain NAS. How is wireshark detects if the message is ciphered or plain NAS? Thanks, Emi'''
date = "2014-10-01T04:53:00Z"
lastmod = "2014-10-01T07:21:00Z"
weight = 36753
keywords = [ "nas" ]
aliases = [ "/questions/36753" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Detect ciphered NAS over S1AP](/questions/36753/detect-ciphered-nas-over-s1ap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We have seen cases were ciphered NAS header actually contains plain NAS. How is wireshark detects if the message is ciphered or plain NAS?</p><p>Thanks, Emi</p></div><div id="question-tags" class="tags-container tags">nas</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '14, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p>Dianalab9<br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-36753" class="comments-container"></div><div id="comment-tools-36753" class="comment-tools"></div><div class="clear"></div><div id="comment-36753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36757"></span>

<div id="answer-container-36757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36757-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, recent Wireshark versions are using a basic heuristic: if the security header type is 2 or 4 and the MAC is not 0, then it checks the protocol discriminator to see whether it's in the allowed range.</p><pre><code>    if ((security_header_type == 2)||(security_header_type == 4)) {
        /* Possible ciphered message */
        if (msg_auth_code != 0) {
            /* Sequence number  Sequence number 9.6 M   V   1 */
            proto_tree_add_item(nas_eps_tree, hf_nas_eps_seq_no, tvb, offset, 1, ENC_BIG_ENDIAN);
            offset++;
            /* Integrity protected and ciphered = 2, Integrity protected and ciphered with new EPS security context = 4 */
            /* Read security_header_type / EPS bearer id AND pd */
            pd = tvb_get_guint8(tvb,offset);
            /* If pd is in plaintext this message probably isn&#39;t ciphered */
            if ((pd != 7) &amp;&amp; (pd != 15) &amp;&amp;
                (((pd&amp;0x0f) != 2) || (((pd&amp;0x0f) == 2) &amp;&amp; ((pd&amp;0xf0) &gt; 0) &amp;&amp; ((pd&amp;0xf0) &lt; 0x50)))) {
                proto_tree_add_text(nas_eps_tree, tvb, offset, len-6,&quot;Ciphered message&quot;);
                return;
            }</code></pre><p>This heuristic might consider some ciphered messages as plain and try to decode it. But it should not detect a plain message as being ciphered. At least it allows to try to decode some messages in EEA0 but with integrity activated. Depending on the Wireshark version you use, you might have a slightly different heuristic (it was refined several times).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '14, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-36757" class="comments-container"><span id="36758"></span><div id="comment-36758" class="comment"><div id="post-36758-score" class="comment-score"></div><div class="comment-text"><p>This helps us a lot! Thanks!</p></div><div id="comment-36758-info" class="comment-info"><span class="comment-age">(01 Oct '14, 08:07)</span> Dianalab9</div></div><span id="36759"></span><div id="comment-36759" class="comment"><div id="post-36759-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-36759-info" class="comment-info"><span class="comment-age">(01 Oct '14, 08:46)</span> grahamb ♦</div></div></div><div id="comment-tools-36757" class="comment-tools"></div><div class="clear"></div><div id="comment-36757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

