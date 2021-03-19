+++
type = "question"
title = "Wireshark crash after launch"
description = '''Hi I&#x27;m trying to use wireshark but if I open the program, it closed it self immediately. Doesn&#x27;t know if I have to install something else in order to make it work. My system: Mac os X 10.10.3 Thanks to everyone who can help me :-)'''
date = "2015-07-14T20:14:00Z"
lastmod = "2015-07-14T20:14:00Z"
weight = 44160
keywords = [ "mac", "macosx", "crash" ]
aliases = [ "/questions/44160" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crash after launch](/questions/44160/wireshark-crash-after-launch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44160-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to use wireshark but if I open the program, it closed it self immediately. Doesn't know if I have to install something else in order to make it work. My system: Mac os X 10.10.3</p><p>Thanks to everyone who can help me :-)</p></div><div id="question-tags" class="tags-container tags">mac macosx crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '15, 20:14</strong></p><img src="https://secure.gravatar.com/avatar/9b5f4312ea7101eb684468be78ddb093?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TrueVegas&#39;s gravatar image" /><p>TrueVegas<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TrueVegas has no accepted answers">0%</span></p></div></div><div id="comments-container-44160" class="comments-container"><span id="44161"></span><div id="comment-44161" class="comment"><div id="post-44161-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark is this?</p><p>If it's not 1.99.x, what's printed if you open up Terminal and run <code>ls -l d/usr/X11</code>?</p><p>If it's 1.99.x, or if it's not and <code>ls -ld /usr/X11</code> reports something like</p><pre><code>lrwxr-xr-x  1 root  wheel  8 May 24 11:49 /usr/X11 -&gt; /opt/X11</code></pre><p>(the date and time may be different), does it pop up a crash report message when it crashes? If so, what does it say? If not, if you open Console, in Utilities, and look under User Diagnostic Reports, are there any for Wireshark? If so, what do they say?</p></div><div id="comment-44161-info" class="comment-info"><span class="comment-age">(14 Jul '15, 21:52)</span> Guy Harris ♦♦</div></div><span id="44170"></span><div id="comment-44170" class="comment"><div id="post-44170-score" class="comment-score"></div><div class="comment-text"><p>I have similar problems and opened a bug for it: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11367">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11367</a></p></div><div id="comment-44170-info" class="comment-info"><span class="comment-age">(15 Jul '15, 04:51)</span> jmayer</div></div><span id="44181"></span><div id="comment-44181" class="comment"><div id="post-44181-score" class="comment-score"></div><div class="comment-text"><p>@jmayer 1) that's a hang, not a crash and 2) you built it yourself, with a Qt you installed in /usr/local, so there may be a difference, especially if TrueVegas is using 1.12.x (in which case I suspect <code>ls -ld /usr/X11</code> will report that there's "No such file or directory").</p></div><div id="comment-44181-info" class="comment-info"><span class="comment-age">(15 Jul '15, 11:17)</span> Guy Harris ♦♦</div></div><span id="44212"></span><div id="comment-44212" class="comment"><div id="post-44212-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris No I have no report and I tried to execute the second line commands with the same output you said (but obviously different date) In console no Wiresharks logs, maybe I'm talking about a crash but it is not really a crash?</p></div><div id="comment-44212-info" class="comment-info"><span class="comment-age">(16 Jul '15, 10:09)</span> TrueVegas</div></div><span id="44215"></span><div id="comment-44215" class="comment"><div id="post-44215-score" class="comment-score"></div><div class="comment-text"><p>OK, so what was printed when you ran <code>ls -ld /usr/X11</code>?</p></div><div id="comment-44215-info" class="comment-info"><span class="comment-age">(16 Jul '15, 11:47)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-44160" class="comment-tools"></div><div class="clear"></div><div id="comment-44160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

