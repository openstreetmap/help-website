+++
type = "question"
title = "saving packets in wireshark"
description = '''I want to know when wireshark saves WIRELESS packet, it captured using various format( pcap/libpcap )...  what it saves exactly complete packet (header and payload ) ?  Suppose wireshark captured 1000 wireless packets ( n if we stopped capturing after this 1000 packets )then  Is all this packets wil...'''
date = "2014-02-08T12:13:00Z"
lastmod = "2014-02-10T03:16:00Z"
weight = 29556
keywords = [ "pcap", "intrusion", "libpcap", "wireshark" ]
aliases = [ "/questions/29556" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [saving packets in wireshark](/questions/29556/saving-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29556-score" class="post-score" title="current number of votes">0</div><span id="post-29556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to know when wireshark saves WIRELESS packet, it captured using various format( pcap/libpcap )... what it saves exactly complete packet (header and payload ) ? Suppose wireshark captured 1000 wireless packets ( n if we stopped capturing after this 1000 packets )then Is all this packets will be put in one single pcap file ? if it is like that how to retrieve each packet and its contain (at least header information ) ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-intrusion" rel="tag" title="see questions tagged &#39;intrusion&#39;">intrusion</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '14, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/4f2e12b298828a7bdd200478480606da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WIDS&#39;s gravatar image" /><p><span>WIDS</span><br />
<span class="score" title="25 reputation points">25</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WIDS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Feb '14, 20:13</strong> </span></p></div></div><div id="comments-container-29556" class="comments-container"></div><div id="comment-tools-29556" class="comment-tools"></div><div class="clear"></div><div id="comment-29556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29572"></span>

<div id="answer-container-29572" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29572-score" class="post-score" title="current number of votes">1</div><span id="post-29572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="WIDS has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When Wireshark captures packets (well, actually dumpcap does that for Wireshark) it stores the frame bytes with a frame header. The frame bytes are the actual content of the whole frame, while the frame header contains meta information like the size of the frame, the time it was captured, and other details.</p><p>If you capture 1000 wireless packets you'll get a file with one file header, 1000 frame headers, and 1000 frame byte sections, in a format like FileHeader - FrameHeader1 - FrameBytes1 - FrameHeader2 - FrameBytes2 - FrameHeader3 - FrameBytes3... and so on. At least if you're using pcap as a format. Other file formats vary and have additional information stored in them, e.g. pcap-ng.</p><p>If you want to retrieve each packet outside of Wireshark you need a library or routine that opens the file and reads the file structure (which, for pcap, is documented <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">here</a>). Keep in mind that later versions of Wireshark use the pcap-ng format, which you can find <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '14, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29572" class="comments-container"><span id="29577"></span><div id="comment-29577" class="comment"><div id="post-29577-score" class="comment-score"></div><div class="comment-text"><p>thank you Jasper once again</p><p>What i want to do in my project</p><ol><li>sniff all WIRELESS (082.11 ) traffic using wireshark</li><li>Save above captured traffic in pcap format</li><li>use C or Java program to retrieve each Packet from each .pcap file ( READ from pcap file )</li><li>For each packet , extract information like IP addresses, port numbers etc from it`s header</li></ol><p>So any more guidance about step 3 and 4.......</p></div><div id="comment-29577-info" class="comment-info"><span class="comment-age">(09 Feb '14, 09:03)</span> <span class="comment-user userinfo">WIDS</span></div></div><span id="29578"></span><div id="comment-29578" class="comment"><div id="post-29578-score" class="comment-score"></div><div class="comment-text"><p>Can I copy selected packets (complete) from two more pcap file and write them in my own seprate pcap file ( if I set Glogal Header parameter to zero or proper value )</p></div><div id="comment-29578-info" class="comment-info"><span class="comment-age">(09 Feb '14, 09:37)</span> <span class="comment-user userinfo">WIDS</span></div></div><span id="29580"></span><div id="comment-29580" class="comment"><div id="post-29580-score" class="comment-score"></div><div class="comment-text"><ol><li>and 2. can be done with dumpcap.</li></ol><p>for 3. you could use the libpcap libraries, see <a href="http://www.tcpdump.org/">http://www.tcpdump.org/</a></p><p>With that you can do 4.</p></div><div id="comment-29580-info" class="comment-info"><span class="comment-age">(09 Feb '14, 11:36)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="29603"></span><div id="comment-29603" class="comment"><div id="post-29603-score" class="comment-score"></div><div class="comment-text"><p>Sir I am doing step 1 and 2 using wire shark then want to use my own program to read packets saved by wireshark</p></div><div id="comment-29603-info" class="comment-info"><span class="comment-age">(10 Feb '14, 02:20)</span> <span class="comment-user userinfo">WIDS</span></div></div><span id="29605"></span><div id="comment-29605" class="comment"><div id="post-29605-score" class="comment-score"></div><div class="comment-text"><p>Yes, that's why in step 3. I pointed you to the libpcap libraries that are documented at tcpdump.org. You can of course write your own packet reading library if you want, but if you don't mind existing libraries you might want to take a look at libpcap. As soon as you have libpcap included in your own program you can then read packets through that library.</p></div><div id="comment-29605-info" class="comment-info"><span class="comment-age">(10 Feb '14, 02:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="29611"></span><div id="comment-29611" class="comment not_top_scorer"><div id="post-29611-score" class="comment-score"></div><div class="comment-text"><p>Here is a list of some libraries for accessing pcap files: <a href="http://en.wikipedia.org/wiki/Pcap#Wrapper_libraries_for_libpcap.2FWinPcap">LINK</a>.</p></div><div id="comment-29611-info" class="comment-info"><span class="comment-age">(10 Feb '14, 03:16)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-29572" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-29572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

