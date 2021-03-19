+++
type = "question"
title = "Wireshark 1.8.x doesn&#x27;t save decryption keys for wireless"
description = '''On several Windows 7 64-bit systems I&#x27;m not able to save decryption keys for decrypting wireless packets. Normally I use the Decryption Keys button on the Wireless toolbar. Also the key management under Preferences -&amp;gt; Protocols -&amp;gt; IEEE 802.11 and the Decryption Keys Settings on the toolbar are...'''
date = "2012-08-15T02:01:00Z"
lastmod = "2012-08-30T19:43:00Z"
weight = 13647
keywords = [ "decryption", "windows7" ]
aliases = [ "/questions/13647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.8.x doesn't save decryption keys for wireless](/questions/13647/wireshark-18x-doesnt-save-decryption-keys-for-wireless)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13647-score" class="post-score" title="current number of votes">0</div><span id="post-13647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On several Windows 7 64-bit systems I'm not able to save decryption keys for decrypting wireless packets. Normally I use the Decryption Keys button on the Wireless toolbar. Also the key management under Preferences -&gt; Protocols -&gt; IEEE 802.11 and the Decryption Keys Settings on the toolbar are not consistent. Does anyone else can confirm this problem?</p><p>Best Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '12, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/e5f17e21feaa02bf10f18d203d4b0369?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wmann&#39;s gravatar image" /><p><span>wmann</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wmann has no accepted answers">0%</span></p></div></div><div id="comments-container-13647" class="comments-container"><span id="13853"></span><div id="comment-13853" class="comment"><div id="post-13853-score" class="comment-score"></div><div class="comment-text"><p>I just discovered this same problem both with XP 32bit and Win7 64bit.</p></div><div id="comment-13853-info" class="comment-info"><span class="comment-age">(23 Aug '12, 21:33)</span> <span class="comment-user userinfo">gdhamp01</span></div></div></div><div id="comment-tools-13647" class="comment-tools"></div><div class="clear"></div><div id="comment-13647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13969"></span>

<div id="answer-container-13969" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13969-score" class="post-score" title="current number of votes">0</div><span id="post-13969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you referring to wpa-psk keys? If so, see my answers to questions <a href="http://ask.wireshark.org/questions/13688/error-updating-record-invalid-key-format">13688</a> or <a href="http://ask.wireshark.org/questions/13951/invalid-key-format-wireshark-182">13951</a>.</p><p>Regarding the key format inconsistency between preferences and wireless toolbar, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7681">bug 7681</a> was filed against it. Feel free to add yourself to the bug CC list if you want to be notified of any updates regarding this issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '12, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Aug '12, 19:43</strong> </span></p></div></div><div id="comments-container-13969" class="comments-container"></div><div id="comment-tools-13969" class="comment-tools"></div><div class="clear"></div><div id="comment-13969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

