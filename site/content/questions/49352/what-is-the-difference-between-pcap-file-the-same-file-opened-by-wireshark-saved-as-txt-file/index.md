+++
type = "question"
title = "What is the difference between pcap file &amp; the same file opened by wireshark &amp; saved as .txt file ?"
description = '''Hi, I have a requirement of converting a hexdump of several packets into format which wireshark can understand. I have downloaded a pcap file online, opened it with wireshark and saved it as .txt file. This .txt file can be again opened by wireshark for analyzing. If I can convert my hexdump into fo...'''
date = "2016-01-18T22:07:00Z"
lastmod = "2016-01-19T04:22:00Z"
weight = 49352
keywords = [ "ethernet", "networking", "network", "ask.wireshark.org", "wireshark" ]
aliases = [ "/questions/49352" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the difference between pcap file & the same file opened by wireshark & saved as .txt file ?](/questions/49352/what-is-the-difference-between-pcap-file-the-same-file-opened-by-wireshark-saved-as-txt-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49352-score" class="post-score" title="current number of votes">0</div><span id="post-49352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a requirement of converting a hexdump of several packets into format which wireshark can understand. I have downloaded a pcap file online, opened it with wireshark and saved it as .txt file. This .txt file can be again opened by wireshark for analyzing.</p><p>If I can convert my hexdump into format present in .txt file then I can analyze it packet by packet. My question here is, what is the difference between pcap format and .txt format. Do I need to convert my hexdump compalsary into pcap format for analyzing ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '16, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/8c9831cf2125cbaf2c8b45ec8b5d2ecf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KamaL&#39;s gravatar image" /><p><span>KamaL</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KamaL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jan '16, 22:58</strong> </span></p></div></div><div id="comments-container-49352" class="comments-container"></div><div id="comment-tools-49352" class="comment-tools"></div><div class="clear"></div><div id="comment-49352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49362"></span>

<div id="answer-container-49362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49362-score" class="post-score" title="current number of votes">1</div><span id="post-49362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="https://wiki.wireshark.org/Development/LibpcapFileFormat">pcap format</a> you are referring to is a binary format for the collection of raw packet data and related meta data. The text format you are referring to is an (ASCII) text interpretation of the packet data and related meta data.</p><p>For hex dumps Wireshark provides an <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html">import function</a>, which is capable to interpret the hex dump and create a pcap file from. There's also a commandline version called <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '16, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-49362" class="comments-container"><span id="49365"></span><div id="comment-49365" class="comment"><div id="post-49365-score" class="comment-score">1</div><div class="comment-text"><p><span>@KamaL</span>, just to add some extra info to <span>@Jaap</span>'s answer: I feel you observe the world using Windows user optics which makes you believe that the file name suffix (.txt, .pcap) determines the format (internal structure) of the file contents.</p><p>In fact, the file name suffix only tells the operating system shell which application to use to open the file when the user double-clicks that file. If you open the application first, you may tell it to open a file with any suffix. In both cases, it is a separate matter whether the application will <em>understand</em> the file format and whether it will <em>recognize</em> it.</p><p>Specifically Wireshark ignores the file name suffix and only looks at internal headers of the file to determine its format; other applications may look at the suffix but this can often be overridden manually (Open as...).</p><p>If you open a file with .pcap suffix in Wireshark and then save it under the same name except that you change the .pcap suffix of the name to .txt suffix, the format of the new file remains the same as that of the original file, unless you change it using the <code>save as type:</code> selector. One of the formats supported is "K12 text", but it differs from the hex dump which Wireshark can import, and Wireshark can "open" it directly, i.e. no need to "import" because its structure is fixed and known.</p><p>To "import", you usually need to provide some details about the format.</p></div><div id="comment-49365-info" class="comment-info"><span class="comment-age">(19 Jan '16, 04:22)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49362" class="comment-tools"></div><div class="clear"></div><div id="comment-49362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

