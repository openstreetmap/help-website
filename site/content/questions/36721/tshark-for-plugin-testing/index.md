+++
type = "question"
title = "Tshark for plugin testing"
description = '''Hi, i have created a Dissector for some new protocols. Now i have to build a continious integration job with Jenkins, where i have to test if the plugin is working correctly. So i thought i can use tshark to dissect a pcap file and than build an job which is checking the createt xml if the dissectio...'''
date = "2014-09-30T05:29:00Z"
lastmod = "2014-09-30T05:53:00Z"
weight = 36721
keywords = [ "dissector", "tshark", "plugin" ]
aliases = [ "/questions/36721" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark for plugin testing](/questions/36721/tshark-for-plugin-testing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36721-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have created a Dissector for some new protocols. Now i have to build a continious integration job with Jenkins, where i have to test if the plugin is working correctly. So i thought i can use tshark to dissect a pcap file and than build an job which is checking the createt xml if the dissection was successfull.</p><p>Now i have the problem, that tshark isnt loading my plugin. Is tshark able to load plugins? If yes, how do i load plugins with tshark?</p><p>greetings Christina</p></div><div id="question-tags" class="tags-container tags">dissector tshark plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '14, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/f65ac046295141d9f33ce4ac1770b5a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Venturina&#39;s gravatar image" /><p>Venturina<br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Venturina has no accepted answers">0%</span></p></div></div><div id="comments-container-36721" class="comments-container"></div><div id="comment-tools-36721" class="comment-tools"></div><div class="clear"></div><div id="comment-36721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36722"></span>

<div id="answer-container-36722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36722-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark uses the same plugins as Wireshark, and loads them in the same manner. tshark is also used in this way in the Wireshark CI build tests, see the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=test">test</a> directory of the Wireshark sources for some test script examples.</p><p>As to your actual issue, it's likely that your CI environment isn't placing the built plugin in the correct place for the copy of tshark that is being run by the tests to load.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '14, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36722" class="comments-container"><span id="36746"></span><div id="comment-36746" class="comment"><div id="post-36746-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it works now.</p></div><div id="comment-36746-info" class="comment-info"><span class="comment-age">(01 Oct '14, 01:43)</span> Venturina</div></div><span id="36747"></span><div id="comment-36747" class="comment"><div id="post-36747-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-36747-info" class="comment-info"><span class="comment-age">(01 Oct '14, 01:50)</span> grahamb ♦</div></div></div><div id="comment-tools-36722" class="comment-tools"></div><div class="clear"></div><div id="comment-36722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

