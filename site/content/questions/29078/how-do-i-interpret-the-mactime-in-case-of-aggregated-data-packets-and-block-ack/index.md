+++
type = "question"
title = "How do I interpret the mactime in case of aggregated data packets and block ack ?"
description = '''In the sample capture output below following are my questions: 1) Packet #1 to #16 belong to same AMPDU but why does !16 have different mactime ? 2) The mactime increases from data pkt #16 to Ack #17, but after that decreases for the subsequent data pkt#18. I have added the mactime delta column afte...'''
date = "2014-01-21T18:30:00Z"
lastmod = "2014-01-21T18:30:00Z"
weight = 29078
keywords = [ "mactime", "ampdu" ]
aliases = [ "/questions/29078" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I interpret the mactime in case of aggregated data packets and block ack ?](/questions/29078/how-do-i-interpret-the-mactime-in-case-of-aggregated-data-packets-and-block-ack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29078-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the sample capture output below following are my questions: 1) Packet #1 to #16 belong to same AMPDU but why does !16 have different mactime ? 2) The mactime increases from data pkt #16 to Ack #17, but after that decreases for the subsequent data pkt#18.</p><p>I have added the mactime delta column after calculation for reference.</p><p>Captures done using Wireshark on Ubuntu using ath9k driver corresponding to AR9287 chipset.</p><p>tshark -r pktFile.pcapng -N t -T fields -E separator=/t -e frame.number -e radiotap.mactime -e radiotap.ampdu.reference -e radiotap.ampdu.flags.last -e col.Protocol -e col.Info</p><p>1 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>2 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>3 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>4 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>5 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>6 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>7 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>8 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>9 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>10 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>11 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>12 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>13 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>14 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>15 2178550855 0 91215 0 UDP Source port: 38953 Destination port: 55225</p><p>16 2178553632 2777 91215 1 UDP Source port: 38953 Destination port: 55225</p><p>17 2178553846 214 802.11 802.11 Block Ack, Flags=........C</p><p>18 2178553697 -149 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>19 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>20 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>21 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>22 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>23 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>24 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>25 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>26 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>27 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>28 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>29 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>30 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>31 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>32 2178553697 0 91216 0 UDP Source port: 38953 Destination port: 55225</p><p>33 2178556479 2782 91216 1 UDP Source port: 38953 Destination port: 55225</p><p>34 2178556693 214 802.11 802.11 Block Ack, Flags=........C</p><p>35 2178556543 -150 91217 0 UDP Source port: 38953 Destination port: 55225</p></div><div id="question-tags" class="tags-container tags">mactime ampdu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '14, 18:30</strong></p><img src="https://secure.gravatar.com/avatar/43e2d9c38f7fe55143e0606580e503bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sudheer&#39;s gravatar image" /><p>Sudheer<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sudheer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jan '14, 18:33</p></div></div><div id="comments-container-29078" class="comments-container"></div><div id="comment-tools-29078" class="comment-tools"></div><div class="clear"></div><div id="comment-29078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

