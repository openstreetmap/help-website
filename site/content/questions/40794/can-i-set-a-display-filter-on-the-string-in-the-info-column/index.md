+++
type = "question"
title = "Can i set a display filter on the string in the &quot;info&quot; column?"
description = '''Sometimes, i&#x27;d like to set a filter on &#x27;all packets that have &quot;TCP Previous segment not captured&quot; in their info string&#x27;, or something else that shows up in the info string column. Is this possible? Right now, i use the &quot;workaround&quot; of searching the packet details of one packet for what causes the st...'''
date = "2015-03-24T02:51:00Z"
lastmod = "2015-03-24T13:20:00Z"
weight = 40794
keywords = [ "filter", "info" ]
aliases = [ "/questions/40794" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Can i set a display filter on the string in the "info" column?](/questions/40794/can-i-set-a-display-filter-on-the-string-in-the-info-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40794-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sometimes, i'd like to set a filter on 'all packets that have "TCP Previous segment not captured" in their info string', or something else that shows up in the info string column. Is this possible?</p><p>Right now, i use the "workaround" of searching the packet details of one packet for what causes the string to be displayed, use "Copy as / Filter" in the right click menu, then use the copied string to build the display filter. However, this is a bit clumsy, and i'd like the display filter input box to show the string i'm searching for instead of the property, especially if there are several <code>and</code>s and <code>or</code>s joined together.</p><p>So, is it possible to filter on the display string?</p></div><div id="question-tags" class="tags-container tags">filter info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '15, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/a020f3d8eff97cdcd668a62a4dfbbed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guntram%20Blohm&#39;s gravatar image" /><p>Guntram Blohm<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guntram Blohm has no accepted answers">0%</span></p></div></div><div id="comments-container-40794" class="comments-container"></div><div id="comment-tools-40794" class="comment-tools"></div><div class="clear"></div><div id="comment-40794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40817"></span>

<div id="answer-container-40817" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40817-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See also <a href="https://ask.wireshark.org/questions/40447/contain-display-filter.">https://ask.wireshark.org/questions/40447/contain-display-filter.</a></p><p>Basically, there is no filter field for the info column in Wireshark (though there is in tshark). So your workaround (search for the string, find a corresponding filter expression and then use that as a filter) is about the best you can get.</p><p>You can of course file an enhancement request to <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and maybe someone will find the interest to add this functionality.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40817" class="comments-container"><span id="55567"></span><div id="comment-55567" class="comment"><div id="post-55567-score" class="comment-score"></div><div class="comment-text"><p>"(though there is in tshark)" - I need the tshark one. Can you guide me a bit about that? For example using tshark, if I want to apply a display filter which returns only those packets whose info section contains the string "abc", how can I do that?</p></div><div id="comment-55567-info" class="comment-info"><span class="comment-age">(15 Sep '16, 09:48)</span> Jesss</div></div><span id="55568"></span><div id="comment-55568" class="comment"><div id="post-55568-score" class="comment-score"></div><div class="comment-text"><p>See the answer by @CraigGarrett to <a href="https://ask.wireshark.org/questions/32574/tshark-column-fields">this</a> question.</p></div><div id="comment-55568-info" class="comment-info"><span class="comment-age">(15 Sep '16, 10:40)</span> grahamb ♦</div></div></div><div id="comment-tools-40817" class="comment-tools"></div><div class="clear"></div><div id="comment-40817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40795"></span>

<div id="answer-container-40795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40795-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try the tcp.analysis.x display filters e.g. tcp.analysis.lost_segment</p><p>Everything that is in the info column is also displayed under the protocol details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Mar '15, 03:32</p></div></div><div id="comments-container-40795" class="comments-container"></div><div id="comment-tools-40795" class="comment-tools"></div><div class="clear"></div><div id="comment-40795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40796"></span>

<div id="answer-container-40796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40796-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Generally all the expert info messages have an associated filter field that should be used in preference to string matching in the info field.</p><p>For your condition, use the filter "tcp.analysis.lost_segment == 1". You can usually determine the filter name by selecting the field of interest in the protocol tree and looking at the status bar.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 03:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40796" class="comments-container"></div><div id="comment-tools-40796" class="comment-tools"></div><div class="clear"></div><div id="comment-40796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

