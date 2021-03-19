+++
type = "question"
title = "School &quot;destination unreachable&quot;."
description = '''Hi all I&#x27;m new to Wireshark. I managed to set up Wireshark to record on the routers mirroring port.  I then recorded 3 minutes of not being able to connect to websites..... It seems like its not possible for local ip&#x27;s to reach the router (192.168.0.1).  It says &quot;destination unreachable&quot;. Why could ...'''
date = "2016-10-02T03:02:00Z"
lastmod = "2016-10-02T14:30:00Z"
weight = 56067
keywords = [ "unreachable", "destination" ]
aliases = [ "/questions/56067" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [School "destination unreachable".](/questions/56067/school-destination-unreachable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56067-score" class="post-score" title="current number of votes">0</div><span id="post-56067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I'm new to Wireshark. I managed to set up Wireshark to record on the routers mirroring port.</p><p>I then recorded 3 minutes of not being able to connect to websites..... It seems like its not possible for local ip's to reach the router (192.168.0.1). It says "destination unreachable".</p><p>Why could that be? Could you help me point me in some direction at what to look for, when trying to troubleshoot with Wireshark? I believe i got a good log at the failure, but i'm not sure how to figure out, what causes the "destination unreachable".</p><p>Best regard Mike Kristensen Denmark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unreachable" rel="tag" title="see questions tagged &#39;unreachable&#39;">unreachable</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '16, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/adffaef3f124dec9c6a9167631efe0f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mikethk&#39;s gravatar image" /><p><span>Mikethk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mikethk has no accepted answers">0%</span></p></div></div><div id="comments-container-56067" class="comments-container"><span id="56068"></span><div id="comment-56068" class="comment"><div id="post-56068-score" class="comment-score"></div><div class="comment-text"><p>From your description I guess that you have connected your PC <strong>only</strong> to the mirroring port of your switch. Is that true?</p></div><div id="comment-56068-info" class="comment-info"><span class="comment-age">(02 Oct '16, 03:09)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="56083"></span><div id="comment-56083" class="comment"><div id="post-56083-score" class="comment-score"></div><div class="comment-text"><p>If the local devices could ping the routers ip before. Some / one of your changes is incorrect.</p><p>So how did you set up the mirror port at the router? Have you changed some routes?</p></div><div id="comment-56083-info" class="comment-info"><span class="comment-age">(02 Oct '16, 14:30)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-56067" class="comment-tools"></div><div class="clear"></div><div id="comment-56067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56081"></span>

<div id="answer-container-56081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56081-score" class="post-score" title="current number of votes">0</div><span id="post-56081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, Mike -</p><p>Not sure I understand completely your situation. IMCP Unreachable destination message can mean, in routing, there's no route active/defined to the IP/subnet. Are you trying to troubleshoot not being able to get to a website? It could be good to take a trace from the source PC in that case. If you want to work your way across the net, you could open a command window and ping your machine IP, then the router IP, and then the FQDN of the target website. This should be a test of each stage of the process, including the DNS resolution of the FQDN to an IP. Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '16, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/52ff5d6b59bd5798a667a6f346a52421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetlevel&#39;s gravatar image" /><p><span>packetlevel</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetlevel has no accepted answers">0%</span></p></div></div><div id="comments-container-56081" class="comments-container"></div><div id="comment-tools-56081" class="comment-tools"></div><div class="clear"></div><div id="comment-56081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

