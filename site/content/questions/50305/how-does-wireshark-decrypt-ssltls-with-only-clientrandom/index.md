+++
type = "question"
title = "How does Wireshark decrypt SSL/TLS with only ClientRandom"
description = '''Hello, I am trying to decrypt a https connection on my machine with java. For that reason I have a system variable set so that Firefox puts the ClientRandom into a txt file. Now when I open a capture with Wireshark and give it access to the txt file with the ClientRandom, it can decrypt the whole ss...'''
date = "2016-02-18T06:59:00Z"
lastmod = "2016-02-19T05:23:00Z"
weight = 50305
keywords = [ "tls", "ssl", "decryption", "https", "ssl_decrypt" ]
aliases = [ "/questions/50305" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does Wireshark decrypt SSL/TLS with only ClientRandom](/questions/50305/how-does-wireshark-decrypt-ssltls-with-only-clientrandom)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50305-score" class="post-score" title="current number of votes">1</div><span id="post-50305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to decrypt a https connection on my machine with java.<br />
For that reason I have a system variable set so that Firefox puts the ClientRandom into a txt file. Now when I open a capture with Wireshark and give it access to the txt file with the ClientRandom, it can decrypt the whole sslstream.<br />
I am now wondering how Wireshark does it. After reading some pages explaining how SSL/TLS works (explaining RFC of TLS) I wonder how to get the Pre-master-secret, since I don't know the private exponent d from the server.<br />
I can see in Wireshark that I send the encrypted PreMaster in the Client Key Exchange, Change Cipher Spec, Finished package. But to decrypt this I would need the private exponent d from the server, wouldn't I?</p><p>Any help is very much appreciated.<br />
Kind Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/1683ee6ee87a65cb866ff23869f5de45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monkey521&#39;s gravatar image" /><p><span>monkey521</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monkey521 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-50305" class="comments-container"></div><div id="comment-tools-50305" class="comment-tools"></div><div class="clear"></div><div id="comment-50305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50311"></span>

<div id="answer-container-50311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50311-score" class="post-score" title="current number of votes">1</div><span id="post-50311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With just the Random from the Client Hello message you cannot decrypt anything. The SSL keylog format (as originally created by Mozilla for the NSS library) stores both the Client Random and the master secret. Wireshark will then try to map the Client Hello to a master secret which can then be used for decryption.</p><p>Since the master-secret is available, the RSA-encrypted pre-master secret does not have to be decrypted. See also slides 6-9 from <a href="https://lekensteyn.nl/files/wireshark-ssl-decryption.pdf#page=6">this presentation on SSL decryption using Wireshark</a> for the relation between various parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span> </br></br></p></div></div><div id="comments-container-50311" class="comments-container"><span id="50337"></span><div id="comment-50337" class="comment"><div id="post-50337-score" class="comment-score"></div><div class="comment-text"><p>Ok, thank you. In the txt file it says ClientRandom in front of the line but as you stated there seems to be the CR and MS, because with only one line in the file i can decrypt the whole traffic in Wireshark.</p></div><div id="comment-50337-info" class="comment-info"><span class="comment-age">(19 Feb '16, 05:23)</span> <span class="comment-user userinfo">monkey521</span></div></div></div><div id="comment-tools-50311" class="comment-tools"></div><div class="clear"></div><div id="comment-50311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

