+++
type = "question"
title = "amin protocol compilation"
description = '''while compiling the AMIN protocol,the command nmake all gives these errors: packet-amin.c packet-amin.c(78) : error C2220: warning treated as error - no &#x27;object&#x27; file generated packet-amin.c(78) : warning C4013: &#x27;dissector_add&#x27; undefined; assuming extern returning int NMAKE : fatal error U1077: &#x27;&quot;C:...'''
date = "2013-04-07T23:45:00Z"
lastmod = "2013-04-08T20:13:00Z"
weight = 20162
keywords = [ "amin", "compiling", "dissector" ]
aliases = [ "/questions/20162" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [amin protocol compilation](/questions/20162/amin-protocol-compilation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20162-score" class="post-score" title="current number of votes">0</div><span id="post-20162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>while compiling the AMIN protocol,the command nmake all gives these errors:</p><pre><code>packet-amin.c
packet-amin.c(78) : error C2220: warning treated as error - no &#39;object&#39; file generated
packet-amin.c(78) : warning C4013: &#39;dissector_add&#39; undefined; assuming extern returning int
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bin\cl.EXE&quot;&#39; : return code &#39;0x2&#39;.</code></pre><p>i had removed ",0" from plugin.rc file in amin dir as suggested somewhere.but still build doesn't work. somebody..help !!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-amin" rel="tag" title="see questions tagged &#39;amin&#39;">amin</span> <span class="post-tag tag-link-compiling" rel="tag" title="see questions tagged &#39;compiling&#39;">compiling</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '13, 23:45</strong></p><img src="https://secure.gravatar.com/avatar/afa04deca78e2ac8df31ecc4deea5bde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajain&#39;s gravatar image" /><p><span>ajain</span><br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajain has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '13, 02:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-20162" class="comments-container"><span id="20165"></span><div id="comment-20165" class="comment"><div id="post-20165-score" class="comment-score"></div><div class="comment-text"><p>Where does the dissector source come from, what version of Wireshark was it created for and what version of Wireshark are you attempting to compile?</p></div><div id="comment-20165-info" class="comment-info"><span class="comment-age">(08 Apr '13, 02:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="20167"></span><div id="comment-20167" class="comment"><div id="post-20167-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.codeproject.com/Articles/19426/Creating-Your-Own-Custom-Wireshark-Dissector">http://www.codeproject.com/Articles/19426/Creating-Your-Own-Custom-Wireshark-Dissector</a> provides the source file.i'm trying to compile it for WS 1.8.5,not sure what ver it was created for?</p></div><div id="comment-20167-info" class="comment-info"><span class="comment-age">(08 Apr '13, 03:26)</span> <span class="comment-user userinfo">ajain</span></div></div><span id="20168"></span><div id="comment-20168" class="comment"><div id="post-20168-score" class="comment-score"></div><div class="comment-text"><p>The article is dated July 2007, so that would probably have been around the 0.99.6 timeframe. A lot of water (and code) as been under the bridge since then, so the dissector may not compile in its original form with 1.8.5.</p></div><div id="comment-20168-info" class="comment-info"><span class="comment-age">(08 Apr '13, 04:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="20169"></span><div id="comment-20169" class="comment"><div id="post-20169-score" class="comment-score"></div><div class="comment-text"><p>dissector_add() has been deprecated in fawor of dissector_add_uint().</p></div><div id="comment-20169-info" class="comment-info"><span class="comment-age">(08 Apr '13, 04:34)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="20170"></span><div id="comment-20170" class="comment"><div id="post-20170-score" class="comment-score"></div><div class="comment-text"><p>so no way of compiling this dissector?can u provide any other ex?where and how would i compile my dissector?</p></div><div id="comment-20170-info" class="comment-info"><span class="comment-age">(08 Apr '13, 05:40)</span> <span class="comment-user userinfo">ajain</span></div></div><span id="20171"></span><div id="comment-20171" class="comment not_top_scorer"><div id="post-20171-score" class="comment-score"></div><div class="comment-text"><p>Have a look in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a>. It is maintained by the Wireshark Developers, so is up to date with the latest dissector practice and not just tossed over the wall and left to languish like the CodeProject dissector.</p></div><div id="comment-20171-info" class="comment-info"><span class="comment-age">(08 Apr '13, 06:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-20162" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-20162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20229"></span>

<div id="answer-container-20229" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20229-score" class="post-score" title="current number of votes">0</div><span id="post-20229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ajain has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Edit the <code>packet-amin.c</code> file and replace all occurrences of <code>dissector_add</code> with <code>dissector_add_uint</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20229" class="comments-container"></div><div id="comment-tools-20229" class="comment-tools"></div><div class="clear"></div><div id="comment-20229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

