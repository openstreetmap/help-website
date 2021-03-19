+++
type = "question"
title = "LDAP SSL decrypt issue"
description = '''Hi everybody, I&#x27;m trying to debug LDAP SSL communication and experience a problem with SSL decryption. I start my capturing before any handshake so I&#x27;m able to see the whole SSL handshake. But after that an application establishes another session which is a short version with ClientHello-&amp;gt;ServerH...'''
date = "2013-09-24T06:16:00Z"
lastmod = "2014-01-09T03:10:00Z"
weight = 25156
keywords = [ "ssl", "decryption", "ldap" ]
aliases = [ "/questions/25156" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP SSL decrypt issue](/questions/25156/ldap-ssl-decrypt-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25156-score" class="post-score" title="current number of votes">0</div><span id="post-25156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody,</p><p>I'm trying to debug LDAP SSL communication and experience a problem with SSL decryption. I start my capturing before any handshake so I'm able to see the whole SSL handshake. But after that an application establishes another session which is a short version with ClientHello-&gt;ServerHello, ChangeCipherSpec, Finished. And after that handshake I'm unable to decode client packets while server are still readable.</p><p>Could you advise me on a way to resolve that issue so that I could decode all the packets after the second handshake?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '13, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/a1802aba0e41710a318294f083cbf8ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PhilippGrigoryev&#39;s gravatar image" /><p><span>PhilippGrigo...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PhilippGrigoryev has no accepted answers">0%</span></p></div></div><div id="comments-container-25156" class="comments-container"></div><div id="comment-tools-25156" class="comment-tools"></div><div class="clear"></div><div id="comment-25156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25414"></span>

<div id="answer-container-25414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25414-score" class="post-score" title="current number of votes">0</div><span id="post-25414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does the second SSL handshake use a "TLS session tickets" that was sent in the first SSL handshake? Wireshark does not (yet) supoort session tickets for decryption. You could disable session tickets and use SSL session-id's instead.</p><p>If that's not the case, are you able to post both SSL handshakes to www.cloudshark.org?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25414" class="comments-container"><span id="25431"></span><div id="comment-25431" class="comment"><div id="post-25431-score" class="comment-score"></div><div class="comment-text"><p>Well, I figured out that the problem starts actually after the malformed packet. It's a frame #27 (packet which Wireshark shows as Application Data[Malformed Packet]). I uploaded the whole session at <a href="http://www.cloudshark.org/captures/2d105476040d">http://www.cloudshark.org/captures/2d105476040d</a></p><p>and that's a fragment from a SSL debug file starting from a handshake frame. And here I can see some decrypted data from Malformed Packet but just here, not in Wireshark. <a href="http://pastebin.com/cRhQJVAm">SSL Dump on PasteBin</a></p></div><div id="comment-25431-info" class="comment-info"><span class="comment-age">(30 Sep '13, 16:23)</span> <span class="comment-user userinfo">PhilippGrigo...</span></div></div><span id="25436"></span><div id="comment-25436" class="comment"><div id="post-25436-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ)</p><p>The capture file and the ssl debug file do not seem to match. Could you decrypt the file you posted on cloudshark again (start with an empty ssl debug file) and post the ssl-debug output again?</p></div><div id="comment-25436-info" class="comment-info"><span class="comment-age">(01 Oct '13, 00:12)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="28717"></span><div id="comment-28717" class="comment"><div id="post-28717-score" class="comment-score"></div><div class="comment-text"><p>I am facing the same issue, after a malformed packet is seen from the client, all the client data are no longer decoded by wireshark</p></div><div id="comment-28717-info" class="comment-info"><span class="comment-age">(09 Jan '14, 03:10)</span> <span class="comment-user userinfo">MSK</span></div></div></div><div id="comment-tools-25414" class="comment-tools"></div><div class="clear"></div><div id="comment-25414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

