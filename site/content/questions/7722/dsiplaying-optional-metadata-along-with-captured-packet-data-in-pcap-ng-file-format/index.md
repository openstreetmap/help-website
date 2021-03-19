+++
type = "question"
title = "Dsiplaying Optional metadata along with captured packet data in PCAP NG file format"
description = '''Hi, I am inserting some metadata in Optional field of Evolved Packet Block in PCAP NG file format. I want wireshark to decode and display those metadata info along with captured protocol data. Is there any provion in wireshark to do this. Or if any modification is required in wireshark, how to proce...'''
date = "2011-11-30T23:18:00Z"
lastmod = "2011-12-05T21:47:00Z"
weight = 7722
keywords = [ "pcapng", "epb", "metadata" ]
aliases = [ "/questions/7722" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dsiplaying Optional metadata along with captured packet data in PCAP NG file format](/questions/7722/dsiplaying-optional-metadata-along-with-captured-packet-data-in-pcap-ng-file-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7722-score" class="post-score" title="current number of votes">0</div><span id="post-7722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am inserting some metadata in Optional field of Evolved Packet Block in PCAP NG file format. I want wireshark to decode and display those metadata info along with captured protocol data. Is there any provion in wireshark to do this. Or if any modification is required in wireshark, how to proceed ??</p><p>Please help.</p><p>Thanks, Ambika</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-epb" rel="tag" title="see questions tagged &#39;epb&#39;">epb</span> <span class="post-tag tag-link-metadata" rel="tag" title="see questions tagged &#39;metadata&#39;">metadata</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '11, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/55898068b61d3986b5fd5996d329c9fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ambika&#39;s gravatar image" /><p><span>ambika</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ambika has no accepted answers">0%</span></p></div></div><div id="comments-container-7722" class="comments-container"></div><div id="comment-tools-7722" class="comment-tools"></div><div class="clear"></div><div id="comment-7722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7736"></span>

<div id="answer-container-7736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7736-score" class="post-score" title="current number of votes">0</div><span id="post-7736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I presume you mean "Enhanced Packet Block" rather than "Evolved Packet Block"; there is no "Evolved Packet Block" in the <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">pcap-NG specification</a>, but there is an <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html#sectionepb">Enhanced Packet Block</a>.</p><p>There is currently no support for reading that information in Wireshark. In order to add that capability, you'd have to modify the API offered by the Wiretap library (in the <code>wiretap</code> directory of the Wireshark source code) to provide that information to its callers, and then modify Wireshark and TShark to display that information. The decoding would probably be done in the <code>packet-frame.c</code> dissector file in the <code>epan/dissectors</code> subdirectory.</p><p>Further discussion of this should be done on the <code>wireshark-dev</code> mailing list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '11, 18:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7736" class="comments-container"><span id="7789"></span><div id="comment-7789" class="comment"><div id="post-7789-score" class="comment-score"></div><div class="comment-text"><p>Hey thanks. I have made changes in wiretap library to dump optional metadata separately to stdout for each captured packet by using Tshark. But still not sure how to pass that info to wireshark for display.</p><p>I will work on it and discuss on the wireshark-dev mailing list as you suggested.</p><p>~ ambika</p></div><div id="comment-7789-info" class="comment-info"><span class="comment-age">(05 Dec '11, 21:47)</span> <span class="comment-user userinfo">ambika</span></div></div></div><div id="comment-tools-7736" class="comment-tools"></div><div class="clear"></div><div id="comment-7736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

