+++
type = "question"
title = "Bug: Broken link to ChExtcapOptions.html on start-up screen"
description = '''At home I see the following options on the start-up screen:  Cisco remote capture: cisco. [I use some Cisco tools on my home network.] Random packet generator: randpkt SSH remote capture: ssh  There is a gear icon to the left of these options, and clicking it opens an &quot;Extcap Interface Options&quot; dial...'''
date = "2016-09-25T09:30:00Z"
lastmod = "2016-09-25T10:23:00Z"
weight = 55815
keywords = [ "bug", "extcap" ]
aliases = [ "/questions/55815" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bug: Broken link to ChExtcapOptions.html on start-up screen](/questions/55815/bug-broken-link-to-chextcapoptionshtml-on-start-up-screen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55815-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At home I see the following options on the start-up screen:</p><ul><li>Cisco remote capture: <code>cisco</code>. [I use some Cisco tools on my home network.]</li><li>Random packet generator: <code>randpkt</code></li><li>SSH remote capture: <code>ssh</code></li></ul><p>There is a gear icon to the left of these options, and clicking it opens an "Extcap Interface Options" dialog box, with various fields populated. In all cases the help button requests a <code>ChExtcapOptions.html</code> page that receives a 404 response.</p><p>The full URL is <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChExtcapOptions.html.">https://www.wireshark.org/docs/wsug_html_chunked/ChExtcapOptions.html.</a> There doesn't seem to be any mention of <code>extcap</code> on the WSUG page that opens at <a href="https://www.wireshark.org/docs/wsug_html_chunked/.">https://www.wireshark.org/docs/wsug_html_chunked/.</a> I see the <code>ChExtcapOptions.html</code> page listed in only one place in the source (master branch): <a href="https://github.com/wireshark/wireshark/blob/master/ui/help_url.c#L268.">https://github.com/wireshark/wireshark/blob/master/ui/help_url.c#L268.</a></p><p>I've posted here because I don't have access to Issues on the GitHub account. I'm on Version 2.2.0 (v2.2.0-0-g5368c50 from master-2.2 (Mac OS 10.9.5.)</p></div><div id="question-tags" class="tags-container tags">bug extcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '16, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/da35e7e2db9ab4fc170fc4ae039ab62b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brannerchinese&#39;s gravatar image" /><p>brannerchinese<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brannerchinese has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '16, 09:34</p></div></div><div id="comments-container-55815" class="comments-container"></div><div id="comment-tools-55815" class="comment-tools"></div><div class="clear"></div><div id="comment-55815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55816"></span>

<div id="answer-container-55816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55816-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark Github account is a remote mirror of the main Git <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree">repo</a>, so don't bother with raising pull requests or issues there.</p><p>The commit that added that code was change <a href="https://code.wireshark.org/review/#/c/8224/21">8224</a> and a comment was made on the change that the page was being worked on.</p><p>To raise an issue use the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a>, as detailed on the <a href="https://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> page on the wiki.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '16, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '16, 10:27</p></div></div><div id="comments-container-55816" class="comments-container"></div><div id="comment-tools-55816" class="comment-tools"></div><div class="clear"></div><div id="comment-55816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

