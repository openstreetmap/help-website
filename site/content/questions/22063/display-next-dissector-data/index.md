+++
type = "question"
title = "Display next dissector data"
description = '''Hi, Is it possible to display information dissected by a upper level dissector on the info column, using a lower level plugin? For example, display isup´s calling party number using a modified mtp3 plugin. Thanks,'''
date = "2013-06-14T07:31:00Z"
lastmod = "2013-06-21T21:05:00Z"
weight = 22063
keywords = [ "display", "plugins" ]
aliases = [ "/questions/22063" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Display next dissector data](/questions/22063/display-next-dissector-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22063-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is it possible to display information dissected by a upper level dissector on the info column, using a lower level plugin? For example, display isup´s calling party number using a modified mtp3 plugin.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">display plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '13, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/41cae5c8111115b7c81a5d2f5a624c14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Renan&#39;s gravatar image" /><p>Renan<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Renan has no accepted answers">0%</span></p></div></div><div id="comments-container-22063" class="comments-container"></div><div id="comment-tools-22063" class="comment-tools"></div><div class="clear"></div><div id="comment-22063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22241"></span>

<div id="answer-container-22241" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22241-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Technically yes, it could be done if you recompile Wireshark with some column-related code changes; otherwise no. However, you could basically accomplish what you want without having to recompile Wireshark by adding a custom column for the isup calling party number, and there are a couple of ways to do that:</p><ol><li>Expand the ISDN User Part packet details tree and find the "<code>ISUP Calling Number: xxxxxxxxx</code>" field, then right-click on it and choose, "<code>Apply as Column</code>". Rearrange the column into any position you like by dragging and dropping.</li><li>From the main menubar: <code>Edit</code> -&gt; <code>Preferences</code> -&gt; <code>Columns</code> -&gt; <code>Add</code> -&gt; <code>Field type: Custom</code> -&gt; <code>Field name: isup.calling</code> -&gt; edit the Title to your liking -&gt; Drag and drop the new column field type to its desired location -&gt; Click <code>OK</code>.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '13, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-22241" class="comments-container"></div><div id="comment-tools-22241" class="comment-tools"></div><div class="clear"></div><div id="comment-22241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

