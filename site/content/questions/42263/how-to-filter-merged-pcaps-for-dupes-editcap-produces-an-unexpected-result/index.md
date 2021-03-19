+++
type = "question"
title = "How to filter merged pcaps for dupes? editcap produces an unexpected result."
description = '''The pcaps were merged with the default &quot;Packets from the input files are merged in chronological order based on each frame&#x27;s timestamp&quot;. There is also the &quot;Mergecap assumes that frames within a single capture file are already stored in chronological order&quot; which may be part of the problem, I&#x27;m just ...'''
date = "2015-05-09T11:41:00Z"
lastmod = "2015-05-11T02:53:00Z"
weight = 42263
keywords = [ "packetloss", "pcap", "editcap", "mergecap", "wifi" ]
aliases = [ "/questions/42263" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter merged pcaps for dupes? editcap produces an unexpected result.](/questions/42263/how-to-filter-merged-pcaps-for-dupes-editcap-produces-an-unexpected-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42263-score" class="post-score" title="current number of votes">0</div><span id="post-42263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The pcaps were merged with the default "Packets from the input files are merged in chronological order based on each frame's timestamp". There is also the "Mergecap assumes that frames within a single capture file are already stored in chronological order" which may be part of the problem, I'm just not sure.</p><p>2 pcaps were captured using airodump simultaneously on 2 separate wifi cards plugged into the same laptop seperated by several meters. This was done to minimize packet loss which seems to always exist for me.</p><p>I used mergecap to merge them.</p><p>Now I'm attempting to remove the duplicate packets that they both have in common.</p><p>But I potentially have a problem here. The editcap -D values all produce different dupe counts. For example the difference between D 5 and D 10 was over 10% (I'm hesitant to commit to a figure from memory, could have been over 20%). But D 15 and D 20 was ~1%.</p><p>So now I need to know whether or not it's normal for APs and clients to produce a lot of dupes? Would removing them be fine or could it corrupt some data?</p><p>I think wifi packets have sequence numbers, is editcap using them? Can it be forced to use only them and then use -D [sequence_max] ?</p><p>Some help would be appreciated. Maybe someone knows a better method to do this altogether.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-editcap" rel="tag" title="see questions tagged &#39;editcap&#39;">editcap</span> <span class="post-tag tag-link-mergecap" rel="tag" title="see questions tagged &#39;mergecap&#39;">mergecap</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '15, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/07f67ca3626cbb5b062aa038958aed1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dingrite&#39;s gravatar image" /><p><span>dingrite</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dingrite has no accepted answers">0%</span></p></div></div><div id="comments-container-42263" class="comments-container"></div><div id="comment-tools-42263" class="comment-tools"></div><div class="clear"></div><div id="comment-42263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42273"></span>

<div id="answer-container-42273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42273-score" class="post-score" title="current number of votes">0</div><span id="post-42273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>editcap doesn't look into packets when deduping, it simply calculates MD5 hashes over the full frame content and compares them to previous hashes.</p><p>-D tells editcap how far it has to look into the past, so -D 10 means compare the current hash to the last 10 hashes (default is 5). Usually, higher values result in more frames being removed because the chance of finding a match in the past is higher. But at some point you'll get all matches, so increasing the -D parameter makes no difference anymore.</p><p>Lets look at an example:</p><pre><code>Frame  1: 000FF9E667DE540E52C917D4D5D4B38C
Frame  2: 0062A32CE6D7B9273A7E0E2D96DC71D3
Frame  3: 000FF9E667DE540E52C917D4D5D4B38C
Frame  4: 0B3812725B8E3182EE027B5F5D90ADB0
Frame  5: 017D189BDAB9C46AE4A3FE8C85C02133
Frame  6: 0C1303358A2A7926E3D27F716297042C
Frame  7: 1040E6AC7B0CA4365FB9089BD3EBE635
Frame  8: 111731B71DEC7FF17347BE6D1FC20AA1
Frame  9: 000FF9E667DE540E52C917D4D5D4B38C
Frame 10: 12CD165F1171BB76368CFAC7FED4E276</code></pre><p>Frames 1, 3 and 9 have the same hash (= are identical). With the default history window of 5 you'll have 1 duplicate found (frame 3) because when the hash of frame 3 is calculated, frame 1 is still in the history. Frame 9 will <strong>not</strong> be removed, because the oldest frame hash in the history window will be frame 4, so no match is found.</p><p>If you increase -D to 10 frames, both duplicates are found and removed. If you set -D to 15 frames, you'll still only get 2 duplicates, so increasing the parameter further doesn't do anything to the result.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '15, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42273" class="comments-container"><span id="42282"></span><div id="comment-42282" class="comment"><div id="post-42282-score" class="comment-score"></div><div class="comment-text"><p>then how could I eliminate dupes in wifi captures? If editcap can't do it, what can?</p></div><div id="comment-42282-info" class="comment-info"><span class="comment-age">(10 May '15, 12:26)</span> <span class="comment-user userinfo">dingrite</span></div></div><span id="42284"></span><div id="comment-42284" class="comment"><div id="post-42284-score" class="comment-score"></div><div class="comment-text"><p>Depends on how your dupes look. I have no capture file that has this kind of problem, so I don't know what to look for.</p></div><div id="comment-42284-info" class="comment-info"><span class="comment-age">(10 May '15, 14:49)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42285"></span><div id="comment-42285" class="comment"><div id="post-42285-score" class="comment-score"></div><div class="comment-text"><p>Wifi packets should have a sequence number that goes up to 4095. Why doesn't it ensure unique hashes for every packet? And I get a different count of dupes even when I go from -D 15 to -D 20. And I'm pretty sure that even when one card misses some packets the timeframes are so small they are at most 1-10 packets apart.</p></div><div id="comment-42285-info" class="comment-info"><span class="comment-age">(10 May '15, 15:04)</span> <span class="comment-user userinfo">dingrite</span></div></div><span id="42296"></span><div id="comment-42296" class="comment"><div id="post-42296-score" class="comment-score"></div><div class="comment-text"><p>Then probably the frames are not exact byte-by-byte duplicates, otherwise editcap should be able to find them.</p></div><div id="comment-42296-info" class="comment-info"><span class="comment-age">(11 May '15, 02:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-42273" class="comment-tools"></div><div class="clear"></div><div id="comment-42273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

