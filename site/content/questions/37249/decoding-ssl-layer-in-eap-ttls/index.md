+++
type = "question"
title = "Decoding SSL layer in EAP-TTLS"
description = '''Hi, sorry if this has been clarified before, but I&#x27;ve had a quick search through the mailing lists and nothing jumps out at me. I am trying to decode EAP-TTLS. Wireshark works out of the box down up as far as TLS layer. That is, I can see the following:  Radius over UDP, or EAPoL fragments EAP packe...'''
date = "2014-10-21T11:04:00Z"
lastmod = "2014-10-21T11:04:00Z"
weight = 37249
keywords = [ "tls", "eap", "eapol", "eap-ttls" ]
aliases = [ "/questions/37249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding SSL layer in EAP-TTLS](/questions/37249/decoding-ssl-layer-in-eap-ttls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, sorry if this has been clarified before, but I've had a quick search through the mailing lists and nothing jumps out at me.</p><p>I am trying to decode EAP-TTLS. Wireshark works out of the box down up as far as TLS layer. That is, I can see the following:</p><ol><li>Radius over UDP, or EAPoL fragments</li><li>EAP packets</li><li>SSL Handshake over a sequence of EAP packets</li></ol><p>After the handshake however, the TLS cipher kicks in and I can't see what's happening. This is a "good thing" in the normal operation of the protocol. I'm trying to perform some diagnostics however so this is a bit of a problem.</p><p>I have the private key and all, so it should in theory be possible to decode this, but I guess it's just a case of making a few modifications.</p><p>I'd be interested in taking a look at adding this feature. It seems this is a solved problem for many other protocols (HTTPS, LDAP) so how hard could it be?</p><p>It seems as though I can see it attempt to decode the TLS layer for the first EAP frame, but then it gives up for the remainder of the session, so all that needs to be done is to correlate the remaining frames. Easy!</p><p>I'll have a look now at the code and see if it makes any sense. If anybody can provide and guidance I would be very grateful.</p><p>Thanks, Rob</p></div><div id="question-tags" class="tags-container tags">tls eap eapol eap-ttls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/b2244263c61892ddd4d2b4d6b4786e6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robert_&#39;s gravatar image" /><p>robert_<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robert_ has no accepted answers">0%</span></p></div></div><div id="comments-container-37249" class="comments-container"><span id="37262"></span><div id="comment-37262" class="comment"><div id="post-37262-score" class="comment-score"></div><div class="comment-text"><p>Very well. Have a look at packet-eap.c and packet-ssl[-utils].c which handle this case. At least that's what the code suggests. Sounds as if it's not working right?</p></div><div id="comment-37262-info" class="comment-info"><span class="comment-age">(22 Oct '14, 01:41)</span> Jaap ♦</div></div></div><div id="comment-tools-37249" class="comment-tools"></div><div class="clear"></div><div id="comment-37249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

