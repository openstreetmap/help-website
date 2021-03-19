+++
type = "question"
title = "Dissector: calculate difference between timestamps in packets"
description = '''Hello guys, My task is as following: i want to extend a custom dissector with the ability to calculate the difference between timestamps. Some packets contain a TLV containing a timestamp and whenever a timestamp TLV occurs after the first timestamp, the difference to the last timestamp should calcu...'''
date = "2013-11-27T00:42:00Z"
lastmod = "2013-11-27T09:12:00Z"
weight = 27471
keywords = [ "timestamp", "dissector", "packet", "time" ]
aliases = [ "/questions/27471" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector: calculate difference between timestamps in packets](/questions/27471/dissector-calculate-difference-between-timestamps-in-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27471-score" class="post-score" title="current number of votes">0</div><span id="post-27471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>My task is as following: i want to extend a custom dissector with the ability to calculate the difference between timestamps. Some packets contain a TLV containing a timestamp and whenever a timestamp TLV occurs after the first timestamp, the difference to the last timestamp should calculated and displayed.</p><p>I do not know yet how to store the values I am retrieving from packets so that i can reuse them at a later point of time. Can anyone show me an example, please?</p><p>Bye, hhhannes</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '13, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/d2ad1b223f1bf47ca43b6c37865b7257?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhhannes&#39;s gravatar image" /><p><span>hhhannes</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhhannes has no accepted answers">0%</span></p></div></div><div id="comments-container-27471" class="comments-container"><span id="27479"></span><div id="comment-27479" class="comment"><div id="post-27479-score" class="comment-score">1</div><div class="comment-text"><p>If I understand you want to save data and use them in another call of your dissector ?</p><p>First packet -&gt; save timestamp<br />
Second packet -&gt; get last timestamp</p><p>I am right ?</p><p>If so use conversation Interface</p></div><div id="comment-27479-info" class="comment-info"><span class="comment-age">(27 Nov '13, 02:55)</span> <span class="comment-user userinfo">Afrim</span></div></div><span id="27495"></span><div id="comment-27495" class="comment"><div id="post-27495-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Are there dissectors which contain good examples for the use of the conversation feature?</p></div><div id="comment-27495-info" class="comment-info"><span class="comment-age">(27 Nov '13, 07:42)</span> <span class="comment-user userinfo">hhhannes</span></div></div><span id="27499"></span><div id="comment-27499" class="comment"><div id="post-27499-score" class="comment-score"></div><div class="comment-text"><p>Yes take a look at epan/dissector/packet-tcp.c</p></div><div id="comment-27499-info" class="comment-info"><span class="comment-age">(27 Nov '13, 07:57)</span> <span class="comment-user userinfo">Afrim</span></div></div><span id="27503"></span><div id="comment-27503" class="comment"><div id="post-27503-score" class="comment-score">3</div><div class="comment-text"><p><span>@Afrim</span>: That may be a bit steep learning curve</p><p><span>@hhhannes</span>: Check <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.request_response_tracking">Request/Response tracking</a></p></div><div id="comment-27503-info" class="comment-info"><span class="comment-age">(27 Nov '13, 09:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-27471" class="comment-tools"></div><div class="clear"></div><div id="comment-27471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

