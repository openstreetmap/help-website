+++
type = "question"
title = "Do I need to enable an option in order to see the EIGRP payload encapsulated into an ESP with ESP-NULL encryption?"
description = '''Good afternoon, I&#x27;m trying to look inside a EIGRP Update packet that is encapsulated over a DMVPN solutions (GRE and ESP with ESP-NULL set). For whatever reason the Data part of the EIGRP is garbage. Any ideas how to fix this problem? Does Wireshark have a limitation on how far it can look inside an...'''
date = "2011-10-13T11:54:00Z"
lastmod = "2011-10-13T14:44:00Z"
weight = 6877
keywords = [ "eigrp", "esp" ]
aliases = [ "/questions/6877" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do I need to enable an option in order to see the EIGRP payload encapsulated into an ESP with ESP-NULL encryption?](/questions/6877/do-i-need-to-enable-an-option-in-order-to-see-the-eigrp-payload-encapsulated-into-an-esp-with-esp-null-encryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6877-score" class="post-score" title="current number of votes">0</div><span id="post-6877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good afternoon,</p><p>I'm trying to look inside a EIGRP Update packet that is encapsulated over a DMVPN solutions (GRE and ESP with ESP-NULL set). For whatever reason the Data part of the EIGRP is garbage.</p><p>Any ideas how to fix this problem? Does Wireshark have a limitation on how far it can look inside an IP packet?</p><p>Thanks G.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eigrp" rel="tag" title="see questions tagged &#39;eigrp&#39;">eigrp</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '11, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/8a891b2fa362e05fc050fe0daa384f8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="calin_112&#39;s gravatar image" /><p><span>calin_112</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="calin_112 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '11, 11:56</strong> </span></p></div></div><div id="comments-container-6877" class="comments-container"><span id="6879"></span><div id="comment-6879" class="comment"><div id="post-6879-score" class="comment-score"></div><div class="comment-text"><p>Same problem with EIGRP over GRE.</p></div><div id="comment-6879-info" class="comment-info"><span class="comment-age">(13 Oct '11, 13:08)</span> <span class="comment-user userinfo">calin_112</span></div></div></div><div id="comment-tools-6877" class="comment-tools"></div><div class="clear"></div><div id="comment-6877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6880"></span>

<div id="answer-container-6880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6880-score" class="post-score" title="current number of votes">0</div><span id="post-6880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, From dev mailing list Hi, I'm looking at en NULL encrypted ESP payload, trying to display it in Wireshark, in order to do so The preferences "Attempt to detect/decode NULL encrypted ESP payloads" must be "ticked" ( No supprise) "Attempt to detect/decode encrypted ESP payloads" must be "un-ticked" is that realy corrrect? Or should this patch be applied?</p><pre><code>C:\wireshark\trunk&gt;svn diff
Index: epan/dissectors/packet-ipsec.c
===================================================================
--- epan/dissectors/packet-ipsec.c      (revision 889)
+++ epan/dissectors/packet-ipsec.c      (working copy)
@@ -1099,8 +1099,7 @@

#ifdef HAVE_LIBGCRYPT
   /* The SAD is not activated */
-  if(g_esp_enable_null_encryption_decode_heuristic &amp;&amp;
-    !g_esp_enable_encryption_decode)
+  if(g_esp_enable_null_encryption_decode_heuristic)
     null_encryption_decode_heuristic = TRUE;

   if(g_esp_enable_encryption_decode || g_esp_enable_authentication_check)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '11, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Oct '11, 05:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-6880" class="comments-container"></div><div id="comment-tools-6880" class="comment-tools"></div><div class="clear"></div><div id="comment-6880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

