+++
type = "question"
title = "Wireshark-QT - Unable to change timestamp presentation format?"
description = '''I am running Wireshark-QT 1.12.0 on OSX 10.9.4. The Wireshark User&#x27;s Guide refers to being able to select different time presentation formats: https://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html However, when I go to the view menu on Wireshark-QT, this is all I see:  Is th...'''
date = "2014-08-21T19:35:00Z"
lastmod = "2014-08-22T11:09:00Z"
weight = 35664
keywords = [ "timestamp", "qt" ]
aliases = [ "/questions/35664" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark-QT - Unable to change timestamp presentation format?](/questions/35664/wireshark-qt-unable-to-change-timestamp-presentation-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running Wireshark-QT 1.12.0 on OSX 10.9.4.</p><p>The Wireshark User's Guide refers to being able to select different time presentation formats:</p><p><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html">https://www.wireshark.org/docs/wsug_html_chunked/ChWorkTimeFormatsSection.html</a></p><p>However, when I go to the view menu on Wireshark-QT, this is all I see:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-08-22_at_12.32.18_pm.png" alt="alt text" /></p><p>Is this simply a feature that hasn't been ported across to Wireshark-QT yet? It seems like a pretty fundamental feature of Wireshark. Is there any other way of changing the timezone column in Wireshark-QT so that it shows the actual timestamp of a packet? This is very useful to correlate events in a packet capture against other events (e.g. loglines, or real-world events).</p><p>Or could there be something funny with the PCAP file I have?</p><p>The commandline that I believe was used to capture the PCAP file was:</p><p><code>sudo tcpdump -Xs0 -Nnpi &lt;INTERFACE&gt; tcp port &lt;PORT&gt; -w &lt;CAPTURE_FILENAME&gt;</code></p></div><div id="question-tags" class="tags-container tags">timestamp qt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '14, 19:35</strong></p><img src="https://secure.gravatar.com/avatar/7c0fa8fb73fe4c951ea79b476007c77d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="victorhooi&#39;s gravatar image" /><p>victorhooi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="victorhooi has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '14, 00:51</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35664" class="comments-container"></div><div id="comment-tools-35664" class="comment-tools"></div><div class="clear"></div><div id="comment-35664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35680"></span>

<div id="answer-container-35680" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35680-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that feature simply seems to not have been ported yet. For the time being you might just go to the preferences and add/change the time columns you need. I usually have three: absolute date &amp; time, delta time displayed, and relative time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '14, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35680" class="comments-container"><span id="37142"></span><div id="comment-37142" class="comment"><div id="post-37142-score" class="comment-score"></div><div class="comment-text"><p>Jasper gives the correct answer so just a nuance. On my mac/Qt version I had to restart Wireshark for the changes to take affect.</p></div><div id="comment-37142-info" class="comment-info"><span class="comment-age">(17 Oct '14, 15:32)</span> Briford</div></div></div><div id="comment-tools-35680" class="comment-tools"></div><div class="clear"></div><div id="comment-35680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

