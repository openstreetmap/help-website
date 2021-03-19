+++
type = "question"
title = "SSL Decryption: &quot;wrong pre_master_secret length&quot;"
description = '''I&#x27;m trying to decrypt an SSL session, but I&#x27;m running into some problems. When I click on &quot;follow SSL Stream&quot; I just get an empty window. After I enabled debug logging, I found the following messages: pcry_private_decrypt: stripping 181 bytes, decr_len 304 ssl_decrypt_pre_master_secret wrong pre_mas...'''
date = "2015-05-16T14:24:00Z"
lastmod = "2015-05-18T19:00:00Z"
weight = 42443
keywords = [ "ssl" ]
aliases = [ "/questions/42443" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Decryption: "wrong pre\_master\_secret length"](/questions/42443/ssl-decryption-wrong-pre_master_secret-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42443-score" class="post-score" title="current number of votes">0</div><span id="post-42443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt an SSL session, but I'm running into some problems. When I click on "follow SSL Stream" I just get an empty window. After I enabled debug logging, I found the following messages:</p><pre><code>pcry_private_decrypt: stripping 181 bytes, decr_len 304
ssl_decrypt_pre_master_secret wrong pre_master_secret length (123, expected 48)
ssl_generate_pre_master_secret: can&#39;t decrypt pre master secret
trying to use SSL keylog in 
failed to open SSL keylog
dissect_ssl3_handshake can&#39;t generate pre master secret
  record: offset = 315, reported_length_remaining = 75
dissect_ssl3_record: content_type 20 Change Cipher Spec</code></pre><p>Can someone tell me if this is the reason for the apparently empty stream? If so, how do I fix it?</p><p>I read elsewhere that this might happen if the private key used for Wireshark doesn't match the private key used by the server, but the keys are definitely identical.</p><p>This is with Wireshark 1.12.1 on Debian Jessie, linked against GnuTLS 3.3.8. I can decrypt the Snakeoil example from the Wireshark Wiki just fine.</p><p>I've uploaded the full <a href="https://www.dropbox.com/s/6kk6oqaj1zmtngl/ssl_debug.txt?dl=0">debug log</a> to and the <a href="https://www.dropbox.com/s/jpar0gnviyf1cwi/imap_starttls.pcapng?dl=0">traffic dump</a>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '15, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/7256049d410aa28c240527e1a779799e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikratio&#39;s gravatar image" /><p><span>Nikratio</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikratio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '15, 08:53</strong> </span></p></div></div><div id="comments-container-42443" class="comments-container"><span id="42447"></span><div id="comment-42447" class="comment"><div id="post-42447-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and which version and what is your Wireshark version? Did you try the snakeoil files with it?</p></div><div id="comment-42447-info" class="comment-info"><span class="comment-age">(17 May '15, 02:34)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="42452"></span><div id="comment-42452" class="comment"><div id="post-42452-score" class="comment-score"></div><div class="comment-text"><p>please add the whole SSL debug log!</p></div><div id="comment-42452-info" class="comment-info"><span class="comment-age">(17 May '15, 06:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42464"></span><div id="comment-42464" class="comment"><div id="post-42464-score" class="comment-score"></div><div class="comment-text"><p><span>@Jaap</span>, @KurtKnochner I've added the missing information.</p></div><div id="comment-42464-info" class="comment-info"><span class="comment-age">(17 May '15, 08:50)</span> <span class="comment-user userinfo">Nikratio</span></div></div><span id="42468"></span><div id="comment-42468" class="comment"><div id="post-42468-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt</span> I've added the full debug log.</p></div><div id="comment-42468-info" class="comment-info"><span class="comment-age">(17 May '15, 09:53)</span> <span class="comment-user userinfo">Nikratio</span></div></div><span id="42470"></span><div id="comment-42470" class="comment"><div id="post-42470-score" class="comment-score"></div><div class="comment-text"><p>"decrypt_ssl3_record: no decoder available" is a much more worrying statement. This means there's relevant info missing for decryption. What if you replace the ebox.rath.org.key port 0 registration with port 143?</p></div><div id="comment-42470-info" class="comment-info"><span class="comment-age">(17 May '15, 11:49)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="42473"></span><div id="comment-42473" class="comment not_top_scorer"><div id="post-42473-score" class="comment-score"></div><div class="comment-text"><p><span>@Jaap</span>: There is no port 0 registration, only one for "start_tls" and one for "993". If I change the one for 993 to 143, the "no decoder available" message persists (this is an imap stream to port 143 using starttls).</p></div><div id="comment-42473-info" class="comment-info"><span class="comment-age">(17 May '15, 15:17)</span> <span class="comment-user userinfo">Nikratio</span></div></div><span id="42485"></span><div id="comment-42485" class="comment not_top_scorer"><div id="post-42485-score" class="comment-score"></div><div class="comment-text"><p>The SSL debug log says there is, the first one?</p><p>For these kinds of problems I usually refer back to the <a href="http://sharkfest.wireshark.org/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">SharkFest presentation by Sake Blok</a>, maybe that can be of help?</p></div><div id="comment-42485-info" class="comment-info"><span class="comment-age">(17 May '15, 22:51)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-42443" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-42443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42484"></span>

<div id="answer-container-42484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42484-score" class="post-score" title="current number of votes">0</div><span id="post-42484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I read elsewhere that this might happen if the private key used for Wireshark doesn't match the private key used by the server, but the keys are definitely identical.</p></blockquote><p>There are two keys available for your server. One for HTTPS (www.domain.org) and one for IMAP STARTLS (ebox.domain.org). I found the URLs in the debug log and in the capture file, so I accessed both via <strong>openssl s_client</strong>. Both certs are different and thus the private keys are different as well.</p><p>Are you sure you've really used the key for ebox.domain.org and not www.domain.org? The filename in the debug file implies that (filenames are identical to the domain name), but you never know! Please double check that.</p><p>BTW: Are you able to decrypt HTTPS traffic with the key for www.domain.org?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '15, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '15, 22:35</strong> </span></p></div></div><div id="comments-container-42484" class="comments-container"><span id="42520"></span><div id="comment-42520" class="comment"><div id="post-42520-score" class="comment-score"></div><div class="comment-text"><p>Yes, the key is definitely correct. I tried switching the keys anyway, and interestingly enough I got the same error. I haven't been able to decrypt HTTPS traffic, because I haven't yet figured out how to tell Apache not to do DH key exchange.</p></div><div id="comment-42520-info" class="comment-info"><span class="comment-age">(18 May '15, 18:57)</span> <span class="comment-user userinfo">Nikratio</span></div></div><span id="42521"></span><div id="comment-42521" class="comment"><div id="post-42521-score" class="comment-score"></div><div class="comment-text"><p>I think I'll repost this question the wireshark-users mailing list. This web interface seems rather ill-suited for going back &amp; forth more than once :-).</p></div><div id="comment-42521-info" class="comment-info"><span class="comment-age">(18 May '15, 19:00)</span> <span class="comment-user userinfo">Nikratio</span></div></div></div><div id="comment-tools-42484" class="comment-tools"></div><div class="clear"></div><div id="comment-42484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

