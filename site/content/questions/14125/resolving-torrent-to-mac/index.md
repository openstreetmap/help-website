+++
type = "question"
title = "Resolving Torrent to MAC"
description = '''Having a bit of trouble finding a string I can use for tshark to get it to capture bittorrent traffic only, and include a mac address. Preferably it would be something like: [time] [MAC] [torrent hash] I got as far as: tshark tcp portrange 6881-6889 -i 3 -w cap -b filesize:4096 -b filenum:100 -T fie...'''
date = "2012-09-07T11:49:00Z"
lastmod = "2012-09-08T04:28:00Z"
weight = 14125
keywords = [ "capture.bittorrent" ]
aliases = [ "/questions/14125" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Resolving Torrent to MAC](/questions/14125/resolving-torrent-to-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14125-score" class="post-score" title="current number of votes">0</div><span id="post-14125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Having a bit of trouble finding a string I can use for tshark to get it to capture bittorrent traffic only, and include a mac address.</p><p>Preferably it would be something like:</p><p>[time] [MAC] [torrent hash]</p><p>I got as far as: tshark tcp portrange 6881-6889 -i 3 -w cap -b filesize:4096 -b filenum:100 -T fields -e eth.src</p><p>But there's several problems there, mainly the lack of the torrent hash and that tcp portrange 6881-6889 doesn't seem to reliably capture torrent traffic at all. (Is there a better way?)</p><p>The objective is to be able to forward takedown notices to the correct users in a network. Any ideas or suggestions would be appreciated. I know which users are registered to which MACs, I just need to be able to link a hash to a MAC at a given time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture.bittorrent" rel="tag" title="see questions tagged &#39;capture.bittorrent&#39;">capture.bittorrent</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '12, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/5a5ed51cef02ef6c73ddb975eec7941c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lurkios&#39;s gravatar image" /><p><span>Lurkios</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lurkios has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Sep '12, 12:04</strong> </span></p></div></div><div id="comments-container-14125" class="comments-container"></div><div id="comment-tools-14125" class="comment-tools"></div><div class="clear"></div><div id="comment-14125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14137"></span>

<div id="answer-container-14137" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14137-score" class="post-score" title="current number of votes">0</div><span id="post-14137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you can't track torrents by assuming a range of ports between 6881-6889. Most torrent clients I know have the option of randomizing their port each time they start, and they can basically use the whole range from 1025 to 65535 if they like. So I doubt that capturing by port is helping you.</p><p>In my opinion the only way to track down torrent traffic is to find a specific traffic pattern that indicates torrent traffic. I haven't looked into that myself so I can't provide you a pattern like that. I know that Intrusion Prevention systems often have the ability to block torrent traffic specifically, so there must be some sort of pattern that works.</p><p>What makes it even harder is that modern torrent programs can even encrypt their traffic (to avoid being throttled by ISPs detecting torrent patterns), so detecting it might not even be possible at all.</p><p>I'm not sure how your network is set up, but if you're NATting connection and the takedown notice comes with an IP and port you could look at the NAT tables to see who the connection was forwarded to. It will probably require to keep NAT table logs for quite some time I guess.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '12, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14137" class="comments-container"></div><div id="comment-tools-14137" class="comment-tools"></div><div class="clear"></div><div id="comment-14137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

