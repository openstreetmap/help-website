+++
type = "question"
title = "Hi. I got problem with &quot;closing file waiting....&quot;"
description = '''When I make multiple file as 100mb.. It appeared on currently capturing session. It seems to be temporary message... but it&#x27;s not finished until I close Wireshark.... please help me.. It happened to stable version of Wireshark 1.8.4'''
date = "2013-01-27T18:10:00Z"
lastmod = "2013-01-28T11:22:00Z"
weight = 17993
keywords = [ "closing", "file" ]
aliases = [ "/questions/17993" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Hi. I got problem with "closing file waiting...."](/questions/17993/hi-i-got-problem-with-closing-file-waiting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17993-score" class="post-score" title="current number of votes">0</div><span id="post-17993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I make multiple file as 100mb.. It appeared on currently capturing session. It seems to be temporary message... but it's not finished until I close Wireshark.... please help me.. It happened to stable version of Wireshark 1.8.4</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-closing" rel="tag" title="see questions tagged &#39;closing&#39;">closing</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '13, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/506b69288b4b67701a277176c697882c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SSH&#39;s gravatar image" /><p><span>SSH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SSH has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jan '13, 11:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-17993" class="comments-container"></div><div id="comment-tools-17993" class="comment-tools"></div><div class="clear"></div><div id="comment-17993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17994"></span>

<div id="answer-container-17994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17994-score" class="post-score" title="current number of votes">0</div><span id="post-17994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try using dumpcap instead. It's a command line tool that you can use to capture packets to disk, and you'll find it in the Wireshark installation directory. Wireshark uses dumpcap itself to capture files, so you can do the same.</p><p>Use <code>dumpcap -D</code> to get a list of capture interfaces first. Then you can run dumpcap with parameter -i and the number of the interface to capture on it.</p><p>A typical dumpcap call could look like this:</p><p><code>dumpcap -i 1 -w capture.pcapng -b filesize:100000</code></p><p>to capture on interface 1, write to file "capture.pcapng" and create a new file each 100MB. In fact, if you use -b like that, each filename will have date and time and a running number added to it to become unique.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '13, 18:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jan '13, 11:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-17994" class="comments-container"></div><div id="comment-tools-17994" class="comment-tools"></div><div class="clear"></div><div id="comment-17994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18010"></span>

<div id="answer-container-18010" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18010-score" class="post-score" title="current number of votes">0</div><span id="post-18010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3046">bug 3046</a> to me. The work-around is to follow the advice that <a href="http://ask.wireshark.org/users/145/jasper">Jasper</a> provided.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '13, 11:22</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18010" class="comments-container"></div><div id="comment-tools-18010" class="comment-tools"></div><div class="clear"></div><div id="comment-18010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

