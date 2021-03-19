+++
type = "question"
title = "How do I reassemble monitor mode 802.11 protocol data into TCP/IP packets?"
description = '''I&#x27;m trying to test Wireshark&#x27;s / my computer&#x27;s ability to capture WiFi packets to and from other computers on the same WiFi network. When I capture in promiscuous non-monitor mode, I get full TCP/IP stack data, including HTTP data. However, I only see data from my computer. So I try promiscuous + mo...'''
date = "2014-04-23T00:11:00Z"
lastmod = "2014-04-23T00:11:00Z"
weight = 32083
keywords = [ "promiscuous", "macosx", "monitor" ]
aliases = [ "/questions/32083" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I reassemble monitor mode 802.11 protocol data into TCP/IP packets?](/questions/32083/how-do-i-reassemble-monitor-mode-80211-protocol-data-into-tcpip-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32083-score" class="post-score" title="current number of votes">3</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to test Wireshark's / my computer's ability to capture WiFi packets to and from other computers on the same WiFi network.</p><p>When I capture in promiscuous non-monitor mode, I get full TCP/IP stack data, including HTTP data. However, I only see data from my computer. So I try promiscuous + monitor mode + network decryption key. When I do this, I see tons of broadcast 802.11 protocol records, but no HTTP, ICMP, or DHCP packets.</p><p>I'm not interested in seeing radio headers, just high level TCP/IP data pertaining to other computers on the network.</p><p>Am I doing something wrong?</p><p>System:</p><ul><li>Wireshark 1.10.7</li><li>Mac OS X 10.9.2 Mavericks</li><li>13" mid-2013 MacBook Air, Intel Haswell Core i7</li></ul></div><div id="question-tags" class="tags-container tags">promiscuous macosx monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 00:11</strong></p><img src="https://secure.gravatar.com/avatar/dfe88469b75efc87cbcbbbc2a975850a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mcandre&#39;s gravatar image" /><p>mcandre<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mcandre has no accepted answers">0%</span></p></div></div><div id="comments-container-32083" class="comments-container"><span id="34900"></span><div id="comment-34900" class="comment"><div id="post-34900-score" class="comment-score"></div><div class="comment-text"><p>I have the same issue, did you ever get this working?</p></div><div id="comment-34900-info" class="comment-info"><span class="comment-age">(24 Jul '14, 15:30)</span> nibeck</div></div><span id="34904"></span><div id="comment-34904" class="comment"><div id="post-34904-score" class="comment-score"></div><div class="comment-text"><p>No, I never did :( I would have most definitely posted the solution if I found one, I hate when people post 'fixed it' without saying how.</p></div><div id="comment-34904-info" class="comment-info"><span class="comment-age">(24 Jul '14, 19:58)</span> mcandre</div></div><span id="36214"></span><div id="comment-36214" class="comment"><div id="post-36214-score" class="comment-score"></div><div class="comment-text"><p>Do you see <em>non</em>-broadcast 802.11 packets? (Check the destination MAC address.)</p></div><div id="comment-36214-info" class="comment-info"><span class="comment-age">(11 Sep '14, 14:11)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-32083" class="comment-tools"></div><div class="clear"></div><div id="comment-32083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

