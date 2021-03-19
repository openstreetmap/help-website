+++
type = "question"
title = "Is this a PCAP file?"
description = '''I received a file that&#x27;s suppose to be a pcap file. Previously, I was directed to http://wiki.wireshark.org/Development/LibpcapFileFormat and was told a PCAP file should begin with a magic number of 0xa1b2c3d4 (byte ordering issue noted). With this file, I don&#x27;t see that. It begins with 0a 0d 0d 0a ...'''
date = "2013-03-08T09:27:00Z"
lastmod = "2013-03-08T13:26:00Z"
weight = 19300
keywords = [ "header", "pcap", "format" ]
aliases = [ "/questions/19300" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is this a PCAP file?](/questions/19300/is-this-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19300-score" class="post-score" title="current number of votes">0</div><span id="post-19300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I received a file that's suppose to be a pcap file. Previously, I was directed to <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">http://wiki.wireshark.org/Development/LibpcapFileFormat</a> and was told a PCAP file should begin with a magic number of 0xa1b2c3d4 (byte ordering issue noted). With this file, I don't see that. It begins with 0a 0d 0d 0a and yet Wireshark has no trouble reading the file. Likewise, pcaputils.py fails and said it's an invalid tcpdump header neither. So, what's in this file and how should I detect the beginning of frame 1?</p><p>Here are the beginning of the file before frame 1 begins (embedded in these 296 bytes are the messages "64-bit Windows 7 Service Pack 1, build 7601" ... "Dumpcap 1.8.5 (SVN Rev 47350 from /trunk-1.8)" ... :</p><p>0a 0d 0d 0a 84 00 00 00 4d 3c 2b 1a 01 00 00 00</p><p>ff ff ff ff ff ff ff ff 03 00 2b 00 36 34 2d 62</p><p>69 74 20 57 69 6e 64 6f 77 73 20 37 20 53 65 72</p><p>76 69 63 65 20 50 61 63 6b 20 31 2c 20 62 75 69</p><p>6c 64 20 37 36 30 31 00 04 00 2d 00 44 75 6d 70</p><p>63 61 70 20 31 2e 38 2e 35 20 28 53 56 4e 20 52</p><p>65 76 20 34 37 33 35 30 20 66 72 6f 6d 20 2f 74</p><p>72 75 6e 6b 2d 31 2e 38 29 00 00 00 00 00 00 00</p><p>84 00 00 00 01 00 00 00 88 00 00 00 01 00 00 00</p><p>ff ff 00 00 02 00 32 00 5c 44 65 76 69 63 65 5c</p><p>4e 50 46 5f 7b 33 45 33 32 42 38 33 33 2d 43 32</p><p>34 38 2d 34 41 31 34 2d 42 37 32 45 2d 35 30 41</p><p>31 36 32 38 41 46 33 43 42 7d 00 00 09 00 01 00</p><p>06 00 00 00 0c 00 2b 00 36 34 2d 62 69 74 20 57</p><p>69 6e 64 6f 77 73 20 37 20 53 65 72 76 69 63 65</p><p>20 50 61 63 6b 20 31 2c 20 62 75 69 6c 64 20 37</p><p>36 30 31 00 00 00 00 00 88 00 00 00 06 00 00 00</p><p>f8 05 00 00 00 00 00 00 2c d6 04 00 5d 06 22 08</p><p>d6 05 00 00 d6 05 00 00</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '13, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/4025240b8c0475c260d9cb7529e827c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecs1749&#39;s gravatar image" /><p><span>ecs1749</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecs1749 has no accepted answers">0%</span></p></div></div><div id="comments-container-19300" class="comments-container"></div><div id="comment-tools-19300" class="comment-tools"></div><div class="clear"></div><div id="comment-19300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19301"></span>

<div id="answer-container-19301" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19301-score" class="post-score" title="current number of votes">2</div><span id="post-19301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ecs1749 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That appears to be a <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html#sectionshb">pcap-ng</a> file. You can check file formats within Wireshark via <em>Statistics→Summary</em> or by using <code>capinfos</code> on the command line. Recent versions of Wireshark save files as pcap-ng by default. If all the packets in the file have the same data link type (e.g. all Ethernet or all 802.11) you should be able to export the file as classic pcap if needed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-19301" class="comments-container"><span id="19314"></span><div id="comment-19314" class="comment"><div id="post-19314-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If all the packets in the file have the same data link type (e.g. all Ethernet or all 802.11) you should be able to export the file as classic pcap if needed.</p></blockquote><p>And if all the packets in the file have the same data link type, libpcap 1.1.0 and later should be able to read it the same way it can read pcap files. Unfortunately, there is no version of WinPcap based on libpcap 1.1.0 or later, and older versions of OSes that ship with libpcap might ship with pre-1.1.0 versions.</p></div><div id="comment-19314-info" class="comment-info"><span class="comment-age">(08 Mar '13, 13:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-19301" class="comment-tools"></div><div class="clear"></div><div id="comment-19301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19302"></span>

<div id="answer-container-19302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19302-score" class="post-score" title="current number of votes">1</div><span id="post-19302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use capinfos (should be alongside the Wireshark binary) to see what sort of file it is, e.g. <code>capinfos -t myoddcapture</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Mar '13, 09:36</strong> </span></p></div></div><div id="comments-container-19302" class="comments-container"></div><div id="comment-tools-19302" class="comment-tools"></div><div class="clear"></div><div id="comment-19302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

