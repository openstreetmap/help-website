+++
type = "question"
title = "Unable to run dumpcap"
description = '''Hi, I am using the windows 7 OS.... and i for the second one command i dont see any output on the CLI.. C:&#92;Users&#92;emohirf&amp;gt;sc query npf SERVICE_NAME: npf  TYPE : 1 KERNEL_DRIVER  STATE : 4 RUNNING  (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)  WIN32_EXIT_CODE : 0 (0x0)  SERVICE_EXIT_CODE : 0 (0x0)  ...'''
date = "2013-07-23T23:54:00Z"
lastmod = "2013-07-24T02:07:00Z"
weight = 23316
keywords = [ "windows", "dumpcap" ]
aliases = [ "/questions/23316" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to run dumpcap](/questions/23316/unable-to-run-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23316-score" class="post-score" title="current number of votes">0</div><span id="post-23316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using the windows 7 OS.... and i for the second one command i dont see any output on the CLI..</p><p>C:\Users\emohirf&gt;sc query npf</p><p>SERVICE_NAME: npf TYPE : 1 KERNEL_DRIVER STATE : 4 RUNNING (STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN) WIN32_EXIT_CODE : 0 (0x0) SERVICE_EXIT_CODE : 0 (0x0) CHECKPOINT : 0x0 WAIT_HINT : 0x0</p><p>C:\Users\emohirf&gt;dumpcap -D -M 'dumpcap' is not recognized as an internal or external command, operable program or batch file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '13, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/959e162efb513fc227dc3b3fd7a18770?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arshmohd&#39;s gravatar image" /><p><span>arshmohd</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arshmohd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>24 Jul '13, 02:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23316" class="comments-container"><span id="23318"></span><div id="comment-23318" class="comment"><div id="post-23318-score" class="comment-score"></div><div class="comment-text"><p>Converted from an "answer" to <a href="http://ask.wireshark.org/questions/17318/how-to-use-wireshark-with-tata-photon-plus">this</a> question about Tata Photon Plus.</p></div><div id="comment-23318-info" class="comment-info"><span class="comment-age">(24 Jul '13, 02:04)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23316" class="comment-tools"></div><div class="clear"></div><div id="comment-23316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23319"></span>

<div id="answer-container-23319" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23319-score" class="post-score" title="current number of votes">3</div><span id="post-23319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have to ensure the directory containing dumpcap.exe is on your path, or provide the path on the command line, the same as for any other program on Windows.</p><p>The simplest fix is to provide the path, e.g. <code>...&gt;C:\program Files\Wireshark\dumpcap -D -M</code> assuming a default install on 32 bit Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23319" class="comments-container"></div><div id="comment-tools-23319" class="comment-tools"></div><div class="clear"></div><div id="comment-23319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

