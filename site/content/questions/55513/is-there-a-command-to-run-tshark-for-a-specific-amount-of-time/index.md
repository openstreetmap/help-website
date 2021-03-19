+++
type = "question"
title = "Is there a command to run tshark for a specific amount of time?"
description = '''Is there a command to tell tshark to capture for, say, 15 minutes then stop? '''
date = "2016-09-13T01:21:00Z"
lastmod = "2016-09-13T07:19:00Z"
weight = 55513
keywords = [ "runtime", "tshark", "timeout" ]
aliases = [ "/questions/55513" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a command to run tshark for a specific amount of time?](/questions/55513/is-there-a-command-to-run-tshark-for-a-specific-amount-of-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a command to tell tshark to capture for, say, 15 minutes then stop?</p></div><div id="question-tags" class="tags-container tags">runtime tshark timeout</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '16, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/3ab01be5b3ec231ca1b6fee9c0c27582?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elektrovert&#39;s gravatar image" /><p>elektrovert<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elektrovert has no accepted answers">0%</span></p></div></div><div id="comments-container-55513" class="comments-container"></div><div id="comment-tools-55513" class="comment-tools"></div><div class="clear"></div><div id="comment-55513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55522"></span>

<div id="answer-container-55522" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55522-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to have <code>tshark</code> capture for 15 minutes and then stop, you need to use the <em>autostop</em> "<code>-a duration:900</code>" option, not the <em>ringbuffer</em> "<code>-b duration:900</code>" option.</p><p>Refer to the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> or <a href="https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html">tshark section of the user guide</a> for more information on this and other <code>tshark</code> options.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '16, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-55522" class="comments-container"><span id="55523"></span><div id="comment-55523" class="comment"><div id="post-55523-score" class="comment-score"></div><div class="comment-text"><p>Right, my bad... I was too quick with this...</p></div><div id="comment-55523-info" class="comment-info"><span class="comment-age">(13 Sep '16, 07:22)</span> Jasper ♦♦</div></div><span id="55547"></span><div id="comment-55547" class="comment"><div id="post-55547-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I'll try this</p></div><div id="comment-55547-info" class="comment-info"><span class="comment-age">(13 Sep '16, 23:30)</span> elektrovert</div></div></div><div id="comment-tools-55522" class="comment-tools"></div><div class="clear"></div><div id="comment-55522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55514"></span>

<div id="answer-container-55514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55514-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>yes, use the -b option with duration:NUM, where NUM is a number of seconds. In your case 15*60.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '16, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-55514" class="comments-container"><span id="55515"></span><div id="comment-55515" class="comment"><div id="post-55515-score" class="comment-score"></div><div class="comment-text"><p>Many thanks!</p></div><div id="comment-55515-info" class="comment-info"><span class="comment-age">(13 Sep '16, 01:24)</span> elektrovert</div></div></div><div id="comment-tools-55514" class="comment-tools"></div><div class="clear"></div><div id="comment-55514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

