+++
type = "question"
title = "Can&#x27;t see WCF traffic - newbie issue"
description = '''I&#x27;ve just installed the latest WS 2.01, I&#x27;m on a laptop, I&#x27;m not really sure about the network interfaces, there seem to be many more listed than I can physically see + one called &#x27;WifFi&#x27; - anyway I think I am selecting them all....I can see lots of http traffic, but when I make a WCF call (using Ba...'''
date = "2015-12-31T07:43:00Z"
lastmod = "2016-01-01T06:49:00Z"
weight = 48769
keywords = [ "wcf", "wireshark" ]
aliases = [ "/questions/48769" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't see WCF traffic - newbie issue](/questions/48769/cant-see-wcf-traffic-newbie-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48769-score" class="post-score" title="current number of votes">0</div><span id="post-48769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've just installed the latest WS 2.01, I'm on a laptop, I'm not really sure about the network interfaces, there seem to be many more listed than I can physically see + one called 'WifFi' - anyway I think I am selecting them all....I can see lots of http traffic, but when I make a WCF call (using BasicHTTPBinding) the call is going and coming back (i.e. i can see the calling app is updating the backend), BUT nothing showing in Wireshark....what might I be doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wcf" rel="tag" title="see questions tagged &#39;wcf&#39;">wcf</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '15, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/2ed0df259c0befb39bf9f9a9966e65c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bertie&#39;s gravatar image" /><p><span>bertie</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bertie has no accepted answers">0%</span></p></div></div><div id="comments-container-48769" class="comments-container"></div><div id="comment-tools-48769" class="comment-tools"></div><div class="clear"></div><div id="comment-48769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48773"></span>

<div id="answer-container-48773" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48773-score" class="post-score" title="current number of votes">0</div><span id="post-48773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is the WCF call to a server on the local machine? If so, WinPCap (the capture mechanism used by Wireshark on Windows) will not see that traffic.</p><p>To capture "loopback" traffic see the wiki page for <a href="https://wiki.wireshark.org/CaptureSetup/Loopback">Loopback Capture setup</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '15, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48773" class="comments-container"><span id="48776"></span><div id="comment-48776" class="comment"><div id="post-48776-score" class="comment-score"></div><div class="comment-text"><p>I'm ashamed to say I think you might have been right! By mistake I was using the wrong config with localhost in - I can see traffic now. I know its slightly off topic, but it is what i'm trying to diag when I got stuck, I'm trying to call the WCF from within an emulator (WinPhone 8.1), and I'm getting nothing thru wireshark, I have a nasty suspicion that its nothing to do with wireshark, but is there any way with WS to see why the call is ending nowhere? (I can see browser traffic thru wireshark from the emulator)</p></div><div id="comment-48776-info" class="comment-info"><span class="comment-age">(31 Dec '15, 09:49)</span> <span class="comment-user userinfo">bertie</span></div></div><span id="48785"></span><div id="comment-48785" class="comment"><div id="post-48785-score" class="comment-score"></div><div class="comment-text"><p>Can you describe your setup in a bit more detail?</p></div><div id="comment-48785-info" class="comment-info"><span class="comment-age">(01 Jan '16, 06:49)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48773" class="comment-tools"></div><div class="clear"></div><div id="comment-48773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

