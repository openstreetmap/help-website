+++
type = "question"
title = "Start and Stop Capture automatically"
description = '''Is there an option in Wireshark to run it between x:00 and y:00 every day?'''
date = "2014-09-24T18:14:00Z"
lastmod = "2014-09-25T01:56:00Z"
weight = 36578
keywords = [ "start", "stop", "automatically" ]
aliases = [ "/questions/36578" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Start and Stop Capture automatically](/questions/36578/start-and-stop-capture-automatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36578-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there an option in Wireshark to run it between x:00 and y:00 every day?</p></div><div id="question-tags" class="tags-container tags">start stop automatically</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 18:14</strong></p><img src="https://secure.gravatar.com/avatar/32fb9474264e66dac4c295002ac0a2dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Santhosh%20Pallikara&#39;s gravatar image" /><p>Santhosh Pal...<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Santhosh Pallikara has no accepted answers">0%</span></p></div></div><div id="comments-container-36578" class="comments-container"></div><div id="comment-tools-36578" class="comment-tools"></div><div class="clear"></div><div id="comment-36578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36587"></span>

<div id="answer-container-36587" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36587-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has no support for starting captures at a specified time. so you'll have to use the scheduler facilities of your OS (cron, scheduled tasks etc. as appropriate), but Wireshark can capture for a defined period of time once started.</p><p>Note that you're also going to get better performance and less likelihood of running out of memory if you use dumpcap (which is what Wireshark actually uses under the covers) to make the captures. See the <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> man page for parameters, especially the -a option to limit the capture duration</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36587" class="comments-container"><span id="36609"></span><div id="comment-36609" class="comment"><div id="post-36609-score" class="comment-score"></div><div class="comment-text"><p>Sure... I can use dumpcap. I reviwed the man page and it talks about options. Is there any video or document with example on how to set this up?</p></div><div id="comment-36609-info" class="comment-info"><span class="comment-age">(25 Sep '14, 11:03)</span> Santhosh Pal...</div></div><span id="36610"></span><div id="comment-36610" class="comment"><div id="post-36610-score" class="comment-score">1</div><div class="comment-text"><p>There is the users guide which has info on starting <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html">Wireshark from the command line</a>, and quite a few of the options are the same, e.g. for a 1 hour run you would use the option <code>-a duration:3600</code>. You would have to provide other required options to make a capture, maybe Google would find something for you, e.g. I found <a href="http://packetlife.net/blog/2011/mar/9/long-term-traffic-capture-wireshark/">this</a> searching for "dumpcap options".</p></div><div id="comment-36610-info" class="comment-info"><span class="comment-age">(25 Sep '14, 11:15)</span> grahamb ♦</div></div></div><div id="comment-tools-36587" class="comment-tools"></div><div class="clear"></div><div id="comment-36587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

