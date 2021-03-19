+++
type = "question"
title = "Understanding offset values  settings icmp fragementation"
description = '''Hello, A certain wireshark sample for icmp fragmentation (attached) is showing following :-   fragment offset: 13bits   offset value ordering as :-  0  1480  2960    length 1518.   From , theory I know usual 8 bytes of offset field will start calculating offset from 0, then for 1400 bytes of data (m...'''
date = "2015-08-28T00:58:00Z"
lastmod = "2015-09-19T11:07:00Z"
weight = 45438
keywords = [ "fragmentation", "icmp" ]
aliases = [ "/questions/45438" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Understanding offset values settings icmp fragementation](/questions/45438/understanding-offset-values-settings-icmp-fragementation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45438-score" class="post-score" title="current number of votes">0</div><span id="post-45438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>A certain wireshark sample for icmp fragmentation (attached) is showing following :-</p><ul><li><p>fragment offset: 13bits</p></li><li><p>offset value ordering as :-</p><pre><code> 0
 1480
 2960</code></pre></li><li><p>length 1518.</p></li></ul><p>From , theory I know usual 8 bytes of offset field will start calculating offset from 0, then for 1400 bytes of data (minus the headers) next value be 1400/8. If I apply same concept to attached pcap It doesn't add up. Why offset values so different even when considering 1500 bytes of data.</p><p>Thanks.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/snip_icmp.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '15, 00:58</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p><span>lazerz</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '15, 01:54</strong> </span></p></div></div><div id="comments-container-45438" class="comments-container"></div><div id="comment-tools-45438" class="comment-tools"></div><div class="clear"></div><div id="comment-45438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45964"></span>

<div id="answer-container-45964" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45964-score" class="post-score" title="current number of votes">1</div><span id="post-45964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lazerz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><span><span>@Pascal Quantin</span></span> explained it correctly. The original ping packet has 5,608 bytes of data. It gets fragmented into four packets of 1480, 1480, 1480, and 1168 bytes. These four packets have offsets of 0, 1480, 2920, and 4440. What's stored in the Fragment Offset field of each IP packet is the offset as the number of 8-byte blocks; in other words, the actual offset divided by 8, so for the four packets, the Fragment Offset fields contain 0, 185, 370, and 555. In the Packet Details pane, Wireshark multiplies the number in the Fragment Offset field by 8 to show us the actual offset in bytes, rather than the number of 8-byte blocks.</p><p><strong>Fragment Offset field / Wireshark Display:</strong></p><p>0 / 0</p><p>185 / 1480</p><p>370 / 2960</p><p>555 / 4440</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '15, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '15, 11:08</strong> </span></p></div></div><div id="comments-container-45964" class="comments-container"></div><div id="comment-tools-45964" class="comment-tools"></div><div class="clear"></div><div id="comment-45964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45439"></span>

<div id="answer-container-45439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45439-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45439-score" class="post-score" title="current number of votes">0</div><span id="post-45439-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Each fragment do not have a hardcoded size of 1400 bytes, but the (total length - header length) bytes as indicated in the IPv4 header. See this <a href="https://en.wikipedia.org/wiki/IPv4#Fragmentation_and_reassembly">link</a> for more details.</p><p>According to the capture you posted to <a href="https://www.wireshark.org/lists/wireshark-users/201508/msg00019.html">Wireshark user mailing list</a>, the IPv4 payload data is 1480 bytes long so the fragmentation perfectly makes sense.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '15, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-45439" class="comments-container"><span id="45440"></span><div id="comment-45440" class="comment"><div id="post-45440-score" class="comment-score"></div><div class="comment-text"><p>Thanks for analysis. However, my original query still remains unanswered which was how these offset values are calc in first place. For for 1480 bytes of data the first offset value taking 8bytes should be 185. If yes why is same not represented in screen-shot shown. Thanks</p></div><div id="comment-45440-info" class="comment-info"><span class="comment-age">(28 Aug '15, 01:55)</span> <span class="comment-user userinfo">lazerz</span></div></div><span id="45443"></span><div id="comment-45443" class="comment"><div id="post-45443-score" class="comment-score"></div><div class="comment-text"><p>OK the initial question was not clear to me.</p><p>Wireshark is displaying the offset as bytes, and not as 8-bytes blocks, as seen in the source code <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ip.c;h=11673c43abfbbb1842866ee7cee54b70efe97a13;hb=refs/heads/master">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ip.c;h=11673c43abfbbb1842866ee7cee54b70efe97a13;hb=refs/heads/master</a></p></div><div id="comment-45443-info" class="comment-info"><span class="comment-age">(28 Aug '15, 02:31)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="45545"></span><div id="comment-45545" class="comment"><div id="post-45545-score" class="comment-score"></div><div class="comment-text"><p>thanks but I believe it doesn't ans the problem.</p></div><div id="comment-45545-info" class="comment-info"><span class="comment-age">(31 Aug '15, 02:04)</span> <span class="comment-user userinfo">lazerz</span></div></div><span id="45552"></span><div id="comment-45552" class="comment"><div id="post-45552-score" class="comment-score"></div><div class="comment-text"><p>What is your problem then?</p></div><div id="comment-45552-info" class="comment-info"><span class="comment-age">(31 Aug '15, 12:52)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="45960"></span><div id="comment-45960" class="comment"><div id="post-45960-score" class="comment-score"></div><div class="comment-text"><p>From frame 3-5 how are offset values calc? (see pic above in question)</p></div><div id="comment-45960-info" class="comment-info"><span class="comment-age">(19 Sep '15, 03:41)</span> <span class="comment-user userinfo">lazerz</span></div></div><span id="45963"></span><div id="comment-45963" class="comment not_top_scorer"><div id="post-45963-score" class="comment-score"></div><div class="comment-text"><p>Again, the offset is given in the IP header and in the info column Wireshark converts it from 8 bytes unit offset to an offset in bytes.</p></div><div id="comment-45963-info" class="comment-info"><span class="comment-age">(19 Sep '15, 09:43)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-45439" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-45439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

