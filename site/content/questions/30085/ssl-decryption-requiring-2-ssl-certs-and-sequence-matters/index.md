+++
type = "question"
title = "SSL decryption requiring 2 SSL certs, and sequence matters?"
description = '''We have an encrypted IIS web server -&amp;gt; IIS app server trace. Encryption is not 2 way, so the cert comes only from the app server side. In order to decrypt the trace, I have to add the pre-go_live cert ( for &quot;myURL-temp.company.com&quot;) to my SSL preferences first, then add in the post-go_live cert (...'''
date = "2014-02-21T09:16:00Z"
lastmod = "2014-02-21T09:16:00Z"
weight = 30085
keywords = [ "ssl", "iis", "certificate" ]
aliases = [ "/questions/30085" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SSL decryption requiring 2 SSL certs, and sequence matters?](/questions/30085/ssl-decryption-requiring-2-ssl-certs-and-sequence-matters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30085-score" class="post-score" title="current number of votes">0</div><span id="post-30085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have an encrypted IIS web server -&gt; IIS app server trace. Encryption is not 2 way, so the cert comes only from the app server side.</p><p>In order to decrypt the trace, I have to add the pre-go_live cert ( for "myURL-temp.company.com") to my SSL preferences first, then add in the post-go_live cert (myURL.company.com ) Then I can decrypt the traffic. Reverse that sequence of certs, and no joy.</p><p>"Client Hello" calls the pre-go_live URL:</p><p>myURL-temp.company.com</p><p>However, the server certificate exchanged is the post-go_live cert for " MyURL.company.com" , as expected.<br />
</p><p>Why in the world do I have to include the pre-go_live cert in the preferences? It's not showing up anywhere I can see in the cert exchange.<br />
</p><p>Does IIS somehow use both certs to do the encryption? ( I'm a Unix guy - you could put in a teaspoon what I know about IIS).<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-iis" rel="tag" title="see questions tagged &#39;iis&#39;">iis</span> <span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '14, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/b83e432f35fa7a8ff9ae9024f4030b57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chavid&#39;s gravatar image" /><p><span>chavid</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chavid has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-30085" class="comments-container"></div><div id="comment-tools-30085" class="comment-tools"></div><div class="clear"></div><div id="comment-30085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

