+++
type = "question"
title = "Decode SSL transport with PEM file that has a passphase"
description = '''I am trying to decode a PCAP file that has SSL transport. It has a PEM file with a passphase. Seems like that is a limitation that it doesn&#x27;t work if the PEM has a passphase. Scenario: View -&amp;gt; Preferences -&amp;gt; SSL -&amp;gt; RSA keys list =&amp;gt; add PEM file with pasephase Any workaround how to remove...'''
date = "2015-11-01T05:06:00Z"
lastmod = "2015-11-01T05:53:00Z"
weight = 47130
keywords = [ "pem", "wireshark" ]
aliases = [ "/questions/47130" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decode SSL transport with PEM file that has a passphase](/questions/47130/decode-ssl-transport-with-pem-file-that-has-a-passphase)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47130-score" class="post-score" title="current number of votes">0</div><span id="post-47130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decode a PCAP file that has SSL transport. It has a PEM file with a passphase. Seems like that is a limitation that it doesn't work if the PEM has a passphase. Scenario: View -&gt; Preferences -&gt; SSL -&gt; RSA keys list =&gt; add PEM file with pasephase</p><p>Any workaround how to remove passphase? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pem" rel="tag" title="see questions tagged &#39;pem&#39;">pem</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '15, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/021f8f9e84e2ba27274d165e39fe4713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoava&#39;s gravatar image" /><p><span>yoava</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoava has no accepted answers">0%</span></p></div></div><div id="comments-container-47130" class="comments-container"></div><div id="comment-tools-47130" class="comment-tools"></div><div class="clear"></div><div id="comment-47130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47132"></span>

<div id="answer-container-47132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47132-score" class="post-score" title="current number of votes">2</div><span id="post-47132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Given a PEM-encoded private key file (beginning with <code>-----BEGIN ENCRYPTED PRIVATE KEY-----</code>), you can remove the passphrase with the <code>openssl</code> program:</p><pre><code>openssl rsa -in encrypted-key.pem  -out key.pem</code></pre><p>The resulting <code>key.pem</code> file will then begin with <code>-----BEGIN RSA PRIVATE KEY-----</code> which is accepted by Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '15, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-47132" class="comments-container"></div><div id="comment-tools-47132" class="comment-tools"></div><div class="clear"></div><div id="comment-47132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

