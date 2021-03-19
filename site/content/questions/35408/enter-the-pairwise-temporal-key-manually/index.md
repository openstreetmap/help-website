+++
type = "question"
title = "enter the pairwise temporal key manually?"
description = '''Hi, I&#x27;m dealing with a proprietary wireless protocol. It uses something similar to WPA, but does not use standard EAPOL handshakes. When I enter the WPA2 password in wireshark for decryption, since it doesn&#x27;t see the EAPOL handshakes, it can&#x27;t determine the Pairwise Temporal Key. I have the PTK, but...'''
date = "2014-08-11T08:40:00Z"
lastmod = "2014-08-11T09:29:00Z"
weight = 35408
keywords = [ "wireless", "decryption", "wifi", "wpa2" ]
aliases = [ "/questions/35408" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [enter the pairwise temporal key manually?](/questions/35408/enter-the-pairwise-temporal-key-manually)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35408-score" class="post-score" title="current number of votes">0</div><span id="post-35408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm dealing with a proprietary wireless protocol. It uses something similar to WPA, but does not use standard EAPOL handshakes. When I enter the WPA2 password in wireshark for decryption, since it doesn't see the EAPOL handshakes, it can't determine the Pairwise Temporal Key. I have the PTK, but it appears there is no way to enter it in manually in wireshark. Is there any way to do this? Any modified versions of wireshark that allow this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '14, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/2014477f50184e7ab46c21a67d8999d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NickZ&#39;s gravatar image" /><p><span>NickZ</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NickZ has no accepted answers">0%</span></p></div></div><div id="comments-container-35408" class="comments-container"></div><div id="comment-tools-35408" class="comment-tools"></div><div class="clear"></div><div id="comment-35408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35409"></span>

<div id="answer-container-35409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35409-score" class="post-score" title="current number of votes">0</div><span id="post-35409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm dealing with a <strong>proprietary wireless protocol</strong>.<br />
Any modified versions of wireshark that allow this?</p></blockquote><p>As that's a <strong>proprietary</strong> wireless protocol, you'll need a <strong>proprietary</strong> version of Wireshark, meaning you need to change the wifi dissector code (including decryption) to make that happen.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '14, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-35409" class="comments-container"><span id="35411"></span><div id="comment-35411" class="comment"><div id="post-35411-score" class="comment-score"></div><div class="comment-text"><p>Right, that's why I'm wondering if anyone has done this before and can make their changes available?</p></div><div id="comment-35411-info" class="comment-info"><span class="comment-age">(11 Aug '14, 09:20)</span> <span class="comment-user userinfo">NickZ</span></div></div><span id="35412"></span><div id="comment-35412" class="comment"><div id="post-35412-score" class="comment-score"></div><div class="comment-text"><p>I don't think so. How big is the chance that anybody uses the same <strong>proprietary</strong> wireless protocol than you, especially as you did not even mention what's exactly <strong>proprietary</strong> within that protocol and how the protocol looks like !?!</p></div><div id="comment-35412-info" class="comment-info"><span class="comment-age">(11 Aug '14, 09:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-35409" class="comment-tools"></div><div class="clear"></div><div id="comment-35409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

