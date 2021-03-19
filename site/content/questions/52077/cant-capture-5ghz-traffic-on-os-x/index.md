+++
type = "question"
title = "Can&#x27;t capture 5ghz traffic on OS X"
description = '''Hey folks,  Recently I&#x27;ve been trying to find an issue with my WiFi that runs on 5ghz using a Mac running Wireshark 2.0.3. Whenever I do a capture with I am only getting 2.4ghz traffic. If I run a capture manually in terminal using airport en0 sniff (channel) I can get the 5ghz traffic I want. Is th...'''
date = "2016-04-29T07:57:00Z"
lastmod = "2016-04-29T09:30:00Z"
weight = 52077
keywords = [ "wireless", "osx", "wireshark" ]
aliases = [ "/questions/52077" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can't capture 5ghz traffic on OS X](/questions/52077/cant-capture-5ghz-traffic-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52077-score" class="post-score" title="current number of votes">0</div><span id="post-52077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hey folks,<br />
</p><p>Recently I've been trying to find an issue with my WiFi that runs on 5ghz using a Mac running Wireshark 2.0.3. Whenever I do a capture with I am only getting 2.4ghz traffic. If I run a capture manually in terminal using airport en0 sniff (channel) I can get the 5ghz traffic I want. Is there any way to specify what channel Wireshark captures on or allow it to capture 5ghz traffic along with 2.4ghz traffic?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/f2b379a72ae7540623c80e646435a1fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="caffeinatedsoap&#39;s gravatar image" /><p><span>caffeinatedsoap</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="caffeinatedsoap has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52077" class="comments-container"></div><div id="comment-tools-52077" class="comment-tools"></div><div class="clear"></div><div id="comment-52077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52082"></span>

<div id="answer-container-52082" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52082-score" class="post-score" title="current number of votes">2</div><span id="post-52082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="caffeinatedsoap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have to set the channel manually after disconnecting from an active network. Easiest way I found was the following tool:</p><p><a href="https://www.adriangranados.com/apps/airtool">https://www.adriangranados.com/apps/airtool</a></p><p>Alternatively, if you find these executables on the system,</p><p>(to disassociate)</p><pre><code>sudo airport -z</code></pre><p>(set channel 36, for instance, on 5GHz)</p><pre><code>sudo airport --channel=36</code></pre><p>I start Wireshark with monitor mode enabled on the wifi adapter to collect packets.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '16, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div></div><div id="comments-container-52082" class="comments-container"><span id="52083"></span><div id="comment-52083" class="comment"><div id="post-52083-score" class="comment-score"></div><div class="comment-text"><p>Thanks Bob, that worked great!</p></div><div id="comment-52083-info" class="comment-info"><span class="comment-age">(29 Apr '16, 09:30)</span> <span class="comment-user userinfo">caffeinatedsoap</span></div></div></div><div id="comment-tools-52082" class="comment-tools"></div><div class="clear"></div><div id="comment-52082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

