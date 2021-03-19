+++
type = "question"
title = "Packets using certain plugins are displayed using a lower level plugin in the packet list after sorting"
description = '''I am trying to fix a strange bug with some dissector plugins, but am not sure where to begin. The bug affects certain packets which use these plugins and causes them to be displayed in the packet list using a lower-level plugin. The packet details for these packets are normal. The bug happens when y...'''
date = "2014-05-21T10:52:00Z"
lastmod = "2014-05-22T09:17:00Z"
weight = 32956
keywords = [ "sort", "packetlist", "dissector", "sorting", "plugin" ]
aliases = [ "/questions/32956" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Packets using certain plugins are displayed using a lower level plugin in the packet list after sorting](/questions/32956/packets-using-certain-plugins-are-displayed-using-a-lower-level-plugin-in-the-packet-list-after-sorting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32956-score" class="post-score" title="current number of votes">0</div><span id="post-32956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to fix a strange bug with some dissector plugins, but am not sure where to begin. The bug affects certain packets which use these plugins and causes them to be displayed in the packet list using a lower-level plugin. The packet details for these packets are normal. The bug happens when you sort by source, destination, protocol, or info in the packet list pane, and affects only those packets which have not been visible in the packet list pane since the last time the pcap file was loaded. This means that if you were to scroll down the packet list until packet No. 15 is at the bottom of the visible packet list, then packet 16 onward will display incorrectly.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/PT_plugin_example_packet_broken.png" alt="broken packets" /></p><p>This is a screenshot of a bugged packet list. Before sorting, all of the packets displayed as GSM SMS, but now after sorting by Destination and sorting back to No., all of the packets after number 6 are displaying incorrectly. The detailed information is still there in the details pane, but it is not displayed in the packet list pane.</p><p>These plugins were written by a former employee and they are quite complicated, so it will take me a while to look through them all looking for anything out of place. Has anyone ever seen a bug like this, and if so, what did you do about it? If not, have you any suggestions where in the plugin I might look to find the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sort" rel="tag" title="see questions tagged &#39;sort&#39;">sort</span> <span class="post-tag tag-link-packetlist" rel="tag" title="see questions tagged &#39;packetlist&#39;">packetlist</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-sorting" rel="tag" title="see questions tagged &#39;sorting&#39;">sorting</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/8f51fdd676352de28608f014b75acbcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20G&#39;s gravatar image" /><p><span>Thomas G</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas G has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '14, 01:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-32956" class="comments-container"></div><div id="comment-tools-32956" class="comment-tools"></div><div class="clear"></div><div id="comment-32956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32958"></span>

<div id="answer-container-32958" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32958-score" class="post-score" title="current number of votes">1</div><span id="post-32958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Thomas G has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably the call to the nex dissector (MTP3) is don under if(tree) which is incorrect. The subdissector should allways be called.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-32958" class="comments-container"><span id="32984"></span><div id="comment-32984" class="comment"><div id="post-32984-score" class="comment-score"></div><div class="comment-text"><p>In which method would I look for if(tree) in the IMF plugin?</p></div><div id="comment-32984-info" class="comment-info"><span class="comment-age">(22 May '14, 05:49)</span> <span class="comment-user userinfo">Thomas G</span></div></div><span id="32990"></span><div id="comment-32990" class="comment"><div id="post-32990-score" class="comment-score"></div><div class="comment-text"><p>From the screenshot above it looks like the IMF plugin calls the MTP3 dissector, check if that's done under if(tree) or some other condition.</p><p>Typically a dissector has a main function dissect_foo() and after a few lines of code writing to columns and the main tree it has</p><p>if(tree){ "dissect the rest of the frame, perhaps calling other routines..." }</p><p>if the call to the MTP3 dissector is done inside this if statement that's probably the problem.</p></div><div id="comment-32990-info" class="comment-info"><span class="comment-age">(22 May '14, 06:34)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="33003"></span><div id="comment-33003" class="comment"><div id="post-33003-score" class="comment-score"></div><div class="comment-text"><p>Removing if(tree) from the plugins seems to fix the problem, but I'm afraid to remove something like that when I'm not entirely sure what it's for. Is there any danger in just removing if(tree)?</p></div><div id="comment-33003-info" class="comment-info"><span class="comment-age">(22 May '14, 09:01)</span> <span class="comment-user userinfo">Thomas G</span></div></div><span id="33005"></span><div id="comment-33005" class="comment"><div id="post-33005-score" class="comment-score"></div><div class="comment-text"><p>If(tree) is used to optimize the code to not perform what's inside the statement if the tree isn't present/vissible e.g packet details required.</p></div><div id="comment-33005-info" class="comment-info"><span class="comment-age">(22 May '14, 09:17)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-32958" class="comment-tools"></div><div class="clear"></div><div id="comment-32958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

