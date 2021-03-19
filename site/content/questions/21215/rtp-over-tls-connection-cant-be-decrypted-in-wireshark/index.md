+++
type = "question"
title = "RTP over TLS connection can&#x27;t be decrypted in wireshark?"
description = '''I tried to decrypt RTP data over TCP in Wireshark. Though in the debug logs I&#x27;m getting decrypted fragments like the following, dissect_ssl enter frame #102 (already visited)  conversation = 05666758, ssl_session = 00000000  record: offset = 0, reported_length_remaining = 101 dissect_ssl3_record: co...'''
date = "2013-05-17T03:27:00Z"
lastmod = "2013-05-17T08:37:00Z"
weight = 21215
keywords = [ "tls", "decryption", "rtp", "ssl" ]
aliases = [ "/questions/21215" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP over TLS connection can't be decrypted in wireshark?](/questions/21215/rtp-over-tls-connection-cant-be-decrypted-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21215-score" class="post-score" title="current number of votes">0</div><span id="post-21215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to decrypt RTP data over TCP in Wireshark. Though in the debug logs I'm getting decrypted fragments like the following,</p><pre><code>dissect_ssl enter frame #102 (already visited)
  conversation = 05666758, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 101
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 23500 found 00000000
association_find: TCP port 443 found 04D24DD8
dissect_ssl3_record decrypted len 69
decrypted app data fragment: ....</code></pre><pre><code>dissect_ssl enter frame #104 (already visited)
  conversation = 05666758, ssl_session = 00000000
  record: offset = 0, reported_length_remaining = 101
dissect_ssl3_record: content_type 23 Application Data
association_find: TCP port 23500 found 00000000
association_find: TCP port 443 found 04D24DD8
dissect_ssl3_record decrypted len 69
decrypted app data fragment: ....
dissect_ssl3_record found association 04D24DD8</code></pre><p>I can see only encrypted packets in wireshark...</p><p>Anything i'm missing? Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/3606fb2f161676306a345c0e2809e550?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kalai&#39;s gravatar image" /><p><span>Kalai</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kalai has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '13, 07:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-21215" class="comments-container"><span id="21226"></span><div id="comment-21226" class="comment"><div id="post-21226-score" class="comment-score"></div><div class="comment-text"><p>How do you know this is RTP over TCP, what profile is used to provide the framing for RTP on this stream based transport?</p></div><div id="comment-21226-info" class="comment-info"><span class="comment-age">(17 May '13, 07:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="21227"></span><div id="comment-21227" class="comment"><div id="post-21227-score" class="comment-score"></div><div class="comment-text"><p>I'm only transferring encrypted RTP from the client side over SSL using DHE suite.I tried to decrypt the data in wireshark but I coudn't...</p></div><div id="comment-21227-info" class="comment-info"><span class="comment-age">(17 May '13, 08:37)</span> <span class="comment-user userinfo">Kalai</span></div></div></div><div id="comment-tools-21215" class="comment-tools"></div><div class="clear"></div><div id="comment-21215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

