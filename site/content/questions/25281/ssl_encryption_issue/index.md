+++
type = "question"
title = "ssl_encryption_issue"
description = '''I captured the FaceTime application (from iPAD) traffic and which is in SSL format. I need to get into TLSV1 format to read and understand this format. so I could I get the TLSV1 format from the SSL format. please help me in decrypting the same. please find the some SSL format packets as shown below...'''
date = "2013-09-26T07:02:00Z"
lastmod = "2013-09-26T07:34:00Z"
weight = 25281
keywords = [ "ssl" ]
aliases = [ "/questions/25281" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ssl\_encryption\_issue](/questions/25281/ssl_encryption_issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25281-score" class="post-score" title="current number of votes">0</div><span id="post-25281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured the FaceTime application (from iPAD) traffic and which is in SSL format. I need to get into TLSV1 format to read and understand this format. so I could I get the TLSV1 format from the SSL format. please help me in decrypting the same.</p><p>please find the some SSL format packets as shown below.</p><pre><code>23  20.393657   115.111.14.7    17.154.239.13   TCP 82  49358 &gt; https [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=16
32  20.903460   17.154.239.13   115.111.14.7    TCP 66  https &gt; 49358 [SYN, ACK] Seq=0 Ack=1 Win=8190 Len=0 MSS=1460 WS=16
33  21.139873   115.111.14.7    17.154.239.13   TCP 64  49358 &gt; https [ACK] Seq=1 Ack=1 Win=262144 Len=0
38  22.571228   115.111.14.7    17.154.239.13   SSL 489 Continuation Data
39  22.571275   115.111.14.7    17.154.239.13   SSL 287 Continuation Data
44  23.013933   17.154.239.13   115.111.14.7    SSL 1499    Continuation Data</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '13, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/eebc158318028b3d80587975407782b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="narus&#39;s gravatar image" /><p><span>narus</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="narus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Sep '13, 07:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-25281" class="comments-container"></div><div id="comment-tools-25281" class="comment-tools"></div><div class="clear"></div><div id="comment-25281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25282"></span>

<div id="answer-container-25282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25282-score" class="post-score" title="current number of votes">0</div><span id="post-25282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>please help me in decrypting the same.</p></blockquote><p>17.154.239.13 is an IP address of an apple server. As you (most certainly) don't have access to the the private key of that server, you cannot decrypt the traffic.</p><p>However, you could intercept the SSL traffic with Fiddler or similar tools. See a similar question a few days ago.</p><blockquote><p><a href="http://ask.wireshark.org/questions/24985/google-analytics-in-native-apps-ipad">http://ask.wireshark.org/questions/24985/google-analytics-in-native-apps-ipad</a></p></blockquote><p>and the link how to use Fiddler with an iWhatever (tm) device.</p><blockquote><p><a href="http://fiddler2.com/documentation/Configure-Fiddler/Tasks/ConfigureForiOS">http://fiddler2.com/documentation/Configure-Fiddler/Tasks/ConfigureForiOS</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '13, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25282" class="comments-container"></div><div id="comment-tools-25282" class="comment-tools"></div><div class="clear"></div><div id="comment-25282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

