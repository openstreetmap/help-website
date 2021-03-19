+++
type = "question"
title = "wireshark stops responding shortly after beginning capture"
description = '''Recently i&#x27;ve seen that soon after beginning a capture, wireshark stops responding and I can&#x27;t use any of the functions. I&#x27;ve installed the most recent stable version (2.2.7) 64-bit for Windows 10 and re-installed WinPCAP, but this didn&#x27;t fix the problem. Any ideas?'''
date = "2017-06-15T12:21:00Z"
lastmod = "2017-06-17T12:33:00Z"
weight = 62050
keywords = [ "not", "responding" ]
aliases = [ "/questions/62050" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark stops responding shortly after beginning capture](/questions/62050/wireshark-stops-responding-shortly-after-beginning-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62050-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently i've seen that soon after beginning a capture, wireshark stops responding and I can't use any of the functions. I've installed the most recent stable version (2.2.7) 64-bit for Windows 10 and re-installed WinPCAP, but this didn't fix the problem. Any ideas?</p></div><div id="question-tags" class="tags-container tags">not responding</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '17, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/166fe471776b0bb86b0c9c48873f0d50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jkoelker&#39;s gravatar image" /><p>jkoelker<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jkoelker has no accepted answers">0%</span></p></div></div><div id="comments-container-62050" class="comments-container"><span id="62136"></span><div id="comment-62136" class="comment"><div id="post-62136-score" class="comment-score"></div><div class="comment-text"><p>Do you have a rough idea of what amount of traffic is passing through the interface at which you capture? What happens if you capture with a highly restrictive capture filter such as <code>icmp</code>, and then you ping some address so that at least something is captured?</p><p>Incidentally, there is also <a href="https://ask.wireshark.org/questions/58009/excessive-memory-usage-with-wireshark-222/62049">an answer to another question</a> which may be an answer to yours as well.</p></div><div id="comment-62136-info" class="comment-info"><span class="comment-age">(19 Jun '17, 12:59)</span> sindy</div></div></div><div id="comment-tools-62050" class="comment-tools"></div><div class="clear"></div><div id="comment-62050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62080"></span>

<div id="answer-container-62080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62080-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would probably reinstall the whole thing (such as follow the uninstall manual) and reinstall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '17, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/9d3bbaecde4b7da8c3fd26d75393c1b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shr00msz&#39;s gravatar image" /><p>shr00msz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shr00msz has no accepted answers">0%</span></p></div></div><div id="comments-container-62080" class="comments-container"><span id="62119"></span><div id="comment-62119" class="comment"><div id="post-62119-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I've tried doing that a couple of times but it hasn't resolved the problem. I even downloaded and installed an older version thinking that might help, but it didn't. Having run wireshark on another computer without issue, I have to conclude that this is likely a problem with my particular machine - maybe some sort of registry setting that's got a bit flipped. Not a huge deal - I'll be replacing this laptop in the near future anyway.</p><p>Thanks.</p></div><div id="comment-62119-info" class="comment-info"><span class="comment-age">(19 Jun '17, 05:20)</span> jkoelker</div></div><span id="62147"></span><div id="comment-62147" class="comment"><div id="post-62147-score" class="comment-score"></div><div class="comment-text"><p>Alright, If your later laptop doesn't work, it might be wireshark's end, or maybe some compatibility issue.</p></div><div id="comment-62147-info" class="comment-info"><span class="comment-age">(19 Jun '17, 19:00)</span> shr00msz</div></div></div><div id="comment-tools-62080" class="comment-tools"></div><div class="clear"></div><div id="comment-62080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

