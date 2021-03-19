+++
type = "question"
title = "&quot;Can&#x27;t dissect FP frame because no per-frame info was attached! over TCP"
description = '''Hi ,i am unable to dissect fp frame packet over tcp anw we got the error &quot;&quot;Can&#x27;t dissect FP frame because no per-frame info was attached!&quot; plz responce'''
date = "2013-05-24T02:43:00Z"
lastmod = "2013-05-24T04:03:00Z"
weight = 21438
keywords = [ "umts-fp" ]
aliases = [ "/questions/21438" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# ["Can't dissect FP frame because no per-frame info was attached! over TCP](/questions/21438/cant-dissect-fp-frame-because-no-per-frame-info-was-attached-over-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21438-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,i am unable to dissect fp frame packet over tcp anw we got the error ""Can't dissect FP frame because no per-frame info was attached!" plz responce</p></div><div id="question-tags" class="tags-container tags">umts-fp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '13, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/5fa560f4e928cb2036f850a4fa37c869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ranjeet%20Nag&#39;s gravatar image" /><p>Ranjeet Nag<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ranjeet Nag has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 May '13, 02:49</p></div></div><div id="comments-container-21438" class="comments-container"></div><div id="comment-tools-21438" class="comment-tools"></div><div class="clear"></div><div id="comment-21438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21440"></span>

<div id="answer-container-21440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21440-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I thought FP was transgered over UDP only, but in general se athe similar questions <a href="http://ask.wireshark.org/tags/umts-fp/">http://ask.wireshark.org/tags/umts-fp/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-21440" class="comments-container"></div><div id="comment-tools-21440" class="comment-tools"></div><div class="clear"></div><div id="comment-21440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21441"></span>

<div id="answer-container-21441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21441-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See: <a href="http://wiki.wireshark.org/FP">http://wiki.wireshark.org/FP</a></p><p>More specifically: The FP dissector is mostly functional, but can currently only be invoked while reading Catapult DCT2000 or Tektronix K12 format traces (these contain the additional information needed in order to properly decode the frames). It would be possible, but challenging, to decode the RRC messages describing the configuration of the lower layers, and use this information to infer how each FP frame should be decoded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-21441" class="comments-container"><span id="21442"></span><div id="comment-21442" class="comment"><div id="post-21442-score" class="comment-score"></div><div class="comment-text"><p>It actually works partly if NBAP and RRC signaling is present.</p></div><div id="comment-21442-info" class="comment-info"><span class="comment-age">(24 May '13, 04:31)</span> Anders ♦</div></div><span id="21443"></span><div id="comment-21443" class="comment"><div id="post-21443-score" class="comment-score"></div><div class="comment-text"><p>Then we should update the Wiki page ;)</p></div><div id="comment-21443-info" class="comment-info"><span class="comment-age">(24 May '13, 05:09)</span> Pascal Quantin</div></div><span id="24201"></span><div id="comment-24201" class="comment"><div id="post-24201-score" class="comment-score"></div><div class="comment-text"><p>How can we determine if RRC signalling is present? Is it as straightforward as seeing packets labelled as RRC? Or does it require some decoding?</p></div><div id="comment-24201-info" class="comment-info"><span class="comment-age">(30 Aug '13, 08:51)</span> davide0089</div></div></div><div id="comment-tools-21441" class="comment-tools"></div><div class="clear"></div><div id="comment-21441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

