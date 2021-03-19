+++
type = "question"
title = "GETVPN or Group VPN decode"
description = '''I am studying Cisco GETVPN or Group VPN that is called by the other vendors. The control plane protocol is using UDP port 848. Is there a protocol to decode it? Thanks!'''
date = "2017-06-25T15:52:00Z"
lastmod = "2017-06-25T15:52:00Z"
weight = 62288
keywords = [ "getvpn" ]
aliases = [ "/questions/62288" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GETVPN or Group VPN decode](/questions/62288/getvpn-or-group-vpn-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62288-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am studying Cisco GETVPN or Group VPN that is called by the other vendors. The control plane protocol is using UDP port 848. Is there a protocol to decode it? Thanks!</p></div><div id="question-tags" class="tags-container tags">getvpn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '17, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/08a7db94810c538eed59c44ad2601ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="difan&#39;s gravatar image" /><p>difan<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="difan has no accepted answers">0%</span></p></div></div><div id="comments-container-62288" class="comments-container"><span id="62328"></span><div id="comment-62328" class="comment"><div id="post-62328-score" class="comment-score"></div><div class="comment-text"><p>A shot in the dark:</p><p>GETVPN is using GDOI (<a href="https://tools.ietf.org/html/rfc6407">RFC6407</a>) and ESP. GDOI itself is based on ISAKMP. As far as I know data packets are transmitted by ESP.</p><p>Have you tried to use 'Decode as' with ISAKMP for your UDP 848 data?</p></div><div id="comment-62328-info" class="comment-info"><span class="comment-age">(27 Jun '17, 04:42)</span> Uli</div></div></div><div id="comment-tools-62288" class="comment-tools"></div><div class="clear"></div><div id="comment-62288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

