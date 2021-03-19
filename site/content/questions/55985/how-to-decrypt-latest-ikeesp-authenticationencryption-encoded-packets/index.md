+++
type = "question"
title = "How to decrypt latest IKE/ESP Authentication/Encryption encoded packets."
description = '''Does Wireshark support decryption of the following algorithms?  AUTH_HMAC_SHA2_384_192  AUTH_HMAC_SHA2_512_256  AUTH_AES_GMAC_128 AUTH_AES_GMAC_192  AUTH_AES_GMAC_256   AUTH_AES_XCBC_MAC_96   ENC_AES_CBC_192  ENC_AES_CBC_256 ENC_AES_GCM_128 ENC_AES_GCM_256 '''
date = "2016-09-29T05:13:00Z"
lastmod = "2016-09-29T11:02:00Z"
weight = 55985
keywords = [ "decryption", "isakmp" ]
aliases = [ "/questions/55985" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decrypt latest IKE/ESP Authentication/Encryption encoded packets.](/questions/55985/how-to-decrypt-latest-ikeesp-authenticationencryption-encoded-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55985-score" class="post-score" title="current number of votes">0</div><span id="post-55985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does Wireshark support decryption of the following algorithms?</p><ul><li>AUTH_HMAC_SHA2_384_192</li><li>AUTH_HMAC_SHA2_512_256</li><li>AUTH_AES_GMAC_128</li><li>AUTH_AES_GMAC_192</li><li>AUTH_AES_GMAC_256</li><li><p>AUTH_AES_XCBC_MAC_96</p></li><li><p>ENC_AES_CBC_192</p></li><li>ENC_AES_CBC_256</li><li>ENC_AES_GCM_128</li><li>ENC_AES_GCM_256</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-isakmp" rel="tag" title="see questions tagged &#39;isakmp&#39;">isakmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '16, 05:13</strong></p><img src="https://secure.gravatar.com/avatar/d7b0ef0df9d8bb5b3fafc3e3115e9812?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jnanesh&#39;s gravatar image" /><p><span>jnanesh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jnanesh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Sep '16, 10:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-55985" class="comments-container"></div><div id="comment-tools-55985" class="comment-tools"></div><div class="clear"></div><div id="comment-55985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55992"></span>

<div id="answer-container-55992" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55992-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55992-score" class="post-score" title="current number of votes">0</div><span id="post-55992-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>AUTH_*</code> sounds like algorithms for authentication, these are strictly not necessary for decryption support. These seem supported though based on a look in the source code.</p><p>AES-CBC suites have been supported for a while (since at least Wireshark 2.0). AES-GCM suites are only supported in the latest development version (v2.3.0rc0-370-gd2ee571, it will end up in the stable 2.4 series in the future).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '16, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-55992" class="comments-container"></div><div id="comment-tools-55992" class="comment-tools"></div><div class="clear"></div><div id="comment-55992-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

