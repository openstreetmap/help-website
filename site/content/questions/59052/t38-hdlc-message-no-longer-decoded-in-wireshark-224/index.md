+++
type = "question"
title = "T.38 HDLC message no longer decoded in Wireshark 2.2.4"
description = '''Wireshark 2.2.4 no longer reassembles the V.21 hdlc-data packets and decodes the message type like DIS, CFR, DCS, etc.  Also, if I have a .pcap file of T.38 packets only it shows UDP. When I do the &#x27;decode as&#x27; there is no longer a choice to select T.38. Anyone have a suggestion for a work around?'''
date = "2017-01-25T10:00:00Z"
lastmod = "2017-01-28T17:34:00Z"
weight = 59052
keywords = [ "t.38" ]
aliases = [ "/questions/59052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [T.38 HDLC message no longer decoded in Wireshark 2.2.4](/questions/59052/t38-hdlc-message-no-longer-decoded-in-wireshark-224)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59052-score" class="post-score" title="current number of votes">0</div><span id="post-59052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark 2.2.4 no longer reassembles the V.21 hdlc-data packets and decodes the message type like DIS, CFR, DCS, etc.<br />
</p><p>Also, if I have a .pcap file of T.38 packets only it shows UDP. When I do the 'decode as' there is no longer a choice to select T.38.</p><p>Anyone have a suggestion for a work around?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-t.38" rel="tag" title="see questions tagged &#39;t.38&#39;">t.38</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '17, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/7c8fc12d9d63cb54dd5be94fadf39d58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mr2872&#39;s gravatar image" /><p><span>mr2872</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mr2872 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-59052" class="comments-container"><span id="59059"></span><div id="comment-59059" class="comment"><div id="post-59059-score" class="comment-score"></div><div class="comment-text"><p>I don't have a capture file to work with, can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-59059-info" class="comment-info"><span class="comment-age">(25 Jan '17, 11:06)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="59062"></span><div id="comment-59062" class="comment"><div id="post-59062-score" class="comment-score"></div><div class="comment-text"><p>Here are 2 Google Drive links</p><p>T38a is the entire capture, the V.21 messages do not display</p><p>T38c is just the T.38 packets, the just show UDP and I can no longer do a 'decode as'</p><p><a href="https://drive.google.com/file/d/0B0Ilix_bf-c8bVEwU2pyakRJS2c/view?usp=sharing_eixpa_nl&amp;ts=5888fbda">https://drive.google.com/file/d/0B0Ilix_bf-c8bVEwU2pyakRJS2c/view?usp=sharing_eixpa_nl&amp;ts=5888fbda</a></p><p><a href="https://drive.google.com/file/d/0B0Ilix_bf-c8cURDZkxETjkyemM/view?usp=sharing_eixpa_nl&amp;ts=5888fbed">https://drive.google.com/file/d/0B0Ilix_bf-c8cURDZkxETjkyemM/view?usp=sharing_eixpa_nl&amp;ts=5888fbed</a></p></div><div id="comment-59062-info" class="comment-info"><span class="comment-age">(25 Jan '17, 12:16)</span> <span class="comment-user userinfo">mr2872</span></div></div><span id="59108"></span><div id="comment-59108" class="comment"><div id="post-59108-score" class="comment-score"></div><div class="comment-text"><p>Almost forgot, there is a third issue. On the page data for the fax data pump, packet 967 is the 'reassembled in packet'. Usually I click on 'message fragments' and 'export packet bytes' into a binary file where I can then use utility fax2tiff to view the page. There is no 'message fragments' in Wireshark 2.2.4 for this page data, but when I open the t38a.pcap in an archived version of Wireshark 1.x.x the 'message fragments' are there and I can export the 'packet bytes'.</p></div><div id="comment-59108-info" class="comment-info"><span class="comment-age">(27 Jan '17, 07:25)</span> <span class="comment-user userinfo">mr2872</span></div></div><span id="59125"></span><div id="comment-59125" class="comment"><div id="post-59125-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Wireshark 2.2.4 no longer reassembles the V.21 hdlc-data packets and decodes the message type like DIS, CFR, DCS, etc.</p></blockquote><p>When I try it with the version on the master branch, it <em>does</em> do reassembly, but what it's <em>not</em> doing is decoding the reassembled data. For example, frame 206 in the t38a capture decodes the "Reassembled T38" as T.30 in 1.12, but just shows it as data in the master branch version of Wireshark. Is that what you meant? (Presumably you meant T.30 rather than V.21 - V.21, "300 BITS PER SECOND DUPLEX MODEM STANDARDIZED FOR USE IN THE GENERAL SWITCHED TELEPHONE NETWORK" is all analog stuff; those modems didn't have to do much fancy stuff with anything HDLC-like.)</p></div><div id="comment-59125-info" class="comment-info"><span class="comment-age">(28 Jan '17, 17:34)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-59052" class="comment-tools"></div><div class="clear"></div><div id="comment-59052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59124"></span>

<div id="answer-container-59124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59124-score" class="post-score" title="current number of votes">1</div><span id="post-59124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>If</em> your first issue was that the reassembled data wasn't being decoded as T.30, for that issue:</p><p>The handoff from T.38 to T.30 was inadvertently broken in Wireshark 2.2; I've fixed it, so the next 2.2.x release should have it.</p><p>For your second issue, the lack of T.38 support in Decode As:</p><p>The ability to decode as T.38 was inadvertently removed in Wireshark 2.2; I've added it back, so the next 2.2.x release should have it.</p><p>For your third issue, the reassembled data not being available to save:</p><p>From looking at the capture, frame 399 contains the first chunk of data, with a sequence number of 154. Frame 400 contains the next chunk, with a sequence number of 155; this continues up to frame 435, with a sequence number of 190.</p><p>However, frame 401 has a sequence number of 208, not 191; there is no packet in the capture with a sequence number of 191.</p><p>I.e., not all the data is available - packets with sequence numbers of 191 through 207 are missing.</p><p>1.12 shouldn't have reassembled the packet, but it did do so, at least on the second pass; 2.2.x fixes that. 2.2.x should also be fixed to 1) indicate that the reassembly failed due to missing packets and 2) not say "Reassembled in:", because it <em>wasn't</em> reassembled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '17, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jan '17, 20:56</strong> </span></p></div></div><div id="comments-container-59124" class="comments-container"></div><div id="comment-tools-59124" class="comment-tools"></div><div class="clear"></div><div id="comment-59124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

