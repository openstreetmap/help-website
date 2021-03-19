+++
type = "question"
title = "Conversation duration calculated without taking the final FIN/ACKs into account"
description = '''Statistics-&amp;gt;Conversation-&amp;gt;duration is a godsend, i don&#x27;t deny that. But it has one flaw (intended by design) : it calculates conversation duration upto (and including) the final closing FINs/ACKs. When the daemon/client/server whatever takes his time cleaning up used connections, this has the ...'''
date = "2014-11-25T08:19:00Z"
lastmod = "2014-11-25T08:31:00Z"
weight = 38125
keywords = [ "duration", "fin" ]
aliases = [ "/questions/38125" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Conversation duration calculated without taking the final FIN/ACKs into account](/questions/38125/conversation-duration-calculated-without-taking-the-final-finacks-into-account)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38125-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Statistics-&gt;Conversation-&gt;duration is a godsend, i don't deny that. But it has one flaw (intended by design) : it calculates conversation duration upto (and including) the final closing FINs/ACKs.</p><p>When the daemon/client/server whatever takes his time cleaning up used connections, this has the unintended consequence of making it harder to find 'abnormal long' connexions, because they are flooded among the 'long' connections which are only due to final close packets.</p><p>My first though was to try and filter out FIN packets, hoping the duration would be adjusted, but it doesn't work, as there are one/two ACK packets <em>after</em> the FIN which i couldn't remove in batch.</p><p>So being stuck here with 25k connections to analyze, i'm coming here for help, and to throw the idea for a little tweak in duration calculations.</p><p><strong>Example #1</strong> : 'abnormaly long' connection** which i want to quickly find</p><p>Client opens connection, waits 3 seconds to sent his GET Then sends it, fetchs the reply, and closes the connection immediately</p><p>This one lasts ~3 sec, due to a the client taking his time before sending the request)</p><p><strong>Example #2</strong> : normal 'long' connection</p><p>Client opens connection, sends get ASAP, get reply ASAP, no problem there.</p><p>Then either the client or the server wait a few (or a bunch) of seconds before closing the connection (let's say 3 sec for the sake of the example)</p><p>So the FIN/ACK + ACKs begin 3s after the last payload packet. And the total duration of the connection is ~3 seconds too, due only to the idle time before closing. <em>BUT</em> the interesting parts of that connection might only have accounted for 0.1 sec !</p><p><strong>My point of view</strong> : let's say i'm looking fo the 'real' slow connection, and let's say that i have 25k connections to filter, i'm back to finding a needle in a haystack. Being able to modify the way the duration is displayed (or calculated, temporarily or not) would make able to spot the "real slow" connections without sifting through the delayed close clutter.</p><p>Basically, a checkbox in the conversation pane to modify the duration calculation to calculate it up to the last packet before the first FIN, or something alike, would be perfect.</p><p><em>Or a similar way to achieve this result, of course !</em></p><p>Thanks in advance for your help, hints, tips or thoughs.</p></div><div id="question-tags" class="tags-container tags">duration fin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '14, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/9b19b7f4d2913d3af6a25f4d1ea94f28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nipil&#39;s gravatar image" /><p>nipil<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nipil has no accepted answers">0%</span></p></div></div><div id="comments-container-38125" class="comments-container"></div><div id="comment-tools-38125" class="comment-tools"></div><div class="clear"></div><div id="comment-38125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38127"></span>

<div id="answer-container-38127" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38127-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think this kind of duration calculation is probably not easy to implement, because it needs a little fuzzy logic to determine if a delay is normal or abnormal. This is also more of a feature request that would have to be put into the <a href="http://bugs.wireshark.org">bug tracker</a>.</p><p>Since you describe your problem as trying to track down client delays before issuing GET requests you may be able to leverage something like the <a href="http://www.tribelabzero.com/transum">transum</a> plugin to do what you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38127" class="comments-container"></div><div id="comment-tools-38127" class="comment-tools"></div><div class="clear"></div><div id="comment-38127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

