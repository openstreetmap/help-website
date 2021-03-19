+++
type = "question"
title = "Not able to configure Wireshark with gnutls!"
description = '''I&#x27;m using this command with make and sudo make install  ./configure --with-gnutls  while installing wireshark version 1.12.0 from source in Linux but I&#x27;m still getting wireshark with no SSL preferences that are related to the decryption.  Any idea why it is not working and how to fix this? Thanks. '''
date = "2014-08-19T18:15:00Z"
lastmod = "2014-08-25T16:19:00Z"
weight = 35600
keywords = [ "decryption", "configure", "ssl", "wireshark" ]
aliases = [ "/questions/35600" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Not able to configure Wireshark with gnutls!](/questions/35600/not-able-to-configure-wireshark-with-gnutls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35600-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35600-score" class="post-score" title="current number of votes">0</div><span id="post-35600-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using this command with <code>make</code> and <code>sudo make install</code></p><pre><code>./configure --with-gnutls</code></pre><p>while installing wireshark version 1.12.0 from source in Linux but I'm still getting wireshark with no SSL preferences that are related to the decryption.</p><p>Any idea why it is not working and how to fix this?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-configure" rel="tag" title="see questions tagged &#39;configure&#39;">configure</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '14, 18:50</strong> </span></p></div></div><div id="comments-container-35600" class="comments-container"></div><div id="comment-tools-35600" class="comment-tools"></div><div class="clear"></div><div id="comment-35600-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35626"></span>

<div id="answer-container-35626" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35626-score" class="post-score" title="current number of votes">0</div><span id="post-35626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What does the ./configure summary output say? Unfortunately "--with-gnutls" does not generate an error if ./configure can't find gnutls so it might still say this:</p><p><code>Use gnutls library : no</code></p><p>in which case Wireshark won't actually be built with the gnutls library.</p><p>(The fact that you can explicitly requested gnutls but silently not get it is a bug.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-35626" class="comments-container"><span id="35630"></span><div id="comment-35630" class="comment"><div id="post-35630-score" class="comment-score"></div><div class="comment-text"><p>I submitted a <a href="https://code.wireshark.org/review/3750">change</a> which will cause ./configure to error out if --with-gnutls is specified but the library is not found.</p></div><div id="comment-35630-info" class="comment-info"><span class="comment-age">(20 Aug '14, 08:18)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="35639"></span><div id="comment-35639" class="comment"><div id="post-35639-score" class="comment-score"></div><div class="comment-text"><p>Oh, and of course if it does use <code>Use gnutls library : no</code> there should be some interesting info somewhere in the <code>./configure</code> output which will explain why gnutls was not detected; chances are it's because you don't have the gnutls development stuff installed or it could be because you have a version of gnutls whose license is incompatible with Wireshark's.</p></div><div id="comment-35639-info" class="comment-info"><span class="comment-age">(20 Aug '14, 11:44)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="35736"></span><div id="comment-35736" class="comment"><div id="post-35736-score" class="comment-score"></div><div class="comment-text"><p>Thank you this was helpful.When I searched the output I found that:</p><p><code>checking for LIBGNUTLS... no GnuTLS &gt;= 3.1.10 not found  checking for LIBGNUTLS... no GnuTLS &gt;= 1.2.0, &lt; 3.0 not found  GnuTLS with compatible license not found, disabling SSL decryption checking for libgcrypt-config... no checking for LIBGCRYPT - version &gt;= 1.1.92... no</code></p><p>I've installed the dev version of the gnutls and this solves the problem.</p></div><div id="comment-35736-info" class="comment-info"><span class="comment-age">(25 Aug '14, 16:18)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-35626" class="comment-tools"></div><div class="clear"></div><div id="comment-35626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35616"></span>

<div id="answer-container-35616" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35616-score" class="post-score" title="current number of votes">0</div><span id="post-35616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You probaly want --with-ssl</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-35616" class="comments-container"><span id="35737"></span><div id="comment-35737" class="comment"><div id="post-35737-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your suggestion but using this configured wireshark with the ssl but not with gnutls.</p></div><div id="comment-35737-info" class="comment-info"><span class="comment-age">(25 Aug '14, 16:19)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-35616" class="comment-tools"></div><div class="clear"></div><div id="comment-35616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

