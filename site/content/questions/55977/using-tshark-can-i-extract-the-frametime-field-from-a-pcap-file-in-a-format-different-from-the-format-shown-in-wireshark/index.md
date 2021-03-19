+++
type = "question"
title = "Using Tshark, can I extract the frame.time field from a .pcap file in a format different from the format shown in Wireshark?"
description = '''I have a .pcap file which displays time (i.e. Arrival Time (for Wireshark and frame.time field for Tshark) in the top/physical/Frame layer) in the Apr 3, 2015 16:58:46.461897000 PDT. I want to get this time in ISO format, like 2007-09-01 04:10:58. Please note that I am not going to take a capture. I...'''
date = "2016-09-28T23:59:00Z"
lastmod = "2016-09-28T23:59:00Z"
weight = 55977
keywords = [ "timestamp", "frame.time", "frame.time.delta", "tshark", "wireshark" ]
aliases = [ "/questions/55977" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Tshark, can I extract the frame.time field from a .pcap file in a format different from the format shown in Wireshark?](/questions/55977/using-tshark-can-i-extract-the-frametime-field-from-a-pcap-file-in-a-format-different-from-the-format-shown-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55977-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a .pcap file which displays time (i.e. <strong><code>Arrival Time</code></strong> (for Wireshark and <code>frame.time</code> field for Tshark) in the top/physical/Frame layer) in the <strong><code>Apr  3, 2015 16:58:46.461897000 PDT</code></strong>.</p><p>I want to get this time in ISO format, like <strong><code>2007-09-01 04:10:58</code></strong>.</p><p>Please note that I am not <em>going to</em> take a capture. I already have a capture file. <strong>I want to use Tshark to extract the field <code>frame.time</code></strong> (which corresponds to <code>Arrival Time</code> in the top network layer in Wireshark) <strong>in a format like <code>2007-09-01 04:10:58</code>, rather than a format like <code>Apr  3, 2015 16:58:46.461897000 PDT</code>.</strong></p><p><strong>Can I do that? How?</strong></p></div><div id="question-tags" class="tags-container tags">timestamp frame.time frame.time.delta tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '16, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p>Jesss<br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div></div><div id="comments-container-55977" class="comments-container"><span id="55978"></span><div id="comment-55978" class="comment"><div id="post-55978-score" class="comment-score">1</div><div class="comment-text"><p>Does <a href="https://ask.wireshark.org/questions/30393/tshark-how-to-output-date-in-iso-format/30415">this answer</a> lack some information?</p></div><div id="comment-55978-info" class="comment-info"><span class="comment-age">(29 Sep '16, 01:48)</span> sindy</div></div><span id="55979"></span><div id="comment-55979" class="comment"><div id="post-55979-score" class="comment-score"></div><div class="comment-text"><p>@sindy Yes, that solution involves adding an extra column and then <em>taking the capture again.</em> I can't take the capture again. I <em>already have</em> the captured data in the form of a .pcap file. Using Tshark, I have to read it and output the time in ISO format. (something like <code>tshark -r myFile.pcap -T field -e frame.time &gt; output.csv</code>)</p></div><div id="comment-55979-info" class="comment-info"><span class="comment-age">(29 Sep '16, 02:03)</span> Jesss</div></div><span id="55980"></span><div id="comment-55980" class="comment"><div id="post-55980-score" class="comment-score"></div><div class="comment-text"><p>The capture is not taken again. The Wireshark gui is used to add a column to the preferences which is then available for use by tshark.</p><p>If you're not specifying individual fields you can use <code>-t ad</code> or <code>-t ud</code> as shown in the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a>.</p></div><div id="comment-55980-info" class="comment-info"><span class="comment-age">(29 Sep '16, 02:45)</span> grahamb ♦</div></div><span id="55988"></span><div id="comment-55988" class="comment"><div id="post-55988-score" class="comment-score"></div><div class="comment-text"><p>Running tshark with <code>-r existing_capture_file_name</code> instead of <code>-i interface_name</code> makes tshark read the existing file instead of taking a live capture and process it, according to the rest of the command line parameters, the same way as if it was a live capture.</p></div><div id="comment-55988-info" class="comment-info"><span class="comment-age">(29 Sep '16, 07:49)</span> sindy</div></div></div><div id="comment-tools-55977" class="comment-tools"></div><div class="clear"></div><div id="comment-55977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

