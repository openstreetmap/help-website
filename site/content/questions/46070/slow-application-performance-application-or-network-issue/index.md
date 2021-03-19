+++
type = "question"
title = "Slow application performance - Application or network issue?"
description = '''Dear Wireshark-Folks, due to the fact that I am not too experienced with wireshark, I would appreciate for some advice whats going on with the following capture: https://www.cloudshark.org/captures/a4fb6e2c187b  Capture was performed on client PC (172.24.112.145) A custom application is running on t...'''
date = "2015-09-23T00:24:00Z"
lastmod = "2015-09-24T02:31:00Z"
weight = 46070
keywords = [ "slow" ]
aliases = [ "/questions/46070" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow application performance - Application or network issue?](/questions/46070/slow-application-performance-application-or-network-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46070-score" class="post-score" title="current number of votes">0</div><span id="post-46070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Wireshark-Folks,</p><p>due to the fact that I am not too experienced with wireshark, I would appreciate for some advice whats going on with the following capture:</p><p><a href="https://www.cloudshark.org/captures/a4fb6e2c187b">https://www.cloudshark.org/captures/a4fb6e2c187b</a></p><ul><li>Capture was performed on client PC (172.24.112.145)</li><li>A custom application is running on this computer, but the behaivor is quite slow.</li><li>This application does database queries, starts transfering files, ... with different servers . You see it inside the capture.</li><li>Malformed packets are, because the capture was anonymized with Tracewrangler. So, data after Layer4 has been removed, but that should do the trick.</li></ul><p>The question is if network/application problem and which application server or the client itself?</p><p>Thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '15, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/b7b46291a0c3593e20b23f68fd638125?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dark_scorp&#39;s gravatar image" /><p><span>dark_scorp</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dark_scorp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Sep '15, 00:33</strong> </span></p></div></div><div id="comments-container-46070" class="comments-container"><span id="46078"></span><div id="comment-46078" class="comment"><div id="post-46078-score" class="comment-score">2</div><div class="comment-text"><p>From capture it looks that slowness is from 172.24.112.245(App),on this server delayed ack is enabled(200ms) and after each empty ack App server is taking approx 800ms to send new data.you should ask your app programmer about this pattern.</p></div><div id="comment-46078-info" class="comment-info"><span class="comment-age">(23 Sep '15, 09:45)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="46100"></span><div id="comment-46100" class="comment"><div id="post-46100-score" class="comment-score">1</div><div class="comment-text"><p>The 800ms delay is from your client, probably building its SQL query.</p><p>As Kishan said, Delayed ACK is on, but as you are doing DB Queries, this is USUALLY a good thing. You could drop it to 100 if you are really worried. But turning it off may flood little packets everywhere.</p><p>Network is fast'ish with(6-7ms). Server OS/SQL is fast (pretty much instant). But the client is causing delays of 800 or 200 ms all the time. And they add up. Between Packets 187 and 250 of stream 6 you have already 6 seconds, of which around 75% is spent waiting on the app to do whatever it is doing.</p></div><div id="comment-46100-info" class="comment-info"><span class="comment-age">(24 Sep '15, 02:28)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="46101"></span><div id="comment-46101" class="comment"><div id="post-46101-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your replies! So I will check the application running localy on the workstation.</p></div><div id="comment-46101-info" class="comment-info"><span class="comment-age">(24 Sep '15, 02:31)</span> <span class="comment-user userinfo">dark_scorp</span></div></div></div><div id="comment-tools-46070" class="comment-tools"></div><div class="clear"></div><div id="comment-46070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

