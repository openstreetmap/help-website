+++
type = "question"
title = "Decoding ssl traffic"
description = '''I am new to wireshare. I am using wireshark 1.4.10. I am trying to capture traffic from a Smalltalk app to a mainframe. I have captured the traffic several times using a http port. Do to security risks the company has shut down the http port and I am trying to use the https port. I have capture the ...'''
date = "2012-07-25T14:54:00Z"
lastmod = "2012-07-26T01:09:00Z"
weight = 13004
keywords = [ "ssl", "decryption" ]
aliases = [ "/questions/13004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding ssl traffic](/questions/13004/decoding-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13004-score" class="post-score" title="current number of votes">0</div><span id="post-13004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshare. I am using wireshark 1.4.10. I am trying to capture traffic from a Smalltalk app to a mainframe. I have captured the traffic several times using a http port. Do to security risks the company has shut down the http port and I am trying to use the https port. I have capture the traffic on the https port several times, but I cannot get the decryption of the data to work. I have tried to follow the manual, but it is not working for me. I understand the manual to say that I need the private key to do the decryption. Is this the case? Is this the only way to do the decryption?</p><p>Thanks,</p><p>Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '12, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/dbe1746678f7435ea9745146c0e9ba7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrisdwyer97&#39;s gravatar image" /><p><span>chrisdwyer97</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrisdwyer97 has no accepted answers">0%</span></p></div></div><div id="comments-container-13004" class="comments-container"></div><div id="comment-tools-13004" class="comment-tools"></div><div class="clear"></div><div id="comment-13004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13010"></span>

<div id="answer-container-13010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13010-score" class="post-score" title="current number of votes">0</div><span id="post-13010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you do need the private key (which resides on the server) to do decryption. This is because in a normal RSA SSL handshake, the information needed to calculate the key that is used for encrypting the traffic is sent by the client to the server, but encrypted with the public key from the server certificate. This means the information can only be derived by using the corresponding private key.</p><p>Then things get a little more complicated as the server might select a DiffieHellman based cipher. In this case, the client and server use randomly generated key-pairs to exchange the information needed to calculate the session key. In this case you can't do decryption with Wireshark.</p><p>Recently there have been added some options to do decryption without supplying the private key, but they all involve supplying the (pre)master secret of each ssl session. Which you normally don't have access to. But they can be obtained by:</p><ul><li>Compiling your own version of Firefox or Chrome with a debug setting that will log the SSL session keys.</li><li>Using "openssl s_client" to communicate to the server and use the debug info on screen</li><li>Having someone with access to the private key use it to decrypt the sessions and export the SSL session keys to a file, which can then be used by you</li></ul><p>For more information about SSL troubleshooting, have a look at <a href="http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-1_SSL_Troubleshooting_with%20_Wireshark_Software.pdf">the presentation I gave at Sharkfest'12</a> :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13010" class="comments-container"></div><div id="comment-tools-13010" class="comment-tools"></div><div class="clear"></div><div id="comment-13010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

