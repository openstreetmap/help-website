+++
type = "question"
title = "RADIUS Disconnect-NAK replies not associated with Disconnect-Requests"
description = '''Hi All, Is it deliberate that RADIUS Disconnect-NAK replies are not associated with their respective Disconnect-Requests based on Packet ID value in them? (a) they have no &quot;This is a response to a request in frame x&quot; line, and (b) their respective Disconnect-Request messages have no &quot;The response to...'''
date = "2014-09-19T06:57:00Z"
lastmod = "2014-09-19T13:18:00Z"
weight = 36451
keywords = [ "radius" ]
aliases = [ "/questions/36451" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RADIUS Disconnect-NAK replies not associated with Disconnect-Requests](/questions/36451/radius-disconnect-nak-replies-not-associated-with-disconnect-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36451-score" class="post-score" title="current number of votes">0</div><span id="post-36451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Is it deliberate that RADIUS Disconnect-NAK replies are not associated with their respective Disconnect-Requests based on Packet ID value in them? (a) they have no "This is a response to a request in frame x" line, and (b) their respective Disconnect-Request messages have no "The response to this request is in frame y" line</p><p>Disconnect-ACK replies have no such problem.</p><p>Not sure how to attach a pcap trace illustrating the issue.</p><p>Update: Packet trace uploaded: <a href="https://drive.google.com/file/d/0B31e47Ucqt4BRzZQYUh6eHJZaVU/edit?usp=sharing">https://drive.google.com/file/d/0B31e47Ucqt4BRzZQYUh6eHJZaVU/edit?usp=sharing</a></p><p>Thanks in advance,</p><p>Dmitriy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '14, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/4c43e04f0ef8eacb2a3173436cb432f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitriy&#39;s gravatar image" /><p><span>Dmitriy</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitriy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '14, 09:02</strong> </span></p></div></div><div id="comments-container-36451" class="comments-container"><span id="36453"></span><div id="comment-36453" class="comment"><div id="post-36453-score" class="comment-score"></div><div class="comment-text"><p>Put your capture in a publically accessible space, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc. and post a link to the capture back here by editing your question, or raise an Incident in the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a> and attach the pcap there. The attachment can be marked "private" to restrict access to the core developers.</p></div><div id="comment-36453-info" class="comment-info"><span class="comment-age">(19 Sep '14, 07:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="36454"></span><div id="comment-36454" class="comment"><div id="post-36454-score" class="comment-score"></div><div class="comment-text"><p>grahamb:</p><p>Done - thank you: <a href="https://drive.google.com/file/d/0B31e47Ucqt4BRzZQYUh6eHJZaVU/edit?usp=sharing">https://drive.google.com/file/d/0B31e47Ucqt4BRzZQYUh6eHJZaVU/edit?usp=sharing</a></p></div><div id="comment-36454-info" class="comment-info"><span class="comment-age">(19 Sep '14, 07:20)</span> <span class="comment-user userinfo">Dmitriy</span></div></div></div><div id="comment-tools-36451" class="comment-tools"></div><div class="clear"></div><div id="comment-36451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36456"></span>

<div id="answer-container-36456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36456-score" class="post-score" title="current number of votes">0</div><span id="post-36456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a bug\enhancement to me, take your pick. Likely to be in the radius dissector not considering a NACK as a reply. Best handled via the Wireshark Bugzilla by raising an entry there, or even submit a patch via <a href="https://code.wireshark.org/review/">Gerrit</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '14, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36456" class="comments-container"><span id="36458"></span><div id="comment-36458" class="comment"><div id="post-36458-score" class="comment-score"></div><div class="comment-text"><p>grahamb:</p><p>Thank you - will try Bugzilla first. Btw I'd also suggest considering NAK as a reply: if there's a NAK there should never be an ACK later.</p><p>Update: just filed it in Bugzilla as: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10487">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10487</a></p></div><div id="comment-36458-info" class="comment-info"><span class="comment-age">(19 Sep '14, 08:30)</span> <span class="comment-user userinfo">Dmitriy</span></div></div><span id="36460"></span><div id="comment-36460" class="comment"><div id="post-36460-score" class="comment-score"></div><div class="comment-text"><p>I agree. Either the folks who created that dissector didn't think about that, or there's a bug and it doesn't work correctly.</p></div><div id="comment-36460-info" class="comment-info"><span class="comment-age">(19 Sep '14, 08:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-36456" class="comment-tools"></div><div class="clear"></div><div id="comment-36456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36469"></span>

<div id="answer-container-36469" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36469-score" class="post-score" title="current number of votes">0</div><span id="post-36469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently there's a config option that affects it:</p><p>Pascal Quantin 2014-09-19 19:03:38 UTC Hi,</p><p>Radius dissector has a parameter allowing you to define what should be the maximum RTT allowed for request/response tracking. By default it is set to 5 seconds but in your capture the Disconnect NAK takes 6.0039 seconds to be received. Simply go to Edit -&gt; Preferences -&gt;Protocols -&gt; Radius -&gt; Request TimeToLive and increase it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '14, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/4c43e04f0ef8eacb2a3173436cb432f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dmitriy&#39;s gravatar image" /><p><span>Dmitriy</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dmitriy has no accepted answers">0%</span></p></div></div><div id="comments-container-36469" class="comments-container"></div><div id="comment-tools-36469" class="comment-tools"></div><div class="clear"></div><div id="comment-36469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

