+++
type = "question"
title = "[Malformed Packet: GSM over IP]"
description = '''Hi, I&#x27;m new to WireShark but I have a Windows host with WireShark running and on this host a customised application sending data to another host on port 5000. I can filter the data and use Follow TCP Stream fine and see the applications network data. However the frames are displayed as [Malformed Pa...'''
date = "2011-01-31T04:07:00Z"
lastmod = "2014-11-13T07:56:00Z"
weight = 2030
keywords = [ "ip", "over", "gsm", "packet", "malformed" ]
aliases = [ "/questions/2030" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[Malformed Packet: GSM over IP\]](/questions/2030/malformed-packet-gsm-over-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2030-score" class="post-score" title="current number of votes">0</div><span id="post-2030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm new to WireShark but I have a Windows host with WireShark running and on this host a customised application sending data to another host on port 5000. I can filter the data and use Follow TCP Stream fine and see the applications network data.</p><p>However the frames are displayed as</p><p>[Malformed Packet: GSM over IP]</p><p>I assume that WireShark is inspecting the frame data and that WireShark thinks that the data inside is a GSM over IP formatted data while it isn't.</p><p>Anyway to 'disable' this misleading matching to GSM over IP?</p><p>Any help would be greatly appreciated!</p><p>Bernd</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-over" rel="tag" title="see questions tagged &#39;over&#39;">over</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '11, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/6898c713ecbd5065535f642ffe15f1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BerndN&#39;s gravatar image" /><p><span>BerndN</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BerndN has no accepted answers">0%</span></p></div></div><div id="comments-container-2030" class="comments-container"><span id="2035"></span><div id="comment-2035" class="comment"><div id="post-2035-score" class="comment-score"></div><div class="comment-text"><p>I see this protocols:</p><p>GSM SMS GSM SMS UD GSM Um GSM_MAP</p><p>Windows Version 1.4.3 from WireShark So thanks for the tip. Somehow I have thought the same before but because I could not find it easily I was confused and thought better to post this here ;)</p></div><div id="comment-2035-info" class="comment-info"><span class="comment-age">(31 Jan '11, 04:39)</span> <span class="comment-user userinfo">BerndN</span></div></div><span id="2048"></span><div id="comment-2048" class="comment"><div id="post-2048-score" class="comment-score"></div><div class="comment-text"><p>Just one more question regarding those frames/packets. I have done some binary editing of old files in Windows. I had files which had a length value after the initial header so that the opening program did know how long the file had to be. But most files had different structures/data structures. I assume that with network packets a lot is also depending on the application creating it. The packets which have been identified by the dissector GSM over IP seems to assume that it finds a checksum at offset 0xnn and that this checksum value should be nnnn instead of 00 00. My understanding is that the header seems similiar to a GSM over IP packet but it is no GSM over IP structure. So to permanently fix it I should write my own, custom dissector?</p><p>Thanks for reading and trying to help!</p><p>Bernd</p></div><div id="comment-2048-info" class="comment-info"><span class="comment-age">(31 Jan '11, 13:02)</span> <span class="comment-user userinfo">BerndN</span></div></div></div><div id="comment-tools-2030" class="comment-tools"></div><div class="clear"></div><div id="comment-2030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2033"></span>

<div id="answer-container-2033" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2033-score" class="post-score" title="current number of votes">2</div><span id="post-2033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Goto the menu Analyze|Protocols. This open a dialog with all protocol dissectors. Look for 'GSM over IP' and remove the check mark. Click apply to see what happens.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2033" class="comments-container"><span id="2036"></span><div id="comment-2036" class="comment"><div id="post-2036-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap. Doing this change it and all looks fine after it. Are those messages/frames/packets now hidden or have they just changed to 'unnamed' data frames/packets?</p></div><div id="comment-2036-info" class="comment-info"><span class="comment-age">(31 Jan '11, 04:48)</span> <span class="comment-user userinfo">BerndN</span></div></div><span id="2045"></span><div id="comment-2045" class="comment"><div id="post-2045-score" class="comment-score"></div><div class="comment-text"><p>No, the Wireshark 'GSM over IP' dissectors just isn't called any more. it now depends on the other dissectors what does happen.</p></div><div id="comment-2045-info" class="comment-info"><span class="comment-age">(31 Jan '11, 12:44)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="37826"></span><div id="comment-37826" class="comment"><div id="post-37826-score" class="comment-score"></div><div class="comment-text"><p>Worked for me</p></div><div id="comment-37826-info" class="comment-info"><span class="comment-age">(13 Nov '14, 07:56)</span> <span class="comment-user userinfo">4m1r</span></div></div></div><div id="comment-tools-2033" class="comment-tools"></div><div class="clear"></div><div id="comment-2033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2032"></span>

<div id="answer-container-2032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2032-score" class="post-score" title="current number of votes">0</div><span id="post-2032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Edit-&gt;preferences-&gt;protocols-&gt;GSM over IP change the TC/UDP ports to 0 or dissable the protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '11, 04:31</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-2032" class="comments-container"></div><div id="comment-tools-2032" class="comment-tools"></div><div class="clear"></div><div id="comment-2032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

