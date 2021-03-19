+++
type = "question"
title = "File transfer over the Internet - TCP RST packet"
description = '''Hi everyone, Having this issue with file transfer and thought you might help on this issue. There is a software installed on client and server used for backups of data files everyday over the Internet.  This software on client side first reads the folders (fetch files) before it starts to transfer t...'''
date = "2017-09-18T04:05:00Z"
lastmod = "2017-09-25T13:58:00Z"
weight = 63602
keywords = [ "tcp" ]
aliases = [ "/questions/63602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [File transfer over the Internet - TCP RST packet](/questions/63602/file-transfer-over-the-internet-tcp-rst-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63602-score" class="post-score" title="current number of votes">0</div><span id="post-63602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, Having this issue with file transfer and thought you might help on this issue. There is a software installed on client and server used for backups of data files everyday over the Internet. This software on client side first reads the folders (fetch files) before it starts to transfer the files to the server on the other side. The issue is that if I select the MAIN folder for back up (hundreds of GB in size), it starts reading/fetching the files but when this completes, the transfer doesn't even start however if I select any sub-folder (e.g. 45 GB) inside the MAIN folder, the transfer completes fine.</p><p>This setup over the Internet used to work a month ago, and if tested on LAN it works fine. I've captured the traffic on both sides and I'm attaching the pics for the relevant part. I've checked the TTL on RST packets but it was 120 which tells it is routed packet.</p><p>Below are the TCP streams from c2s and s2c.</p><p>Note: there is a firewall in between, but I don't think it's the issue since transfer is working fine for smaller file size.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/s2c_wireshark_gCqdzjN.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/c2s_wireshark_LeQmHxo.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '17, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/dcc35d073c1104aa8b1a8e2e9ca23dfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws101&#39;s gravatar image" /><p><span>ws101</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws101 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63602" class="comments-container"></div><div id="comment-tools-63602" class="comment-tools"></div><div class="clear"></div><div id="comment-63602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63603"></span>

<div id="answer-container-63603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63603-score" class="post-score" title="current number of votes">1</div><span id="post-63603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The c2s shows retransmits for a 1514 bytes packet (TCP Length=1460) for 192.168.0.250 -&gt; 84.22.37.252. Therefore I guess it is a MTU issue.</p><p>Things to check:</p><ul><li>Is ICMP need frag blocked on the path?</li><li>Can you change the MTU of 192.168.0.250?</li><li>Where on the path is the "big" packet blocked?</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '17, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></img></div></div><div id="comments-container-63603" class="comments-container"><span id="63604"></span><div id="comment-63604" class="comment"><div id="post-63604-score" class="comment-score"></div><div class="comment-text"><p>If MTU was an issue, wouldn't the MSS be &lt; than 1460 in the SYN/ACK packet on negotiation?</p></div><div id="comment-63604-info" class="comment-info"><span class="comment-age">(19 Sep '17, 06:24)</span> <span class="comment-user userinfo">ws101</span></div></div><span id="63606"></span><div id="comment-63606" class="comment"><div id="post-63606-score" class="comment-score"></div><div class="comment-text"><p>Not necessarily. You've said that you have "backups of data files over the Internet". MSS in he SYN/ACK packet is defined by endpoints, and they are not aware of MTUs throughout all Internet data path. Initially endpoint is aware only of it's own connected interface MTU.</p></div><div id="comment-63606-info" class="comment-info"><span class="comment-age">(19 Sep '17, 07:56)</span> <span class="comment-user userinfo">Packet_vlad</span></div></div><span id="63614"></span><div id="comment-63614" class="comment"><div id="post-63614-score" class="comment-score"></div><div class="comment-text"><p>It's strange how transfer works fine for tens of GB and not for hundreds of GB?!</p></div><div id="comment-63614-info" class="comment-info"><span class="comment-age">(19 Sep '17, 13:33)</span> <span class="comment-user userinfo">ws101</span></div></div><span id="63615"></span><div id="comment-63615" class="comment"><div id="post-63615-score" class="comment-score"></div><div class="comment-text"><p>Could be possible that with the "small" transfer there are no packets with 1500 Bytes packets. Or the path is different.</p><p>To work around this issue you can try to reduce the MSS on 84.22.37.252.</p></div><div id="comment-63615-info" class="comment-info"><span class="comment-age">(20 Sep '17, 03:00)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="63640"></span><div id="comment-63640" class="comment not_top_scorer"><div id="post-63640-score" class="comment-score"></div><div class="comment-text"><p>Bypassed the FW and it worked!!</p></div><div id="comment-63640-info" class="comment-info"><span class="comment-age">(25 Sep '17, 01:14)</span> <span class="comment-user userinfo">ws101</span></div></div><span id="63641"></span><div id="comment-63641" class="comment"><div id="post-63641-score" class="comment-score">1</div><div class="comment-text"><p>"Bypassing the FW" doesn't sound like a good (=secure) solution ;-)</p></div><div id="comment-63641-info" class="comment-info"><span class="comment-age">(25 Sep '17, 07:00)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="63642"></span><div id="comment-63642" class="comment not_top_scorer"><div id="post-63642-score" class="comment-score"></div><div class="comment-text"><p>It's a test to isolate the issue.</p></div><div id="comment-63642-info" class="comment-info"><span class="comment-age">(25 Sep '17, 07:14)</span> <span class="comment-user userinfo">ws101</span></div></div><span id="63644"></span><div id="comment-63644" class="comment not_top_scorer"><div id="post-63644-score" class="comment-score"></div><div class="comment-text"><p>Alright, that's what I hoped to hear.</p></div><div id="comment-63644-info" class="comment-info"><span class="comment-age">(25 Sep '17, 13:58)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-63603" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-63603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

