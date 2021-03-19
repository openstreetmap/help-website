+++
type = "question"
title = "Using hexviewer to look at the pcap file, how do you know the start of frame?"
description = '''I have a question regarding opening the pcap file from wireshark using a hexviewer and looking at the raw data, I can&#x27;t find the start frame delimiter. Is the frame format the same as standard 802.11 or is it different? Thanks for your time and help.'''
date = "2013-07-01T15:16:00Z"
lastmod = "2013-07-10T09:14:00Z"
weight = 22527
keywords = [ "hexdataframeformat" ]
aliases = [ "/questions/22527" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using hexviewer to look at the pcap file, how do you know the start of frame?](/questions/22527/using-hexviewer-to-look-at-the-pcap-file-how-do-you-know-the-start-of-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22527-score" class="post-score" title="current number of votes">0</div><span id="post-22527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a question regarding opening the pcap file from wireshark using a hexviewer and looking at the raw data, I can't find the start frame delimiter. Is the frame format the same as standard 802.11 or is it different? Thanks for your time and help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hexdataframeformat" rel="tag" title="see questions tagged &#39;hexdataframeformat&#39;">hexdataframeformat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '13, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/320250ab70b248159a7d2783bbc420a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emma&#39;s gravatar image" /><p><span>emma</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emma has no accepted answers">0%</span></p></div></div><div id="comments-container-22527" class="comments-container"></div><div id="comment-tools-22527" class="comment-tools"></div><div class="clear"></div><div id="comment-22527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22528"></span>

<div id="answer-container-22528" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22528-score" class="post-score" title="current number of votes">5</div><span id="post-22528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="emma has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">Here's a description of the pcap file format</a>, and <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">here's a description of the pcap-ng file format</a>; those are the two standard Wireshark file formats. Older versions defaulted to pcap; newer versions default to pcap-ng.</p><p>In pcap files, packets are in the records that appear after the file header, and the lowest-level contents of the packet are described by the link-layer header type value in the file header.</p><p>In pcap-ng files, packets are in Packet Blocks, Enhanced Packet Blocks, or Simple Packet Blocks; Wireshark uses Enhanced Packet Blocks. Each packet has an interface ID value, which refers to one of the interfaces described by Interface Description Blocks in the file. The lowest-level contents of the packet are described by the link-layer header type value in the Interface Description Block for the interface on which the packet arrived.</p><p><a href="http://www.tcpdump.org/linktypes.html">Here is a description of the link-layer header type values</a>. If you have 802.11 traffic, the link-layer header type will be one of:</p><ul><li><code>LINKTYPE_IEEE802_11</code> (105), in which the packet data looks like Figure 8-1 of IEEE Std 802.11-2012, i.e. the packet data begins with the Frame Control field, followed by the Duration/ID field, followed by the Address 1 field, etc.;</li><li><code>LINKTYPE_IEEE802_11_PRISM</code> (119), in which the packet data begins with <a href="http://www.tcpdump.org/linktypes/LINKTYPE_IEEE802_11_PRISM.html">a Prism header giving some metadata for the packet</a>, followed by packet data that looks like Figure 8-1 of IEEE Std 802.11-2012;</li><li><code>LINKTYPE_IEEE802_11_RADIOTAP</code> (127), in which the packet data begins with <a href="http://www.radiotap.org">a radiotap header giving some metadata for the packet</a>, followed by packet data that looks like Figure 8-1 of IEEE Std 802.11-2012;</li><li><code>LINKTYPE_IEEE802_11_AVS</code> (163), in which the packet begins with <a href="http://web.archive.org/web/20040803232023/http://www.shaftnet.org/~pizza/software/capturefrm.txt">an AVS header giving some metadata for the packet</a>, followed by packet data that looks like Figure 8-1 of IEEE Std 802.11-2012;</li><li><code>LINKTYPE_PPI</code>, in which the packet begins with <a href="http://www.cacetech.com/documents/PPI%20Header%20format%201.0.7.pdf">a fairly complicated header giving metadata for the packet, in addition to a link-layer header type value</a>, followed by packet data of the type given by the link-layer header type value in the PPI header (for example, <code>LINKTYPE_IEEE802_11</code>, in which case the packet data would look like Figure 8-1 of IEEE Std 802.11-2012).</li></ul><p>In <em>none</em> of those formats will you see any PHY-layer information such as the SFD.</p><p>So the frame format <em>is</em> the same as the 802.11 frame format <em>as described in section 8 "Frame formats" of IEEE Std 802.11-2012</em>; it is <em>not</em> the same as the format as described in:</p><ul><li>section 14 "Frequency-Hopping spread spectrum (FHSS) PHY specification for the 2.4 GHz industrial, scientific, and medical (ISM) band";</li><li>section 16 "DSSS PHY specification for the 2.4 GHz band designated for ISM applications";</li><li>section 17 "High Rate direct sequence spread spectrum (HR/DSSS) PHY specification" (i.e., 802.11b);</li><li>section 18 "Orthogonal frequency division multiplexing (OFDM) PHY specification" (i.e., 802.11a);</li><li>section 19 "Extended Rate PHY (ERP) specification" (i.e., 802.11g);</li><li>section 20 "High Throughput (HT) PHY specification" (i.e., 802.11n);</li><li>the drafts for IEEE 802.11ac;</li></ul><p>because it does not contain the PHY-layer information given there.</p><p>So you can't find the start frame delimiter because it isn't there, just as the Ethernet start frame delimiter isn't in <code>LINKTYPE_ETHERNET</code> (1) captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22528" class="comments-container"><span id="22529"></span><div id="comment-22529" class="comment"><div id="post-22529-score" class="comment-score"></div><div class="comment-text"><p>A nice use case for <a href="http://www.wireshark.org/lists/wireshark-dev/201306/msg00101.html">Fileshark</a> ... assuming we can even call it that, considering <a href="https://www.fileshark.us/">https://www.fileshark.us/</a>?</p></div><div id="comment-22529-info" class="comment-info"><span class="comment-age">(01 Jul '13, 18:10)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="22817"></span><div id="comment-22817" class="comment"><div id="post-22817-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your organized and efficient answer :)</p></div><div id="comment-22817-info" class="comment-info"><span class="comment-age">(10 Jul '13, 09:14)</span> <span class="comment-user userinfo">emma</span></div></div></div><div id="comment-tools-22528" class="comment-tools"></div><div class="clear"></div><div id="comment-22528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

