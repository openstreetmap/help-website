+++
type = "question"
title = "Apcon Timestamp decoded as &#x27;VSS-Monitoring ethernet trailer&#x27;"
description = '''I have a capture file that was e-gressed from an Apcon smart-tap but when I view the trace file in Wireshark v 1.10.5, it shows the header as &quot;VSS-Monitoring ethernet trailer&#x27;.  Does Wireshark support Apcon timestamp yet? Or is that in same format as VSS-Monitoring?'''
date = "2014-03-04T16:43:00Z"
lastmod = "2014-03-04T17:48:00Z"
weight = 30421
keywords = [ "apcon", "vss-monitoring", "timstamp" ]
aliases = [ "/questions/30421" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Apcon Timestamp decoded as 'VSS-Monitoring ethernet trailer'](/questions/30421/apcon-timestamp-decoded-as-vss-monitoring-ethernet-trailer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30421-score" class="post-score" title="current number of votes">0</div><span id="post-30421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture file that was e-gressed from an Apcon smart-tap but when I view the trace file in Wireshark v 1.10.5, it shows the header as "VSS-Monitoring ethernet trailer'.</p><p>Does Wireshark support Apcon timestamp yet? Or is that in same format as VSS-Monitoring?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-apcon" rel="tag" title="see questions tagged &#39;apcon&#39;">apcon</span> <span class="post-tag tag-link-vss-monitoring" rel="tag" title="see questions tagged &#39;vss-monitoring&#39;">vss-monitoring</span> <span class="post-tag tag-link-timstamp" rel="tag" title="see questions tagged &#39;timstamp&#39;">timstamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/48b1ff62ccc5e052bbcefb9b8e43cb58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="techynewbie&#39;s gravatar image" /><p><span>techynewbie</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="techynewbie has no accepted answers">0%</span></p></div></div><div id="comments-container-30421" class="comments-container"></div><div id="comment-tools-30421" class="comment-tools"></div><div class="clear"></div><div id="comment-30421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30424"></span>

<div id="answer-container-30424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30424-score" class="post-score" title="current number of votes">0</div><span id="post-30424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"VSS-Monitoring" refers to devices from <a href="http://www.vssmonitoring.com">VSS Monitoring</a> (who are owned by a conglomerate named <a href="http://www.danaher.com">Danaher</a>). <a href="http://www.apcon.com">APCON</a> are a separate company, so, unless either they copied VSS Monitoring, VSS Monitoring copied them, they both copied somebody else, or they coincidentally invented the same trailer format, the APCON trailer isn't the same as the VSS Monitoring trailer.</p><p>We don't have any support for APCON trailers. Somebody would have to develop it and contribute it. APCON's Web site doesn't have any obvious documentation for it, so somebody would either have to find documentation for their trailer format or reverse-engineer it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 17:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30424" class="comments-container"></div><div id="comment-tools-30424" class="comment-tools"></div><div class="clear"></div><div id="comment-30424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

