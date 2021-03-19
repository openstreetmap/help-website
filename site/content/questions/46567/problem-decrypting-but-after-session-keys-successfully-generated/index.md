+++
type = "question"
title = "Problem decrypting, but after session keys successfully generated"
description = '''Hi all I have an SSL conversation, and have applied the private RSA key of the server. From the debug file, I can see that the SSL dissector reaches the stage at which the session keys are generated and a server and client decoders are created and are using AES256. The stage reached is Server: Chang...'''
date = "2015-10-15T07:54:00Z"
lastmod = "2015-10-15T10:41:00Z"
weight = 46567
keywords = [ "ssl", "session", "key" ]
aliases = [ "/questions/46567" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem decrypting, but after session keys successfully generated](/questions/46567/problem-decrypting-but-after-session-keys-successfully-generated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46567-score" class="post-score" title="current number of votes">0</div><span id="post-46567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I have an SSL conversation, and have applied the private RSA key of the server.</p><p>From the debug file, I can see that the SSL dissector reaches the stage at which the session keys are generated and a server and client decoders are created and are using AES256.</p><p>The stage reached is Server: Change Cipher Spec, Finished</p><p>However the application data thereafter is not being decrypted correctly.</p><p>Presumably if I had the incorrect RSA key, then Wireshark couldn't get as far as generating the session keys? If so, then how could it fail to decrypt the application data using the session key?</p><p>Any help gratefully received!</p><p>Robert</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '15, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/03bd741d32edec34e0d3ec40d6f92fdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronslow&#39;s gravatar image" /><p><span>ronslow</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronslow has no accepted answers">0%</span></p></div></div><div id="comments-container-46567" class="comments-container"><span id="46571"></span><div id="comment-46571" class="comment"><div id="post-46571-score" class="comment-score"></div><div class="comment-text"><p>And in fact I checked the RSA key using <a href="https://ask.wireshark.org/questions/22813/not-able-to-decrypt-ssl-data-with-private-keys">https://ask.wireshark.org/questions/22813/not-able-to-decrypt-ssl-data-with-private-keys</a> and it's the correct key!</p></div><div id="comment-46571-info" class="comment-info"><span class="comment-age">(15 Oct '15, 09:27)</span> <span class="comment-user userinfo">ronslow</span></div></div><span id="46575"></span><div id="comment-46575" class="comment"><div id="post-46575-score" class="comment-score"></div><div class="comment-text"><p>What Wireshark version are you using and what cipher suite is listed in the Server Hello? Do you have a ClientKeyExchange? If not, see point three of <a href="https://ask.wireshark.org/questions/45220/having-trouble-decrypting-tlsv1-traffic-using-private-key-of-the-server/45231.">https://ask.wireshark.org/questions/45220/having-trouble-decrypting-tlsv1-traffic-using-private-key-of-the-server/45231.</a></p></div><div id="comment-46575-info" class="comment-info"><span class="comment-age">(15 Oct '15, 10:41)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-46567" class="comment-tools"></div><div class="clear"></div><div id="comment-46567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

