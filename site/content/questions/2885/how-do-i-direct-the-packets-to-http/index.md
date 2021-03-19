+++
type = "question"
title = "How do I direct the packets to http?"
description = '''Hi, I have dissector which dissects the packet at port 80 but If its not my packet its not going to http dissector what should i do? please help.  when do I use dissector_delete? '''
date = "2011-03-16T23:36:00Z"
lastmod = "2011-03-17T00:06:00Z"
weight = 2885
keywords = [ "dissector_delete", "http", "port" ]
aliases = [ "/questions/2885" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I direct the packets to http?](/questions/2885/how-do-i-direct-the-packets-to-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2885-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have dissector which dissects the packet at port 80 but If its not my packet its not going to http dissector what should i do? please help. when do I use dissector_delete?</p></div><div id="question-tags" class="tags-container tags">dissector_delete http port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '11, 23:36</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p>niks3089<br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-2885" class="comments-container"></div><div id="comment-tools-2885" class="comment-tools"></div><div class="clear"></div><div id="comment-2885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2888"></span>

<div id="answer-container-2888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2888-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>dissector_delete()</code> is used only for the static dissector configuration, that is the per dissection session. If you need to do this per packet you should look into using heuristic dissectors. These return to the dissection engine whether or not they recognized the packet. If not the dissection engine passes the packet to the next one. In your case that would be the HTTP dissector. Make sure to set TCP dissector preference "Try heuristic sub-dissectors first"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 00:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2888" class="comments-container"><span id="2890"></span><div id="comment-2890" class="comment"><div id="post-2890-score" class="comment-score"></div><div class="comment-text"><p>I have a signature to detect my packet. If it is not present it should return back to the wireshark where it will decide which port it should go to. How can I do this? Thanks in advance</p></div><div id="comment-2890-info" class="comment-info"><span class="comment-age">(17 Mar '11, 00:52)</span> niks3089</div></div></div><div id="comment-tools-2888" class="comment-tools"></div><div class="clear"></div><div id="comment-2888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

