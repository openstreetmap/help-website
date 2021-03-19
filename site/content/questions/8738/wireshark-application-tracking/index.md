+++
type = "question"
title = "wireshark application tracking"
description = '''hi, does wire-shark help track which application is connecting to the internet, just like geoip where we know which ip the os connects to, cause i think there is a rootkit installed in my laptop which connects to a &quot;gay&quot; network somewhere in Korea &quot;175.41.3.0 to 255&quot;, i don&#x27;t want to format and re-i...'''
date = "2012-01-31T21:47:00Z"
lastmod = "2012-02-02T02:13:00Z"
weight = 8738
keywords = [ "geoip", "application", "wireshark" ]
aliases = [ "/questions/8738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark application tracking](/questions/8738/wireshark-application-tracking)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8738-score" class="post-score" title="current number of votes">0</div><span id="post-8738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, does wire-shark help track which application is connecting to the internet, just like geoip where we know which ip the os connects to, cause i think there is a rootkit installed in my laptop which connects to a "gay" network somewhere in Korea "175.41.3.0 to 255", i don't want to format and re-install cause all my office work is on the laptop, i tried to use free version of ad-aware but no joy. thanks if anyone knows how to do this.... debby.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span> <span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '12, 21:47</strong></p><img src="https://secure.gravatar.com/avatar/821b7b7585dfc693d7653ecca733d8f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="debby%20dale&#39;s gravatar image" /><p><span>debby dale</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="debby dale has no accepted answers">0%</span></p></div></div><div id="comments-container-8738" class="comments-container"></div><div id="comment-tools-8738" class="comment-tools"></div><div class="clear"></div><div id="comment-8738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8739"></span>

<div id="answer-container-8739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8739-score" class="post-score" title="current number of votes">0</div><span id="post-8739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, as of this writing, Wireshark does not yet provide this capability. The feature has been requested in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1184">bug 1184</a>; however, it has not yet been implemented by anyone.</p><p>You might look into using other tools instead, such as <a href="http://en.wikipedia.org/wiki/Netstat">netstat</a> or Microsoft's <a href="http://www.microsoft.com/download/en/details.aspx?id=4865">Network Monitor</a> tool if you happen to be working on a Windows platform.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '12, 22:57</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8739" class="comments-container"><span id="8741"></span><div id="comment-8741" class="comment"><div id="post-8741-score" class="comment-score">1</div><div class="comment-text"><p>Still, Wireshark can help to see which port and destination IP is used in conversations, and the port number helps to track down the application using that port when doing <strong>netstat -ano</strong> or <strong>netstat -anb</strong></p></div><div id="comment-8741-info" class="comment-info"><span class="comment-age">(01 Feb '12, 00:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="8772"></span><div id="comment-8772" class="comment"><div id="post-8772-score" class="comment-score"></div><div class="comment-text"><p>i will try ms network monitor cause im using win 7..many thanks for your help/</p></div><div id="comment-8772-info" class="comment-info"><span class="comment-age">(02 Feb '12, 02:13)</span> <span class="comment-user userinfo">debby dale</span></div></div></div><div id="comment-tools-8739" class="comment-tools"></div><div class="clear"></div><div id="comment-8739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

