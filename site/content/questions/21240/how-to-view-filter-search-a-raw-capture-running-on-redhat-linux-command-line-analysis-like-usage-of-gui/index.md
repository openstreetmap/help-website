+++
type = "question"
title = "How to view, filter, search a raw capture running on RedHat Linux / Command line analysis like usage of GUI"
description = '''I basically want to type in a string to search a raw capture within Linux vs GUI. How is the possible? what are all the commands(within reason)? '''
date = "2013-05-17T13:14:00Z"
lastmod = "2013-05-17T17:00:00Z"
weight = 21240
keywords = [ "capture", "analysis", "linux" ]
aliases = [ "/questions/21240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to view, filter, search a raw capture running on RedHat Linux / Command line analysis like usage of GUI](/questions/21240/how-to-view-filter-search-a-raw-capture-running-on-redhat-linux-command-line-analysis-like-usage-of-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21240-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I basically want to type in a string to search a raw capture within Linux vs GUI. How is the possible? what are all the commands(within reason)?</p></div><div id="question-tags" class="tags-container tags">capture analysis linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/cf7dcb7ac4cc7a6548cb76a447b22c14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vurcos&#39;s gravatar image" /><p>Vurcos<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vurcos has no accepted answers">0%</span></p></div></div><div id="comments-container-21240" class="comments-container"></div><div id="comment-tools-21240" class="comment-tools"></div><div class="clear"></div><div id="comment-21240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21249"></span>

<div id="answer-container-21249" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21249-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could try the following display filter:</p><p><code>frame contains "YourString"</code></p><p>either in the Wireshark GUI, or as value to the parameter "-R" when running tshark, e.g. <code>tshark -r "capturefile.pcap" -R "frame contains \"YourString\""</code>.</p><p>If you use quotation marks within a filter on the command line you need to escape them with a backslash, as seen in the example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21249" class="comments-container"></div><div id="comment-tools-21249" class="comment-tools"></div><div class="clear"></div><div id="comment-21249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

