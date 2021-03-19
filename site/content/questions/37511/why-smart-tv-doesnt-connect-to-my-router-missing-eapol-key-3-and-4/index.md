+++
type = "question"
title = "why smart tv doesn&#x27;t connect to my router? (missing eapol key 3 and 4)"
description = '''i have a new smart tv from philips with last firmware but it doesn&#x27;t connect to my router (sitecom wl-154) it only says failed to connect my router doesn&#x27;t have wps and is using wpa2 psk aes (rsna-psk ccmp) 802.11g wireshark show key 1, 2 and then again 1,2 for some times but never 3 or 4 with other...'''
date = "2014-10-31T13:18:00Z"
lastmod = "2014-11-02T10:24:00Z"
weight = 37511
keywords = [ "tv", "eapol", "authentication", "smart", "missing" ]
aliases = [ "/questions/37511" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [why smart tv doesn't connect to my router? (missing eapol key 3 and 4)](/questions/37511/why-smart-tv-doesnt-connect-to-my-router-missing-eapol-key-3-and-4)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37511-score" class="post-score" title="current number of votes">0</div><span id="post-37511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have a <strong>new smart tv</strong> from philips with last firmware but it <strong>doesn't connect to my router</strong> (sitecom wl-154) it only says failed to connect</p><p>my router doesn't have wps and is using wpa2 psk aes (rsna-psk ccmp) 802.11g <strong>wireshark show key 1, 2 and then again 1,2 for some times but never 3 or 4</strong> with other router tv connects succesfully (other has wps but i haven't used it) (onda communication PN51T) (also wpa 2 psk aes) every device works on my router (wl-154) (pc, xbox, nintendo ds, mobile phone...) but tv not so is not a router problem but... tv works with other router so is not tv...</p><p>the only difference that i found is that every device that i use authenticate with 802.1x-2001 but tv uses 802.1x-2004 (from wireshark) maybe my router doesn't support 2004?? and other router has wps (and a nice wps vulnerability: you set wps push button in settings but pin is never disabled and is fixed to 12345670 so reaver crack it in 5 sec... '-_-)</p><p>someone has a solution?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tv" rel="tag" title="see questions tagged &#39;tv&#39;">tv</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-authentication" rel="tag" title="see questions tagged &#39;authentication&#39;">authentication</span> <span class="post-tag tag-link-smart" rel="tag" title="see questions tagged &#39;smart&#39;">smart</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '14, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/cc7db0f2da4d16cd02a5741ec5cb8468?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dohuff&#39;s gravatar image" /><p><span>dohuff</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dohuff has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Nov '14, 06:52</strong> </span></p></div></div><div id="comments-container-37511" class="comments-container"></div><div id="comment-tools-37511" class="comment-tools"></div><div class="clear"></div><div id="comment-37511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37537"></span>

<div id="answer-container-37537" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37537-score" class="post-score" title="current number of votes">1</div><span id="post-37537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dohuff has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>someone has a solution?</p></blockquote><p>This sounds like a firmware problem with your TV set or your router, so there is nothing Wireshark or the community can do for you!</p><p>Please contact the vendor support of the TV set and ask them for a firmware update.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '14, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37537" class="comments-container"><span id="37544"></span><div id="comment-37544" class="comment"><div id="post-37544-score" class="comment-score"></div><div class="comment-text"><p>that is what i think too i think is a tv problem since every device can connect to my router and every device can set static ip, certificate for wpa2 enterprise tv is limited in settings (there is static ip but you can't select it)</p></div><div id="comment-37544-info" class="comment-info"><span class="comment-age">(02 Nov '14, 10:24)</span> <span class="comment-user userinfo">dohuff</span></div></div></div><div id="comment-tools-37537" class="comment-tools"></div><div class="clear"></div><div id="comment-37537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

