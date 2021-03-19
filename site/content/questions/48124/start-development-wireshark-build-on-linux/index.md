+++
type = "question"
title = "Start development wireshark build on linux"
description = '''I&#x27;ve build wireshark v2.1.0 (using cmake) and installed it to /tmp directory. For now i&#x27;ve got a problem - &quot;No interfaces found&quot;. I&#x27;ve copied dumpcap from /usr/bin locally to /tmp/bin directory and give all right that it need. Already installed wireshark from debian repository (1.12.0) works fine an...'''
date = "2015-12-01T03:56:00Z"
lastmod = "2015-12-01T05:44:00Z"
weight = 48124
keywords = [ "development", "testing", "linux" ]
aliases = [ "/questions/48124" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Start development wireshark build on linux](/questions/48124/start-development-wireshark-build-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48124-score" class="post-score" title="current number of votes">0</div><span id="post-48124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've build wireshark v2.1.0 (using cmake) and installed it to /tmp directory. For now i've got a problem - "No interfaces found". I've copied dumpcap from /usr/bin locally to /tmp/bin directory and give all right that it need. Already installed wireshark from debian repository (1.12.0) works fine and sees all interfaces.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-testing" rel="tag" title="see questions tagged &#39;testing&#39;">testing</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/4c60eaad3bf660591697eba323786208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qmor&#39;s gravatar image" /><p><span>qmor</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qmor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Dec '15, 08:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48124" class="comments-container"></div><div id="comment-tools-48124" class="comment-tools"></div><div class="clear"></div><div id="comment-48124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48132"></span>

<div id="answer-container-48132" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48132-score" class="post-score" title="current number of votes">0</div><span id="post-48132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Developers Guide, <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcRunFirstTime.html#ChSrcRunFirstTimeUnix">Sect 3.6.1</a> Run generated Wireshark, Unix/Linux implies that you can't capture from the built version, I'm not sure if that's true these days. Did you set the environment variable as stated?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48132" class="comments-container"><span id="48133"></span><div id="comment-48133" class="comment"><div id="post-48133-score" class="comment-score"></div><div class="comment-text"><p>yes i've set ld.so.conf.d/wireshark.conf path to fresh wireshark bin and lib and then run ldconfig.</p><p>Maybe i need anything else?</p></div><div id="comment-48133-info" class="comment-info"><span class="comment-age">(01 Dec '15, 05:16)</span> <span class="comment-user userinfo">qmor</span></div></div><span id="48134"></span><div id="comment-48134" class="comment"><div id="post-48134-score" class="comment-score"></div><div class="comment-text"><p>That's not what the instructions say. Unfortunately I'm unable to help you any further as I'm a Windows guy. Where it just runs after build :-)</p></div><div id="comment-48134-info" class="comment-info"><span class="comment-age">(01 Dec '15, 05:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48135"></span><div id="comment-48135" class="comment"><div id="post-48135-score" class="comment-score"></div><div class="comment-text"><p>i've tried to start as Sect 3.6.1 said:</p><pre><code>WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1 ./wireshark</code></pre><p>it's much easier to run (no need any ldconfig changes) but it's still no interfaces in list</p></div><div id="comment-48135-info" class="comment-info"><span class="comment-age">(01 Dec '15, 05:34)</span> <span class="comment-user userinfo">qmor</span></div></div><span id="48136"></span><div id="comment-48136" class="comment"><div id="post-48136-score" class="comment-score"></div><div class="comment-text"><p>To me that would imply some permissions problem, but as to what it is I can't help any further. Hopefully someone else will chime in.</p></div><div id="comment-48136-info" class="comment-info"><span class="comment-age">(01 Dec '15, 05:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48132" class="comment-tools"></div><div class="clear"></div><div id="comment-48132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

