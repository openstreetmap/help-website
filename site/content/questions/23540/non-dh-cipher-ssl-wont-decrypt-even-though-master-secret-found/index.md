+++
type = "question"
title = "(non-DH cipher) SSL won&#x27;t decrypt even though master secret found"
description = '''On Ubuntu Linux, wireshark fails to decrypt an SSL session which does NOT use a DH cipher.  I&#x27;m using Firefox with sslkeylogfile.  Looking at the debug file, it appears that wireshark CAN find master secret, yet fails to decrypt. Here&#x27;s the relevant snippet from the debug file:  ...  checking keylog...'''
date = "2013-08-04T14:46:00Z"
lastmod = "2013-08-09T05:15:00Z"
weight = 23540
keywords = [ "squid", "stunnel" ]
aliases = [ "/questions/23540" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [(non-DH cipher) SSL won't decrypt even though master secret found](/questions/23540/non-dh-cipher-ssl-wont-decrypt-even-though-master-secret-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23540-score" class="post-score" title="current number of votes">0</div><span id="post-23540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On Ubuntu Linux, wireshark fails to decrypt an SSL session which does NOT use a DH cipher.<br />
I'm using Firefox with sslkeylogfile.<br />
Looking at the debug file, it appears that wireshark CAN find master secret, yet fails to decrypt.<br />
Here's the relevant snippet from the debug file:<br />
</p><pre><code>...
 checking keylog line: CLIENT_RANDOM 51fec5231f20bd12d79c7de8ea8d55433b99c06c47bf5a087aa1e1fd209bde01 2df2f3ad233352799947aecf5b831e971170f089cf17ec98d82e5e312a8005663920d14f66e21eecdfb2f06efda72f72
found master secret in key log
ssl_generate_keyring_material not enough data to generate key (0x31 required 0x37 or 0x57)
dissect_ssl3_handshake can&#39;t generate keyring material
  record: offset = 267, reported_length_remaining = 47
...</code></pre><p>Firefox uses a Squid proxy server. The connection between Firefox and Squid takes place over a Stunnel's SSL tunnel.<br />
Firefox -----(wireshark on loopback)---------&gt; stunnel A ---&gt; stunnel B --&gt; Squid --&gt; Internet</p><p>The interesting thing is that when I remove stunnel and connect:<br />
Firefox ------(wireshark on loopback)--------&gt; Squid --&gt; Internet<br />
(Without changing a single setting in wireshark), then I CAN decrypt successfully.</p><p>Here are links to wireshark capture with stunnel (failed to decrypt):<br />
<a href="http://cloudshark.org/captures/745529928d7f">http://cloudshark.org/captures/745529928d7f</a></p><p>SSLkeylogfile generated during this session:<br />
<a href="http://pastebin.com/6wkpsUah">http://pastebin.com/6wkpsUah</a></p><p>Debug file (frame 22 is of interest):<br />
<a href="http://pastebin.com/3pEVdkqB">http://pastebin.com/3pEVdkqB</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-squid" rel="tag" title="see questions tagged &#39;squid&#39;">squid</span> <span class="post-tag tag-link-stunnel" rel="tag" title="see questions tagged &#39;stunnel&#39;">stunnel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '13, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/5539b49a6661453d168b03c047917c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansmith&#39;s gravatar image" /><p><span>dansmith</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansmith has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '13, 02:38</strong> </span></p></div></div><div id="comments-container-23540" class="comments-container"></div><div id="comment-tools-23540" class="comment-tools"></div><div class="clear"></div><div id="comment-23540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23676"></span>

<div id="answer-container-23676" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23676-score" class="post-score" title="current number of votes">0</div><span id="post-23676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dansmith has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The solution turned out to be a bizarre one. stunnel A was listening on a random port 33308 when decryption was failing. As soon as I would make stunnel A listen on ports 80 or 8080, the decryption would succeed, for any other ports it would fail. I'm completely mistified. How can a port number influence the decryption of an SSL session?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '13, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/5539b49a6661453d168b03c047917c5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dansmith&#39;s gravatar image" /><p><span>dansmith</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dansmith has one accepted answer">50%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Aug '13, 05:19</strong> </span></p></div></div><div id="comments-container-23676" class="comments-container"></div><div id="comment-tools-23676" class="comment-tools"></div><div class="clear"></div><div id="comment-23676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

