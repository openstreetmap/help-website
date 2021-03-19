+++
type = "question"
title = "How does save as work in wireshark ??"
description = '''I would like to know how wireshark can save the capture in different formats '''
date = "2011-10-24T22:53:00Z"
lastmod = "2011-10-25T01:01:00Z"
weight = 7057
keywords = [ "save" ]
aliases = [ "/questions/7057" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How does save as work in wireshark ??](/questions/7057/how-does-save-as-work-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7057-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know how wireshark can save the capture in different formats</p></div><div id="question-tags" class="tags-container tags">save</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '11, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-7057" class="comments-container"><span id="7138"></span><div id="comment-7138" class="comment"><div id="post-7138-score" class="comment-score">1</div><div class="comment-text"><p>How to set a different format as the default one? I mean where can i Hardcode this?</p></div><div id="comment-7138-info" class="comment-info"><span class="comment-age">(28 Oct '11, 03:19)</span> Sriramula Ra...</div></div></div><div id="comment-tools-7057" class="comment-tools"></div><div class="clear"></div><div id="comment-7057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7058"></span>

<div id="answer-container-7058" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7058-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you want to know how it works internally, or how you use it at all?</p><p>Using it is simple, just use File -&gt; Save File As, and set the "Save as Type" to whatever file format you need. In the packet range you can chose just to save the packets currently displayed (if there is a filter), or some specific packet ranges. Since this is so simple, I guess you already figured that one out (but just in case...)</p><p>The other thing - how Wireshark can save in different formats isn't that complicated either - there are a couple of modules that "know" how (in what format, meaning structures etc.) the other network analyzers write their files, and mimics it. It's basically the same like the loading routines, which do the same with loading various file formats; they have "knowledge" of the file structure and interpret the data being read.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '11, 01:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7058" class="comments-container"><span id="7094"></span><div id="comment-7094" class="comment"><div id="post-7094-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick reply ...Yes i wanted to know how it worked internally ..I also wanted to know what are the files it has relation with ...When i do save as i would like k12 textfile format to come first i would like to hardcode it ..Is it possible !!</p></div><div id="comment-7094-info" class="comment-info"><span class="comment-age">(27 Oct '11, 04:17)</span> flashkicker</div></div><span id="7095"></span><div id="comment-7095" class="comment"><div id="post-7095-score" class="comment-score">1</div><div class="comment-text"><p>The issue with hard-coding your own solution is that you'll have to keep rebuilding your own version of WS each time a new one comes out.</p><p>While I don't think hard-coding k12 textfile format would be acceptable to all the other users of WS, a preference to select the default save format might be.</p><p>Raise an entry for this on the WS <a href="https://bugs.wireshark.org/bugzilla/">bugtracker</a> and mark it as an enhancement.</p></div><div id="comment-7095-info" class="comment-info"><span class="comment-age">(27 Oct '11, 04:35)</span> grahamb ♦</div></div></div><div id="comment-tools-7058" class="comment-tools"></div><div class="clear"></div><div id="comment-7058-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

