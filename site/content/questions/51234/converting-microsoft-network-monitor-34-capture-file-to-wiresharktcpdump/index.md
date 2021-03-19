+++
type = "question"
title = "converting Microsoft Network Monitor 3.4 capture file to &quot;wireshark/tcpdump&quot;"
description = '''Hi. I want to convert Microsoft Network Monitor 3.4 capture file to &quot;wireshark/tcpdump&quot; Wireshark reads the capture file but the &quot;save as&quot; is greyed out'''
date = "2016-03-28T08:50:00Z"
lastmod = "2016-03-29T23:54:00Z"
weight = 51234
keywords = [ "convert", "capture-file" ]
aliases = [ "/questions/51234" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [converting Microsoft Network Monitor 3.4 capture file to "wireshark/tcpdump"](/questions/51234/converting-microsoft-network-monitor-34-capture-file-to-wiresharktcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51234-score" class="post-score" title="current number of votes">0</div><span id="post-51234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I want to convert Microsoft Network Monitor 3.4 capture file to "wireshark/tcpdump"</p><p>Wireshark reads the capture file but the "save as" is greyed out</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-capture-file" rel="tag" title="see questions tagged &#39;capture-file&#39;">capture-file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '16, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/08f0927c223814704c76dad8fb4fdd94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mostafa%20Nafady&#39;s gravatar image" /><p><span>Mostafa Nafady</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mostafa Nafady has no accepted answers">0%</span></p></div></div><div id="comments-container-51234" class="comments-container"><span id="51246"></span><div id="comment-51246" class="comment"><div id="post-51246-score" class="comment-score"></div><div class="comment-text"><p>What type of network (Ethernet, Wi-Fi, etc.) was it captured on? Not all Network Monitor network types can be saved as pcap or pcapng files.</p></div><div id="comment-51246-info" class="comment-info"><span class="comment-age">(28 Mar '16, 19:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="51268"></span><div id="comment-51268" class="comment"><div id="post-51268-score" class="comment-score"></div><div class="comment-text"><p>wifi capture</p></div><div id="comment-51268-info" class="comment-info"><span class="comment-age">(29 Mar '16, 12:35)</span> <span class="comment-user userinfo">Mostafa Nafady</span></div></div></div><div id="comment-tools-51234" class="comment-tools"></div><div class="clear"></div><div id="comment-51234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51270"></span>

<div id="answer-container-51270" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51270-score" class="post-score" title="current number of votes">1</div><span id="post-51270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mostafa Nafady has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wi-Fi captures from Network Monitor cannot be converted to pcap or pcapng captures, because there's no link-layer header type value for use in pcap/pcapng captures that corresponds to the type of radio metadata provided in Network Monitor Wi-Fi captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '16, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51270" class="comments-container"><span id="51279"></span><div id="comment-51279" class="comment"><div id="post-51279-score" class="comment-score"></div><div class="comment-text"><p>Deleted my answer, WiFi capture wasn't there when I wrote it.</p></div><div id="comment-51279-info" class="comment-info"><span class="comment-age">(29 Mar '16, 23:54)</span> <span class="comment-user userinfo">DarrenWright</span></div></div></div><div id="comment-tools-51270" class="comment-tools"></div><div class="clear"></div><div id="comment-51270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

