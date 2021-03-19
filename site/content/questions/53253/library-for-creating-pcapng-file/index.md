+++
type = "question"
title = "Library for creating pcapng file"
description = '''Hi, I have a IRIG106 http://irig106.org/ file that I want to convert to pcapng.  The IRIG106 file has a number of channels similar to the multiple interfaces that pcapng supports. Is there a library that I can use to help populate a pcapng file?  Looking at https://wiki.wireshark.org/Development/Pca...'''
date = "2016-06-06T14:23:00Z"
lastmod = "2016-06-07T14:21:00Z"
weight = 53253
keywords = [ "pcapng" ]
aliases = [ "/questions/53253" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Library for creating pcapng file](/questions/53253/library-for-creating-pcapng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53253-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a IRIG106 <a href="http://irig106.org/">http://irig106.org/</a> file that I want to convert to pcapng.</p><p>The IRIG106 file has a number of channels similar to the multiple interfaces that pcapng supports.</p><p>Is there a library that I can use to help populate a pcapng file?</p><p>Looking at <a href="https://wiki.wireshark.org/Development/PcapNg">https://wiki.wireshark.org/Development/PcapNg</a> it appears that the wiretap API may do what I am looking but I have no idea how to use wiretap outside of Wireshark.</p><p>Worst case I will just follow the spec (<a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.htm">http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.htm</a>).</p><p>Any thoughts or ideas?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">pcapng</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/334b3772ba24e093b1c83a07da9e12c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20B&#39;s gravatar image" /><p>Rob B<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob B has no accepted answers">0%</span></p></div></div><div id="comments-container-53253" class="comments-container"></div><div id="comment-tools-53253" class="comment-tools"></div><div class="clear"></div><div id="comment-53253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="53259"></span>

<div id="answer-container-53259" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53259-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all you should definitely hop over to non-obsolete <a href="https://github.com/pcapng/pcapng">documentation</a>.</p><p>Second, this format is still being formed, as is the software surrounding it. Therefore things may be documented for the file format, while the code in Wireshark / wiretap is trailing and in flux. It may not be easy to use these parts outside of Wireshark at all. There's no effort being made in having these libraries useful on their own.</p><p>But the good news is that the file format is not that complicated. It shouldn't be too difficult to whip something together that writes the blocks you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53259" class="comments-container"><span id="53279"></span><div id="comment-53279" class="comment"><div id="post-53279-score" class="comment-score"></div><div class="comment-text"><p>Understood. Thanks</p></div><div id="comment-53279-info" class="comment-info"><span class="comment-age">(07 Jun '16, 06:38)</span> Rob B</div></div></div><div id="comment-tools-53259" class="comment-tools"></div><div class="clear"></div><div id="comment-53259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53291"></span>

<div id="answer-container-53291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53291-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're running on a newer version of OS X, it has functions in libpcap to write pcapng files; <a href="http://opensource.apple.com/source/libpcap/libpcap-54/">that version of libpcap is open-source</a>, so you can use that code. It's not documented in the standard man pages that come with OS X, but the source includes a <code>pcap_ng.3</code> man page that documents them (but that's not shipped with the OS).</p><p>(The OS X libpcap code in question is licensed under the APSL, so if it were incorporated into the standard libpcap, it would put libpcap under the APSL, which has patent clauses that some OSes that ship libpcap might find objectionable, so that code won't be incorporated into libpcap unless Apple relicenses it.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '16, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53291" class="comments-container"></div><div id="comment-tools-53291" class="comment-tools"></div><div class="clear"></div><div id="comment-53291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53295"></span>

<div id="answer-container-53295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53295-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>By the way, if the goal is to have <em>Wireshark or TShark</em> read those files, an alternative would be to modify the libwiretap code to be able to read them. That wouldn't help with standard binaries, but if those changes are submitted to the Wireshark project and incorporated into the source code, they'll appear in a future version of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '16, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53295" class="comments-container"><span id="53296"></span><div id="comment-53296" class="comment"><div id="post-53296-score" class="comment-score"></div><div class="comment-text"><p>The only problem with this solution is that these files can be very large 200+GB. So I was planning on splitting the file while filling the pcapng format.</p></div><div id="comment-53296-info" class="comment-info"><span class="comment-age">(07 Jun '16, 14:25)</span> Rob B</div></div></div><div id="comment-tools-53295" class="comment-tools"></div><div class="clear"></div><div id="comment-53295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

