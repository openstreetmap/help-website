+++
type = "question"
title = "802.11 HT capapbilities TXBF field decode seems incorrect"
description = '''Transmit Beam Forming (TxBF) Capabilities: 0x1807ff1f .... .... .... .... .... .... .... ...1 = Transmit Beamforming: Supported .... .... .... .... .... .... .... ..1. = Receive Staggered Sounding: Supported .... .... .... .... .... .... .... .1.. = Transmit Staggered Sounding: Supported .... .... ....'''
date = "2014-06-08T01:11:00Z"
lastmod = "2014-06-08T01:11:00Z"
weight = 33543
keywords = [ "wlan", "ht", "capabilities" ]
aliases = [ "/questions/33543" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 HT capapbilities TXBF field decode seems incorrect](/questions/33543/80211-ht-capapbilities-txbf-field-decode-seems-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33543-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Transmit Beam Forming (TxBF) Capabilities: 0x1807ff1f<br />
.... .... .... .... .... .... .... ...1 = Transmit Beamforming: Supported<br />
.... .... .... .... .... .... .... ..1. = Receive Staggered Sounding: Supported<br />
.... .... .... .... .... .... .... .1.. = Transmit Staggered Sounding: Supported<br />
.... .... .... .... .... .... .... 1... = Receive Null Data packet (NDP): Supported<br />
.... .... .... .... .... .... ...1 .... = Transmit Null Data packet (NDP): Supported<br />
.... .... .... .... .... .... ..0. .... = Implicit TxBF capable: Not supported<br />
.... .... .... .... .... .... 00.. .... = Calibration: incapable (0x00000000) .... .... .... .... .... ...0 .... .... = STA can apply TxBF using CSI explicit feedback: Not supported<br />
.... .... .... .... .... ..0. .... .... = STA can apply TxBF using uncompressed beamforming feedback matrix: Not supported<br />
.... .... .... .... .... .0.. .... .... = STA can apply TxBF using compressed beamforming feedback matrix: Not supported<br />
.... .... .... .... ...0 0... .... .... = Receiver can return explicit CSI feedback: not supported (0x00000000)<br />
.... .... .... .... .00. .... .... .... = Receiver can return explicit uncompressed Beamforming Feedback Matrix: not supported (0x00000000)<br />
.... .... .... ...0 0... .... .... .... = STA can compress and use compressed Beamforming Feedback Matrix: not supported (0x00000000)<br />
.... .... .... .00. .... .... .... .... = Minimal grouping used for explicit feedback reports: No grouping supported (0x00000000)<br />
.... .... ...0 0... .... .... .... .... = Max antennae STA can support when CSI feedback required: 1 TX antenna sounding (0x00000000)<br />
.... .... .00. .... .... .... .... .... = Max antennae STA can support when uncompressed Beamforming feedback required: 1 TX antenna sounding (0x00000000)<br />
.... ...0 0... .... .... .... .... .... = Max antennae STA can support when compressed Beamforming feedback required: 1 TX antenna sounding (0x00000000)<br />
.... .00. .... .... .... .... .... .... = Maximum number of rows of CSI explicit feedback: 1 row of CSI (0x00000000)<br />
...0 0... .... .... .... .... .... .... = Maximum number of space time streams for which channel dimensions can be simultaneously estimated: 1 space time stream (0x00000000)<br />
000. .... .... .... .... .... .... .... = Reserved: 0x00000000</p><p>Confirmed the observation on v1.10.6 and 1.11.3.</p></div><div id="question-tags" class="tags-container tags">wlan ht capabilities</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '14, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/43e2d9c38f7fe55143e0606580e503bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sudheer&#39;s gravatar image" /><p>Sudheer<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sudheer has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jun '14, 01:12</p></div></div><div id="comments-container-33543" class="comments-container"><span id="33555"></span><div id="comment-33555" class="comment"><div id="post-33555-score" class="comment-score"></div><div class="comment-text"><p>Do I need to file a bug ?</p></div><div id="comment-33555-info" class="comment-info"><span class="comment-age">(08 Jun '14, 12:17)</span> Sudheer</div></div><span id="33556"></span><div id="comment-33556" class="comment"><div id="post-33556-score" class="comment-score">1</div><div class="comment-text"><p>Yes please do so with a capture attached. The fix seems obvious but it would be better if you could add a sample pcap so as to verify the fix.</p></div><div id="comment-33556-info" class="comment-info"><span class="comment-age">(08 Jun '14, 12:40)</span> Pascal Quantin</div></div></div><div id="comment-tools-33543" class="comment-tools"></div><div class="clear"></div><div id="comment-33543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

