+++
type = "question"
title = "How can I get ISIS Neighbors if no Display Filter Reference exists?"
description = '''I need to get IS and ES Neighbors as well as Area Address for ISIS packets, but I do not see any Display Reference Filter for such. Can someone advise on how this may be done without parsing an ASCII text dump from tshark.'''
date = "2012-04-04T07:23:00Z"
lastmod = "2012-04-04T14:51:00Z"
weight = 9926
keywords = [ "neighbors", "area_address", "isis" ]
aliases = [ "/questions/9926" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get ISIS Neighbors if no Display Filter Reference exists?](/questions/9926/how-can-i-get-isis-neighbors-if-no-display-filter-reference-exists)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9926-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to get IS and ES Neighbors as well as Area Address for ISIS packets, but I do not see any Display Reference Filter for such. Can someone advise on how this may be done without parsing an ASCII text dump from tshark.</p></div><div id="question-tags" class="tags-container tags">neighbors area_address isis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '12, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/fc5169bb878375dad7670efe17fb5f1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clayton2710&#39;s gravatar image" /><p>clayton2710<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clayton2710 has no accepted answers">0%</span></p></div></div><div id="comments-container-9926" class="comments-container"></div><div id="comment-tools-9926" class="comment-tools"></div><div class="clear"></div><div id="comment-9926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9944"></span>

<div id="answer-container-9944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9944-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Modify the ISIS dissector to add named fields for the items in question and then file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> with your patch, so that these changes get into a standard version of Wireshark, or file a bug on the Wireshark Bugzilla asking for that to be done and, once it's done, use that version of Wireshark?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9944" class="comments-container"><span id="9969"></span><div id="comment-9969" class="comment"><div id="post-9969-score" class="comment-score"></div><div class="comment-text"><p>Perhaps, I should have been more concise with my question. These fields are already dissected, because they show up in the Details pane of Wireshark. However, there is no Display Filter Reference for the IS and ES Neighbors. I did finally find the Area Address reference. I need to process several hundred to thousand packet captures, so I obviously need automation. I can already look at the Details pane and see the data. Please do not suggest 'tshark -r (my-pcap.cap) -V' and then process those files for the data, it would be much too time consuming and take too much disk space. Many of these capture files have thousand to hundreds of thousand packets.</p></div><div id="comment-9969-info" class="comment-info"><span class="comment-age">(05 Apr '12, 12:54)</span> clayton2710</div></div><span id="9970"></span><div id="comment-9970" class="comment"><div id="post-9970-score" class="comment-score"></div><div class="comment-text"><p>They may be dissected, but they do not have named fields corresponding to them, which is why there is no Display Filter Reference for them; Wireshark just puts them into the protocol tree as an unnamed text display, which means that the <em>ONLY</em> way to get them from an unmodified version of Wireshark is from the -V output from TShark.</p><p>Without making the changes I mentioned, there's nothing that can be done about the "much too time consuming", but, as both UN\*X systems and Windows support pipes in commands, you could try piping the output of TShark to a script rather than writing it to a file.</p></div><div id="comment-9970-info" class="comment-info"><span class="comment-age">(05 Apr '12, 13:05)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9944" class="comment-tools"></div><div class="clear"></div><div id="comment-9944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

