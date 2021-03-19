+++
type = "question"
title = "tshark -T fields output same info and format as -T text -x"
description = '''Hello, I am trying to write a script that will remove duplicate packets (layer 3 and above) by comparing the data in two consecutive packets (or along a sliding window) and if they are identical, it will throw out the duplicates. The packets are not 100% duplicates since the MACs and TTLs are differ...'''
date = "2013-03-12T08:08:00Z"
lastmod = "2013-03-12T08:13:00Z"
weight = 19388
keywords = [ "duplicates", "fields", "frame", "tshark", "text" ]
aliases = [ "/questions/19388" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -T fields output same info and format as -T text -x](/questions/19388/tshark-t-fields-output-same-info-and-format-as-t-text-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19388-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to write a script that will remove duplicate packets (layer 3 and above) by comparing the data in two consecutive packets (or along a sliding window) and if they are identical, it will throw out the duplicates. The packets are not 100% duplicates since the MACs and TTLs are different, but from layer 3 and above they are identical. Therefore, editcap -d won't work, as it requires the MD5 hash to be the same.</p><p>The way I would like to do this is to output the data like this:</p><p><code>Mar  5, 2013 19:34:39.738281000 0000  00 15 f1 9c f8 00 00 01 fc 0d 68 c0 81 00 0c 90   ..........h..... 0010  08 10 46 a0 04 62 00 00 00 00 6e 11 05 c5 ac 10   ..E..c....~..... 0020  57 c6 ac 10 82 3e 13 c4 1a 0a 04 4f de 41 52 45   W....&gt;.....O.ARE 0030  47 49 53 54 45 52 20 73 69 70 3a 66 61 70 2e 61   GISTER sip:data. ... 0460  36 2e 31 43 30 2e 36 32 3a 37 36 22 36 3b 6c 63   6.120.62:3626;fd 0470  3e 0d 0a 0d 0a                                    &gt;....</code></p><p>Then I can use a script to check the data for duplicates and use the timestamp at the beginning of the packet to read it back into a pcap file.</p><p>The command below summarizes what I have so far. What I need is the <code>MAGIC_FIELDS_THAT_WORK_LIKE_-Ttext_-x</code> part. The fields should give the offset, hex output in the middle like the above example, and ascii output on the right like the above example.</p><p><code>$ tshark -r $input_file -T fields -e frame.time -e MAGIC_FIELDS_THAT_WORK_LIKE_-Ttext_-x | awk -f remove_duplicates.awk | text2pcap -t "%b  %d, %Y %H:%M:%S." -q - $output_file</code></p><p>Please note that the -t argument to text2pcap didn't actually work for me. I had to reformat the time a little before it worked. Also, I realize that the packets aren't 100% identical, since the layer 2 information is changed with different MAC's and TTL's. But I want to look only at layer 3 and above for my filtering.</p><p>Thanks for any help you can provide!</p></div><div id="question-tags" class="tags-container tags">duplicates fields frame tshark text</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/e96b0196e8e968b1a2d8f6ddfda87ab1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lemurshark&#39;s gravatar image" /><p>Lemurshark<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lemurshark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '13, 09:03</p></div></div><div id="comments-container-19388" class="comments-container"></div><div id="comment-tools-19388" class="comment-tools"></div><div class="clear"></div><div id="comment-19388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19389"></span>

<div id="answer-container-19389" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19389-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does editcap with the -d option (along with the -D and -w options that set the frame window and time window for dups respectively) not meet your needs? Editcap should be installed along with Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19389" class="comments-container"><span id="19390"></span><div id="comment-19390" class="comment"><div id="post-19390-score" class="comment-score"></div><div class="comment-text"><p>I believe that editcap with -d requires 100% duplicate packets, down to layer 2 even. What I'm capturing is (for instance) a packet coming into a node and the same packet getting forwarded on to another node. So the packet data and layer 3 and above is the same, but the MACs are different and the TTL is different, which I think threw off editcap earlier. I'm also often capturing the same packets on different nodes and merging those capture files together. Again in that case the layer 3 and above is the same, but layer 2 is different.</p></div><div id="comment-19390-info" class="comment-info"><span class="comment-age">(12 Mar '13, 08:27)</span> Lemurshark</div></div><span id="19391"></span><div id="comment-19391" class="comment"><div id="post-19391-score" class="comment-score"></div><div class="comment-text"><p>Ok. I failed on reading comprehension of your question.</p></div><div id="comment-19391-info" class="comment-info"><span class="comment-age">(12 Mar '13, 09:00)</span> grahamb ♦</div></div><span id="19392"></span><div id="comment-19392" class="comment"><div id="post-19392-score" class="comment-score"></div><div class="comment-text"><p>I updated the text of the original post to reflect the nature of the duplicate packets. Thanks for your suggestion</p></div><div id="comment-19392-info" class="comment-info"><span class="comment-age">(12 Mar '13, 09:00)</span> Lemurshark</div></div></div><div id="comment-tools-19389" class="comment-tools"></div><div class="clear"></div><div id="comment-19389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

