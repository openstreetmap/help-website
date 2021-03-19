+++
type = "question"
title = "Is it possible to capture the host name of and for every HTTP request over TLS?"
description = '''Let me try to explain what I would like to do with an example. I start a live capturing traffic over eth0 and what I would like to see is the host name for every HTTP request performed over TLS: ➜ ~ sudo tshark -i eth0 -T fields -e ssl.handshake.extensions_server_name -R ssl.handshake.extensions_ser...'''
date = "2016-02-25T02:20:00Z"
lastmod = "2016-02-25T03:27:00Z"
weight = 50498
keywords = [ "tshark" ]
aliases = [ "/questions/50498" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to capture the host name of and for every HTTP request over TLS?](/questions/50498/is-it-possible-to-capture-the-host-name-of-and-for-every-http-request-over-tls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50498-score" class="post-score" title="current number of votes">0</div><span id="post-50498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Let me try to explain what I would like to do with an example. I start a live capturing traffic over eth0 and what I would like to see is the host name for every HTTP request performed over TLS:</p><pre><code>➜  ~ sudo tshark -i eth0 -T fields -e ssl.handshake.extensions_server_name -R ssl.handshake.extensions_server_name
tshark: Lua: Error during loading:
 [string &quot;/usr/share/wireshark/init.lua&quot;]:46: dofile has been disabled due to running Wireshark as superuser. See http://wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user.
tshark: -R without -2 is deprecated. For single-pass filtering use -Y.
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on &#39;eth0&#39;</code></pre><p>Now I open Chromium in private mode and enter facebook.com - this is what gets captured:</p><pre><code>www.facebook.com
fbstatic-a.akamaihd.net
fbstatic-a.akamaihd.net
fbstatic-a.akamaihd.net
fbstatic-a.akamaihd.net
fbcdn-static-b-a.akamaihd.net
fbcdn-static-b-a.akamaihd.net
fbcdn-static-b-a.akamaihd.net
fbcdn-static-b-a.akamaihd.net
fbcdn-static-b-a.akamaihd.net
10 clients1.google.com
fbcdn-static-b-a.akamaihd.net</code></pre><p>But if I do a full refresh with [Ctrl]+[F5] nothing is added to that list. As I understand this is b/c what I capture is the host information communicated during the handshake which is not reperformed for a request to an already established TLS connection.</p><p>So my question would be - what would I have to filter for to basically get the host name for every single request over TLS?</p><p>I suspect this is not possible to be done by filtering b/c that information is not relayed for every request - but maybe there is an equivalent solution?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '16, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/c44e61d34981ed01ab4bc25c3df52fc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raffael1984&#39;s gravatar image" /><p><span>Raffael1984</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raffael1984 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '16, 02:23</strong> </span></p></div></div><div id="comments-container-50498" class="comments-container"></div><div id="comment-tools-50498" class="comment-tools"></div><div class="clear"></div><div id="comment-50498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50502"></span>

<div id="answer-container-50502" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50502-score" class="post-score" title="current number of votes">1</div><span id="post-50502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Raffael1984 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I suspect this is not possible to be done by filtering b/c that information is not relayed for every request</p></blockquote><p>Unless the <code>Ctrl</code> <code>F5</code> causes the browser to close an already established TLS session and open a new one, there is no TLS establishment phase, so no packet contains the <code>ssl.handshake.extensions_server_name</code> protocol field.</p><p>The http requests sent using an already established TLS-encrypted TCP session do contain the target url, but by the very principle of TLS:</p><ul><li><p>you cannot see their contents unless you have enough information to decrypt the TLS,</p></li><li><p>they cannot be sent to any other host than the one to which the TLS session has been established.</p></li></ul><p>Therefore:</p><ul><li><p>if you are interested only in the list of hosts visited, you have to start capturing before the TLS session establishment to all of them, and you do not need anything else.</p></li><li><p>if you want to see the details of target urls of the individual http requests sent to each host, you still have to start capturing before the TLS session establishments to all the hosts, because otherwise you would not be able to decipher the TLS sessions and thus see the http requests in plaintext. See Q&amp;A for https decryption on this site for details.</p></li></ul><p>With decryption working properly, you can use <code>http.host</code> and <code>http.request.uri</code> fields the same way like the <code>ssl.handshake.extensions_server_name</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50502" class="comments-container"></div><div id="comment-tools-50502" class="comment-tools"></div><div class="clear"></div><div id="comment-50502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

