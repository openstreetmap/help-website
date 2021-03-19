+++
type = "question"
title = "Continuously decrypting HTTP"
description = '''Is there a way to continuously decrypt WPA encoded HTTP packets 24/7? I can run tshark and decrypt packets fine when the capture contains the EAPOL handshake. But on subsequent captures tshark cannot decrypt packets because the handshake is not present. Is there a way to get tshark to &quot;remember&quot; the...'''
date = "2014-04-10T13:51:00Z"
lastmod = "2014-04-15T01:54:00Z"
weight = 31735
keywords = [ "wpa2", "decrypt", "wpa", "ptk", "http" ]
aliases = [ "/questions/31735" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Continuously decrypting HTTP](/questions/31735/continuously-decrypting-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31735-score" class="post-score" title="current number of votes">0</div><span id="post-31735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to continuously decrypt WPA encoded HTTP packets 24/7? I can run tshark and decrypt packets fine when the capture contains the EAPOL handshake. But on subsequent captures tshark cannot decrypt packets because the handshake is not present. Is there a way to get tshark to "remember" the handshake context? Can the PTK be saved and fed into subsequent captures?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span> <span class="post-tag tag-link-ptk" rel="tag" title="see questions tagged &#39;ptk&#39;">ptk</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '14, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/8ad3e2b0f09bb769cd6b23c7fa9149b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magnumb&#39;s gravatar image" /><p><span>Magnumb</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magnumb has no accepted answers">0%</span></p></div></div><div id="comments-container-31735" class="comments-container"></div><div id="comment-tools-31735" class="comment-tools"></div><div class="clear"></div><div id="comment-31735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31832"></span>

<div id="answer-container-31832" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31832-score" class="post-score" title="current number of votes">0</div><span id="post-31832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without a code change that's not possible. There are similar problems with multiple EAPOL handshakes in the cpature file.</p><p>See here:</p><blockquote><p><a href="http://ask.wireshark.org/questions/26146/decrypting-wlan-packets-when-capture-has-multiple-eapol-key-changes">http://ask.wireshark.org/questions/26146/decrypting-wlan-packets-when-capture-has-multiple-eapol-key-changes</a><br />
<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9313">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9313</a><br />
</p></blockquote><p>So, if you need this feature and you think it's something others might need as well, please file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and post the link in a comment here.</p><p><strong>++ UPDATE ++</strong></p><p>There is a open source tool that could be useful for you.</p><blockquote><p><a href="https://github.com/mfontanini/dot11decrypt">https://github.com/mfontanini/dot11decrypt</a></p></blockquote><p>It does exactly what you need, decrypt wifi traffic on-the-fly.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '14, 12:54</strong> </span></p></div></div><div id="comments-container-31832" class="comments-container"></div><div id="comment-tools-31832" class="comment-tools"></div><div class="clear"></div><div id="comment-31832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

