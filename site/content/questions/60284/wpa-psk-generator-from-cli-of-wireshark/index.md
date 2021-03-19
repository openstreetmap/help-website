+++
type = "question"
title = "WPA PSK Generator from CLI of Wireshark"
description = '''Hello forum, under https://wireshark.org/tools/wpa-psk.html it&#x27;s possible to generate the PSK (if passphrase and the SSID is known :-) This is a nice thing, but I would like to be able to generate the PSK myself and heard that many things can be done from the command line (cli) of Wireshark. Questio...'''
date = "2017-03-23T09:34:00Z"
lastmod = "2017-03-23T09:34:00Z"
weight = 60284
keywords = [ "psk" ]
aliases = [ "/questions/60284" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WPA PSK Generator from CLI of Wireshark](/questions/60284/wpa-psk-generator-from-cli-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60284-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello forum,</p><p>under <a href="https://wireshark.org/tools/wpa-psk.html">https://wireshark.org/tools/wpa-psk.html</a> it's possible to generate the PSK (if passphrase and the SSID is known :-)</p><p>This is a nice thing, but I would like to be able to generate the PSK myself and heard that many things can be done from the command line (cli) of Wireshark.</p><p>Question: Is this for the generation of the PSK as well the case? How?</p><p>Thank you very much!</p><p>Jo</p></div><div id="question-tags" class="tags-container tags">psk</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '17, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/c08acf577aad3b14e932ee8f48cf7d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph123&#39;s gravatar image" /><p>joseph123<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph123 has no accepted answers">0%</span></p></div></div><div id="comments-container-60284" class="comments-container"><span id="60287"></span><div id="comment-60287" class="comment"><div id="post-60287-score" class="comment-score"></div><div class="comment-text"><p>I know of this CLI tool that can do it, with some minor effort:</p><p><a href="https://www.aircrack-ng.org/doku.php?id=airolib-ng">https://www.aircrack-ng.org/doku.php?id=airolib-ng</a></p><p>A quick test took a couple of commands to get the PMK to be produced as a string of hex characters from an SSID:Passphrase set. With some work you may be able to distill down to a single command; at the very least this could all be scripted (e.g. bash or whatever) and get a single command to show the calculated PMK, if that is important. I tested on Linux.</p><p>If you search on here</p><p>(example: <a href="https://ask.wireshark.org/questions/24249/decrypt-wpa-with-tshark)">https://ask.wireshark.org/questions/24249/decrypt-wpa-with-tshark)</a></p><p>there are ways to run tshark and enter the SSID/Passphrase as an option. This does not provide the exact behavior you specified, but is effective for decrypting protected data frames. You may have other requirements that require the presentation of the actual PMK so this may not help.</p></div><div id="comment-60287-info" class="comment-info"><span class="comment-age">(23 Mar '17, 12:20)</span> Bob Jones</div></div></div><div id="comment-tools-60284" class="comment-tools"></div><div class="clear"></div><div id="comment-60284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

