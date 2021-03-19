+++
type = "question"
title = "calling a plugin dissector from another plugin dissector"
description = '''hi all, I have created two plugin dissectors for two different packets of a same protocol. But i cant use the wireshark to dissect both of the packets at the same time, i need to run the wireshark separately for each of the packet using the plugins for those packets. There is no issue in dissecting ...'''
date = "2015-08-12T05:36:00Z"
lastmod = "2015-08-13T01:33:00Z"
weight = 44999
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/44999" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [calling a plugin dissector from another plugin dissector](/questions/44999/calling-a-plugin-dissector-from-another-plugin-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44999-score" class="post-score" title="current number of votes">0</div><span id="post-44999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all, I have created two plugin dissectors for two different packets of a same protocol. But i cant use the wireshark to dissect both of the packets at the same time, i need to run the wireshark separately for each of the packet using the plugins for those packets. There is no issue in dissecting the packets, But now i want to run the wireshark in such a way that it can use both the plugins at the same time and call the plugin according to the packet.</p><p>So in order to do this thing i used "call_dissector(plugin_handle, tvb, pinfo, tree);" in one of my plugin which calls second plugin if the packet is for second plugin. And to detect the type of packet i have the msgid which i can use successfully to know that which packet is this,</p><p>Now the problem is that when i trying to dissect the packet in wireshark it giving me the following error, "ERROR:packet.c:2281:call_dissector_only: assertion failed: (handle != NULL)"</p><p>i have used find_dissector("dissector_name"); to get the refernce of the plugin dissector..</p><p>please help me on this and tell me how i can do this ..</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/4f516d44975f0778735c91ae9f71624b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zombimind&#39;s gravatar image" /><p><span>zombimind</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zombimind has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Aug '15, 05:40</strong> </span></p></div></div><div id="comments-container-44999" class="comments-container"><span id="45037"></span><div id="comment-45037" class="comment"><div id="post-45037-score" class="comment-score"></div><div class="comment-text"><p>anybody please help on this, i am not finding any way to do this, suggest me something</p><p>many thanks in advance</p></div><div id="comment-45037-info" class="comment-info"><span class="comment-age">(13 Aug '15, 00:10)</span> <span class="comment-user userinfo">zombimind</span></div></div><span id="45043"></span><div id="comment-45043" class="comment"><div id="post-45043-score" class="comment-score">1</div><div class="comment-text"><p>I don't see why you should have two dissectors for the same protocol, that sounds wierd but:</p><p>Did you register the dissector name in the register routine with new_register_dissector(); or register_dissector(); and have the find_dissector() call in the handoff routine?</p></div><div id="comment-45043-info" class="comment-info"><span class="comment-age">(13 Aug '15, 01:05)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="45044"></span><div id="comment-45044" class="comment"><div id="post-45044-score" class="comment-score"></div><div class="comment-text"><p>thanks for replying anders, actually the single dissector which i was having before for my protocol can dissect a particular packet, but now i have another packet which comes under the same protocol and needed to be dissect. so i created a plugin dissector for the 2nd packet so whenever the 2nd packet is there, this plugin dissector can be used by the previously existed dissector.</p><p>And yeah i didnt register my plugin dissector as you said with either "register_dissector" nor with "new_register_dissector", i will try this way,</p><p>thanks</p></div><div id="comment-45044-info" class="comment-info"><span class="comment-age">(13 Aug '15, 01:31)</span> <span class="comment-user userinfo">zombimind</span></div></div></div><div id="comment-tools-44999" class="comment-tools"></div><div class="clear"></div><div id="comment-44999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45042"></span>

<div id="answer-container-45042" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45042-score" class="post-score" title="current number of votes">1</div><span id="post-45042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're passing in a NULL handle as the first parameter, it should be the handle of the dissector you wish to call. I suspect the result of <code>find_dissector()</code> is NULL.</p><p>It's possible that the second dissector hasn't registered when you make the find_dissector call.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '15, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-45042" class="comments-container"><span id="45045"></span><div id="comment-45045" class="comment"><div id="post-45045-score" class="comment-score"></div><div class="comment-text"><p>yeah thats true, the result of find_dissector() is NULL and the reason i think is that, it is not registered,</p><p>thanks for your reply</p></div><div id="comment-45045-info" class="comment-info"><span class="comment-age">(13 Aug '15, 01:33)</span> <span class="comment-user userinfo">zombimind</span></div></div></div><div id="comment-tools-45042" class="comment-tools"></div><div class="clear"></div><div id="comment-45042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

