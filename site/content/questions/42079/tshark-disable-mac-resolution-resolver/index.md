+++
type = "question"
title = "Tshark disable MAC resolution (resolver)"
description = '''I&#x27;m running Tshark to test for WiFi probes but sometimes I get instead of 40:0e:85:02:6a:a6 a Apple_df:76:88. Is there any way to get the REAL Mac instead of the resolved MAC? I already tried column.format with &quot;%uhs&quot; but this does not seem to work? Is there any way to disable this MAC lookup/resolu...'''
date = "2015-05-05T06:51:00Z"
lastmod = "2015-05-05T07:03:00Z"
weight = 42079
keywords = [ "tshark", "columns" ]
aliases = [ "/questions/42079" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark disable MAC resolution (resolver)](/questions/42079/tshark-disable-mac-resolution-resolver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42079-score" class="post-score" title="current number of votes">0</div><span id="post-42079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Tshark to test for WiFi probes but sometimes I get instead of <code>40:0e:85:02:6a:a6</code> a <code>Apple_df:76:88</code>. Is there any way to get the REAL Mac instead of the resolved MAC? I already tried <code>column.format</code> with <code>"%uhs"</code> but this does not seem to work?</p><p>Is there any way to disable this MAC lookup/resolution in the output of tshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '15, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/c990756255cdafe397a0266c4b1dcc93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudohenk&#39;s gravatar image" /><p><span>sudohenk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudohenk has no accepted answers">0%</span></p></div></div><div id="comments-container-42079" class="comments-container"></div><div id="comment-tools-42079" class="comment-tools"></div><div class="clear"></div><div id="comment-42079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42080"></span>

<div id="answer-container-42080" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42080-score" class="post-score" title="current number of votes">1</div><span id="post-42080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sudohenk has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should be able to disable MAC address resolution by either turning it off in Wireshark (Edit -&gt; Preferences -&gt; Name Resolution -&gt; Resolve MAC addresses) or by specifying the "<code>-o nameres.mac_name:FALSE</code>" option on the <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> command-line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '15, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-42080" class="comments-container"></div><div id="comment-tools-42080" class="comment-tools"></div><div class="clear"></div><div id="comment-42080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

