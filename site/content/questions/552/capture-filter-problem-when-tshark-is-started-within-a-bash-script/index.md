+++
type = "question"
title = "capture filter problem when tshark is started within a bash-script"
description = '''Hi,  I have a little problem when starting tshark out of a bash-script. Here a short part from the script: BIN=&quot;/usr/bin/tshark&quot; OPTS=&quot; -f &#92;&quot;port 5026 and (host 10.65.27.138 or host 10.65.27.137 or host 10.65.27.139)&#92;&quot; -a duration:10 -i eth1 -n -q -w /data/traces/files/test2.pcap&quot; echo $BIN $OPTS $B...'''
date = "2010-10-20T03:21:00Z"
lastmod = "2010-10-20T06:25:00Z"
weight = 552
keywords = [ "capture-filter", "tshark", "script" ]
aliases = [ "/questions/552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter problem when tshark is started within a bash-script](/questions/552/capture-filter-problem-when-tshark-is-started-within-a-bash-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-552-score" class="post-score" title="current number of votes">0</div><span id="post-552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a little problem when starting tshark out of a bash-script. Here a short part from the script:</p><pre><code>BIN=&quot;/usr/bin/tshark&quot;
OPTS=&quot; -f \&quot;port 5026 and (host 10.65.27.138 or host 10.65.27.137 or host 10.65.27.139)\&quot; -a duration:10 -i eth1 -n -q -w /data/traces/files/test2.pcap&quot;
echo $BIN $OPTS
$BIN $OPTS</code></pre><p>Now I'm receiving following output:</p><pre><code>/usr/bin/tshark -f &quot;port 5026 and (host 10.65.27.138 or host 10.65.27.137 or host 10.65.27.139)&quot; -a duration:10 -i eth1 -n -q -w /data/traces/files/tma_ffm_1_smpp_hsbu1a1/test2.pcap
tshark: Capture filters were specified both with &quot;-f&quot; and with additional command-line arguments</code></pre><p>When starting tshark directly from the bash with the output of "echo $BIN $OPTS" everything is working fine. I've tried several versions of declaring $OPTS like</p><ul><li>OPTS=" -f "filters" "</li><li>OPTS=' -f "filters" '</li><li>OPTS=" -f 'filter' "</li></ul><p>but all with the same result as mentioned above. Tested with tshark 0.99.6, 1.0.5 and 1.2.8</p><p>Hope anyone can help me again ;)</p><p>BR Sascha</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/db9b0d7d89cd815ac939136eacbb1d4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sascha&#39;s gravatar image" /><p><span>Sascha</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sascha has one accepted answer">100%</span></p></div></div><div id="comments-container-552" class="comments-container"></div><div id="comment-tools-552" class="comment-tools"></div><div class="clear"></div><div id="comment-552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="556"></span>

<div id="answer-container-556" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-556-score" class="post-score" title="current number of votes">0</div><span id="post-556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sascha has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi again,</p><p>dont think it's a good solution, but I found an usable workaround:</p><pre><code>OPTS=&quot; -b duration:900 -i eth2 -n -q -w /data/traces/files/tma_ffm_1_smpp_hsbu1b1/tma_ffm_1_smpp_hsbu1b1.pcap port 5026 and (host 10.65.27.138 or host 10.65.27.137 or host 10.65.27.139)&quot;</code></pre><p>As all the last arguments are interpreted as capture filter, this is working.</p><p>If anybody knows a better way, please let me know.</p><p>BR Sascha</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '10, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/db9b0d7d89cd815ac939136eacbb1d4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sascha&#39;s gravatar image" /><p><span>Sascha</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sascha has one accepted answer">100%</span></p></div></div><div id="comments-container-556" class="comments-container"></div><div id="comment-tools-556" class="comment-tools"></div><div class="clear"></div><div id="comment-556-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

