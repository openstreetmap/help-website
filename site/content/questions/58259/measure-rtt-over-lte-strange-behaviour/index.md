+++
type = "question"
title = "Measure RTT over LTE , strange behaviour"
description = '''Hi all, I hope anybody can help me. I&#x27;m trying to measure the RTT for TCP packets over LTE. I have running a server with a file (size 1K) and I download this file 10 times with wget on a client, capturing the packets with tcpdump. To get the RTT I analyze this packets by observing both SYN-SYN/ACK t...'''
date = "2016-12-20T09:43:00Z"
lastmod = "2016-12-20T09:43:00Z"
weight = 58259
keywords = [ "rtt", "fin", "syn", "tcp" ]
aliases = [ "/questions/58259" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Measure RTT over LTE , strange behaviour](/questions/58259/measure-rtt-over-lte-strange-behaviour)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58259-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I hope anybody can help me. I'm trying to measure the RTT for TCP packets over LTE. I have running a server with a file (size 1K) and I download this file 10 times with wget on a client, capturing the packets with tcpdump. To get the RTT I analyze this packets by observing both SYN-SYN/ACK time difference and the FIN/ACK - FIN/ACK time difference. I expected to get values in the same magnigute. But I observe, that the SYN-SYN/ACK round trip time is always 3-5 times bigger than FIN/ACK RTT.</p><p>Example:</p><p><code>| No. | Time   | Source | Destination | Protocol | Info    | RTT     | | 1   | 0.000  | 100.xx | 195.xx      | TCP      | SYN     | 0.000   | | 2   | 0.156  | 195.xx | 100.xx      | TCP      | SYN,ACK | 0.156   | | ... | ...    | ...    | ...         | ...      | ...     | ...     | | 8   | 0.3744 | 100.xx | 195.xx      | TCP      | FIN,ACK | 0.000   | | 9   | 0.4055 | 195.xx | 100.xx      | TCP      | FIN,ACK | 0.03118 |</code></p><p>As you can see, the FIN,ACK rtt is 5 times smaller than the initial SYN-ACK RTT? I can observe this behaviour for most of the packets. But why ?</p><p>What i also observe, the RTT is the first time very big (0.156ms) and than downloading the file again it gets smaller (0.045ms)? I disable caching (wget --no-cache)</p><p>Thanks for your help,</p><p>Dieter</p></div><div id="question-tags" class="tags-container tags">rtt fin syn tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '16, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/479c5bb186cca824739da910b6c2def4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DieterMeier&#39;s gravatar image" /><p>DieterMeier<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DieterMeier has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Dec '16, 10:13</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58259" class="comments-container"><span id="58278"></span><div id="comment-58278" class="comment"><div id="post-58278-score" class="comment-score"></div><div class="comment-text"><p>A complete guess, but it could be that the first time you connect the mobile device has to do a RACH to get an uplink grant, whereas for subsequent packets you get an uplink grant more quickly?</p></div><div id="comment-58278-info" class="comment-info"><span class="comment-age">(21 Dec '16, 12:42)</span> MartinM</div></div></div><div id="comment-tools-58259" class="comment-tools"></div><div class="clear"></div><div id="comment-58259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

