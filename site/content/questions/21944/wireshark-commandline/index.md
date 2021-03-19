+++
type = "question"
title = "wireshark commandline"
description = '''When following command executed wireshark -i &#92;DEVICE&#92;NPF_{42C75388-2A3B-4C42-B581-F1E7604B7255} -k -f port 80 -c 10 wireshark:You can&#x27;t specify both a live capture and a capture file to be read. Any reason for this message'''
date = "2013-06-11T20:44:00Z"
lastmod = "2013-06-11T23:44:00Z"
weight = 21944
keywords = [ "commandline" ]
aliases = [ "/questions/21944" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark commandline](/questions/21944/wireshark-commandline)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21944-score" class="post-score" title="current number of votes">0</div><span id="post-21944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When following command executed</p><p>wireshark -i \DEVICE\NPF_{42C75388-2A3B-4C42-B581-F1E7604B7255} -k -f port 80 -c 10</p><p>wireshark:You can't specify both a live capture and a capture file to be read.</p><p>Any reason for this message</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-commandline" rel="tag" title="see questions tagged &#39;commandline&#39;">commandline</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '13, 20:44</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '13, 20:54</strong> </span></p></div></div><div id="comments-container-21944" class="comments-container"></div><div id="comment-tools-21944" class="comment-tools"></div><div class="clear"></div><div id="comment-21944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21948"></span>

<div id="answer-container-21948" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21948-score" class="post-score" title="current number of votes">2</div><span id="post-21948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to contain the capture filter in quotes:</p><p>wireshark -i \DEVICE\NPF_{42C75388-2A3B-4C42-B581-F1E7604B7255} -k -f "port 80" -c 10</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-21948" class="comments-container"><span id="21949"></span><div id="comment-21949" class="comment"><div id="post-21949-score" class="comment-score"></div><div class="comment-text"><p>Thanks it worked but wireshark -i \DEVICE\NPF_{42C75388-2A3B-4C42-B581-F1E7604B7255} -k -f tcp -c 10 is working with out any quotes.</p></div><div id="comment-21949-info" class="comment-info"><span class="comment-age">(11 Jun '13, 21:05)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="21950"></span><div id="comment-21950" class="comment"><div id="post-21950-score" class="comment-score"></div><div class="comment-text"><p>That one works without quotes because there is no space in it. If you have spaces, you need quotes to contain it otherwise it thinks "port" is your capture filter and it doesn't know what 80 is.</p></div><div id="comment-21950-info" class="comment-info"><span class="comment-age">(11 Jun '13, 21:10)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="21956"></span><div id="comment-21956" class="comment"><div id="post-21956-score" class="comment-score">1</div><div class="comment-text"><p>Another note, if you run <code>tshark -D</code> you will get a list of the configured adaptors ordered by "index" and that index number can be used in place of the \Device\NPF_{GUID} string, e.g. <code>tshark -i 1 ...</code></p></div><div id="comment-21956-info" class="comment-info"><span class="comment-age">(11 Jun '13, 23:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-21948" class="comment-tools"></div><div class="clear"></div><div id="comment-21948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

