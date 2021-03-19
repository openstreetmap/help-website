+++
type = "question"
title = "dumpcap invalid argument for port number"
description = '''I&#x27;ve tried this in different variations but every time it comes up with the same message &quot;Invalid argument: 5003&quot; dumpcap -i en0 -f “dst port 5003 and src port 5003” -b duration:3600 -b files:25 -w fmpackets.cap using in Mac OSX terminal.'''
date = "2013-11-26T14:24:00Z"
lastmod = "2013-11-26T14:39:00Z"
weight = 27450
keywords = [ "capture-filter", "dumpcap" ]
aliases = [ "/questions/27450" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [dumpcap invalid argument for port number](/questions/27450/dumpcap-invalid-argument-for-port-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27450-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've tried this in different variations but every time it comes up with the same message "Invalid argument: 5003"</p><p>dumpcap -i en0 -f “dst port 5003 and src port 5003” -b duration:3600 -b files:25 -w fmpackets.cap</p><p>using in Mac OSX terminal.</p></div><div id="question-tags" class="tags-container tags">capture-filter dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '13, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/f1bafaeecb80dd566876022697e94723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dumpy&#39;s gravatar image" /><p>Dumpy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dumpy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '13, 14:33</p></div></div><div id="comments-container-27450" class="comments-container"></div><div id="comment-tools-27450" class="comment-tools"></div><div class="clear"></div><div id="comment-27450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27456"></span>

<div id="answer-container-27456" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27456-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>dumpcap -i en0 -f “dst port 5003 and src port 5003” -b duration:3600 -b files:25 -w fmpackets.cap</code></pre><p>Try, instead</p><pre><code>dumpcap -i en0 -f &quot;dst port 5003 and src port 5003&quot; -b duration:3600 -b files:25 -w fmpackets.cap</code></pre><p>I.e., use regular ASCII quote marks, not opening and closing Unicode quotation marks; the command-line interpreters on OS X only allow ASCII single and double quotes as quote marks, just as they do on every other UN*X (because they're the <em>same</em> command-line interpreters as on other UN*Xes:</p><pre><code>$ bash --version
GNU bash, version 3.2.48(1)-release (x86_64-apple-darwin12)
Copyright (C) 2007 Free Software Foundation, Inc.
$ ksh --version
  version         sh (AT&amp;T Research) 93u 2011-02-08
$ tcsh --version
tcsh 6.17.00 (Astron) 2009-07-10 (x86_64-apple-darwin) options wide,nls,dl,al,kan,sm,rh,color,filec
$ zsh --version
zsh 4.3.11 (i386-apple-darwin12.0)</code></pre><p>on Mountain Lion, for example). They do not allow “ or ” to be used to quote strings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27456" class="comments-container"><span id="27461"></span><div id="comment-27461" class="comment"><div id="post-27461-score" class="comment-score"></div><div class="comment-text"><p>That was it!!! Thank you!!</p></div><div id="comment-27461-info" class="comment-info"><span class="comment-age">(26 Nov '13, 22:16)</span> Dumpy</div></div></div><div id="comment-tools-27456" class="comment-tools"></div><div class="clear"></div><div id="comment-27456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

