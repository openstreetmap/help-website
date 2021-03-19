+++
type = "question"
title = "WPA-PWD Decryption Key Format"
description = '''Hi! Tried to put my WPA key in Wireshark -&amp;gt; Preferences -&amp;gt; Protocols -&amp;gt; IEEE 802.11, using the format: Some&#92;Pa55:Free Internet! &quot;Free Internet!&quot; really is the name of my AP, and it&#x27;s given me problems before with other (CLI) apps because of the whitespace and the bang, but quoting generally...'''
date = "2013-01-14T11:58:00Z"
lastmod = "2013-01-15T15:25:00Z"
weight = 17672
keywords = [ "decryption", "wpa-pwd", "key" ]
aliases = [ "/questions/17672" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WPA-PWD Decryption Key Format](/questions/17672/wpa-pwd-decryption-key-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17672-score" class="post-score" title="current number of votes">0</div><span id="post-17672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! Tried to put my WPA key in Wireshark -&gt; Preferences -&gt; Protocols -&gt; IEEE 802.11, using the format:</p><p>Some\Pa55:Free Internet!</p><p>"Free Internet!" really is the name of my AP, and it's given me problems before with other (CLI) apps because of the whitespace and the bang, but quoting generally solves that. Also, my real password does have a backslash in it. Since it doesn't seem to be working, and I've tried it both SSID first, and password first, (Wireshark says it will ignore invalid formats), I am wondering if any of these "non-standard" characters are throwing it off. In other words, do they need to be escaped? Quoted? I'm not sure how Wireshark would parse it. Any advice on format, using my examples, would be appreciated. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-wpa-pwd" rel="tag" title="see questions tagged &#39;wpa-pwd&#39;">wpa-pwd</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '13, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/410bcf085eff0251c8a3d99d1f187717?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudont&#39;s gravatar image" /><p><span>sudont</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudont has no accepted answers">0%</span></p></div></div><div id="comments-container-17672" class="comments-container"></div><div id="comment-tools-17672" class="comment-tools"></div><div class="clear"></div><div id="comment-17672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17673"></span>

<div id="answer-container-17673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17673-score" class="post-score" title="current number of votes">0</div><span id="post-17673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you try URI-style percent encoding, e.g.</p><pre><code>Some%5CPa55:Free%20Internet!</code></pre><p>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '13, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-17673" class="comments-container"><span id="17698"></span><div id="comment-17698" class="comment"><div id="post-17698-score" class="comment-score"></div><div class="comment-text"><p>I'm starting to wonder if the problem is with the kind of packets I have. I need to figure out a way to generate traffic and collect packets at the same time. Maybe I'll collect the packets with KisMac so I can use an external card, and see if that's not it.</p></div><div id="comment-17698-info" class="comment-info"><span class="comment-age">(15 Jan '13, 07:13)</span> <span class="comment-user userinfo">sudont</span></div></div><span id="17708"></span><div id="comment-17708" class="comment"><div id="post-17708-score" class="comment-score"></div><div class="comment-text"><p>OK, that was the problem. The packets I was looking at simply weren't encrypted. Now that I have some proper packets, it reads, "Decrypted CCMP Data."</p></div><div id="comment-17708-info" class="comment-info"><span class="comment-age">(15 Jan '13, 15:25)</span> <span class="comment-user userinfo">sudont</span></div></div></div><div id="comment-tools-17673" class="comment-tools"></div><div class="clear"></div><div id="comment-17673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

