+++
type = "question"
title = "Searching for a Packet Sequence"
description = '''Is there an efficient way in Wireshark to search for a particular packet sequence in a capture file? For example, I want to search for a sequence of three consecutive packets, where: packet 1 is a first particular type of packet, packet 2 is a second particular type of packet, and packet 3 is a thir...'''
date = "2012-05-31T08:57:00Z"
lastmod = "2012-05-31T10:30:00Z"
weight = 11490
keywords = [ "packetsearch", "packetsequence" ]
aliases = [ "/questions/11490" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Searching for a Packet Sequence](/questions/11490/searching-for-a-packet-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11490-score" class="post-score" title="current number of votes">0</div><span id="post-11490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there an efficient way in Wireshark to search for a particular packet sequence in a capture file? For example, I want to search for a sequence of three consecutive packets, where: packet 1 is a first particular type of packet, packet 2 is a second particular type of packet, and packet 3 is a third particular type of packet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetsearch" rel="tag" title="see questions tagged &#39;packetsearch&#39;">packetsearch</span> <span class="post-tag tag-link-packetsequence" rel="tag" title="see questions tagged &#39;packetsequence&#39;">packetsequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '12, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/9bacdaf55a95f9cbe8f22bb66092859b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kali&#39;s gravatar image" /><p><span>Kali</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kali has no accepted answers">0%</span></p></div></div><div id="comments-container-11490" class="comments-container"></div><div id="comment-tools-11490" class="comment-tools"></div><div class="clear"></div><div id="comment-11490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11491"></span>

<div id="answer-container-11491" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11491-score" class="post-score" title="current number of votes">0</div><span id="post-11491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kali has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot search for a "sequence", but you can combine display filters with <strong>or</strong> to get almost the same result.</p><blockquote><p><code>dns.qry.name contains "facebook.com" or (http.request and http.host contains "facebook.com") or (icmp and ip.addr eq 69.171.242.11)</code><br />
</p></blockquote><p>This will show:</p><ol><li>the dns request to *.<a href="http://facebook.com">facebook.com</a></li><li>then the HTTP Request to that site</li><li>and then a ping to one IP address of facbook</li></ol><p>That's the only way of doing it, without Lua. If you tell us a bit more about your usecase (pattern to match), we might be able to give more detailed "instructions".</p><p>With Lua, you can create a Listener and look for whatever criteria you are interested. However that requires programming skills or somebody to do it for you.</p><blockquote><p><code>http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '12, 09:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '12, 09:34</strong> </span></p></div></div><div id="comments-container-11491" class="comments-container"><span id="11494"></span><div id="comment-11494" class="comment"><div id="post-11494-score" class="comment-score"></div><div class="comment-text"><p>Thanks much for the response, Kurt. Maybe Lua is the answer. In particular, I am looking for an efficient way to search a huge wlan capture file for the following packet sequence: 1) Beacon packet with non-zero TIM; 2) Null Function packet with PM bit clear; 3) ACK; 4) Data packet; 5) ACK.</p></div><div id="comment-11494-info" class="comment-info"><span class="comment-age">(31 May '12, 10:16)</span> <span class="comment-user userinfo">Kali</span></div></div><span id="11497"></span><div id="comment-11497" class="comment"><div id="post-11497-score" class="comment-score"></div><div class="comment-text"><p>O.K. is one criteria the order of the packets, meaning: do they have to appear in the order to be a valid match? If so, Lua is one way to do it. However, it requires some programming skills to write that script. Another way would be tshark with a display filter that matches all of those conditions (like my facebook example) and some script (Perl, bash, ) to filter out only those packets that appear in the defined order.</p></div><div id="comment-11497-info" class="comment-info"><span class="comment-age">(31 May '12, 10:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-11491" class="comment-tools"></div><div class="clear"></div><div id="comment-11491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

