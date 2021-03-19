+++
type = "question"
title = "No remote interfaces found"
description = '''Trying to do a remote capture on a Windows 7 Pro PC, from my PC(same ) No matter what I do, I&#x27;m getting this on 2 PC&#x27;s where I installed winpcap(v4)  I&#x27;m an administrator on the PC&#x27;s, and the service IS running.. Thoughts? Thanks, Rich'''
date = "2015-12-02T10:27:00Z"
lastmod = "2017-03-20T21:56:00Z"
weight = 48204
keywords = [ "remote-monitoring" ]
aliases = [ "/questions/48204" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No remote interfaces found](/questions/48204/no-remote-interfaces-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48204-score" class="post-score" title="current number of votes">0</div><span id="post-48204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to do a remote capture on a Windows 7 Pro PC, from my PC(same ) No matter what I do, I'm getting this on 2 PC's where I installed winpcap(v4) <img src="https://osqa-ask.wireshark.org/upfiles/Capture_gW6ixcv.PNG" alt="alt text" /></p><p>I'm an administrator on the PC's, and the service IS running..</p><p>Thoughts?</p><p>Thanks, Rich</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-monitoring" rel="tag" title="see questions tagged &#39;remote-monitoring&#39;">remote-monitoring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/0c69c6bbd60e7ffa44ef7a278b36f0ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="celticpiping&#39;s gravatar image" /><p><span>celticpiping</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="celticpiping has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '15, 10:36</strong> </span></p></div></div><div id="comments-container-48204" class="comments-container"></div><div id="comment-tools-48204" class="comment-tools"></div><div class="clear"></div><div id="comment-48204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48218"></span>

<div id="answer-container-48218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48218-score" class="post-score" title="current number of votes">0</div><span id="post-48218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Exactly what steps did you take, and when you say "the service IS running," what service are you referring to?</p><p>Installing winpcap is necessary, but that's not all that's required for remote capture. You also have to run rpcapd.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 17:43</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-48218" class="comments-container"><span id="48444"></span><div id="comment-48444" class="comment"><div id="post-48444-score" class="comment-score"></div><div class="comment-text"><p>apologies for not responding sooner. I had NOT started the daemon, and run it as 'administrator' though it's NOT working on the production PC I wish to monitor, it IS working on a tst PC.</p><p>Thanks! Rich</p></div><div id="comment-48444-info" class="comment-info"><span class="comment-age">(11 Dec '15, 05:09)</span> <span class="comment-user userinfo">celticpiping</span></div></div><span id="60207"></span><div id="comment-60207" class="comment"><div id="post-60207-score" class="comment-score"></div><div class="comment-text"><p>hi... i also have same issues i've been try enable service IS and run rpcapd..and that result also same "no remote interfaces found" could u help me master..please</p></div><div id="comment-60207-info" class="comment-info"><span class="comment-age">(20 Mar '17, 21:56)</span> <span class="comment-user userinfo">Littleboy</span></div></div></div><div id="comment-tools-48218" class="comment-tools"></div><div class="clear"></div><div id="comment-48218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

