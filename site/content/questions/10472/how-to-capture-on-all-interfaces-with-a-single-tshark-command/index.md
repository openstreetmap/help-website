+++
type = "question"
title = "How to capture on all interfaces with a single Tshark command?"
description = '''Current wireshark version support capturing on multiple adapters at the same time, can we do this from the command line as well? At the moment i&#x27;m stuck with: C:&#92;Progra~1&#92;Wireshark&#92;tshark.exe -i 2 -a duration:600 -n -w &quot;%subor%&quot;  i would very much like something like this: C:&#92;Progra~1&#92;Wireshark&#92;tsha...'''
date = "2012-04-27T02:06:00Z"
lastmod = "2012-05-03T10:36:00Z"
weight = 10472
keywords = [ "tshark" ]
aliases = [ "/questions/10472" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture on all interfaces with a single Tshark command?](/questions/10472/how-to-capture-on-all-interfaces-with-a-single-tshark-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10472-score" class="post-score" title="current number of votes">0</div><span id="post-10472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Current wireshark version support capturing on multiple adapters at the same time, can we do this from the command line as well? At the moment i'm stuck with:</p><pre><code>C:\Progra~1\Wireshark\tshark.exe -i 2 -a duration:600 -n  -w &quot;%subor%&quot;</code></pre><p>i would very much like something like this:</p><pre><code>C:\Progra~1\Wireshark\tshark.exe -i any -a duration:600 -n  -w &quot;%subor%&quot;</code></pre><p>is this possible? Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '12, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p><span>Marc</span><br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-10472" class="comments-container"></div><div id="comment-tools-10472" class="comment-tools"></div><div class="clear"></div><div id="comment-10472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10486"></span>

<div id="answer-container-10486" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10486-score" class="post-score" title="current number of votes">1</div><span id="post-10486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marc has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By "current version" I assume you mean trunk or 1.7.x, right?</p><p>The tshark man page for those versions says that you can use the "-i" option multiple times to specify capturing on multiple interfaces.</p><p>(1.6 only supports capturing on multiple interfaces on Linux where the pseudo-device "any" can be used.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '12, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-10486" class="comments-container"><span id="10645"></span><div id="comment-10645" class="comment"><div id="post-10645-score" class="comment-score"></div><div class="comment-text"><p>Ah, very good Jeff, thanks!! i did not know you could also repeat the -i option, (and yes i meant 1.7.2)</p></div><div id="comment-10645-info" class="comment-info"><span class="comment-age">(03 May '12, 10:20)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="10646"></span><div id="comment-10646" class="comment"><div id="post-10646-score" class="comment-score">1</div><div class="comment-text"><p>As this is a Q&amp;A site, please don't forget to Accept the answer if it answered your question--see the FAQ.</p><p>Anyway, you're welcome!</p></div><div id="comment-10646-info" class="comment-info"><span class="comment-age">(03 May '12, 10:36)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-10486" class="comment-tools"></div><div class="clear"></div><div id="comment-10486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

