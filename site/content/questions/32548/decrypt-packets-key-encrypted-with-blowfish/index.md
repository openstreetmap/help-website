+++
type = "question"
title = "Decrypt packets (key encrypted with Blowfish)"
description = '''I want to decrypt a few packets that a program on my computer is sending/receiving. It uses Blowfish to encrypt the packets and I have the key which is necessary to decrypt it again.  Now, how can I set up Wireshark to use this key to decrypt incoming Blowfish packets? And in case this isn&#x27;t possibl...'''
date = "2014-05-06T07:51:00Z"
lastmod = "2014-05-09T08:51:00Z"
weight = 32548
keywords = [ "blowfish" ]
aliases = [ "/questions/32548" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypt packets (key encrypted with Blowfish)](/questions/32548/decrypt-packets-key-encrypted-with-blowfish)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32548-score" class="post-score" title="current number of votes">0</div><span id="post-32548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to decrypt a few packets that a program on my computer is sending/receiving.<br />
It uses Blowfish to encrypt the packets and I have the key which is necessary to decrypt it again.<br />
</p><p>Now, how can I set up Wireshark to use this key to decrypt incoming Blowfish packets?<br />
And in case this isn't possible, do you know some application that would allow me to do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-blowfish" rel="tag" title="see questions tagged &#39;blowfish&#39;">blowfish</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/78589ecc2012537b87db3f5d733d3ebc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sookx&#39;s gravatar image" /><p><span>sookx</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sookx has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-32548" class="comments-container"><span id="32557"></span><div id="comment-32557" class="comment"><div id="post-32557-score" class="comment-score"></div><div class="comment-text"><blockquote><p>a few packets that a program on my computer is sending/receiving. It uses Blowfish to encrypt the packets</p></blockquote><p>What is the protocol used to send the packets?</p></div><div id="comment-32557-info" class="comment-info"><span class="comment-age">(06 May '14, 10:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32560"></span><div id="comment-32560" class="comment"><div id="post-32560-score" class="comment-score"></div><div class="comment-text"><p>Are you using a 128-bit key?</p><blockquote><p>Bruce Schneier of Counterpane Systems developed the Blowfish cipher algorithm. RFC 2451 shows that Blowfish uses key sizes from 40 to 448 bits. The Default size is 128 bits. We will only accept key sizes of 128 bits, because libgrypt only accept this key size. Have a look to <a href="http://www.schneier.com">http://www.schneier.com</a> for more information. BLOWFISH-CBC uses an IV of 8 octets.</p></blockquote><p><a href="http://wiki.wireshark.org/ESP_Preferences">http://wiki.wireshark.org/ESP_Preferences</a></p></div><div id="comment-32560-info" class="comment-info"><span class="comment-age">(06 May '14, 10:11)</span> <span class="comment-user userinfo">DDay</span></div></div><span id="32579"></span><div id="comment-32579" class="comment"><div id="post-32579-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span> It uses UDP.<br />
<span>@DDay</span> Yes, it uses a 128-bit key.</p></div><div id="comment-32579-info" class="comment-info"><span class="comment-age">(07 May '14, 01:20)</span> <span class="comment-user userinfo">sookx</span></div></div><span id="32580"></span><div id="comment-32580" class="comment"><div id="post-32580-score" class="comment-score"></div><div class="comment-text"><p>If you have UDP packets with encrypted user data you would have to write your own dissector registering for an UDP port and do the decryption there.</p></div><div id="comment-32580-info" class="comment-info"><span class="comment-age">(07 May '14, 01:53)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="32615"></span><div id="comment-32615" class="comment"><div id="post-32615-score" class="comment-score"></div><div class="comment-text"><blockquote><p><span></span><span>@Kurt Knochner</span> It uses UDP.</p></blockquote><p>Well, yes. Thanks.</p><p>But what I meant is this: what encryption protocol (or scheme) is being used, like HTTPS, IPSEC, OpenVPN, etc.</p><p>You can't just decrypt UDP without knowing the protocol being used, especially if you want Wireshark to do the decryption.</p></div><div id="comment-32615-info" class="comment-info"><span class="comment-age">(07 May '14, 11:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32626"></span><div id="comment-32626" class="comment not_top_scorer"><div id="post-32626-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span> As far as I know it uses a custom binary protocol and every packet is encrypted with Blowfish. SO I guess that you could basically just run the decryption algorithm on the contents of a packet.</p></div><div id="comment-32626-info" class="comment-info"><span class="comment-age">(07 May '14, 17:27)</span> <span class="comment-user userinfo">sookx</span></div></div></div><div id="comment-tools-32548" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32666"></span>

<div id="answer-container-32666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32666-score" class="post-score" title="current number of votes">1</div><span id="post-32666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>As far as I know <strong>it uses a custom binary protocol</strong> and every packet is encrypted with Blowfish.</p></blockquote><p>well, if it's a <strong>custom</strong> binary protocol, you won't be able to do anything unless you know the protocol. I don't mean UDP, I mean the way the data is encoded in the UDP frame.</p><blockquote><p>SO <strong>I guess that you could basically just run the decryption algorithm</strong> on the contents of a packet.</p></blockquote><p>No, you can't, because without any knowledge about the parameters for encryption, you can't decrypt the data. What you need is:</p><ul><li>key size (128, 256, 512 Bit)</li><li>key derivation function (how do they create the crypto key from the pass phrase)</li><li>is the Key salted: yes/no</li><li>Blowfish block size</li><li>padding methods</li><li>is each frame encrypted for itself, or do they encrypt a larger block of data and then send chunks in single UDP frames</li><li>etc.</li><li>etc.</li></ul><p>Without that information, there is no way to decrypt the data, other than a brute force of all possible combinations, which is a totally pointless operation unless you are working for the NSA ;-).</p><p>So, if you want to decrypt those frames, you will need (at least):</p><ul><li>all of the things mentioned above</li><li>somebody who writes a Wireshark dissector that takes all the information and does the actual decryption. You can use the https dissector as an example.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '14, 11:56</strong> </span></p></div></div><div id="comments-container-32666" class="comments-container"></div><div id="comment-tools-32666" class="comment-tools"></div><div class="clear"></div><div id="comment-32666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

