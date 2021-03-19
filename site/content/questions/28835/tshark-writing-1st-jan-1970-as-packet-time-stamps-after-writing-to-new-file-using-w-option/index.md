+++
type = "question"
title = "tshark writing 1st jan 1970 as packet time stamps after writing to new file using -w option"
description = '''Hi All, Iam getting strange issue, when iam trying to split file using -R filter and writing to a new file, all packets for time stamp are marked as 1st Jan 1970. Below is the command iam using. ./tshark.exe -n -r time_issue.pcapng -2 -R &#x27;!gtp&amp;amp;&amp;amp;!icmp&amp;amp;&amp;amp;dns&#x27; -w time_issueSplit2.pcapng ...'''
date = "2014-01-13T02:41:00Z"
lastmod = "2014-01-13T06:57:00Z"
weight = 28835
keywords = [ "tshark" ]
aliases = [ "/questions/28835" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark writing 1st jan 1970 as packet time stamps after writing to new file using -w option](/questions/28835/tshark-writing-1st-jan-1970-as-packet-time-stamps-after-writing-to-new-file-using-w-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28835-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, Iam getting strange issue, when iam trying to split file using -R filter and writing to a new file, all packets for time stamp are marked as 1st Jan 1970. Below is the command iam using. ./tshark.exe -n -r time_issue.pcapng -2 -R '!gtp&amp;&amp;!icmp&amp;&amp;dns' -w time_issueSplit2.pcapng</p><p>Iam Using TShark 1.10.5 (SVN Rev 54262 from /trunk-1.10) does any body have any idea why its happining.</p><p>Thanx a Lot</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '14, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/6e2c174538a70ebd24ccfd974c476351?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saji%20Nair&#39;s gravatar image" /><p>Saji Nair<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saji Nair has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '14, 21:35</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-28835" class="comments-container"></div><div id="comment-tools-28835" class="comment-tools"></div><div class="clear"></div><div id="comment-28835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28839"></span>

<div id="answer-container-28839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28839-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can <strong>confirm</strong> that behavior. <strong>However</strong>, it only happens with <code>-2 -R</code> and not with <code>-Y</code> (should also work in your case).</p><p>Please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '14, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28839" class="comments-container"></div><div id="comment-tools-28839" class="comment-tools"></div><div class="clear"></div><div id="comment-28839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

