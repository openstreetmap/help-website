+++
type = "question"
title = "How to print a list of tshark interfaces to a txt file?"
description = '''Looks simple but is annoying... dumpcap.exe -D &amp;gt;&amp;gt; interfaces.txt  or: tshark.exe -D &amp;gt;&amp;gt; interfaces.txt  Because interface numbers can be different among different machines, i want to use this command to sort out the Local Ethernet Cable connection and use it as a variable in my tshark scr...'''
date = "2012-03-08T05:26:00Z"
lastmod = "2012-03-08T06:02:00Z"
weight = 9429
keywords = [ "interfaces", "tshark", "networkinterfaces" ]
aliases = [ "/questions/9429" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to print a list of tshark interfaces to a txt file?](/questions/9429/how-to-print-a-list-of-tshark-interfaces-to-a-txt-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9429-score" class="post-score" title="current number of votes">0</div><span id="post-9429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looks simple but is annoying...</p><pre><code>dumpcap.exe -D &gt;&gt; interfaces.txt</code></pre><p>or:</p><pre><code>tshark.exe -D &gt;&gt; interfaces.txt</code></pre><p>Because interface numbers can be different among different machines, i want to use this command to sort out the Local Ethernet Cable connection and use it as a variable in my tshark script after sorting this out first... but i can't seem to print a list to a txt file?!</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '12, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p><span>Marc</span><br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-9429" class="comments-container"></div><div id="comment-tools-9429" class="comment-tools"></div><div class="clear"></div><div id="comment-9429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9431"></span>

<div id="answer-container-9431" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9431-score" class="post-score" title="current number of votes">3</div><span id="post-9431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marc has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thats because the output of <code>dumpcap -D</code> isn't printed to stdout, but to stderr, and what you're trying to do is to redirect stdout to a file. So you need to redirect stderr instead.</p><p>Try this: <strong><code>dumpcap -D 2&gt;interfaces.txt</code></strong>, where the "2&gt;" stands for "please redirect stderr".</p><p>See this <a href="http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/redirection.mspx?mfr=true">Microsoft Ressource</a> for a detailed explanation of the redirecting of handles.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '12, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Mar '12, 05:36</strong> </span></p></div></div><div id="comments-container-9431" class="comments-container"><span id="9432"></span><div id="comment-9432" class="comment"><div id="post-9432-score" class="comment-score"></div><div class="comment-text"><p>Djeez! That was very fast ;-) Thanks Jasper!</p></div><div id="comment-9432-info" class="comment-info"><span class="comment-age">(08 Mar '12, 05:40)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="9433"></span><div id="comment-9433" class="comment"><div id="post-9433-score" class="comment-score"></div><div class="comment-text"><p>Could i use this in 1 commandline? ie something like.. tshark.exe -D | grep therightinterface | tshark capturecommandline</p></div><div id="comment-9433-info" class="comment-info"><span class="comment-age">(08 Mar '12, 05:50)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="9434"></span><div id="comment-9434" class="comment"><div id="post-9434-score" class="comment-score"></div><div class="comment-text"><p>Depends... you'll have to redirect stderr to stdout to be able to pipe it, e.g. like this: <strong>tshark -D 2&gt;&amp;1|grep therightinterface...</strong></p></div><div id="comment-9434-info" class="comment-info"><span class="comment-age">(08 Mar '12, 06:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-9431" class="comment-tools"></div><div class="clear"></div><div id="comment-9431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

