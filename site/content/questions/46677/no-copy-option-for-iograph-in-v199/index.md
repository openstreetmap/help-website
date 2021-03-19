+++
type = "question"
title = "No copy option for iograph in v1.99?"
description = '''Previous versions of wireshark you could copy the x,y values in csv style from the iograph feature, to use in other graphing software. That button has been removed in version 1.99, and I can&#x27;t find similar functionality elsewhere in wireshark. Has this function been removed?'''
date = "2015-10-18T14:59:00Z"
lastmod = "2015-10-19T01:48:00Z"
weight = 46677
keywords = [ "copy", "csv", "iograph" ]
aliases = [ "/questions/46677" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [No copy option for iograph in v1.99?](/questions/46677/no-copy-option-for-iograph-in-v199)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46677-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Previous versions of wireshark you could copy the x,y values in csv style from the iograph feature, to use in other graphing software. That button has been removed in version 1.99, and I can't find similar functionality elsewhere in wireshark. Has this function been removed?</p></div><div id="question-tags" class="tags-container tags">copy csv iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '15, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/f94457aed80c398e4355dd7d2f69a780?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fruglemonkey&#39;s gravatar image" /><p>fruglemonkey<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fruglemonkey has no accepted answers">0%</span></p></div></div><div id="comments-container-46677" class="comments-container"></div><div id="comment-tools-46677" class="comment-tools"></div><div class="clear"></div><div id="comment-46677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46686"></span>

<div id="answer-container-46686" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46686-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's still present in the GTK+ code, but it's absent from the Qt code; the default UI toolkit for 1.99/2.x is Qt, so it's not present in the default versions of Wireshark.</p><p>Please file a bug on this on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, so that the lack of "Copy" functionality is recorded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '15, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-46686" class="comments-container"><span id="46687"></span><div id="comment-46687" class="comment"><div id="post-46687-score" class="comment-score"></div><div class="comment-text"><p>Filed here: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11613">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11613</a></p></div><div id="comment-46687-info" class="comment-info"><span class="comment-age">(19 Oct '15, 02:06)</span> fruglemonkey</div></div><span id="46722"></span><div id="comment-46722" class="comment"><div id="post-46722-score" class="comment-score"></div><div class="comment-text"><p>Thanks, ended up using the GTK version and it was present as you said.</p></div><div id="comment-46722-info" class="comment-info"><span class="comment-age">(19 Oct '15, 15:04)</span> fruglemonkey</div></div></div><div id="comment-tools-46686" class="comment-tools"></div><div class="clear"></div><div id="comment-46686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

