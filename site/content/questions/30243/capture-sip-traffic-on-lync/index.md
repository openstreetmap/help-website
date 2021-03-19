+++
type = "question"
title = "Capture SIP traffic on LYNC"
description = '''I have to run a long-term capture to find a SIP scenario, which causes some issues. I have downloaded the Lync certificate to Wireshark, and restarted the device I want to capture to get the initial handshake. This works fine Now I want to capture to a file instead, with 15 minutes interval. I resta...'''
date = "2014-02-27T11:51:00Z"
lastmod = "2014-02-27T16:06:00Z"
weight = 30243
keywords = [ "ssl", "lync" ]
aliases = [ "/questions/30243" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture SIP traffic on LYNC](/questions/30243/capture-sip-traffic-on-lync)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30243-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30243-score" class="post-score" title="current number of votes">0</div><span id="post-30243-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to run a long-term capture to find a SIP scenario, which causes some issues. I have downloaded the Lync certificate to Wireshark, and restarted the device I want to capture to get the initial handshake. This works fine Now I want to capture to a file instead, with 15 minutes interval. I restart the device again. The first file that gets saved has the initial handshake, and I'm able to see the SIP traffic. However when the Wireshark starts on the next file, it seems that the "decrytption" stops, and only encrypted packets is displyed. Is there a workaround for this? Let's say I save the capture to file for every 15 minutes, and I need to find a call captured after 2 hours. I can of course disable "Update list of packets in real time" to increase performance, and at the same time put in different filters, to minimize the amount of other traffic.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-lync" rel="tag" title="see questions tagged &#39;lync&#39;">lync</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/4b35b84c2601f7e57f10b80beb3fce65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gchrist&#39;s gravatar image" /><p><span>gchrist</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gchrist has no accepted answers">0%</span></p></div></div><div id="comments-container-30243" class="comments-container"></div><div id="comment-tools-30243" class="comment-tools"></div><div class="clear"></div><div id="comment-30243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30248"></span>

<div id="answer-container-30248" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30248-score" class="post-score" title="current number of votes">1</div><span id="post-30248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume wireshark uses the RSA private key you gave it to figure out the master secret and symmetric key exchanged during the TLS handshake, at the start of the Lync's TCP/TLS session. Since only the first file will have those TLS handshake packets, subsequent files can't be decrypted. (the RSA private key is only used during the TLS handshake)</p><p>It looks like in preferences-&gt;SSL you can tell wireshark that master secret (not the private key, but rather the master secret exchanged during the handshake) in a separate file. But if I recall, TLS uses AES in CBC mode, so without the previous blocks I don't see how it could decrypt those other files. But maybe I'm remembering TLS wrong, so you could try it.</p><p>If all else fails, you could write a Lua script to write the unencrypted SIP message contents into multiple files, without using wireshark's built-in multi-file writing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30248" class="comments-container"></div><div id="comment-tools-30248" class="comment-tools"></div><div class="clear"></div><div id="comment-30248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

