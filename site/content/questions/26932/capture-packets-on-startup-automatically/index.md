+++
type = "question"
title = "Capture packets on startup automatically"
description = '''Is there any way to make the Wireshark capture packets automatically and save it in a file on startup of Windows? Kindly help me to fix this. Thanks'''
date = "2013-11-13T03:17:00Z"
lastmod = "2013-11-14T04:39:00Z"
weight = 26932
keywords = [ "windows", "capture", "startup", "packet" ]
aliases = [ "/questions/26932" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packets on startup automatically](/questions/26932/capture-packets-on-startup-automatically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26932-score" class="post-score" title="current number of votes">0</div><span id="post-26932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to make the Wireshark capture packets automatically and save it in a file on startup of Windows? Kindly help me to fix this.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '13, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/b3bc2dd686651b1ec4a64787f1dd173b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bala92n&#39;s gravatar image" /><p><span>bala92n</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bala92n has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '13, 05:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-26932" class="comments-container"><span id="26992"></span><div id="comment-26992" class="comment"><div id="post-26992-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is there any way to make the Wireshark capture packets automatically and save it in a file on startup of Windows?</p></blockquote><p>why do you want to do that?</p><p>Are you trying to figure out if something (malware) sends data to the internet, or do you want to create a (kind of) automated network capture device, based on windows?</p></div><div id="comment-26992-info" class="comment-info"><span class="comment-age">(14 Nov '13, 04:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26932" class="comment-tools"></div><div class="clear"></div><div id="comment-26932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26934"></span>

<div id="answer-container-26934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26934-score" class="post-score" title="current number of votes">0</div><span id="post-26934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. First, run Wireshark from a command line prompt by entering "wireshark -D" to get a list of interfaces (you can also use "dumpcap -D" if you want). Note the index of the interface you want to capture on.</p><p>Next, create a batch file that contains the line</p><p><code>wireshark -i [InterfaceID] -k</code></p><p>and put a shortcut to that link into your startup folder. That should do the trick.</p><p>If you want to furter customize the process (like setting an capture file name or other options) you can always run "wireshark -h" to get a list of all command line parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '13, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '13, 03:30</strong> </span></p></div></div><div id="comments-container-26934" class="comments-container"><span id="26939"></span><div id="comment-26939" class="comment"><div id="post-26939-score" class="comment-score"></div><div class="comment-text"><p>That will only start the capture at some point during user login. To start the capture at windows start-up an alternative will have to be employed, usually modifying Local Group Policy.</p></div><div id="comment-26939-info" class="comment-info"><span class="comment-age">(13 Nov '13, 05:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="26952"></span><div id="comment-26952" class="comment"><div id="post-26952-score" class="comment-score"></div><div class="comment-text"><p>Correct. It depends on what the definition of "startup of Windows" means :-) My solution requires a user to log in of course.</p></div><div id="comment-26952-info" class="comment-info"><span class="comment-age">(13 Nov '13, 08:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-26934" class="comment-tools"></div><div class="clear"></div><div id="comment-26934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

