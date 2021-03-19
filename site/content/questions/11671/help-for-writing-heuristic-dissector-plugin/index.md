+++
type = "question"
title = "help for writing heuristic dissector plugin"
description = '''I intend to write a plugin using heuristic dissector.I am using eth heuristic dissector and my protocol relevant data will be part of ethernet payload and located at the end of ethernet payload.Now in dissect_myproto , the tree pointer will directly/autonomously point to my protocol relevant data wh...'''
date = "2012-06-05T09:36:00Z"
lastmod = "2012-06-05T12:49:00Z"
weight = 11671
keywords = [ "heuristics", "plugin", "wireshark" ]
aliases = [ "/questions/11671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [help for writing heuristic dissector plugin](/questions/11671/help-for-writing-heuristic-dissector-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11671-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I intend to write a plugin using heuristic dissector.I am using eth heuristic dissector and my protocol relevant data will be part of ethernet payload and located at the end of ethernet payload.Now in dissect_myproto , the tree pointer will directly/autonomously point to my protocol relevant data when my dissector gets called or i will have to manipulate it to point to my protocol relevant data ?</p></div><div id="question-tags" class="tags-container tags">heuristics plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11671" class="comments-container"></div><div id="comment-tools-11671" class="comment-tools"></div><div class="clear"></div><div id="comment-11671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11681"></span>

<div id="answer-container-11681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11681-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to read <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">README.developer</a> in the source tree.</p><p>As discussed on your very similar question, tvb is a pointer to the buffer containing the data from the packet that you will dissect, pinfo is a pointer to lots of other information about the packet and tree is a pointer to the proto tree where you put the <strong>results</strong> of your dissection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11681" class="comments-container"><span id="11695"></span><div id="comment-11695" class="comment"><div id="post-11695-score" class="comment-score"></div><div class="comment-text"><p>ok,my mistake. In my question when i said "tree" , i meant tvb. All this confusion has arisen due to call_dissector ,actually my protocol relevant data lies at end of ethernet payload so i wondering do i have to use call_dissector for eth first and then do my dissection ?</p></div><div id="comment-11695-info" class="comment-info"><span class="comment-age">(05 Jun '12, 16:01)</span> yogeshg</div></div><span id="11696"></span><div id="comment-11696" class="comment"><div id="post-11696-score" class="comment-score"></div><div class="comment-text"><p>let me explain myself more , earlier my protocol relevant data was coming first thing in ethernet payload and i was dissecting it followed by call to dissector for ip for eg. :-</p><p>ip_handle = find_dissector("ip");</p><p>call_dissector(ip_handle,....</p><p>But now my proto data is at the end of ethernet payload , so do i need to reverse this ? do i need to call_dissector for ip first and then do my dissection on my proto data ? .. Hope i made clear myself this time</p></div><div id="comment-11696-info" class="comment-info"><span class="comment-age">(05 Jun '12, 16:49)</span> yogeshg</div></div></div><div id="comment-tools-11681" class="comment-tools"></div><div class="clear"></div><div id="comment-11681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

