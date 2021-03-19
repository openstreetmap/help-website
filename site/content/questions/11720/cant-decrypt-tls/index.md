+++
type = "question"
title = "Can&#x27;t decrypt TLS"
description = '''I&#x27;ve added the server&#x27;s private key to the RSA keys list, confirmed the connection is over TLSv1.0 with a DES-CBC3-SHA cipher, and made sure to capture the entire handshake including ClientHello, but Wireshark still can&#x27;t decrypt the connection. What am I doing wrong? I&#x27;ve got the debug console open...'''
date = "2012-06-06T10:40:00Z"
lastmod = "2012-06-06T16:56:00Z"
weight = 11720
keywords = [ "ssl", "tlsv1" ]
aliases = [ "/questions/11720" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can't decrypt TLS](/questions/11720/cant-decrypt-tls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11720-score" class="post-score" title="current number of votes">0</div><span id="post-11720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've added the server's private key to the RSA keys list, confirmed the connection is over TLSv1.0 with a DES-CBC3-SHA cipher, and made sure to capture the entire handshake including ClientHello, but Wireshark still can't decrypt the connection. What am I doing wrong?</p><p>I've got the debug console open, but it remains blank the whole time - would that have useful info? Since the server is just for testing, I can provide the private key and URL if it would help.</p><p>Edit: The server's at <a href="https://etscene.net:8888">https://etscene.net:8888</a>, and the private key is:</p><pre><code>-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '12, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/6a9437ead3e069f0c602cb9560e431a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alek%20Storm&#39;s gravatar image" /><p><span>Alek Storm</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alek Storm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '12, 11:32</strong> </span></p></div></div><div id="comments-container-11720" class="comments-container"></div><div id="comment-tools-11720" class="comment-tools"></div><div class="clear"></div><div id="comment-11720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11726"></span>

<div id="answer-container-11726" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11726-score" class="post-score" title="current number of votes">1</div><span id="post-11726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alek Storm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using an early version of 1.6? There were two bugs (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6032">Bug 6032</a> and <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6033">Bug 6033</a>) that made decryption a little more tricky...</p><p>If so, please upgrade to the latest 1.6.x version... If not, can you show us your SSL-debug file?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '12, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-11726" class="comments-container"><span id="11727"></span><div id="comment-11727" class="comment"><div id="post-11727-score" class="comment-score"></div><div class="comment-text"><p>Not sure if upgrading to 1.6.8 is what fixed it, but I also had to change the "Protocol" field in the RSA keys list to "data", since I'm decrypting SPDY. Thanks!</p></div><div id="comment-11727-info" class="comment-info"><span class="comment-age">(06 Jun '12, 16:56)</span> <span class="comment-user userinfo">Alek Storm</span></div></div></div><div id="comment-tools-11726" class="comment-tools"></div><div class="clear"></div><div id="comment-11726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11724"></span>

<div id="answer-container-11724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11724-score" class="post-score" title="current number of votes">1</div><span id="post-11724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Works for me, what does your ssl debug log show? That's set in the SSL preferences for Wireshark.</p><p>You say you added the key to the RSA Keys list, what info did you set there? I have:</p><p><code>66.228.59.249 8888 http path/to/your/keyfile</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11724" class="comments-container"></div><div id="comment-tools-11724" class="comment-tools"></div><div class="clear"></div><div id="comment-11724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

