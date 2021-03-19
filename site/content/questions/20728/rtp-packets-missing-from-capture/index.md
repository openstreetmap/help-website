+++
type = "question"
title = "rtp packets missing from capture"
description = '''Hi i used packeTH to create an RTP stream for G7231 payload and wireshark to capture the traffic.I am building UDP packets with RTP payload on one end (windows 7) and on the wireshark(other end windows 7) but I can only see IP packets(info column= IP fragmented protocol). Decode as option can be app...'''
date = "2013-04-22T22:39:00Z"
lastmod = "2013-04-23T06:12:00Z"
weight = 20728
keywords = [ "g723", "rtp" ]
aliases = [ "/questions/20728" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rtp packets missing from capture](/questions/20728/rtp-packets-missing-from-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20728-score" class="post-score" title="current number of votes">0</div><span id="post-20728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i used packeTH to create an RTP stream for G7231 payload and wireshark to capture the traffic.I am building UDP packets with RTP payload on one end (windows 7) and on the wireshark(other end windows 7) but I can only see IP packets(info column= IP fragmented protocol). Decode as option can be applied only if we can see as UDP packets, right? so what should be done if its showing only as IP packets? Thanks in advance...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g723" rel="tag" title="see questions tagged &#39;g723&#39;">g723</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/0b4665fffd26edce75d5be2f5cfdc3e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hann712&#39;s gravatar image" /><p><span>hann712</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hann712 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>22 Apr '13, 23:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20728" class="comments-container"><span id="20731"></span><div id="comment-20731" class="comment"><div id="post-20731-score" class="comment-score"></div><div class="comment-text"><p>Check the preferences of the IP dissector to see if reassembly is on, not sure if checksums should be dissabled. Your IP packets should not be fragmented (biger than MTU) when using G7231 I would have thought, you might want to look at that.</p></div><div id="comment-20731-info" class="comment-info"><span class="comment-age">(23 Apr '13, 00:41)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="20733"></span><div id="comment-20733" class="comment"><div id="post-20733-score" class="comment-score"></div><div class="comment-text"><p>can you please upload a sample capture file somewhere (google docs, dropbox, etc.) and post the link here?</p></div><div id="comment-20733-info" class="comment-info"><span class="comment-age">(23 Apr '13, 06:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20728" class="comment-tools"></div><div class="clear"></div><div id="comment-20728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

