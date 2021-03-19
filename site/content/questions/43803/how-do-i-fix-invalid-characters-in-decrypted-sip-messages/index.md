+++
type = "question"
title = "How do I fix invalid characters in decrypted SIP messages?"
description = '''Hello all, First of all - thank you to everyone in the forums, it&#x27;s an extremely helpful tool! Second, I&#x27;m somewhat of a newb when it comes to decrypting TLS with wireshark using session keys. I am somewhat familiar with decrypting using private keys (which is what I&#x27;m resorting to here). Lastly, I&#x27;...'''
date = "2015-07-01T21:47:00Z"
lastmod = "2015-07-01T21:47:00Z"
weight = 43803
keywords = [ "ssl", "sip" ]
aliases = [ "/questions/43803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fix invalid characters in decrypted SIP messages?](/questions/43803/how-do-i-fix-invalid-characters-in-decrypted-sip-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43803-score" class="post-score" title="current number of votes">0</div><span id="post-43803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>First of all - thank you to everyone in the forums, it's an extremely helpful tool! Second, I'm somewhat of a newb when it comes to decrypting TLS with wireshark using session keys. I am somewhat familiar with decrypting using private keys (which is what I'm resorting to here). Lastly, I'm probably missing a key bit of information - if that's the case let me know or point me in the right direction and I'll provide it.</p><p>I'm capturing packets from an embedded device that's using TLS and has really bad application logging - I can see most information from the application logging but I need to verify that what the application log is telling me is actually being sent across the wire. I have the private key imported into WS I see key exchange, client and server finish key exchange and agree on cipher suite The application uses, or attempts to use LZ77-8K compression</p><p>I successfully decrypt 2 SIP messages with the same call ID (a negotiate from client and 200 OK back from server). I see that successfully show in wireshark and it correctly identifies the packet type as "sip"</p><p>Every message after that is not identified as sip (and are also unique/new call IDs), and following the SSL stream shows why. Immediately succeeding packets' "Decrypted SSL data" have invalid characters preceding the SIP messages, including:</p><p>".....]" "......" ".....~"</p><p>removing those characters from the "Decrypted SSL Data" presents a usable SIP message. What I can't figure out is the why, or more specifically, how to determine the "why" - encryption issue, compression issue, or something else. This lasts for 7 SIP messages. Server-side logging (at the application layer) shows normal SIP messages reaching the server, without the additional characters.</p><p>After those 7 SIP Messages I have many more that become roughly 90% undecipherable. The decrypted data contains primarily non-alpha ascii characters, however about 10% of the characters are readable and consistent with what would be included in the SIP messages (both SIP headers and XML/content).</p><p>I have seen this type of data when using SSL-inspection devices and proxies, however neither are in the mix here. I'm directly spanning the port for the device prior to the packets/frames touching anything else.</p><p>Any thoughts from the community on what additional information I can provide to assist in resolving the issue?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 21:47</strong></p><img src="https://secure.gravatar.com/avatar/ef9d7b5f13fd9e3d7cfa1d199c44528c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UCninja&#39;s gravatar image" /><p><span>UCninja</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UCninja has no accepted answers">0%</span></p></div></div><div id="comments-container-43803" class="comments-container"></div><div id="comment-tools-43803" class="comment-tools"></div><div class="clear"></div><div id="comment-43803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

