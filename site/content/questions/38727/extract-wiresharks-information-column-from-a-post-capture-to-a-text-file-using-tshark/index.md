+++
type = "question"
title = "Extract Wireshark&#x27;s information column from a post capture to a text file using tshark?"
description = '''Looking on how to extract the Information column that is displayed in wireshark from a completed capture using Tshark and dumping it into a text file. I know it can be done with Wireshark manually but I need to do it from command-line so it can be used in a script. I am familiar with some commands o...'''
date = "2014-12-26T21:32:00Z"
lastmod = "2015-01-29T06:39:00Z"
weight = 38727
keywords = [ "column", "text", "extract", "tshark", "information" ]
aliases = [ "/questions/38727" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extract Wireshark's information column from a post capture to a text file using tshark?](/questions/38727/extract-wiresharks-information-column-from-a-post-capture-to-a-text-file-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38727-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Looking on how to extract the Information column that is displayed in wireshark from a <em>completed</em> capture using Tshark and dumping it into a text file. I know it can be done with Wireshark manually but I need to do it from command-line so it can be used in a script. I am familiar with some commands of Tshark but can't figure the correct switch to get the "Information Column".</p><pre><code>tshark - r &lt;input&gt; -T fields (questionable part) &gt; output.txt</code></pre><p>Use case: After outputting the information column to a text file will use Powershell to extract any names of executables which have an executbale extension and have been downloaded i.e. .bat, .com, .scr, .exe, etc. This will be for a work network, obvious there should be many .exe's for various softwares updating periodically but any of the others will hopefully alert us to nefarious activities.</p></div><div id="question-tags" class="tags-container tags">column text extract tshark information</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '14, 21:32</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p>zer0day<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div></div><div id="comments-container-38727" class="comments-container"></div><div id="comment-tools-38727" class="comment-tools"></div><div class="clear"></div><div id="comment-38727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38728"></span>

<div id="answer-container-38728" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Funny, it always seems to happen, soon as I ask a question I then find my answer excuse my process. The command below does what I was looking for.</p><pre><code>tshark -V -r path\capture.cap &gt; path\output.txt</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Dec '14, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/7c34b5795df1aaa486754544342bfc1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zer0day&#39;s gravatar image" /><p>zer0day<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zer0day has 3 accepted answers">60%</span></p></div></div><div id="comments-container-38728" class="comments-container"></div><div id="comment-tools-38728" class="comment-tools"></div><div class="clear"></div><div id="comment-38728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39481"></span>

<div id="answer-container-39481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39481-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are using windows， pls try</p><p>tshark -T fields _ws.col.Info</p><p>_ws.col I think that mean wireshark column and .Info must be samed with colume name</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '15, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/f9775485852eb2d6edf9ec1761349e59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hu%20Paul&#39;s gravatar image" /><p>Hu Paul<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hu Paul has no accepted answers">0%</span></p></div></div><div id="comments-container-39481" class="comments-container"><span id="39530"></span><div id="comment-39530" class="comment"><div id="post-39530-score" class="comment-score"></div><div class="comment-text"><p>Was helpful, thanks for sharing</p></div><div id="comment-39530-info" class="comment-info"><span class="comment-age">(31 Jan '15, 21:57)</span> zer0day</div></div><span id="51180"></span><div id="comment-51180" class="comment"><div id="post-51180-score" class="comment-score"></div><div class="comment-text"><p>@Hu Paul Thanks a lot for sharing this (y)</p></div><div id="comment-51180-info" class="comment-info"><span class="comment-age">(25 Mar '16, 06:14)</span> rabeeljaved</div></div></div><div id="comment-tools-39481" class="comment-tools"></div><div class="clear"></div><div id="comment-39481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

