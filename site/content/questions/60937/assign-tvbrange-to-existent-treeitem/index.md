+++
type = "question"
title = "Assign TVBrange to existent treeitem"
description = '''Hi, I created a treeitem without tvbrange specified (because by the time of creation I don&#x27;t know the beginning of tvbrange. Then I start decoding, moving from the end of packet to start direction (this is a feature of that proprietary protocol), adding sub-items to the treeitem, this time with tvbr...'''
date = "2017-04-20T21:59:00Z"
lastmod = "2017-04-20T21:59:00Z"
weight = 60937
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/60937" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Assign TVBrange to existent treeitem](/questions/60937/assign-tvbrange-to-existent-treeitem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60937-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I created a treeitem without tvbrange specified (because by the time of creation I don't know the beginning of tvbrange. Then I start decoding, moving from the end of packet to start direction (this is a feature of that proprietary protocol), adding sub-items to the treeitem, this time with tvbrange. Finally, when all sub-items are decoded and added to the original treeitem, I know total treeitem size and it's beginning. So now I would like to specify tvbrange to the treeitem to make it highlighted when selected. Is there any way to do it?</p><p>In developer-guide I can only see treeitem:setlen(), treeitem:settext(), ... but nothing for set beginning of tvb range.</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '17, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/7b432318b5dbe445b296505f9f7f1c3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maximk&#39;s gravatar image" /><p>maximk<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maximk has no accepted answers">0%</span></p></div></div><div id="comments-container-60937" class="comments-container"></div><div id="comment-tools-60937" class="comment-tools"></div><div class="clear"></div><div id="comment-60937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

