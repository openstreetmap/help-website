+++
type = "question"
title = "Analyse lose of connection"
description = '''Hello,  I have each day some looses of connection (+-10) between a supervision program on a server and a device. I have put a wireshark to analyse this problem and here is what i get when the loose of connection happens : TCP ACKed unseen segment. (ip.src=server and ip.dest=device) TCP Previous segm...'''
date = "2016-12-05T03:09:00Z"
lastmod = "2016-12-06T04:57:00Z"
weight = 57858
keywords = [ "segment_not_captured", "unseen_segment", "acked", "tcp" ]
aliases = [ "/questions/57858" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Analyse lose of connection](/questions/57858/analyse-lose-of-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57858-score" class="post-score" title="current number of votes">0</div><span id="post-57858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have each day some looses of connection (+-10) between a supervision program on a server and a device. I have put a wireshark to analyse this problem and here is what i get when the loose of connection happens :</p><p>TCP ACKed unseen segment. (ip.src=server and ip.dest=device)</p><p>TCP Previous segment not captured.(ip.src=device and ip.dest=host)</p><p>TCP Keep-Alive. (from device to server)</p><p>TCP Keep-Alive ACK. (from server to device)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Erreur_QFRxW0w.png" alt="alt text" /></p><p>Where does this problem could come from ?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-segment_not_captured" rel="tag" title="see questions tagged &#39;segment_not_captured&#39;">segment_not_captured</span> <span class="post-tag tag-link-unseen_segment" rel="tag" title="see questions tagged &#39;unseen_segment&#39;">unseen_segment</span> <span class="post-tag tag-link-acked" rel="tag" title="see questions tagged &#39;acked&#39;">acked</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '16, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/6f12a9b996e365e64375f92575b59706?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stabuloosh&#39;s gravatar image" /><p><span>Stabuloosh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stabuloosh has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57858" class="comments-container"><span id="57864"></span><div id="comment-57864" class="comment"><div id="post-57864-score" class="comment-score"></div><div class="comment-text"><p>Can you provide a packet capture via Cloudshark? Or at minimum, a screenshot with much more data that's not broken up into parts for Server and Device?</p><p>There's not much here to go with right now. It looks like Server needs to send some data to Device every so often, and it may happen so infrequently that Device needs to send a Keepalive. A whole packet capture can help provide more context on this and help figure out the problem. For example, if you're losing TCP connections, you should be seeing the TCP FIN or RST packets. I don't see that in your screenshot.</p></div><div id="comment-57864-info" class="comment-info"><span class="comment-age">(05 Dec '16, 07:14)</span> <span class="comment-user userinfo">jeantunis</span></div></div><span id="57894"></span><div id="comment-57894" class="comment"><div id="post-57894-score" class="comment-score"></div><div class="comment-text"><p>You can find the capture below.</p><p><a href="https://www.cloudshark.org/captures/7176abfd2d92">https://www.cloudshark.org/captures/7176abfd2d92</a></p><p>ip==10.150.10.69 = server</p><p>ip==10.150.104.51 = device</p><p>Indeed the server (where runs the supervision programm) sends data to the device often to see the state of the device.</p><p>Thanks a lot.</p></div><div id="comment-57894-info" class="comment-info"><span class="comment-age">(06 Dec '16, 04:57)</span> <span class="comment-user userinfo">Stabuloosh</span></div></div></div><div id="comment-tools-57858" class="comment-tools"></div><div class="clear"></div><div id="comment-57858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

